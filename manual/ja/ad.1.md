# 名前

ad - AppleDouble ファイルユーティリティ 一式

# 概要

`ad [ ls | cp | mv | rm | set ] [...]`

`ad [ -v | --version ]`

# 説明

**ad**は、Netatalk 互換の AppleDouble ファイルユーティリティ一式である。Netatalk 共有ボリューム内の AppleDouble データ (ファイルの拡張属性や、同じディレクトリ内の.\_fileや、**.AppleDouble**ディレクトリ内のファイル) とCNIDデータベースを適切に更新する。

# 有効なコマンド

List files and directories.

> `ad ls [-dRl[u]] {file|dir [...]}`

ファイルやディレクトリをコピーする。

> `ad cp [-aipvf] {src_file} {dst_file}`

> `ad cp -R [-aipvf] {src_file|src_directory ...} {dst_directory}`

ファイルやディレクトリを移動する。

> `ad mv [-finv] {src_file} {dst_file}`

> `ad mv [-finv] {src_file|src_directory ...} {dst_directory}`

ファイルやディレクトリを削除する。

> `ad rm [-Rv] {file|directory}`

ファイルにメタデータを設定する。

> `ad set [-t type] [-c creator] [-l label] [-f flags] [-a attributes] {file}`

バージョンを表示する。

> `ad -v | --version`

# ad ls

ファイルやディレクトリをリストする。 オプション:

**-d**

> ディレクトリを単純なファイルとしてリストする

**-R**

> サブディレクトリを再帰的にリストする

**-l**

> 長い出力。AFP infoをリストする

**-u**

> UNIX infoをリストする

*長い出力の説明*

    <unixinfo> <FinderFlags> <AFP Attributes> <Color> <Type> <Creator> <CNID from AppleDouble> <name>

    FinderFlags (valid for (f)iles and/or (d)irectories):

      d = On Desktop                      (f/d)
      e = Hidden extension                (f/d)
      m = Shared (can run multiple times) (f)
      n = No INIT resources               (f)
      i = Inited                          (f/d)
      c = Custom icon                     (f/d)
      t = Stationery                      (f)
      s = Name locked                     (f/d)
      b = Bundle                          (f/d)
      v = Invisible                       (f/d)
      a = Alias file                      (f/d)

    AFP Attributes:

      y = System                          (f/d)
      w = No write                        (f)
      p = Needs backup                    (f/d)
      r = No rename                       (f/d)
      l = No delete                       (f/d)
      o = No copy                         (f)

    Note: any letter appearing in uppercase means the flag is set but it's a directory for which the flag is not allowed.

# ad cp

ファイルやディレクトリをコピーする。

上の概要で示した一番目の形式では、cpユーティリティはsrc_fileの内容をdst_fileへコピーする。二番目の形式では、それぞれの名前のsrc_fileの内容は配布先のdst_directoryにコピーされる。ファイル自身の名前は変更されない。ファイルを自分自身へコピーしようとしているのをcpが検出したら、コピーは失敗する。

AFPボリュームへのコピーであると検出された場合、CNIDデータベースデーモンに接続し、全てのコピーはCNIDデータベースの手続きを踏む。ターゲットがAFPボリュームの場合はAppleDoubleデータもまたコピーされ、必要なら作成される。

オプション:

**-a**

> アーカイブモード。**-Rp** と同じ。

**-f**

> それぞれの配布先パス名が既に存在している場合、それを削除してから新しいファイルを作成する。パーミッションに関わらず確認プロンプトを出さない。(**-f** オプションは手前の **-i** オプションと **-n** オプションを無効にする。)

**-i**

> 存在するファイルに上書きする前に、標準エラー出力にプロンプトを出す。もし標準入力からの返答が'y'または'Y'で始まるならばファイルコピーを試みる。(**-i** オプションは手前の **-f** オプションと **-n** オプションを無効にする。)

**-n**

