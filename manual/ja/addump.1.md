# 名前

addump - AppleSingle/AppleDouble フォーマットのデータをダンプする

# 概要

`addump [-a] [ FILE | DIR ]`

`addump [-e] [ FILE | DIR ]`

`addump [-f] [FILE]`

`addump [-d] [FILE]`

`addump [ -h | -help | --help ]`

`addump [ -v | -version | --version ]`

# 説明

**addump** はAppleSingle/AppleDoubleフォーマットのデータをダンプする。

このスクリプトはメーラ、アーカイバ、Mac OS
X、Netatalkなどが生成する様々なAppleSingle/AppleDoubleデータをダンプできる。

<FILE\>\|<DIR\>がない、または<FILE\>\|<DIR\>が「-」であるとき、標準入力を読み込む。

# オプション

**-a** \[<FILE\>|<DIR\>\]

> これがデフォルトである。<FILE\>または<DIR\>のためのAppleSingle/AppleDoubleデータを自動的にダンプする。もしFILEがAppleSingle/AppleDoubleフォーマットでないなら、拡張属性と<.AppleDouble/FILE\>と<.\_FILE\>を探する。もし<DIR\>なら、拡張属性と<DIR/.AppleDouble/.Parent\>と<.\_DIR\>を探する。

**-e** <FILE\>|<DIR\>

> <FILE\>または<DIR\>の拡張属性をダンプする。

**-f** \[<FILE\>\]

> <FILE\>をダンプする。FinderInfoがFileInfoであると仮定する。

**-d** \[<FILE\>\]

> <FILE\>をダンプする。FinderInfoがDirInfoであると仮定する。

**-h**, **-help**, **--help**

> ヘルプを表示して終了する

**-v**, **-version**, **--version**

> バージョンを表示して終了する

# 注記

FinderInfoがFileInfoなのかDirInfoなのかを検出する方法がない。デフォルトでは、addumpはそれがファイルなのかディレクトリなのか、親ディレクトリが.AppleDoubleか、ファイル名が.\_\*か、ファイル名が.Parentかなどを調査する。

もしオプション**-e**または**-f**または**-d**を設定した場合、FinderInfoを仮定し他のデータを探さない。

# 関連項目

ad(1), getfattr(1), attr(1), runat(1), getextattr(8), lsextattr(8)

# 著者

[CONTRIBUTORS](https://netatalk.io/contributors) を参照
