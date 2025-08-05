# 名前

nbplkup, nbprgstr, nbpunrgstr — NBP データベースにアクセスするツール群

# 概要

**nbplkup**

**nbprgstr** [-A *address*] [-m *Mac charset*] [-p *port*] *obj:type@zone*

**nbpunrgstr** [-A *address*] [-D *address*] [-m *Mac charset*] [-s] [-f | -l] *obj:type@zone*

# 説明

**nbprgstr** は、指定された *port* で、**atalkd**(8) に *nbpname*
を登録する。**nbpunrgstr** は、*atalkd* に、*nbpname* がアドバタイズされなくなったことを通知する。

**nbplkup**は、AppleTalkインターネットに登録されているエンティティを最大
*maxresponses* (デフォルトは 1000) 個表示する。*nbpname*は、**nbp_name**(3)によって解析される。*object*
または*type*の\`*=*'は任意のものに一致し、*zone*の\`*\**'はローカルゾーンを意味する。デフォルト値は、NBPLKUP
環境変数から取得され、*nbpname*として解析される。

-A が指定された場合、このアドレスは検索に使用するローカルアドレスとして使用される。-D
が指定された場合、このアドレスは検索の送信先アドレスとして使用される。-f および -l オプションを使用すると、デフォルトの BrRq の代わりに
FwdReq および LkUp 操作を使用できる。

BrRqは、ルータ（デフォルトではローカルのatalkdインスタンス）に、AppleTalkインターネットワーク全体にルックアップ要求を伝播するよう要求する。これは一般的に最も有用なため、デフォルトのオプションとなっている。不明な場合は、BrRqを使用してください。

LkUp
はノードに自身の情報のみを問い合わせる。特定のノードにバインドされている名前を問い合わせたり、ブロードキャスト宛先を指定してルータレスネットワークで行われるような検索をシミュレートしたりするために使用できる。FwdReq
は、指定されたゾーンのメンバーである直接接続されたネットワークに検索を伝播するようルータに要求しますが、それ以上のインターネットワークには伝播させない。これは、大規模なインターネットワークや、扱いにくいノードのキャッシュのトラブルシューティングに役立つ。

-s が指定されている場合、出力はスクリプトに適した形式で印刷される。各応答に対して、最初にアドレスが印刷され、次に 1
つのスペース、名前とタイプ、最後に改行が続く。

-m が指定された場合、文字列は指定された Macintosh 文字セットで解釈される。-m が指定されていない場合、nbplkup はデフォルトで
MacRoman を使用する。

# 環境変数

NBPLKUP

> nbplkup のデフォルトの nbpname

ATALK_MAC_CHARSET

> Appletalk ネットワーク上のクライアントが使用するコードページ

ATALK_UNIX_CHARSET

> このシェルで拡張文字を表示するために使用するコードページ。

# 例

ローカル ゾーンでタイプ *LaserWriter* のすべてのデバイスを検索する。

    example% nbplkup :LaserWriter
                   Petoskey:LaserWriter        7942.129:218
                 Gloucester:LaserWriter        8200.188:186
                     Rahway:LaserWriter        7942.2:138
                 517 Center:LaserWriter        7942.2:132
                      ionia:LaserWriter        7942.2:136
         Evil DEC from Hell:LaserWriter        7942.2:130
                  Hamtramck:LaserWriter        7942.2:134
             Iron Mountain :LaserWriter        7942.128:250
    example%
    
ローカル ゾーン内のタイプ *netatalk* のすべてのデバイスを検索し、スクリプトに適した出力を提供する。

    example% nbplkup -s :netatalk
    5.42:4 netatalk-build:netatalk
    4.162:4 prometheus:netatalk
    8.31:4 Tiryns:netatalk
    example%

# 参照

nbp_name(3), atalkd(8)

# 著者

[CONTRIBUTORS](https://netatalk.io/contributors) を参照
