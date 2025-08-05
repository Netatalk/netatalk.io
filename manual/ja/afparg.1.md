# 名前

afparg — AFPサーバーにコマンドを送信する

# 概要

**afparg** [-1234567lVv] [-h *host*] [-p *port*] [-s *volume*] [-u *user*] [-w *password*] [-f *command*]

# 説明

**afparg** は、認証されたユーザーで AFP サーバーにコマンドを送信するためのシンプルなツールである。
サーバー上のファイルを検査したり、簡単なファイル操作を実行したりするために使用できる。

使用可能なコマンドとその引数の一覧を表示するには、*afparg -l* を実行してください。

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

**-f** *コマンド* *引数*
: 実行するコマンド

**-h** *host*
: サーバーのホスト名またはIPアドレス（デフォルト: localhost）

**-l**
: 利用可能なコマンドを一覧表示して終了する

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

# 設定

テストランナーの AFP クライアントは現在 ClearTxt UAM のみをサポートしている。netatalk の afp.conf で UAM
を設定する。

    [Global]
    uam list = uams_clrtxt.so

# 例

利用可能なコマンドとその引数を一覧表示する

    $ afparg -l
    FPResolveID CNID
    FPEnumerate dir
    FPCopyFile source dest
    FPLockrw d | r file
    FPLockw d | r file

CNIDをファイル名に解決する

    $ afparg -h 10.0.0.8 -u myuser -w mypass -s "test volume" -f FPResolveID 18
    ======================
    FPResolveID with args:
    Trying to resolve id 18
    Resolved ID 18 to: 'AFP_Reference.pdf'

共有ボリューム上のディレクトリ内のファイルを一覧表示する

    $ afparg -h 10.0.0.8 -u myuser -w mypass -s "test volume" -f FPEnumerate "my dir"
    file1
    file2

共有ボリューム上のファイルのコピーを作成する

    $ afparg -h 10.0.0.8 -u myuser -w mypass -s "test volume" -f FPCopyFile AFP_Reference.pdf AFP_Reference2.pdf
    ======================
    FPCopyFile with args:
    source: "AFP_Reference.pdf" -> dest: "AFP_Reference2.pdf"

読み取り/書き込みロックでファイルのデータフォークを開く

    $ afparg -h 10.0.0.8 -u myuser -w mypass -s "test volume" -f FPLockrw d AFP_Reference2.pdf
    ======================
    FPOpen with read/write lock
    source: "AFP_Reference2.pdf"

# 関連項目

**afp_logintest**(1), **afp_spectest**(1), **afpd**(8)
