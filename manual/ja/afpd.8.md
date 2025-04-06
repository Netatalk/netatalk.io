# 名前

afpd — Apple Filing Protocol デーモン

# 概要

`afpd [-d] [-F configfile]`

`afpd [ -v | -V | -h ]`

# 説明

**afpd**はUnixファイルシステムにApple Filing Protocol (AFP)インターフェースを提供する。これは通常、**netatalk**(8)によってブート時に起動される。

**afpd**はファイルサーバの挙動と設定を決めるために*afp.conf*を利用する。

# オプション

**-d**

> デーモンをターミナルから切り離さない。

**-v**

> バージョン情報を出力して終了する。

**-V**

> 詳細情報を表示してから終了する。

**-h**

> ヘルプを表示してから終了する。

**-F** <configfile\>

> 利用する設定ファイルを指定する。

# シグナル

最終手段を除いて、ユーザの**afpd**をシャットダウンするために*SIGKILL
(-9)*を使うのは推奨しない。なぜなら、CNIDデータベースが矛盾したままになるかもしれないからである。**afpd**を終了する安全な方法は、*SIGTERM
(-15)*シグナルを送ってそれ自身が停止するのを待つことである。

メインの**afpd**プロセスにSIGTERMやSIGUSR1を送れば子プロセスに伝わるので、全部に作用するだろう。

SIGTERM

> きれいに終了する。マスタプロセスから子プロセスに伝わる。

SIGQUIT

> マスタ**afpd**にこれを送ると全ての子プロセスを終了する。休止時間なしでAFPサービスを実施するのに使われる。

SIGHUP

> afpdに*SIGHUP*を送ると設定ファイルを再読み込みする。

SIGINT

> 子プロセスの**afpd**に*SIGINT*を送ると、このプロセスの*max_debug*ログを有効にする。ログは*/tmp/afpd.PID.XXXXXX*に送られる。更に*SIGINT*を送ると元のログ設定に戻る。

SIGUSR1

> **afpd**プロセスはクライアントに「The server is going down for
maintenance.」というメッセージを送り、5分後に自身を終了する。新規接続を許さない。子プロセスのafpdにこれを送った場合、他の子プロセスには影響しない。それでもメインプロセスは終了するだろうし、全ての新規接続は無効になる。

SIGUSR2

> **afpd**プロセスはビルド時に設定したメッセージディレクトリの下のmessage.pidという名前のファイルを探する。発見したプロセスについて、その内容をメッセージとして対応するAFPクライアントに送る。メッセージを送った後にファイルは削除される。このシグナルは子プロセスの**afpd**にのみ送るべき。

# ファイル

*afp.conf*

> afpdが使う設定ファイル

*afp_signature.conf*

> サーバシグネチャのリスト

*afp_voluuid.conf*

> Time MachineボリュームのUUIDのリスト

*extmap.conf*

> ファイル名拡張子マッピング

*message.pid*

> ユーザへ送るメッセージの内容。

# 関連項目

netatalk(8), hosts_access(5), afp.conf(5), afp_signature.conf(5),
afp_voluuid.conf(5), extmap.conf(5), dbd(1)

# 著者

[CONTRIBUTORS](https://netatalk.io/contributors) を参照
