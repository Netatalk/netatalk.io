# 名前

a2boot — Apple II ネットブート サーバー デーモン

# 概要

`a2boot [-d] [-n nbpname]`

`a2boot [ -v | -V ]`

# 説明

**a2boot** は、Apple IIe および IIGS コンピュータ用のネットブート
サーバーである。互換性のあるクライアントが AppleTalk ネットワーク経由で
ProDOS または GS/OS を起動できるようにする。 これは、AppleShare File
Server for Macintosh の初期バージョンに含まれていた Apple II
ネットブート ソフトウェアと機能的に同等である。

デーモンを実行すると、次のハードコードされた AFP ボリュームが作成される。

- Apple //e Boot

- Apple //gs

- ProDOS16 Image

これらのボリュームをブート ボリュームとして機能させるには、適切な ProDOS または GS/OS システム
ファイルをこれらのボリュームに取り込む必要がある。 詳細については、AppleShare File Server for Macintosh
のドキュメントを参照してください。

# オプション

**-d**

> デバッグ モード。つまり、制御 TTY から切り離されない。

**-n** <nbpname\>

> このサーバーを *nbpname*
として登録する。デフォルトではホスト名になる。

**-v** | **-V**

> バージョン情報を出力して終了する。

# 著者

[CONTRIBUTORS](https://netatalk.io/contributors) を参照
