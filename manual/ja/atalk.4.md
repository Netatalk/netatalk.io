# 名前

atalk — AppleTalk プロトコル ファミリ

# 概要

    #include <sys/types.h>
    #include <netatalk/at.h>

# 説明

AppleTalk プロトコル ファミリは、データグラム配信プロトコル (DDP)  の上位層にあり、AppleTalk
アドレス形式を使用するプロトコルのコレクションである。AppleTalk ファミリは、SOCK_STREAM (ADSP)、SOCK_DGRAM
(DDP)、SOCK_RDM (ATP)、および SOCK_SEQPACKET (ASP) を提供する。現在、DDP
のみがカーネルに実装されている。ATP と ASP は、Netatalk のユーザー レベルのライブラリに実装されている。

# アドレス指定

AppleTalk アドレスは 3 バイトの量で、ネットワーク バイト
オーダーで保存される。インクルード ファイル *<netatalk/at.h\>* は
AppleTalk アドレス形式を定義する。

AppleTalk プロトコル ファミリのソケットは、次のアドレス構造を使用する:

    struct sockaddr_at {
        short sat_family;
        unsigned char sat_port;
        struct at_addr sat_addr;
        char sat_zero[ 8 ];
    };

ソケットのポートは、**bind**(2) で設定できる。 *bind* のノードは、常に *ATADDR_ANYNODE*:
"このノード"でなければならない。ネットは、*ATADDR_ANYNET* または *ATADDR_LATENET*。 *ATADDR_ANYNET*
は、マシンの "プライマリ" アドレス (最初に構成されたアドレス) に対応する。 *ATADDR_LATENET*
により、送信パケット内のアドレスはパケットの送信時に決定される(つまり、遅れて決定される)。*ATADDR_LATENET* は、ネットワーク
インターフェイスごとに 1 つのソケットを開くことと同じ。ソケットのポートと プライマリ アドレスまたは *ATADDR_LATENET*
のいずれかが、**getsockname**(2) で返される。

# 関連項目

bind(2), getsockname(2), atalkd(8)

# 著者

[CONTRIBUTORS](https://netatalk.io/contributors) を参照
