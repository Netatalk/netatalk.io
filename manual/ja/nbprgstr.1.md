# 名前

nbprgstr, nbpunrgstr — ネットワーク上の AppleTalk エントリ登録を管理する

# 概要

**nbprgstr** [-A *address*] [-m *Mac charset*] [-p *port*] *nbpname*

**nbpunrgstr** [-A *address*] [-m *Mac charset*] *nbpname*

# 説明

**nbprgstr** は指定された *port* で *nbpname* を **atalkd**(8) に登録する。

**nbpunrgstr** は *nbpname* がもはや広告されないことを **atalkd** に通知する。

これは Name-Binding Protocol (NBP) を使用して AppleTalk ネットワークと対話する。*nbpname* は
**nbp_name**(3) によって解析される。

# オプション

**-A** *address*
> 検索に使用するローカルアドレスとして *address* を使用する。

**-m** *Mac charset*
> 指定された Macintosh 文字セットで文字列を解釈する。
> 指定されていない場合、nbplkup はデフォルトで MacRoman を使用する。

**-p** *port*
> エンティティを登録するポートとして *port* を使用する。

**nbpname**
> 使用する NBP 名。
>
> *nbpname* は *obj:type@zone* の形式の文字列で、ここで *obj* はオブジェクト名、
> *type* はオブジェクトのタイプ、*zone* はゾーン名である。
> *obj* と *type* は任意の文字列にできるが、*zone* は有効なゾーン名でなければならない。
> *object* または *type* に対する \`*=*' は何でも一致し、*zone* に対する \`*\**' はローカルゾーンを意味する。

# 例

ローカルゾーンにエンティティ "myhost:Foobar" を DDP アドレス 65280.68 で登録する。

    example% nbprgstr -A 65280.68 myhost:Foobar
    example% nbplkup
                            myhost:Foobar                             65280.68:128
    example%

エンティティ "myhost:Foobar" の登録を取り消す。

    example% nbpunrgstr myhost:Foobar
    example% nbplkup
    example%

# 参照

nbp_name(3), nbplkup(1), atalkd(8)

# 著者

[CONTRIBUTORS](https://netatalk.io/contributors) を参照