> 存在するファイルを上書きしない。
(**-n** オプションは手前の **-f** オプションと-iオプションを無効にする。)

**-p**

> 以下に示すそれぞれのコピー元ファイルの属性を、パーミッションが許す限り維持する:
変更時刻、アクセス時刻、ファイルフラグ、ファイルモード、ユーザIDグループID。ユーザIDとグループIDが維持されない場合、エラーメッセージは表示されず、終了コードは変更されない。

**-R**

> もしsrc_fileでディレクトリを指定した場合、cpはそのディレクトリと全体のサブツリーをコピーする。もしsrc_fileが「/」で終わっている場合、ディレクトリ自身ではなく中身をコピーする。

**-v**

> コピーしたファイルを詳細に表示する。

**-x**

> ファイルシステムのマウントポイントを横断しない。

# ad mv

ファイルやディレクトリを移動する。

AFPボリューム内のファイルを移動し、必要に応じてCNIDデータベースを更新する。以下のどちらかの場合はファイルをコピーしてからコピー元を削除する。

- 移動元または移動先がAFPボリュームでない

- 移動元AFPボリュームと移動先AFPボリュームが異なる

オプション:

**-f**

> 配布先パスに上書きする前に確認プロンプトを出さない。(**-f** オプションは手前の **-i** オプションと **-n** オプションを無効にする。)

**-i**

> 存在するファイルに上書きする前に、標準エラー出力にプロンプトを出す。もし標準入力からの返答が'y'または'Y'で始まるならば移動を試みる。(**-i** オプションは手前の **-f** オプションと **-n** オプションを無効にする。)

**-n**

> 存在するファイルを上書きしない。
(**-n** オプションは手前の **-f** オプションと-iオプションを無効にする。)

**-v**

> 移動したファイルを詳細に表示する。

# ad rm

ファイルやディレクトリを削除する。

rmユーティリティはコマンドラインで指定した非ディレクトリ型のファイルを削除しようと試みる。もしファイルやディレクトリがAFPボリューム上にあるなら、対応するCNIDをボリュームデータベースから削除する。

オプションは次の通り。

**-R**

> それぞれのファイル引数の下のファイル階層を削除しようと試みる。

**-v**

> ファイルを削除するときに詳細を表示する。

# ad set

ファイルにメタデータを設定する。

set ユーティリティは、AFP ボリューム内のファイルのメタデータを変更する。

オプションは次の通り。

**-t** <type\>

> ファイルの 4 文字のファイル タイプを変更する。

**-c** <creator\>

> ファイルの 4 文字の作成者タイプを変更する。

**-l** <label\>

> ファイルの色ラベルを変更する。使用可能な色については、以下のリストを参照。

**-f** <flags\>

> ファイルの Finder
フラグを変更する。使用可能なフラグについては、以下のリストを参照。大文字はフラグを設定し、小文字はフラグを削除する。

**-a** <attributes\>

> ファイルの属性を変更する。使用可能な属性については、以下のリストを参照。大文字はフラグを設定し、小文字はフラグを削除する。

*旗の説明*

    Color Labels:

      none | grey | green | violet | blue | yellow | red | orange

    Finder Flags (valid for (f)iles and/or (d)irectories):

      d = On Desktop                      (f/d)
      e = Hidden extension                (f/d)
      m = Shared (can run multiple times) (f)
      n = No INIT resources               (f)
      i = Inited                          (f/d)
      c = Custom icon                     (f/d)
      t = Stationery                      (f)
      s = Name locked                     (f/d)
      b = Bundle                          (f/d)
      v = Invisible                       (f/d)
      a = Alias file                      (f/d)

    AFP Attributes:

      y = System                          (f/d)
      w = No write                        (f)
      p = Needs backup                    (f/d)
      r = No rename                       (f/d)
      l = No delete                       (f/d)
      o = No copy                         (f)

# 参照

dbd(1), addump(1)

# 著者

[CONTRIBUTORS](https://netatalk.io/contributors) を参照
