# Netatalk のセットアップ

## AFP ファイルサーバーのセットアップ

AFP (Apple Filing Protocol)  はアップル・マッキントッシュのファイルサービスに用いるプロトコルである。AFP
プロトコルは年を追うごとに進展を見せ、最終バージョンは OS X Lion (10.7) で加えられた "AFP 3.4" である。

Netatalk の afpd デーモンはアップルのクライアントに対して AFP ファイルサービスを提供する。設定ファイルは *afp.conf*
のみで、"ini" スタイルの構文で記述する。

Netatalk はリモートバックアップのための Time Machine とインデックス検索のための Spotlight との互換性を提供する。

ボリュームを Time Machine のターゲットにするには、オプション **time machine = yes** を使う。

Spotlight のインデックスを有効にするには、適切な場所でオプション **spotlight = yes** を設定する。

Netatalk 2.1 以降では UNIX シンボリックリンクをサーバー上で使うことができる。セマンティクスは例えば NFS
と同じである、すなわち、Netatalk
はサーバー側でシンボリックリンクを追わないが、代わりにクライアント側でシンボリックリンクを解決できるよう完全に転送して、
結果としてクライアントのファイルシステムのビュー内でしかるべき場所を示すリンクとなる。

### afp.conf

*afp.conf* は、AFP ファイルサーバー及び提供する AFP ボリュームの挙動と設定を決定するために afpd が使用する設定ファイルである。

*afp.conf* は複数のサーバーセクションに分割できる。すなわち：

[Global]

> グローバルセクションで基本的なサーバーオプションを定義する

[Homes]

> ホームセクションでユーザーのホームボリュームを定義する

**Global** とも **Homes**、とも呼ばれないセクションは単なる一つの AFP ボリュームであると解釈される

**Homes** を定義してユーザーのホームディレクトリを共有するために、 `basedir regex` オプションを明記しなければならない。
これは全てのユーザーのホームの親ディレクトリのパスあるいは正規表現からなる単純な文字列でよい。

例：

    [Homes]
    basedir regex = /home

この場合、AFP サーバーにログインできるユーザーはそれぞれ `/home/（ユーザー名）` というパス名でのユーザーボリュームを使用できる。

より複雑なセットアップで、例えば二つの異なったファイルシステムにわたって分割された、 大量のユーザーホームディレクトリーのあるサーバーなら：

- /RAID1/homes

- /RAID2/morehomes

以下の設定が必要である：

    [Homes]
    basedir regex = /RAID./.*homes

もし、**basedir regex** にシンボリックリンクが含まれる場合、 正規化された絶対パスを指定すべきである。つまり、パス */home*
から */usr/home* にシンボリックリンクがはられていた場合：

    [Homes]
    basedir regex = /usr/home

他の使用できるオプションの詳細な解説については [afp.conf](afp.conf.5.html) の man page を参照いただきたい。

## CNID バックエンド

SMB や NFS のようなほかのプロトコルとは異なり、ほとんどの場合、AFP プロトコルはファイルやディレクトリをパスではなく ID
を通して参照している。（その ID は CNID とも言われ、カタログ・ノード ID (Catalog Node ID) の略である） 典型的には、まず
AFP リクエストで、例えば、“サーバーさん id 167 のディレクトリにある、ファイル名 'Test'
というのを開いてください。”といった調子でディレクトリ IDとファイル名を用いる。例えば、Mac での "Aliases" は基本的には ID
として作用する（より最近の AFP クライアントでは絶対パスにフォールバックするが、これは Finder
のみで当てはまることであり、アプリケーションでは当てはまらない）。

AFP ボリュームにある各々のファイルに一意のファイル ID が割り当てられる。仕様により ID は絶対に再利用禁止であり、ID は 32 bit
の数字である。（ディレクトリ ID も同じ ID プールを使用する）このため、ある AFP ボリュームにおよそ 40
億個以上のファイル・フォルダーを書き込むと、その時点で ID
プールが枯渇され、当該ボリュームへの新ファイルの書き込みができなくなる。愚痴はなしということでお願いしたい :-)

Netatalk はホストのファイルシステム内で ID
とファイルあるいはフォルダーのマップ（ID
との対応付け）をする必要がある。 それを実現するためにいくつかの異なる
CNID
バックエンドが用意されていて、*afp.conf*
設定ファイル内で **cnid scheme**
オプションで選択が可能である。CNID
バックエンドは基本的には、ストアされた ID <-\>
名前を一対一対応させるデータベースである。

CNID データベースはデフォルトではシステムの状態ディレクトリパス（例：*/var/lib*）の下にある *netatalk/CNID*
サブディレクトリに置かれる。コンパイル時に *-Dwith-statedir-path=PATH* オプションで場所を変えられる。

CNID データベースの検証・修復・再構築のために用いることができる **dbd** という名のコマンドが用意されていている。

> **注記**

> netatalk で作業する上で、いくつかの CNID
に関する点を留意しておかなければならない。すなわち：

> - "**vol dbnest = yes**"
が指定してある時以外はボリュームをネスト（入れ子）にしてはならない。

> - CNID バックエンドはデータベースである。それ故 afpd
はファイルサーバーとデータベースの混成物とならしめている。

