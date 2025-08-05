# 名前

fce_listen — Netatalk ファイルシステム変更イベントリスナーアプリケーション

# 概要

**fce_listen** [-h *host*] [-p *port*]

# 説明

**fce_listen** は、Netatalk の Filesystem Change Event (FCE) プロトコルのシンプルなリスナーである。
AFP サーバーから受信した UDP データグラムを標準出力に出力する。

# オプション

**-h** *ホスト*
: サーバーのホスト名またはIPアドレス

**-p** *ポート*
: サーバーポート番号

# 例

afp.conf で、netatalk が localhost のポート58585のリスナーに FCE パケットを送信するように設定する。

    [Global]
    fce listener = localhost:58585
    fce version = 2
    fce events = fmod,fdel,ddel,fcre,dcre,fmov,dmov,login,logout

localhost のポート58585で FCE イベントをリッスンする

    $ fce_listen -h localhost -p 58585
    Listening for Netatalk FCE datagrams on localhost:58585...
    FCE Start
    ID: 1, Event: FCE_LOGIN, pid: 429918, user: nobody, Path: 
    ID: 2, Event: FCE_LOGOUT, pid: 429918, user: nobody, Path: 
    FCE Start
    ID: 1, Event: FCE_LOGIN, pid: 429924, user: myuser, Path: 
    ID: 2, Event: FCE_FILE_DELETE, pid: 429924, user: myuser, Path: /srv/afpme/Read Me First copy
    ID: 3, Event: FCE_DIR_CREATE, pid: 429924, user: myuser, Path: /srv/afpme/untitled folder
    ID: 4, Event: FCE_DIR_MOVE, pid: 429924, user: myuser, source: /srv/afpme/untitled folder, Path: /srv/afpme/My Folder
    ID: 5, Event: FCE_FILE_MOVE, pid: 429924, user: myuser, source: /srv/afpme/LICENSE, Path: /srv/afpme/My Folder/LICENSE

# 関連項目

**afpd**(8)
