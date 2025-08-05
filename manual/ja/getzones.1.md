# 名前

getzones — AppleTalk ゾーン名を一覧表示する

# 概要

**getzones** [-g | -l | -m | -q network | -z *zone*] [-c *Mac charset*] [*address*]

# 説明

*Getzones* は、Zone Information Protocol (ZIP) を使用して AppleTalk
ゾーン名のリストを取得するために使用される。GetZoneList 要求を
AppleTalk ルーターに送信する。デフォルトでは、ローカルで実行されている
**atalkd**(8) にリクエストを送信する。

# オプション

**-g**

> 現在のネットワークの現在のデフォルトゾーンと有効なネットワーク範囲を取得する。
これは、ZIP形式のGetNetInfoリクエストを送信することで実現される。
GetNetInfoに応答するのはシードルータのみであるため、通常はブロードキャストで送信する。

**-l**

> ローカル ゾーンを一覧表示する。これは、GetLocalZones
要求を送信することで実現される。

**-m**

> ローカル ゾーンの名前のみを一覧表示する。これは、ZIP GetMyZone
リクエストを送信することで実現される。

**-q**

> 特定のネットワーク範囲で利用可能なゾーンを一覧表示する。
これは、ZIPクエリを送信することで実現される。
拡張ネットワークで利用可能なゾーンをクエリする場合は、通常、範囲内の最初のネットワーク番号を使用する必要がある。

**-z**

> GetNetInfoを送信して、*zone* がこのネットワークに対して有効なゾーンであるかどうかを確認する。
*zone* が有効な場合は 0 で終了し、*zone* が無効の場合は 2 で終了する。
また、ゾーンが無効な場合は要求されたゾーンの代わりに使用するデフォルトのゾーンを含むネットワーク構成を出力する。

**-c**

> ゾーン名を解釈する際に使用するMacintosh文字セットを設定する。
指定しない場合は、デフォルトでMacRomanが使用される。

*address*

> AppleTalk ルーターに *address* で接続する。 *address*
は、**atalk_aton**(3) によって解析される。

# 例

AppleTalkインターネットワーク上のすべてのゾーンを表示する：

    example$ getzones
    Ethernet
    LocalTalk
    AirTalk
    example$

このネットワークをシードしているルータから現在のネットワークのデフォルトのゾーンとネットワーク構成を取得する。

    example$ getzones -g 0.255
    Network range: 3-10
    Flags (0xa0): requested-zone-invalid only-one-zone
    Requested zone: 
    Zone multicast address: 09:00:07:00:00:a8
    Default zone: Ethernet
    example$
    
OtherNetが現在のネットワークの有効なゾーンであるかどうかを確認する：

    example$ getzones -z Othernet 0.255 >/dev/null || echo "bad zone"
    bad zone
    example$

# 関連項目

atalk_aton(3), atalkd(8)

# 著者

[CONTRIBUTORS](https://netatalk.io/contributors) を参照