> - もしファイルシステムに空き容量がなくなった場合、データベースは破損するかもしれない。
それを回避するために取る策としては、**vol dbpath**
オプションを使用して、
データベースファイルをどこか別の場所に置く、か、クオータを使っているならば
CNID
データベースフォルダーがクオータなしでユーザー／グループのオーナーとなっているか確認する。のいずれかである。

> - NFS 経由でマウントされているボリュームの CNID
データベースには注意すべきである。
いずれにしろそのような構成にすると決める事自体かなり無謀である。
が、さらにデータベースもその上に置くとなると決定的にトラブルの元となる。要はデータベースの破損である。もしどうしても
NFS
マウントしたボリュームを使わねばならない場合はデータベースをローカルディスクに置くために
**vol dbpath** ディレクティブを使用するべきである。

### dbd

CNID データベースへのアクセスは cnid_dbd デーモンプロセスのみに制限されている。afpd プロセスはデータベースの読み込みと更新のために
cnid_dbd デーモン とやりとりをする。 データベースが破損する可能性は経験的にはほぼゼロである。

本バックエンドは Netatalk 2.1 以来、デフォルトのバックエンドとなっている。

### last

last バックエンドはメモリーにデータを保持する tdb データベースである。故永続性がなく、ID
はカレントセッションでしか有効ではない。netatalk 3.0 からは、それは*読み込み専用モード*になっている。このバックエンドは例えば
CD-ROM や自動化テスト などに有用である。

これは基本的には **afpd** が netatalk バージョン 1.5以前で CNID データの保存方法に一致している。

### mysql

CNID バックエンドは MySQL サーバーを使用する。MySQL サーバーはシステム管理者がプロビジョニングする必要がある。

## Charsets/Unicode

### なぜ Unicode？

内部的には、コンピューターは文字（キャラクター）について、 テキストについて何も知らない、唯一“数字（数）”ならコンピュータにもわかる。
それ故各々の“字”には“数”が割り当てられている。キャラクターセット、しばしば *charset* あるいは *codepage*
とも呼ばれるが、これは“数”と“字”の一対一対応を規定している。

二つあるいはそれ以上のコンピューターがお互いに通信する必要がある場合、各々は同じキャラクターセットを使う必要がある。1960 年代には ASCII
(American Standard Code for Information Interchange) キャラクターセットが
ASA（米国標準協会：the American Standards Association）によって標準化された。 オリジナルの ASCII
形式は、英語で用いられるアルファベット及び数字を網羅するのに十分な数より多い 128 のキャラクターを表している。今日においても、ASCII
はコンピューターで使われるキャラクタースキームの標準的なものである。

国際的にもっと都合よく、そして若干内輪向けの記号文字を含めるために、つづくバージョンでは 256 のキャラクターを規定した。
このエンコードの仕様だと一文字はきっちり 1 バイトに収まるが、明らかに、256 キャラクターというのは、
いろいろな言語で用いる全ての文字を一つのキャラクターに一対一対応させるのに依然十分ではなかった。

結果的には後にローカライズされたキャラクターセットが規定された。例えば ISO-8859 キャラクターセットである。
ほとんどのオペレーティングシステムベンダーは自らの要求を満たすために、独自のキャラクターセットを導入した。すなわち IBM であれば *コードページ
437 (DOSLatinUS)*、アップルは *MacRoman* コードページ、などである。127 以上のキャラクターが定義されているものを*拡張*
キャラクターと呼ぶ。 これらのキャラクターセットは異なるキャラクターに同じ番号をふってあるので、
他のキャラクターセットとまたはキャラクターセット同士で衝突を起こす。

そういったキャラクターセットのほぼ全てが 256 個のキャラクターを定義していて、最初の 128 個（0 から 127 まで）のキャラクターを
ASCII と同一対応となるようにしている。結果的に、違ったコードページを使っているシステム同士の通信では、事実上 ASCII
キャラクターセット限定となった。

この問題を新たに解決するために、より大きいキャラクターセットが規定された。より多くのキャラクターマッピングの場所を確保するために、
これらのキャラクターセットは一つのキャラクターの格納のために最低でも 2 バイトを使用する。 このためそういったキャラクターセットは*マルチバイト*
キャラクターセットと呼ばれる。

