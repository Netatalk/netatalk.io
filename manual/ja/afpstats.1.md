# 名前

afpstats — netatalk AFP サーバの利用状況を参照する

# 概要

**afpstats**

# 説明

**afpstats** は netatalk AFP サーバに接続しているユーザ、そのマウントされたボリューム、ログイン時間に関する情報を一覧表示する。

# 注記

この機能を利用するには、**afpd** が AFP 統計サポートでビルドされている必要があり、これは "**afpd -V**"
で確認できる。さらに、ホストは D-Bus を実行しており、通常 netatalk に付属の *netatalk-dbus.conf*
という設定ファイルを通じて有効になる *org.netatalk.AFPStats* サービスを定義するポリシーで構成されている必要がある。

最後に、実行時に netatalk で AFP 統計を有効にするには、"**afpstats = yes**" を *afp.conf*
に設定する必要がある。

# 例

    $ afpstats
    Connected user   PID      Login time        State          Mounted volumes
    alice            452547   Apr 28 21:58:50   active         Test Volume, alice's Home
    charlie          451969   Apr 28 21:21:32   active         My AFP Volume

# 関連項目

afpd(8), afp.conf(5), dbus-daemon(1)

# 著者

[CONTRIBUTORS](https://netatalk.io/contributors) を参照
