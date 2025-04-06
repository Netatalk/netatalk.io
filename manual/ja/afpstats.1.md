# 名前

afpstats — AFP サーバの利用状況を参照する

# 概要

**afpstats**

# 説明

**afpstats** は接続中のユーザ、マウント中のボリュームなどの利用状況が参照できる。

# 注記

**afpd**がD-Busをサポートしなければならない。"**afpd -V**"でそれをチェックしてください。

その上、*afp.conf* で"**afpstats = yes**"を設定しなければならない。

# 例

    $ afpstats
    Connected user   PID      Login time        State          Mounted volumes
    sandy            452547   Apr 28 21:58:50   active         Test Volume, sandy's Home
    charlie          451969   Apr 28 21:21:32   active         My AFP Volume

# 関連項目

afpd(8), afp.conf(5), dbus-daemon(1)

# 著者

[CONTRIBUTORS](https://netatalk.io/contributors) を参照
