# 名前

cnid_metad — 要求に応じて cnid_dbd デーモンを起動するデーモン

# 概要

`cnid_metad [-d] [-F configuration file]`

`cnid_metad [ -v | -V ]`

# 説明

**cnid_metad**は*afpd*からの要求を待ち、*cnid_dbd*デーモンのインスタンスを起動する。一度起動した*cnid_dbd*インスタンスの状態を絶えず把握し、もし必要なら再起動する。 **cnid_metad**は通常、**netatalk**(8)によってブート時に起動され、シャットダウンまでずっと動作する。

# オプション

**-d**

> **cnid_metad** はフォアグラウンドに留まり、更に標準入力、標準出力、標準エラー出力のファイル記述子を開いたままにする。デバッグに有用。

**-F** <configuration file\>

> 設定ファイルとして*configuration
file*を使う。デフォルトは*afp.conf*である。

**-v**, **-V**

> バージョンを表示してから終了する。

# 注意事項

**cnid_metad**はSIGPIPEを除くいかなるシグナルもブロックしないし補足もしない。従って、受け取ったほとんどのシグナルにより終了する。これは、**cnid_metad**により起動した全ての*cnid_dbd*のインスタンスを優雅に終了させる。このような状況により、サブプロセスにアクセスするIPCは**cnid_metad**によりメモリ上で維持されるだけなので、これは望ましい動作だといえる。**cnid_metad**が再起動したあとすぐ、**afpd**プロセスは透過的に再接続する。

# 関連項目

netatalk(8), cnid_dbd(8), afpd(8), dbd(1), afp.conf(5)

# 著者

[CONTRIBUTORS](https://netatalk.io/contributors) を参照
