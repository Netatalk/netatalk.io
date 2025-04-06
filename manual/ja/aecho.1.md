# 名前

aecho - AppleTalk Echo Protocol プロトコル パケットをネットワーク ホストに送信する

# 概要

`aecho [-c count] [ address | nbpname ]`

# 説明

**aecho** は、指定された AppleTalk **address** または **nbpname** で指定されたホストに Apple Echo Protocol (AEP) パケットを繰り返し送信し、応答が受信されたかどうかを報告する。リクエストは 1 秒あたり 1 つの速度で送信される。

**address** は、**atalk_aton**(3) によって解析される。 **nbpname** は、**nbp_name**(3) によって解析される。 nbp タイプのデフォルトは \`*Workstation*' である。

**aecho**
が終了すると、送信されたパケットの数、受信した応答の数、および失われたパケットの割合が報告される。応答が受信された場合、最小、平均、および最大の往復時間が報告される。

# 例

特定のホストが稼働していて、AEP パケットに応答しているかどうかを確認する:

    example% aecho bloodsport
    11 bytes from 8195.13: aep_seq=0. time=10. ms
    11 bytes from 8195.13: aep_seq=1. time=10. ms
    11 bytes from 8195.13: aep_seq=2. time=10. ms
    11 bytes from 8195.13: aep_seq=3. time=10. ms
    11 bytes from 8195.13: aep_seq=4. time=10. ms
    11 bytes from 8195.13: aep_seq=5. time=9. ms
    ^C
    ----8195.13 AEP Statistics----
    6 packets sent, 6 packets received, 0% packet loss
    round-trip (ms)  min/avg/max = 9/9/10

# オプション

**-c** <count\>

> *count* パケット後に停止する。

# 関連項目

ping(1), atalk_aton(3), nbp_name(3), aep(4), atalkd(8)

# 著者

[CONTRIBUTORS](https://netatalk.io/contributors) を参照
