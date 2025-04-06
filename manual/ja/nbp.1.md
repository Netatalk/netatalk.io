# 名前

nbplkup, nbprgstr, nbpunrgstr — NBP データベースにアクセスするツール群

# 説明

**nbprgstr** は、指定された <port\> で、**atalkd**(8) に <nbpname\>
を登録する。**nbpunrgstr** は、*atalkd* に、<nbpname\>
がアドバタイズされなくなったことを通知する。

**nbplkup** は、AppleTalk インターネットに登録されているエンティティを最大
<maxresponses\> (デフォルトは 1000) 個表示する。 <nbpname\>
は、**nbp_name**(3)によって解析される。 *object*
または*type*の\`*=*'は任意のものに一致し、*zone*の\`*\**'はローカルゾーンを意味する。デフォルト値は、*NBPLKUP*
環境変数から取得され、<nbpname\> として解析される。

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

# 参照

nbp_name(3), atalkd(8)

# 著者

[CONTRIBUTORS](https://netatalk.io/contributors) を参照
