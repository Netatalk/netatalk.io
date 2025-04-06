# 名前

macipgw — MacIP ゲートウェイ デーモン

# 概要

`macipgw [-d debugclass] [-f configfile] [-n nameserver] [-u
unprivileged-user] [-z zone] [network] [netmask]`

`macipgw [ -v | -V ]`

# 説明

**macipgw** は、AppleTalk のみのネットワークを介して接続されたデバイスに IP 接続を提供する。つまり、LocalTalk または Apple Remote Access (ARA)。**macipgw** は通常、*/etc/rc* から起動される。

MacIP (以前は KIP と呼ばれていました) は、IP パケットを AppleTalk パケットにカプセル化できるプロトコルである。
**macipgw** は、AppleTalk ネットワーク上の MacIP ゲートウェイとして自身を登録し、トンネル
インターフェイスを設定して起動する (**tun**(4) を参照)。次に、AppleTalk ネットワークから受信した IP パケットをトンネル
インターフェイスを介してカーネルに転送する。同様に、トンネル経由で受信された IP パケットは、宛先 IP アドレスに登録されている AppleTalk
デバイスに転送される。

他の MacIP ゲートウェイとは異なり、**macipgw** は動作するために独自の IP (サブネット)
ネットを必要とし、登録されたアドレスに対してプロキシ ARP を使用しない。ゲートウェイは、常にネットワークの最初のアドレスをローカル
アドレスとして使用する。つまり、ネットワーク 192.168.1.0/24 の場合は 192.168.1.1 になる。

存在する場合、**macipgw** は */usr/etc/macipgw.conf* (または同等の pkgconf パス)
から構成オプションを読み取る。コマンド ライン オプションは、構成ファイル オプションよりも優先される。例については以下を参照してください。

**macipgw** は、*LOG_DAEMON* 機能の下で、**syslog**(3) を介して操作メッセージをログに記録する。

# オプション

**-d** <debugclass\>

> デーモンがフォークせず、すべてのアクションのトレースが書き込まれるように指定する*stdout*
に出力する。 debugclass の有用な値については、ソース
コードを参照してください。

**-f** <configfile\>

> 設定情報については、*macipgw.conf* ではなく、<configfile\>
を参照する。

**-n** <nameserver\>

> ゲートウェイ経由で接続された AppleTalk デバイスが使用する DNS ネーム
サーバーの IP アドレスを指定する。

**-u** <unprivileged-user\>

> サーバーの起動後に、ルート権限を削除してユーザー unprivileged-user
に変更する。

**-z** <zone\>

> **macipgw**
は、デフォルトのゾーンではなく、ゾーンに登録する必要がある。

**-v** | **-V**

> バージョン情報を表示して終了する。

<network\>

> クライアントに使用するネットワーク番号を指定する。

<netmask\>

> ネットワークのネットマスクを指定する。

# 例

## 例： macipgw 呼び出し

    /usr/local/libexec/macipgw -n 192.168.1.1 -z "Remote Users" 192.168.1.0 255.255.255.0

**macipgw** を起動し、ゲートウェイ経由で接続されたデバイスにクラス C ネットワーク 192.168.1.0
を割り当て、**macipgw** が動作しているシステムをネーム サーバーとして使用でき、ゾーン Remote Users
に登録する必要があることを指定する。

## 例： macipgw.conf 構成ファイル

    [Global]
    network = 192.168.151.0
    netmask = 255.255.255.0
    nameserver = 8.8.8.8
    zone = My Zone
    unprivileged user = foobar

# 関連項目

tun(4), ip(4), atalkd(8), syslog(3), syslogd(8)

# バグ

ログ メッセージ以外に、どの AppleTalk デバイスがゲートウェイを使用しているかに関する情報はない。

# 著者

Stefan Bethke <Stefan.Bethke@Hanse.DE\>
