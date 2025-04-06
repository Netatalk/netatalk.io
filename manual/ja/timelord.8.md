# 名前

timelord — Macintosh タイム サーバー デーモン

# 概要

`timelord [-d] [-l] [-n nbpname]`

`timelord [ -v | -V ]`

# 説明

**timelord** は、**tardis** クライアントを使用する Macintosh
コンピュータ用のシンプルなタイム サーバーである。Macintosh 用の "Timelord"
CDEV と同じ機能を備えている。

**tardis** は Chooser 拡張機能として実装されている。Chooser で、Mac
のシステム時間を同期する **timelord**
インスタンスを選択する。同期されると、**tardis**
は起動時に自動的にサーバーと同期するか、Mac
の実行中に定期的にスケジュールされて同期する (後者には tardis 1.4
が必要)。

# オプション

**-d**

> デバッグ モード。つまり、制御 TTY から切り離されない。

**-l**

> サーバーのタイム ゾーン調整されたローカル時間を返する。
このオプションがない場合のデフォルトの動作は GMT になる。

**-n** <nbpname\>

> このサーバーを *nbpname*
として登録する。デフォルトではホスト名になる。

**-v** | **-V**

> バージョン情報を出力して終了する。

# 著者

[CONTRIBUTORS](https://netatalk.io/contributors) を参照
