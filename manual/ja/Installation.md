# インストール

> 【警告】 以前のバージョンからNetatalk 4にアップグレードする前に、
このマニュアルの[アップグレード](Upgrading.html)の章を必ずお読みください。

## Netatalk の入手の仕方

この件の最新の情報は [netatalk のホームページ](https://netatalk.io) を一読いただきたい。

### バイナリーパッケージ

Netatalk のバイナリーパッケージは、いくつかの Linux、BSD、Solaris
ディストリビューションに含まれている。通常の配布元も見たいだろうと思う。

既知の Netatalk パッケージのリストは [Repology の Netatalk
ページ](https://repology.org/project/netatalk/versions) を見るとよい。

第三者が提供しているパッケージ リポジトリも参照する手もある。例えば、Red Hat 派生 Linux ディストリビューションの為の
[rpmfind](https://rpmfind.net/)、 Solaris 系 OS の為の
[OpenCSW](https://www.opencsw.org/)、そして macOS の為の
[Homebrew](https://brew.sh/) か [MacPorts](https://www.macports.org/)。

### ソースパッケージ

tar で固めた Netatalk 安定版ソースコードは [GitHub の Netatalk
リリースページ](https://github.com/Netatalk/netatalk/releases)にある。

ソースコードは [Netatalk Git リポジトリ](https://github.com/Netatalk/netatalk) からも入手できる。

ソースコードから Netatalk をビルドする方法については
[インストールクイックスタート](https://netatalk.io/install) を参照のこと。

## 前提条件

Netatalk は、いくつかのサードパーティのライブラリとユーティリティに依存している。Netatalk
をビルドする前に、いくつかの必須パッケージをインストールする必要がある。さらに、機能を強化するためにいくつかのオプションパッケージをインストールすることができる。

### 必要なサードパーティソフトウェア

- bstring

    Netatalk は、メモリセーフな文字列データの操作と取得のために「Better String Library」を活用している。
    Mike Steinert氏の [bstring](https://github.com/msteinert/bstring) 
    フォークのバージョン 1.0.1 以降を推奨するが、
    Paul Hsieh氏によるオリジナルの [bstrlib](https://bstring.sourceforge.net/) 
    ライブラリのどのバージョンでも、理論的には同様に動作するはず。

    共有 *bstring* ライブラリがない場合、Netatalk ビルドシステムはライブラリを 
    Meson サブプロジェクトとしてビルドおよびインストールする。

- iniparser

    iniparser ライブラリは設定ファイルを解析するために使用される。
    最低でもバージョン 3.1 が必要であり、4.0 以降が推奨される。

- libevent

    netatalk サービス コントローラー デーモンの内部イベント
    コールバックは、 libevent バージョン 2 に基づいて構築されている。

- Libgcrypt

    [Libgcrypt](https://gnupg.org/software/libgcrypt/)
    ライブラリは、標準のユーザー認証モジュール (UAM)
    の暗号化を提供する。これらは、DHX2、DHCAST128 (別名 DHX)、および
    RandNum である。

#### CNID データベースバックエンド一覧

CNIDスキームを有効するには、以下のデータベースライブラリの少なくとも1つが必要になる。いずれか1つがない場合は、*last*
バックエンドのみ利用可能となりるが、これは読み取り専用モードで動作するため、日常的な使用には推奨しない。

- Berkeley DB

    デフォルトのdbd CNIDバックエンドは、Berkeley DBを使用して一意のファイル識別子を保存します。
    書き込みの時に最低でもバージョン 4.6 が必要となる。

    推奨バージョンは 5.3 である Sleepycat
    ライセンスで提供された最終リリースである。

- MySQL または MariaDB

    MySQL 互換のクライアント ライブラリを活用することで、netatalk
    は、スケーラビリティと信頼性に優れた MySQL CNID
    バックエンドを使用して構築できる。管理者は、このバックエンドで使用するために別のデータベース
    インスタンスを用意する必要がある。

- SQLite v3

    SQLite ライブラリ バージョン3は、SQLite CNID バックエンドが有効にする。
    設定不要の代替バックエンドである。
    本バックエンドは**実験的**であり、テスト目的でのみ使用すること。

### 任意のサードパーティソフトウェア

Netatalk はその機能性を拡充するために以下のサードパーティソフトウェアを使用することができる。

- ACL と LDAP

    LDAPは、ACLの高度な権限スキームと連携して動作するオープンで業界標準のユーザー
    ディレクトリ プロトコルである。一部のオペレーティング システムではACL
    とLDAPライブラリがシステムに組み込まれているが、他のオペレーティング
    システムではこの機能を有効にするためにサポート
    パッケージをインストールする必要がある。

- Bonjour 用の Avahi または mDNSresponder

    Mac OS X 10.2 以降では、自動サービス検出に Bonjour (別名 Zeroconf)
    を使用する。 Netatalk は、Avahi または mDNSResponder を使用して AFP
    ファイル共有と Time Machine ボリュームをアドバタイズできる。

    Avahi を使用する場合は、D-Bus または D-Bus サポートを有効になっている
    Avahi ライブラリは必要になる。

- cmark、cmark-gfm、またはpandoc

    Netatalk のドキュメントはMarkdown形式で作成されている。
    マニュアルページのソースは標準に準拠したCommonMarkで構成され、
    ドキュメントの残りの部分はGitHub風の Markdown (gfm)で作成されている。

    pandocライブラリは最もきれいな出力を生成するが、他の2つのオプション
    よりもはるかにリソースを消費する。cmarkのリファレンス実装が最も広く配布
    されているが、cmark-gfm はテーブルのようなGitHub拡張機能をよりよく扱う。

- CrackLib

    Random Number UAM と netatalk 独自の **afppasswd** パスワード
    マネージャを使用する場合、CrackLib は netatalk
    での認証に弱いパスワードを設定するのを防ぐのに役立つ。

    別途配布されることもある CrackLib dictionaryパッケージ
    もコンパイル時にも実行時にも必須である。

- D-Bus

    D-Bus はプロセス間にメッセージを通信するメカニズムを提供し、下記
    Netatalk 機能に使われる： Spotlight、Avahi を使用した Zeroconf、および
    **afpstats** ツール。

- GLib および GIO

    D-Bus とのインターフェースとして、**afpstats** ツールに使われる。

- iconv

    iconv は、多くの文字エンコードの変換ルーチンを提供する。Netatalk
    は、ISO-8859-1
    など、組み込みの変換がない文字セットを提供するためにこれを使用する。glibc
    システムでは、Netatalk は glibc が提供する iconv
    実装を使用できる。それ以外の場合は、GNU libiconv 実装を使用できる。

- Kerberos V

    Kerberos v5 は、マサチューセッツ工科大学で発明されたクライアント
    サーバー ベースの認証プロトコルである。Kerberos
    ライブラリを使用すると、netatalk は既存の Kerberos
    インフラストラクチャでの認証用に GSS UAM ライブラリを作成できる。

- PAM

    PAM は、ユーザーを認証するための柔軟なメカニズムを提供する。 PAM は
    SUN Microsystems
    によって発明された。Linux-PAM は、ローカル
    システム管理者がアプリケーションによるユーザー認証方法を選択できるようにする共有ライブラリ
    スイートである。

- Perl

    Netatalk の管理ユーティリティ スクリプトは、Perl ランタイム バージョン
    5.8 以降に依存する。必須 Perl モジュールは以下： *IO::Socket::IP*
    (asip-status) 又は *Net::DBus* (afpstats)。

- po4a

    po4a の助けを借りて、Netatalk のドキュメントは他の言語に翻訳できる。gettext
    を使用して、ソース ファイルから翻訳可能な文字列を抽出し、PO
    ファイルに保存されている翻訳と結合する。

- TCP ラッパー

    Wietse Venema のネットワーク ロガー。TCPD または LOG_TCP とも呼ばれる。

    セキュリティオプションは次のとおり。
    ホスト、ドメイン、および/またはサービスごとのアクセス制御、ホスト名のスプーフィングまたはホスト
    アドレスのスプーフィングの検出。ブービートラップを使用して早期警告システムを実装する。

- LocalSearch または Tracker

    Netatalk は、Spotlight 互換の検索インデックスのメタデータバックエンドとして、
    [GNOME LocalSearch](https://gnome.pages.gitlab.gnome.org/localsearch/index.html)
    （以前は Tracker）バージョン3以降を使用する。

- talloc / bison / flex

    Spotlight には、Samba の talloc ライブラリ、bison などの Yacc
    パーサー、flex などのレキサーも必要。

- UnicodeData.txt

    Netatalk の Unicode 文字変換テーブルを再生成するには、
    [Unicode 文字データベース](https://www.unicode.org/Public/UNIDATA/UnicodeData.txt)
    が必要である。

    これは、開発者やパッケージ マネージャーが Netatalk の Unicode 
    文字変換テーブルを再生成したい場合に関連する。

## Netatalk の起動と停止

Netatalk ディストリビューションには、コンパイル前にビルド システムに指定されたオプションに応じて調整される、オペレーティング
システム固有の起動スクリプト テンプレートがいくつか付属している。現在、テンプレートは、一般的な Linux ディストリビューション、BSD
バリアント、Solaris 派生、および macOS 用のプラットフォーム固有のスクリプトに加えて、systemd、openrc 用に提供されている。

ソースからビルドする場合、Netatalk ビルド システムは、どの
initスタイルがプラットフォームに適しているかを検出しようとする。また、**with-init-style**オプションを指定して、必要な特定のタイプの起動スクリプト
をインストールするようにビルドシステムを構成することもできる。構文については、ビルド システムのヘルプテキストを参照してください。

新しい Linux、\*BSD、および Solaris
のようなディストリビューションが定期的に登場し、上記の他のシステムの起動手順も変更される可能性があるため、起動スクリプトを盲目的にインストールするのではなく、まずシステムで機能することを確認することをお勧めする。

Linux ディストリビューション、RPM、または BSD パッケージなどの固定セットアップの一部として Netatalk
を使用する場合は、おそらく適切に準備されているだろう。したがって、前の段落は、Netatalk を自分でコンパイルした人にほとんど当てはまる。

次のデーモンは、使用するスタートアップ スクリプト メカニズムによって起動する必要がある:

- netatalk

スタートアップ スクリプトがない場合は、このデーモンを直接 (root として)  起動し、使い終わったら SIGTERM で終了することもできる。

さらに、構成ファイル *afp.conf* が適切な場所にあることを確認してください。 **netatalk -V**
コマンドを実行すると、netatalk がファイルの場所を予測しているかどうかを問い合わせることができる。

AppleTalk サービスを実行する場合は、**atalkd** デーモンに加えて、オプションの
**papd**、**timelord**、**a2boot** デーモンも起動する必要がある。詳細については、このマニュアルの
[AppleTalk](AppleTalk.html) の章を参照してください。
