# 名前

netatalk — Netatalk AFP サーバのサービス コントローラ デーモン

# 概要

**netatalk** [-F *configfile*]

**netatalk** [-v | -V]

# 説明

**netatalk** は、複数のフォーク型デーモンで構成される Netatalk AFP ファイルサーバーを
制御するためのデーモンである。
ほとんどの導入では、各デーモンを個別に起動・停止するのではなく、
netatalk を集中管理に使用する。
netatalk デーモンは通常、ブート時に init システムによって起動される。

コントローラーデーモンは、AFP デーモン **afpd** と CNID メタデーモン **cnid_metad** を起動する。後者は、CNID
データベースデーモン **cnid_dbd** を起動する。

4つのデーモンの設定はすべて、afp.conf という単一の設定ファイルで管理される。

# オプション

**-d**

> デーモンをターミナルから切り離さない。

**-F** *configfile*

> 利用する設定ファイルを指定する。

**-v** | **-V**

> バージョン情報を出力して終了する。

# シグナル

SIGTERM

> NetatalkのAFPデーモンとCNIDデーモンを停止する

SIGHUP

> *SIGHUP*を送るとNetatalkのAFPデーモンとCNIDデーモンが設定ファイルを再読み込みする。

# ファイル

*afp.conf*

> **netatalk**(8)と**afpd**(8)と**cnid_metad**(8)が使う設定ファイル

# 関連項目

afpd(8), cnid_metad(8), afp.conf(5)

# 著者

[CONTRIBUTORS](https://netatalk.io/contributors) を参照
