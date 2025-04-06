# 名前

asip-status — AFP サーバに機能を問い合わせる

# 概要

`asip-status [ -4 | -6 ] [-d] [-i] [-x] [HOSTNAME] [PORT]`

`asip-status [ -4 | -6 ] [-d] [-i] [-x] [ HOSTNAME:PORT ]`

`asip-status [ -v | -version | --version ]`

# 説明

**asip-status**は、<HOSTNAME\>:<PORT\>で示したAFPサーバにFPGetSrvrInfoリクエストを送信し、その結果を表示する。すなわち、そのサーバがAFPサービスで提供する"Machine
type"、サーバ名、サポートするAFPバージョン、ユーザ認証モジュール(UAM)、AFPフラグ、サーバシグネチャ、ネットワークアドレスである。

<PORT\>を与えない場合は、デフォルトのAFPポートである548が使われる。

Netatalk 3.1.9以降では、 **asip-status**
はIPv4とIPv6の両方をサポートする。どちらのIPバージョンを利用するかは、あなたのシステムが決定する。利用するIPバージョンを指定するには、-4または-6オプションを使うことができる。

# オプション

**-4**

> IPv4のみを使う。

**-6**

> IPv6のみを使う。

**-d**

> デバッグ出力を有効にする。

**-i**

> もしアイコンがあれば、それを表示する。

**-x**

> 16進ダンプ出力を有効にする。

**-v**, **-version**, **--version**

> バージョンを表示する。

# 例

    $ asip-status 192.168.1.15
    AFP reply from 192.168.1.15:548 via IPv4
    Flags: 1  Cmd: 3  ID: 57005
    Reply: DSIGetStatus
    Request ID: 57005
    Machine type: Macintosh
    AFP versions: AFPVersion 1.1,AFPVersion 2.0,AFPVersion 2.1,AFP2.2
    UAMs: Cleartxt passwrd,Randnum exchange,2-Way Randnum exchange
    Volume Icon & Mask: Yes
    Flags:
        SupportsCopyFile
        SupportsChgPwd
        SupportsServerMessages
        SupportsServerSignature
        SupportsTCP/IP
        SupportsSuperClient
    Server name: bookchan
    Signature:
    04 1d 65 23 04 1d 65 23 04 1d 65 23 04 1d 65 23  ..e#..e#..e#..e#

    Network address: 192.168.1.15:548 (IPv4 address and port)
    Network address: 65280.128 (ddp address)

    $ asip-status myserver:10548
    AFP reply from myserver:10548 via IPv6
    Flags: 1  Cmd: 3  ID: 57005
    Reply: DSIGetStatus
    Request ID: 57005
    Machine type: Netatalk3.1.9
    AFP versions: AFP2.2,AFPX03,AFP3.1,AFP3.2,AFP3.3,AFP3.4
    UAMs: DHX2,DHCAST128
    Volume Icon & Mask: Yes
    Flags:
        SupportsCopyFile
        SupportsServerMessages
        SupportsServerSignature
        SupportsTCP/IP
        SupportsSrvrNotifications
        SupportsOpenDirectory
        SupportsUTF8Servername
        SupportsUUIDs
        SupportsExtSleep
        SupportsSuperClient
    Server name: myserver
    Signature:
    ea 56 61 0d bf 29 36 31 fa 6a 8a 24 a8 f0 cc 1d  .Va..)61.j.$....

    Network address: [fd00:0000:0000:0000:0000:0000:0001:0160]:10548 (IPv6 address + port)
    UTF8 Servername: myserver

# 著者

[CONTRIBUTORS](https://netatalk.io/contributors) を参照