標準化されたマルチバイトキャラクターエンコード方式として知られているものの一つとして
[ユニコード](http://www.unicode.org/)がある。 マルチバイトキャラクターセット使用の大きな利点として“それ一つで済む”がある。
二つのコンピューターが通信しているときに両者が同じキャラクターセットを使用しているか確認する必要がない。

### Apple で使われている（使われていた）キャラクターセット

過去に Apple クライアントは、ネットワーク間の通信のためにシングルバイトのキャラクターセットを使用していた。 年を経るに従い、Apple
はいくつものキャラクターセットを定義したが、欧米ユーザーは *MacRoman* コードセットを最もよく使用するであろう。

Apple の定義したコードページに含まれるもの：

- MacArabic, MacFarsi

- MacCentralEurope

- MacChineseSimple

- MacChineseTraditional

- MacCroatian

- MacCyrillic

- MacDevanagari

- MacGreek

- MacHebrew

- MacIcelandic

- MacJapanese

- MacKorean

- MacRoman

- MacRomanian

- MacThai

- MacTurkish

Mac OS X 以降そして AFP3 以降では [UTF-8](http://www.utf-8.com/)  が用いられる。UTF-8 は
Unicode キャラクターを ASCII 互換のやり方でエンコードする。各々の Unicode キャラクターは一個から六個の ASCII
キャラクターにエンコードされる。 故に、UTF-8
自体が本当のキャラクターセットなのではなく、ユニコードキャラクターセットのエンコーディングなのである。

厄介なことにも Unicode はいくつかの
*[normalization（正規化）](http://www.unicode.org/reports/tr15/index.html)*
方式を規定している。[Samba](http://www.samba.org)  はほとんどの UNIX ツールも好んで用いる
*precomposed* Unicode を使用する。一方 Apple は *decomposed* normalization を使うことに決めた。

例として、文字 'ä'（小文字aにダイエリシスがついたもの）についてみてみる。Precomposed normalization を使えば
Unicode はこの文字に 0xE4 を対応付ける。Decomposed normalization では 'ä' を正確には 0x61 と
0x308 の二つの文字に対応付ける。0x61 は 'a' に、0x308 は *COMBINING DIAERESIS*に対応付けられている。

Netatalk では precomposed UTF-8 を *UTF8* と、decomposed UTF-8 を *UTF8-MAC* と呼ぶ。

### afpd とキャラクターセット

新しい AFP 3.x クライアントも古い AFP 2.x クライアントも同時にサポートするために、afpd
は使われている様々なキャラクターセット間の変換が可能であることを必要とした。AFP 3.x クライアントは常に UTF8-MAC を、AFP 2.x
クライアントは Apple コードページのうちの一つを使う。

本稿執筆時点（訳注：原文の）で、netatalk は以下の Apple コードページをサポートしている：

- MAC_CENTRALEUROPE

- MAC_CHINESE_SIMP

- MAC_CHINESE_TRAD

- MAC_CYRILLIC

- MAC_GREEK

- MAC_HEBREW

- MAC_JAPANESE

- MAC_KOREAN

- MAC_ROMAN

- MAC_TURKISH

afpd は三つの異なるキャラクターセットオプションを扱う：

unix charset

> これはオペレーティングシステムの内側で使われているコードページである。もし指定されていなければ、デフォルトで
**UTF8** になる。もし **LOCALE** が指定されていて、 システムが UNIX locales
をサポートしていれば、afpd はコードページを検出しようとし、afpd
は検出したコードページを使って設定ファイルを読む。なので、ボリューム名やログインメッセージなどに拡張文字を使うことができる。

mac charset

> 既に述べたように、旧式の Mac OS クライアント（AFP 2.2 までのもの）は
afpd と通信するのにコードページを用いる。しかしながら、AFP
プロトコルにはクライアントが使用しているコードページの折り合いをつけるというサポートはない。もしほかのどこかで指定されていないと、
afpd は *MacRoman* コードページが使われていると仮定する。
クライアントが別のコードページ、例えば *MacCyrillic* を使っていたならば,
それを明示的に設定**しなければならない**だろう。

vol charset

> これは afpd がディスク上のファイル名として使うべき charset
を定義する。デフォルトでは **unix charset** と同じである。もし
[iconv](http://www.gnu.org/software/libiconv/)
がインストールしてあるならば、iconv
が提供するキャラクターセットも使用することができる。

afpd はファイルをUNIXのファイルシステムに保存する時、拡張マッキントッシュキャラクター、あるいは
UNIXのファイル名として不正なキャラクターを保持する手段が必要である。初期のバージョンでは、いわゆる
CAPエンコーディングを使った。拡張キャラクター
(\>0x7F) は :xx の 16 進数に変換される。例えば、アップルのロゴ
(MacRoman: 0xF0) は :f0 として保存される。
いくつかの特殊なキャラクターも :xx という表記に変換される。'/' は :2f
にエンコードされる。もし、**usedots**オプションが設定されていなければ、先頭のピリオド '.' は :2e
にエンコードされる。

本ドキュメントでのバージョンではファイル名のデフォルトエンコーディングとして **UTF8** を使っているにもかかわらず、'/' は ':'
に変換される。欧米のユーザーにとって別の有用な設定として **vol charset = ISO-8859-15** もあり得る。

もし、あるキャラクターが **mac charset** から選定した **vol charset** への変換ができない場合、マック上で -50
エラーを受け取るだろう。 *注意*： 可能な限り常に、デフォルトの UTF8 ボリュームフォーマットにしてください。

## 認証

### AFP 認証の基本

Apple は AFP クライアントとサーバー間の認証のために "User Authentication Modules" (UAM)
と呼ばれる柔軟なモデルを選んだ。AFP クライアントがまず最初に AFP サーバーと接続するとき、 サーバーが提供している UAM
のリストを問い合わせる。そして、クライアントがサポートしている最も強い暗号化の UAM を選ぶ。

数個の UAM は時間をかけて Apple が開発してものであり、サードパーティの開発者によるものもある。

### Netatalk でサポートされている UAM

Netatalk はデフォルトで以下のものをサポートしている：

- "No User Authent" UAM（ユーザー認証なしのゲスト接続）

- "Cleartxt Passwrd" UAM（クリアテキスト(平文)パスワード、暗号化なし）

- "Randnum exchange"、"2-Way Randnum exchange" UAM
（乱数交換・双方向乱数交換、弱いパスワード暗号化、パスワードを別途保存する）

- "DHCAST128" UAM（より強いパスワード暗号化）

- "DHX2" UAM（DHCAST128 の後継版）

他にもオプションとして以下のような UAM がある：

- "Client Krb v2" UAM （Kerberos V、macOS で“シングルサインオン”環境には最も適当である――下記参照）

"**uam list**" を **Global** セクションで定義することによって、どの UAM を有効化すべきか設定できる。**afpd**
はどの UAM を使っているのか、UAM を有効化した時に問題が起こっているのかどうかを、**netatalk.log** あるいは起動時の
syslog にログとして保存する。**asip-status** も AFP サーバーで有効な UAM の問い合わせをするのに使うことができる。

ある特定の UAM がサーバー上で有効であるということが、直ちに、
クライアントもそれを使うことができるということを意味するわけではない。クライアント側でのサポートもまた必要である。Classic Mac OS
が使われている古い Macintosh では、DHCAST128 のサポートは AppleShare クライアント 3.8.x 以降には存在している。

macOS では、AFP クライアントをもっと冗長にするクライアント側のテクニックがいくつかあるので、使用する UAM
と折り合いをつけるまでに何が起こっているのか見ることができる。[このヒント](https://web.archive.org/web/20080312054723/http://article.gmane.org/gmane.network.netatalk.devel/7383/)
と比較してみるとよい。

### どの UAM を有効にすべきか？

それは主に、ニーズとサポートする必要がある macOS クライアントの種類に依存する。ネットワークが macOS (Mac OS X)
クライアントのみで構成されている場合は、DHX2 で十分であり、最も強力な暗号化を提供する。

- サーバーのボリュームに本当にゲストアクセスを供することが必要な場合以外は、"No User Authent"
が無効化されているか確認すべきである。さもないと、意図しない権限のないアクセスを引き起こすことにもなる。
ゲストアクセスを有効にしなければならない場合は、アクセスコントロールを使って、
ボリューム各々についてゲストアクセスを有効化することを強制するように気を配るべきである。

    注意：Apple II NetBoot サービス (**a2boot**) を使用して AFP 経由で
    Apple //e を起動するには、「ユーザー認証なし」が必要である。

- "ClearTxt Passwrd" UAM ではパスワードがネットワーク上を暗号化されずに伝わっていくので、
字句そのまんまに良くない。クライアント側のみならずサーバー側でも無効にするよう務めるべきである。

    注意：もし NetBoot サービスを使用している Mac OS 8/9
    にサービスを提供したい場合、uams_cleartxt.so の UAM が必要となる。
    これはそういった Mac のファームウエアに組み込まれた AFP
    クライアントがこうした基本的な形の認証しか扱わないためである。

- "Randnum exchange" と "2-Way Randnum exchange" は 56 ビット DES
暗号化しか使わないので、これらもやはり回避すべきである。
そしてなおかつ不利なのは、パスワードがサーバーに平文テキストとして保存されなければならないこと、および PAM 環境とも古典的な /etc/shadow
とも統合がとれない （もしクライアントがこれらの UAM を使わなければならない場合、**afppasswd**
ユーティリティを使って別途パスワードを管理しなければならない）という点である。

    ただし、これは 漢字Talk 7.1 以前で使用できる最も強力な認証形式である。

- "DHCAST128" ("DHX") あるいは "DHX2" は PAM との統合と強力な暗号化とが組み合わせられているので、
ほとんどの人々にとって良い妥協案であろう。

- Kerberos V ("Client Krb v2") UAM を用いれば、Kerberos
チケットを用いて真のシングルサインオン環境を実装することが可能である。パスワードがネットワークを通して送られることもない。
その代わり、ユーザーのパスワードは AppleShare サーバーへのサービスチケットを暗号から復号するのに用いられる。
サービスチケットにはクライアントの暗号鍵と幾らかの暗号化されたデータが含まれる （それは AppleShare
サーバーだけが復号できる）。サービスチケットの暗号化された部分がサーバーに送られ、ユーザーを認証するのに使われる。afpd
サービスプリンシパル検知の実装の仕方のために、この認証方法は中間者攻撃に対して脆弱である。

様々な UAM の技術的実装についてのより詳細な概要については、Apple の [File Server
Security](http://developer.apple.com/library/mac/#documentation/Networking/Conceptual/AFP/AFPSecurity/AFPSecurity.html#//apple_ref/doc/uid/TP40000854-CH232-SW1)
ページを見ていただきたい。

### 特定の UAM で別の認証ソースを使う

いくつかの UAM は別の認証バックエンドを使えるようにしてある。いわゆる **uams_clrtxt.so**、**uams_dhx.so** 及び
**uams_dhx2.so** である。これらは */etc/passwd* (*/etc/shadow*) からの古典的 UNIX
パスワードでも、システムがサポートしていれば PAM でもどちらでも使うことができる。 **uams_clrtxt.so** は
**uams_passwd.so** ないしは **uams_pam.so** へのシンボリックリンクとして、 **uams_dhx.so** は
**uams_dhx_passwd.so** ないしは **uams_dhx_pam.so** へのシンボリックリンクとして、さらには
**uams_dhx2.so** は **uams_dhx2_passwd.so** ないしは
**uams_dhx2_pam.so**へのシンボリックリンクとすることができる。

なので、もし Netatalk の UAM フォルダー（デフォルトで */etc/netatalk/uams/*）が以下のようであれば、PAM
さもなくば古典的な UNIX パスワードを使用しているわけである。

    uams_clrtxt.so -> uams_pam.so
    uams_dhx.so -> uams_dhx_pam.so
    uams_dhx2.so -> uams_dhx2_pam.so

PAM を使用することで最も有利なのは、例えば LDAP 経由、あるいは NIS 経由などの集約した認証環境に Netatalk
を統合できることである。そのような環境でのユーザーのログイン資格情報 (credentials) の保護は、UAM
そのものが供している暗号化の強さにもまた依存している。 ということを常に念頭においていただきたい。なので、"ClearTxt Passwrd" や
"Randnum exchange" のような弱い UAM をネットワーク上から 完全に除去することを考えるべきである。

### Netatalk UAM を概要表

公式にサポートされているUAMの概観。

| UAM | No User Auth | Cleartxt Passwrd | RandNum Exchange | DHCAST128 | DHX2 | Kerberos V |
|-----|--------------|------------------|------------------|-----------|------|------------|
| パスワード長 | ゲストアクセス | 最大 8 文字 | 最大 8 文字 | 最大 64 文字 | 最大 256 文字 | Kerberos チケット |
| サポートするクライアント | 全ての Mac OS のバージョンで組み込み済 | 10.0 を除く全ての Mac OS のバージョンで組み込み済。 最近のバージョンでは明示的にアクティブ化する必要がある。 | ほとんど全ての Mac OS のバージョンで組み込み済 | AppleShare クライアント 3.8.4 より組み込み済で、3.8.3 では macOS の AFP クライアントに統合したプラグインとしての用意あり。 | Mac OS X 10.2 より組み込み済 | Mac OS X 10.2 より組み込み済 |
| 暗号化 | クライアント・サーバー間で認証なくゲストアクセス可能。 | パスワードがネットワーク上を暗号化されずに伝わっていく。 字句そのままに悪いので、可能ならば全面的に使用を回避すべき （注意：NetBoot サービスの提供には ClearTxt UAM が必要） | DES, 56 ビットに相当する 8 バイトの乱数がネットワーク上に送出。オフラインの辞書攻撃に対して脆弱。 パスワードがサーバー上で平文であることが求められる。 | パスワードは 128 ビット SSL で暗号化され、ユーザーはサーバーに認証されるが、“逆もまた真”ではない。 このため中間者攻撃に対して弱い。 | パスワードは libgcrypt の CAST 128、CBC モードを用いて暗号化される。 ユーザーはサーバーに認証されるが、“逆もまた真”ではない。このため中間者攻撃に対して弱い。 | パスワードがネットワークを通して送られることがない。サービスプリンシパル検知の方法が原因で、 この認証方法は中間者攻撃に対して脆弱である。 |
| サーバーがサポートする共有オブジェクト | uams_guest.so | uams_cleartxt.so | uams_randnum.so | uams_dhx.so | uams_dhx2.so | uams_gss.so |
| パスワードの保管方法 | なし | システム認証ないしはPAM | パスワードは別のテキストファイルに平文として保存される | システム認証ないしはPAM | システム認証ないしはPAM | Kerberosキー配布センター |

### SSH トンネリング

トンネリングや VPN のたぐいのもの全ては、AFP 認証や UAM に関してすべきことは概ね皆無である。
しかしながらアップルが「SSHを用いて安全な接続を可能にする」というオプションを導入して以来、
多数の人が両者について混乱する傾向にある。以下ではその点についても述べる。

#### 手動で AFP セッションをトンネリング

これは、"AFP over TCP" を“話すことができる”最初の AFP サーバーがネットワークに登場して以来うまく動作する。リモートサーバーの
AFP ポートをローカルの 548 番以外の異なるポートにトンネルし、その後ローカルでこのポートににつなげるだけである。macOS
では以下のようにすればよい。

    ssh -l $USER $SERVER -L 10548:127.0.0.1:548 sleep 3000

トンネルを確立したならば、“サーバーに接続”ダイアログで `"afp://127.0.0.1:10548"` を使うことができる。ローカルの AFP
クライアントは Mac のローカル 10548 番ポートに接続し、そのポートは SSH を通してリモートサーバーの AFP ポート（デフォルトでは
548 番を使う）に転送されているので、端緒の接続試行も含めて全ての AFP トラフィックがネットワークを暗号化されて送られる。

この手のトンネルは、もし、“真の” VPN を使えないが、インターネットを通じて、弱い認証機構しかない AFP
サーバーにアクセスしなければならない場合の理想的な解決手段である。**ssh** の "-C" オプションでデータ圧縮が可能であり、トンネルの端点を
AFP クライアント、サーバーどちらとも異なるようにすることが可能である （詳細については SSH
のドキュメントと比較してほしい）という点に留意すべきである。

#### 自動的にトンネル AFP 接続を確立する

Apple は Mac OS X 10.2 から 10.4 で、「サーバーに接続」ダイアログに
「SSHを用いて安全な接続を可能にする」チェックボックスを追加した。この考えの裏にあるのは：サーバーが SSH
で接続できるというサインを出した時、macOS の AFP クライアントはトンネルを確立しようとし、自動的に全ての AFP
トラフィックをこのトンネルを通して送る。ということなのである。

しかし、この機能が初めて…部分的に、動作するようになるのに Mac OS X 10.3 までかかった。SSH トンネルが確立できない時、AFP
クライアントは**何の通知もなく**暗号化していない AFP 接続試行にフォールバックした。

"**advertise ssh**" および "**fqdn**" オプション両方を **Global**
セクションで設定（設定を変更したら、afpd を再起動した後 **asip-status** で二重チェックするべき）した時は、SSH トンネルした
AFP リクエストの扱いが可能であることを Netatalk の afpd
はレポートする。しかし、このオプションを決して使用したくなくなる２、３の理由がある：

- こう言うような機能を必要とする大部分のユーザーは、 おそらく使い慣れている VPN はあるとしたら、 通常のVPNを使用して AFP
サーバーが実行されているネットワークに接続し、 AFP サーバーにアクセスする方が簡単だろう。

    とはいっても、１台のAFPサーバーに接続するという単純なケースでは、
    VPNより直接SSH接続の方がパフォーマンス的に良いだろう。噂と違って、SSH
    経由のトンネリングでは、いわゆる「TCP-over-TCP
    メルトダウン」は発生しない。何故なら、トンネリングされるAFPデータが
    TCPデータをカプセル化していないためである。

-
このようにSSHでその場をしのぐことはAFP認証機構に直接統合された通常のUAMではないし、代わりにこの方法では、トンネルの確立を**試行**できるのかどうなのかのサインをクライアントに送るために、単一のフラグを用いる。このため、何かがおかしい時に何が起こっているのかを見ようとする気を失ってしまう。

-
全ての接続試行はlocalhostから行われているように見えるので、**macusers**のようなNetatalkツールによって、どのマシンがログオンしているのか制御ができない。

-
実際、AFPセッションが全てがSSHで暗号化されていることを確実にしたい場合は、afpdへのアクセスをlocalhostのみ発信される接続に制限する必要がある。たとえば、Wietse
VenemaのTCPラッパーを使用するか、適切なファイアウォールやパケットフィルタリング機能を使用するなど。

    そうしなければ、10.2 から 10.3.3 を使っている場合は、予想とは逆に：
    トンネルの確立に失敗したという通知一つもなく、ネットワーク上で暗号化されていない
    AFPの通信（ログイン資格情報を含む）が起こりえるということである。Appleは
    Mac OS X 10.3.4 になってそれをはじめて修正した。

-
SSH経由で全てのAFPセッションを暗号化するることは、Netatalkサーバーの負荷の著しい上昇を招く可能性がある。ユーザーが信頼できるネットワーク経由で接続している場合、そのような暗号化は無駄かもしれない。

## ACL のサーポート

afp の ACL サポートは Solaris の ZFS ACL、派生したプラットフォーム、そして、Linux の POSIX 1e ACL
で実装されている。

### 設定

基本的な方式で運用するならば設定することは何もない。Netatalk は ACL をオンザフライで読み込み、そののちいわゆる UARights
パーミションビット経由で AFP クライアントに送られる有効なパーミッションを算出する。 マック上では、これらのビットを Finder
ウィンドウ内のパーミッションと調整するために Finder が使用する。例：UNIX のモードでは書き込み専用だが ACL
がユーザーに書き込み権限を与えているフォルダーは有効な読み書き権限を表示する。権限のマッピングなしに Finder
は読み込み専用アイコンを表示するだろうし、ユーザーはそのフォルダーに書き込みはできないであろう。

デフォルトでは、認証ユーザーに有効なパーミションは UNIX のモードではなく、前記 UARights
の機構のみに対応付けられる。この挙動は設定オプション [map acls](afp.conf#options-for-acl-handling)
で修正することができる。

しかしながら、Finder の“情報を見る”ウィンドウでもターミナルでも、ACL を見ることは不可能で、そこで見ているのは OS X で ACL
がどのように設計されたのかという結果である。もしクライアント上でも ACL
を表示させたいと思うならば、諸々を認証ドメイン（ディレクトリサービス、例えば、LDAP
やOpenDirectory）の一部と、より内包されているようにして、クライアント側でもサーバー側でもセットアップをおこなうべきである。
その理由は、macOS ACL が ただ、uid と gid だけでなく UUID と紐付いているためである。このため、afpd
は全てのファイルシステムの uid と git を UUID に紐付けできなければならない。そうすれば、afpd は macOS の UUID
に紐付けた UNIX uid と gid も含めたサーバー側の ACL を返すことができる。

Netatalk は LDAP クエリーを使ってディレクトリサーバーに問い合わせができる。ディレクトリサーバー（Active
Directory、Open Directory）が既にユーザーとグループの UUID 属性を提供している。 あるいはディレクトリサーバー（例えば
OpenLDAP）に使用されていない属性を再利用する（あるいは新たに追加する）のいずれかである。

より踏み込むと：

1.  ZFS を使っている Solarisの ZFS ボリュームごとに対して、

    Netatalk を使用したいと思っているあらゆるボリュームを ZFS ACL
    がわかるように構成すべきである：

        aclinherit = passthrough
        aclmode = passthrough

    このひとひねりが何をするのか、どのように適用するのか、についての説明は、ホストの
    ZFS ドキュメンテーション（例えば man zfs）を確認のこと。

2.  認証ドメイン

    サーバーとクライアントがセキュリティ連携の一部となっていて、ユーザー
    id データは共通のソースから出てこなければならない。Darwin の ACL は
    UUID に基づいている。なので、AFP 3.2 での ACL の仕様は Darwin の ACL
    である。故に id
    データのソースは全てのユーザーとグループの属性を提供できなければならない。ここで
    UUID は ASCII テキストとして保管されている。言い換えれば：

    - UUID を何らかの属性に保管している場合は Open Directory サーバーないしは LDAP サーバーが必要である。

    - クライアントはこのサーバーを使用するように構成されていなければならない。

    - サーバーは nsswitch と PAM 経由で使用されるよう構成しなければならない。

    - Netatalk が LDAP 検索クエリでユーザーとグループの UUID を引き出せるように、*afp.conf* 内で [ACL
      専用のオプション](afp.conf.html#options-for-acl-handling)を使って Netatalk
      を設定しなければならない。

### macOS の ACL

アクセス制御リスト (ACL) と共に、macOS は正統的な UNIX のパーミッションモデルの有力な拡張を提案した。 ACL
は、所定のユーザーあるいはグループのパーミッションのセットを明示的に許可したり拒否するアクセス制御エントリー (ACE) の番号つきリストである。

ユーザー ID、またはグループ ID と紐付いている UNIX パーミッションとは異なり、ACL は UUID
と紐付いている。この理由により、あるオブジェクトの ACL にアクセスすると、サーバーとクライアントは、UUID と ユーザー／グループ ID
間の変換をしてくれる、共通のディレクトリサービスを使うことを要求される。

ACL と UNIX のパーミションの相互関係は比較的シンプルなものである。ACL はオプションなので、UNIX
パーミションはアクセス制御のデフォルトのメカニズムの役割をする。オブジェクトの UNIX パーミションを変更しても ACL は手付かずのままで、ACL
の修正でもオブジェクトの UNIX パーミションは決して変更されない。アクセスチェックの間、macOS は最初に以下の順序で ACE
の評価をして、オブジェクトの ACL を検査する： 全てのリクエスト権限が許可されるまで、リクエストされた権限が ACE
によって明示的に拒否された、あるいはリストの最後までたどり着いた。である。ACL がない、あるいは ACL
に許可されたパーミションがリクエストを実行するのに十分でない場合、macOS は次にオブジェクトの UNIX パーミションの評価に入る。 つまり、ACL
は常に UNIX のパーミションより優先順位が上位ということである。

### ZFS の ACL

ZFS の ACL はほぼ macOS の ACL に匹敵するものである。 両者ともほぼ同一の良い粒度のパーミションと設定の継承が提供されている。

### POSIX の ACL

#### 概要

macOS あるいは NFSv4 の ACL と比較すると、Posix ACL は、伝統的な UNIX
パーミションの制限を打開するには異質で汎用性のないアプローチを表現している。実装は Posix 標準を取り込んだものを基礎としている。

Posix 1003.1e 標準では二つのタイプの ACL を定義している。ファイルとディレクトリは、
アクセスチェックのために問い合わせを受けるアクセス ACL を保持することができる。 ディレクトリはアクセスチェックには向いていないデフォルトの ACL
も保持することができる。デフォルトの ACL 付きでディレクトリの内側に新規オブジェクトが作成された時、デフォルトの ACL はそれがアクセス ACL
であるものとして新規オブジェクトに適用される。サブディレクトリは親ディレクトリのデフォルト ACL を継承する。
継承制御にそれ以上のメカニズムは何もない。

設計上、Posix ACL と macOS 間の違いに含まれている特筆すべき点は：

- パーミションモデルは何も細分化されていない。UNIX のパーミション同様、Posix ACLは読み込み、書き込み、そして実行権限を区別している。

- ACL 内のエントリーに順序はない。

- Posix ACLは権限を許可することしかできない。エントリーから権限を明示的に拒否する手立てはない。

- UNIX パーミションは特別なエントリーとして ACL に統合されている。

Posix 1003.1e は 6 つの異なるタイプの ACL エントリーを定義している。前半の 3 つは標準の UNIX
パーミションを統合するのに用いられている。これらは ACL として最小限の形であり、存在することは必須であり、
そして各々のタイプにつきたった一つのエントリーだけが ACL 内に許される。

- ACL_USER_OBJ：所有ユーザー（オーナー）のアクセス権限。

- ACL_GROUP_OBJ：所有グループ（オーナーグループ）のアクセス権限。

- ACL_OTHER：あらゆるユーザー・グループに対するアクセス権限。

残りのエントリーのタイプは伝統的パーミションモデルの拡張である：

- ACL_USER：あるユーザーに対するアクセス権を許可する。

- ACL_GROUP：あるグループに対するアクセス権を許可する。

- ACL_MASK：ACL_GROUP_OBJ、ACL_USER および ACL_GROUP
タイプのエントリーで許可されうるアクセス権の最大値を制限する。名前の示すように、このエントリーはマスクとして働く。一つの ACL あたり一個だけの
ACL_MASK エントリーが許される。もし ACL に、ACL_USER ないしは ACL_GROUP
エントリーが含まれているのであれば、ACL_MASK エントリーも存在しなければならない。さもなくば、ACL_MASK はオプションである。

ACL を意識していないアプリケーションとの互換性を維持のため、Posix 1003.1e は、オブジェクトの UNIX
パーミションを検索したり処理するシステムコールやユーティリティーのセマンティクスを変える。オブジェクトが必要最低限の ACL
のみ保持している場合、UNIX パーミションのグループパーミションビットは ACL_GROUP_OBJ エントリーの値に対応する。

しかしながら、もし ACL に ACL_MASK エントリーが含まれている場合、 上記システムコールやユーティリティーの挙動は異なるものとなる。UNIX
パーミションのグループパーミションビットは ACL_MASK エントリーの値に対応する、すなわち、"chmod g-w"
の呼び出しは、グループに対する書き込みアクセスを無効にするだけでなく、 ACL_USER ないしは ACL_GROUP
エントリーによって許可されていた書き込みアクセスのエンティティ全てを無効にするのである。

#### POSIX ACL から macOS の ACL へのマッピング

クライアントがオブジェクトの ACL を読み込もうとした時、afpd は Posix ACL からそれに等価な macOS の ACL
にマップする。オブジェクトの ACL の書き込みには afpd が macOS の ACL を Posix ACL
にマップすることが要求される。Posix ACL の設計上の制約から、マッピングを経た結果がオリジナルの ACL
のセマンティクスと概ね同じになるような正確なマッピングを見出すことは通常不可能である。

- afpd はパーミション一式を拒否したエントリーを通告なしに破棄する。これは Posix の設計では表現する手立てがないためである。

- Posix ACL ではエントリーが順序付きではないので、順序を保管するのは不可能である。

- 継承制御もまた厳しい制限を受けやすい：

  - only_inherit フラグが設定されたエントリーはディレクトリのデフォルト ACL の一部にしかならない。

  - 少なくとも file_inherit、directory_inherit ないしは limit_inherit
    のうち一つが設定されたエントリーはディレクトリアクセスとデフォルト ACL の一部分となる。しかし継承に課せられた制約は無視される。

- Posix 側により細分化されたパーミションモデルがないことで、 結果としては通常は許可されるパーミションが増えるという結果になる。

macOS クライアントは Posix 1003.1e 特有の UNIX パーミションと ACL_MASK との関係を意識していないので、afpd
は互換性問題を回避するためにこの機能をクライアントに公開せず、そして afpd は \*unix パーミションと ACL をアップルの AFP
用リファレンス実装がするのと同じ方法で扱う。オブジェクトの UNIX パーミションがリクエストされた時、afpd
は適切なグループ権限を算出し、FPUNIXPrivs 構造の "permissions" と "ua_permissions"
要素を介し、オーナーおよび全ての者のアクセス権限も共に付して、リクエストした側に結果を返す。（Apple Filing Protocol
Reference の 181 ページ参照） オブジェクトのパーミションを変更すると、afpd は常に
ACL_USER_OBJ、ACL_GROUP_OBJ および ACL_OTHERS を更新する。もし ACL_MASK
エントリーも存在すれば、新しいグループの権限が有効になり、かつ、既存の ACL_USER あるいは ACL_GROUP
型のエントリーは手付かずになるような ACL_MASK の値の再計算を afpd が行う。

## ファイルシステム変更イベント

Netatalk には素敵なファイルシステム変更イベント (Filesystem Change Events, FCE)
機構が含まれている。ここで、afpd プロセスは、なにがしかのファイルシステムイベントについて、関心を寄せているリスナーに、UDP
ネットワークデータグラム経由で通知する。

この機能はデフォルトでは無効になっている。有効にするには、afp.conf の **fce listener** オプションを、FCE
イベントを受け取るべきホストのホスト名または IP アドレスに設定する。

Netatalk には、UDP データグラムを受信した AFP サーバーについての情報を出力する簡単な FCE リスナーアプリケーション
**fce_listen** が含まれている。このアプリケーションのソースコードは、UDP パケットのフォーマットについてのドキュメントとしても役立つ。

### FCE v1

現在サポートされているファイルシステム変更イベントは以下である：

- ファイル変更：file modification (fmod)

- ファイル削除：file deletion (fdel)

- ディレクトリ削除：directory deletion (ddel)

- ファイル作成：file creation (fcre)

- ディレクトリ削除：directory deletion (ddel)

### FCE v2

FCE v2 イベントは、アクションを実行したユーザーなどの追加のコンテキストを提供する。FCE v2 を使用する場合は、以下のイベントも取得できる：

- ファイル移動 (fmov)

- ディレクトリー移動 (dmov)

- ユーザーログイン (login)

- ユーザーログアウト (logout)

## Spotlight Compatible Search

**spotlight** オプションを使って、グローバルで、あるいは、ボリューム単位ごとに Netatalk の Spotlight
互換検索とインデックス化を有効にできる。

> **警告**

> 一旦 Spotlight をどこか単一のボリュームで有効にすると、Spotlight
が無効にされたことになるその他全てのボリュームでは全く検索できないようになる。

The **dbus-daemon** バイナリは Spotlight 機能のためにインストールしなければならない。dbus-daemon へのパスは
"configure" の with-dbus-daemon オプションで決定する。

**dbus-daemon** バイナリが、他のパスにインストールされている場合、 パスを指示するためにグローバルオプション **dbus
daemon** を用いなければならない。例えば Solaris 上で OpenCSW 由来の Tracker を用いている場合は以下のようにする：

    dbus daemon = /opt/csw/bin/dbus-daemon
