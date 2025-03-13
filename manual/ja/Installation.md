# インストール

> **警告**

> Netatalk 2 または 3 から Netatalk 4
にアップグレードする前に、このマニュアルの[アップグレード](Upgrading.html)
の章を必ずお読みください。

## Netatalk の入手の仕方

この件の最新の情報は [netatalk のホームページ](https://netatalk.io) を一読いただきたい。

### バイナリーパッケージ

Netatalk のバイナリーパッケージは、いくつかの Linux、BSD、Solaris
ディストリビューションに含まれている。通常の配布元も見たいだろうと思う。

第三者が提供しているパッケージ リポジトリも参照する手もある。例えば、Red Hat 派生 Linux ディストリビューションの為の
[rpmfind](https://rpmfind.net/)、 Solaris 系 OS の為の
[OpenCSW](https://www.opencsw.org/)、そして macOS の為の
[Homebrew](https://brew.sh/) か [MacPorts](https://www.macports.org/)。

### ソースパッケージ

#### ターボール

tar で固めた Netatalk 安定版ソースコードは [GitHub の Netatalk
リリースページ](https://github.com/Netatalk/netatalk/releases)にある。

#### Git

Git レポジトリ のダウンロードは迅速で容易である：

1.  Git がインストールしてあることを確認する。**which git** は git のパスを示してくれるはずである。

        $ which git
        /usr/bin/git

2.  ソースを取得してみよう。

        $ git clone https://github.com/Netatalk/netatalk.git netatalk-code
        Cloning into 'netatalk-code'...
        remote: Enumerating objects: 41592, done.
        ...
        Resolving deltas: 100% (32227/32227), done.

    上記で Git リポジトリから、Netatalk
    のソース全体の完全でまっさらのコピーを含む *netatalk-code*
    という名前のローカルディレクトリが作成される。

3.  ブランチやタグを指定しない場合は、最先端の開発コードが取得さる。例えば、最新の安定した Netatalk 3.1
    コードを入手するには、「branch-netatalk-3-1」という名前のブランチをチェックアウトする：

        $ git checkout branch-netatalk-3-1

4.  レポジトリのコピーを最新の状態にしておきたい場合、適宜以下を実行する。

        $ git pull

## Netatalk のコンパイル

### 前提条件

#### 必要なサードパーティソフトウェア

- Berkeley DB

    デフォルトのdbd CNIDバックエンドは、Berkeley DBを使用して一意のファイル識別子を保存します。書き込みの時に最低でもバージョン 4.6 が必要となる。

    推奨バージョンは 5.3 である Sleepycat
    ライセンスで提供された最終リリースである。

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

#### 任意のサードパーティソフトウェア

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

- cmark もしくは cmark-gfm

    Netatalk のドキュメントは Markdown 形式で作成されている。
    マニュアル ページのソースは標準に準拠した CommonMark で構成され、
    ドキュメントの残りの部分は GitHub 風の Markdown (gfm) で作成されている。

    cmark を使用して Markdown ソースから roff マニュアル ページを生成し、cmark-gfm を使用して HTML ページを含むすべてのドキュメントを生成できる。
    後者は利用可能な場合は、前者は必要ない。

- CrackLib

    Random Number UAM と netatalk 独自の **afppasswd** パスワード
    マネージャを使用する場合、CrackLib は netatalk
    での認証に弱いパスワードを設定するのを防ぐのに役立つ。

    ランタイム パッケージで別途配布されることもある CrackLib
    辞書も必須である。

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

- MySQL または MariaDB

    MySQL 互換のクライアント ライブラリを活用することで、netatalk
    は、スケーラビリティと信頼性に優れた MySQL CNID
    バックエンドを使用して構築できる。管理者は、このバックエンドで使用するために別のデータベース
    インスタンスを用意する必要がある。

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

    セキュリティオプションは次のとおり。ホスト、ドメイン、および/またはサービスごとのアクセス制御、ホスト名のスプーフィングまたはホスト
    アドレスのスプーフィングの検出。ブービートラップを使用して早期警告システムを実装する。

- Tracker もしくは TinySPARQL / LocalSearch

    Netatalkは、Spotlight検索インデックスのメタデータ バックエンドとして
    [Tracker](https://tracker.gnome.org) またはそれ以降のバージョンである
    TinySPARQL/[LocalSearch](https://gnome.pages.gitlab.gnome.org/localsearch/)
    を使用する。必要な最小限のバージョンは 0.7 である。これは
    [SPARQL](https://gnome.pages.gitlab.gnome.org/tracker/)
    をサポートする最初のバージョンだからである。

- talloc / bison / flex

    Spotlight には、Samba の talloc ライブラリ、bison などの Yacc
    パーサー、flex などのレキサーも必要。

- UnicodeData.txt

    ビルド システムは、Perl と Unicode 文字データベースを使用して、NetatalkのUnicode
    文字変換ソースを生成する。

### Netatalk のコンパイル

ビルドシステムの使い方、コードのコンフィグ又はビルドの手順書は [Install Quick Start](/install.html)
というのがあるので、ご参考まで。

特定の OS に対しての具体的なビルド事例は [Netatalk をソースコードからコンパイルする](Compilation.html)
付録を参考してください。

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
