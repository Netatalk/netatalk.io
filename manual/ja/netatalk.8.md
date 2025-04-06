# 名前

netatalk — Netatalk AFP サーバのサービス コントローラ デーモン

# 概要

`netatalk [-F configfile]`

`netatalk [ -v | -V ]`

# 説明

**netatalk**は、AFPデーモン**afpd**とCNIDデーモン**cnid_metad**の起動と再起動を請け負うサービスコントローラデーモンである。

# オプション

**-d**

> デーモンをターミナルから切り離さない。

**-F** <configfile\>

> 利用する設定ファイルを指定する。

**-v** | **-V**

> バージョン情報を出力して終了する。

# シグナル

SIGTERM

> Netatalkサービス、AFPデーモンとCNIDデーモンを停止する

SIGHUP

> *SIGHUP*を送るとAFPデーモンが設定ファイルを再読み込みする。

# ファイル

*afp.conf*

> **netatalk**(8)と**afpd**(8)と**cnid_metad**(8)が使う設定ファイル

# 関連項目

afpd(8), cnid_metad(8), afp.conf(5)

# 著者

[CONTRIBUTORS](https://netatalk.io/contributors) を参照
