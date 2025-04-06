# 名前

extmap.conf — ファイル名拡張子マッピングを指定するために afpd が利用する設定ファイル

# 説明

**extmap.conf**はファイル名拡張子マッピングを指定するために**afpd**が利用する設定ファイルである。

設定行は以下のように構成される。

`.extension [ type [ creator ] ]`

ハッシュ文字(“#”)  で始まるいかなる行も無視される。ドットで始まる行はファイル名拡張子マッピングを指定する。拡張子 '.'
は他の非分類Unixファイルのデフォルトのタイプとクリエータを設定する。

# 例

## 例： 拡張子がjpgで、タイプが"JPEG"、クリエータが"ogle"

    .jpg "JPEG" "ogle"

## 例： 拡張子がlzhで、タイプが"LHA"、クリエータは設定されていない

    .lzh "LHA"

# 関連項目

afp.conf(5), afpd(8)

# 著者

[CONTRIBUTORS](https://netatalk.io/contributors) を参照
