# 名前

extmap.conf — ファイル名拡張子マッピングを指定するために afpd が利用する設定ファイル

# 説明

**extmap.conf**はファイル名拡張子をMac OSのtype/creatorマッピングを指定するために**afpd**が利用する設定ファイルである。

Classic Mac
OSでは、type/creatorはファイルのタイプと開くのに使われるアプリケーションを決定するために利用されるファイルシステムメタデータである。それぞれ4文字で構成される。

このスキームはMac OS X 10.4 Tigerまで部分的にサポートされていたが、Mac OS X 10.5
Leopardではファイル拡張子を直接調べるのに代わって削除された。

設定行は以下のように構成される。

    .extension [ type [ creator ] ]

タイプは必須であるが、クリエータはオプションである。

ハッシュ文字(“#”)  で始まるいかなる行も無視される。ドットで始まる行はファイル名拡張子マッピングを指定する。拡張子 '.'
は他の非分類Unixファイルのデフォルトのタイプとクリエータを設定する。

# 例

## 例： typeとcreatorを設定する

拡張子がjpgで、タイプが"JPEG"、クリエータが"ogle"である。これはMac OS XではPreview.appにマッピングされる。

    .jpg "JPEG" "ogle"

## 例： typeのみを設定する

拡張子がlzhで、タイプが"LHA"、クリエータは設定されていない。

    .lzh "LHA"

# 関連項目

afp.conf(5), afpd(8)

# 著者

[CONTRIBUTORS](https://netatalk.io/contributors) を参照
