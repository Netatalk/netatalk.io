# 名前

nbplkup — ネットワーク上の登録された AppleTalk エンティティを検索する

# 概要

**nbplkup** [-A *address*] [-D *address*] [-m *Mac charset*] [-r *responses*] [-s] [-f | -l] [*nbpname*]

# 説明

**nbplkup** は AppleTalk ネットワークに登録されているエンティティを最大 *responses* 件（デフォルトは 1000 件）表示する。

デフォルトでは、ローカルゾーン内のすべてのエンティティを検索する。*nbpname*
が指定されている場合、検索はその名前に一致するエンティティのみを返すようにフィルタリングできる。

これは Name-Binding Protocol (NBP) を使用して AppleTalk ネットワークと対話する。*nbpname* は
**nbp_name**(3) によって解析される。

# オプション

**-A** *address*
> 検索に使用するローカルアドレスとして *address* を使用する。

**-D** *address*
> 検索を送信する宛先アドレスとして *address* を使用する。

**-m** *Mac charset*
> 指定された Macintosh 文字セットで文字列を解釈する。
> 指定されていない場合、nbplkup はデフォルトで MacRoman を使用する。

**-r** *responses*
> 応答の数を *responses*（デフォルトは 1000）に制限する。

**-s**
> スクリプトに適した形式で出力を印刷する。
> 各応答について、最初にアドレスが印刷され、その後に単一のスペース、その後に名前とタイプが続き、最後に改行が続く。

**-f**
> 検索要求にデフォルトの *BrRq* の代わりに *FwdReq* 操作を使用する。
>
> -l と一緒に使用できない。

**-l**
> 検索要求にデフォルトの *BrRq* の代わりに *LkUp* 操作を使用する。
>
> -f と一緒に使用できない。

**nbpname**
> 使用する NBP 名。
>
> *nbpname* は *obj:type@zone* の形式の文字列で、ここで *obj* はオブジェクト名、
> *type* はオブジェクトのタイプ、*zone* はゾーン名である。
> *obj* と *type* は任意の文字列にできるが、*zone* は有効なゾーン名でなければならない。
> *object* または *type* に対する \`*=*' は何でも一致し、*zone* に対する \`*\**' はローカルゾーンを意味する。

## 注記

**-BrRq** はルーター（デフォルトではローカルの atalkd インスタンス）に、AppleTalk
インターネットワーク全体にわたって検索要求を伝播するように依頼する。これは一般的に最も有用であるため、デフォルトのオプションである。疑わしい場合は、*BrRq*
を使用する。

*LkUp*
はノードに対して自分自身について尋ねる。それは特定のノードにバインドされている名前を照会するため、またはブロードキャスト宛先を指定することによって、ルーターのないネットワークで行われる種類の検索をシミュレートするために使用できる。

*FwdReq*
はルーターに対して、指定されたゾーンのメンバーである直接接続されたネットワークに検索を伝播するように依頼するが、インターネットワーク全体にそれ以上伝播しないようにする。これは大規模なインターネットワークで役立つ場合があり、または難治性ノードのキャッシュをトラブルシューティングするために役立つ場合がある。

# 環境変数

NBPLKUP

> nbplkup のデフォルト nbpname、形式は *obj:type@zone*

# 例

ローカルゾーン内のタイプ *LaserWriter* のすべてのデバイスを検索する。

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
    
ローカルゾーン内のタイプ *netatalk* のすべてのデバイスを検索し、スクリプトに適した出力を提供する。

    example% nbplkup -s :netatalk
    5.42:4 netatalk-build:netatalk
    4.162:4 prometheus:netatalk
    8.31:4 Tiryns:netatalk
    example%

# 参照

nbp_name(3), nbprgstr(1), nbpunrgstr(1), atalkd(8)

# 著者

[CONTRIBUTORS](https://netatalk.io/contributors) を参照
