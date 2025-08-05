# 名前

afp_logintest — AFP認証とDSIセッションテストスイート

# 概要

**afp_logintest** [-1234567CmVv] [-h *host*] [-p *port*] [-s *volume*] [-u *user*] [-w *password*]

# 説明

**afp_logintest** は、DSIセッションとAFPクライアントからの認証のためのテストスイートである。
AFPサーバーとのDSIセッションを確立するための様々なハッピーパステストとコーナーケーステストを実行し、
利用可能なUAMのサブセットを使用してユーザー認証を行う。

# オプション

**-1**
: AFP 2.1プロトコルバージョンを使用する

**-2**
: AFP 2.2プロトコルバージョンを使用する

**-3**
: AFP 3.0プロトコルバージョンを使用する

**-4**
: AFP 3.1プロトコルバージョンを使用する

**-5**
: AFP 3.2プロトコルバージョンを使用する

**-6**
: AFP 3.3プロトコルバージョンを使用する

**-7**
: AFP 3.4プロトコルバージョンを使用する

**-C**
: 端末出力でANSIカラーをオフにする

**-h** *host*
: サーバーのホスト名またはIPアドレス（デフォルト: localhost）

**-m**
: Mac OS ネイティブ AFP サーバー互換モードでテストを実行する

**-p** *port*
: サーバーポート番号（デフォルト: 548）

**-u** *ユーザー名*
: 認証用のユーザー名

**-v**
: 詳細出力

**-V**
: 超詳細出力

**-w** *パスワード文字列*
: 認証用のパスワード

# 前提条件

ゲスト認証とクリアテキスト認証をテストするには、それぞれ *uams_guest* と *uams_clrtxt.so* UAM を使用するように
netatalk を設定する必要がある。下記事例の通り、netatalk の afp.conf で UAM を設定する。

    [Global]
    uam list = uams_clrtxt.so uams_guest.so

さらに、非ゲスト認証をテストするには、ユーザー名とパスワードをテストランナーに渡す必要がある。

# 例

10.0.0.10で実行されているAFPサーバーに対して、ユーザー認証なしですべてのテストを実行する。

    $ ./build/test/testsuite/afp_logintest -h 10.0.0.10
    Logintest:test1: DSI with no open session - PASSED
    Logintest:test2: DSI with open session - PASSED
    Logintest:test3: Guest login - PASSED
    Logintest:test5: Clear text login - SKIPPED (username/password for the AFP server)
    Logintest:test6: DSIOpenSession non zero parameter should be ignored by the server - SKIPPED (username/password for the AFP server)

# 関連項目

**afp_lantest**(1), **afp_spectest**(1), **afparg**(1), **afpd**(8)
