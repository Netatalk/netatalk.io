# 名前

nbp_name — NBP 名の解析

# 概要

    int nbp_name(name,
        obj,
        type,
        zone);
    char *name;
    char **obj;
    char **type;
    char **zone;

# 説明

**nbp_name()** は、ユーザーが指定した名前を、そのコンポーネント オブジェクト、タイプ、およびゾーンに解析する。 *obj*、*type*、*zone* は参照渡しされ、呼び出し元のデフォルト値を指す必要がある。**nbp_name()** は、解析された値へのポインタを変更する。 *name* は、*object:type@**zone* の形式である。ここで、*object*、 *:type、*、および *@**zone* はそれぞれ、*obj*、 *type*、*zone,* です。*type* の前には \`*:*' が、*zone* の前には \`*@*' がなければならない。

# 例

**afpd**(8)'s **-n** オプションの引数は、**nbp_name()** で解析される。 *obj*
のデフォルト値は、マシンのホスト名の最初のコンポーネントになる (**gethostbyname**(3) によって返される)。*type*
のデフォルト値は "AFPServer" で、*zone* のデフォルト値は "\*" (デフォルト ゾーン) になる。*obj* と *type*
はデフォルト値を保持しながら、*afpd* をデフォルト以外のゾーンに登録するには、次のように呼び出す。

    afpd -n @some-other-zone

# バグ

*obj*、*type*、および *zone*
は、呼び出しごとに上書きされる可能性のある静的領域へのポインタを返する。

# 著者

[CONTRIBUTORS](https://netatalk.io/contributors) を参照
