# 名前

rtmpqrt - AppleTalkルーティング情報を照会する

# 概要

**rtmpqry** [-a | -r] [ -A local_address ] [remote_address]

# 説明

**rtmpqry** は、AppleTalk ルーターが RTMP プロトコルを使用してアドバタイズしている
ルーティング情報を照会し、表示するために使用される。デフォルトでは、ローカルの atalkd インスタンスに照会する。

# オプション

**-a**

> すべてのルートを照会し、スプリットホライズン処理によってドロップされるルートは抑制しない。
一般的に（このオプションが省略されている場合も）、ルータは、意味はないためにパケットを送信した場合に
そのパケットが同じインターフェースから別のルータに直接返送されるようなルートをアドバタイズしない。
ただし、インターネットワークの構造を可視化するために、すべてのルートを確認することが有用な場合がある。

**-r**

> ルートではなく、RTMPネットワークメタデータのみをリクエストする。

**-A**

> 指定されたローカルAppleTalkアドレスにバインドする。

# 例

現在のネットワークのネットワーク範囲とシードルーターを取得する：

    example$ rtmpqry -r 0.255
    Router: 9.239
    Network(s): 3 - 10
    example$

12.1 のルータからすべてのルートを取得する：

    example$ rtmpqry -a 12.1
    3 - 10 distance 0 via 12.1
    11 distance 0 via 12.1
    12 distance 0 via 12.1

    example$

# 関連項目

atalk_aton(3), atalkd(8), getzones(1)

# 著者

[CONTRIBUTORS](https://netatalk.io/contributors) を参照
