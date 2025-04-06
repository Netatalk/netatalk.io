# 名前

getzones — AppleTalk ゾーン名を一覧表示する

# 概要

`getzones [ -m | -l ] [address]`

# 説明

*Getzones* は、Zone Information Protocol (ZIP) を使用して AppleTalk
ゾーン名のリストを取得するために使用される。GetZoneList 要求を
AppleTalk ルーターに送信する。デフォルトでは、ローカルで実行されている
**atalkd**(8) にリクエストを送信する。

# オプション

**-m**

> ローカル ゾーンの名前のみを一覧表示する。これは、ZIP GetMyZone
リクエストを送信することで実現される。

**-l**

> ローカル ゾーンを一覧表示する。これは、GetLocalZones
要求を送信することで実現される。

*address*

> AppleTalk ルーターに *address* で接続する。 *address*
は、**atalk_aton**(3) によって解析される。

# 関連項目

atalk_aton(3), atalkd(8)

# 著者

[CONTRIBUTORS](https://netatalk.io/contributors) を参照
