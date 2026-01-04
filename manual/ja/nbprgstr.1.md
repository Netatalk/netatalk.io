# 名前

nbprgstr, nbpunrgstr — ネットワーク上の AppleTalk エントリ登録を管理する

# 概要

**nbprgstr** [-A *アドレス*] [-m *Mac 文字セット*] [-p *ポート*] *nbp名*

**nbpunrgstr** [-A *アドレス*] [-m *Mac 文字セット*] *nbp名*

# 説明

**nbprgstr** は指定された *ポート* で *nbp名* を **atalkd**(8) に登録する。

**nbpunrgstr** は *nbp名* がもはや広告されないことを **atalkd** に通知する。

これは Name-Binding Protocol (NBP) を使用して AppleTalk ネットワークと対話する。*nbp名* は
**nbp_name**(3) によって解析される。

# オプション

**-A** *アドレス*
> 検索に使用するローカルアドレスとして *アドレス* を使用する。

**-m** *Mac 文字セット*
> 指定された Macintosh 文字セットで文字列を解釈する。
> 指定されていない場合、nbplkup はデフォルトで MacRoman を使用する。

**-p** *ポート*
> エンティティを登録するポートとして *ポート* を使用する。

**nbp名**
> 使用するNBP名。
>
> *nbp名* は *obj:type@zone* の形式の文字列で、ここで *obj* はオブジェクト名、
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
