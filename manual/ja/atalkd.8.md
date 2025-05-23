# 名前

atalkd — ユーザーランド AppleTalk ネットワーク マネージャ デーモン

# 概要

**atalkd** [-f *configfile*] [-P *pidfile*] [-1] [-2] [-d] [-t]

**atalkd** [-v | -V]

# 説明

**atalkd** は、すべてのユーザー レベルの AppleTalk ネットワーク管理を担当する。これには、ルーティング、名前の登録と検索、ゾーン検索、および AppleTalk Echo プロトコル (**ping**(8) に類似)  が含まれる。具体的には、AppleTalk プロトコル ファミリの RTMP、NBP、ZIP、および AEP プロトコルに対応する。

OS の init システムは通常、起動時に **atalkd** デーモンを起動する。デーモンは最初に構成ファイル **atalkd.conf**
を読み取る。構成ファイルがない場合、またはインターフェイスが定義されていない場合、**atalkd**
は使用可能なすべてのインターフェイスを構成しようとし、構成ファイルを作成する。設定ファイルの形式の詳細については、**atalkd.conf**(5)
を参照してください。

# オプション

**-1**

> AppleTalk Phase 1 を強制する。

**-2**

> AppleTalk Phase 2 を強制する。

**-d**

> デーモンをターミナルから切り離さないで、追加のデバッグ情報を stdout
に書き込む。

**-f** *configfile*

> 設定情報については、**atalkd.conf**ではなく、*configfile*
を参照してください。

**-P** *pidfile*

> **atalkd** がプロセス ID を保存するファイルを指定する。

**-t**

> 遷移ルーティングをオンにする。

**-v** | **-V**

> バージョン情報を出力して終了する。

# ルーティング

既存の AppleTalk ネットワークに **atalkd** ルーターを接続する場合は、まずローカル ネットワーク管理者に連絡して適切なネットワーク
アドレスを取得する必要がある。

**atalkd**は、複数のインターフェイスを構成することでインターフェイス間のルーティングを提供できる。各インターフェースには、1から 65279 までの一意のネット範囲 を割り当てる必要がある (0 から 65535 は無効で、65280 から 65534までのアドレスは起動用に予約されている)。最も小さい有効なネット範囲を選択するのが最善。つまり、LAN上に 3 台のマシンがある場合は、1000未満のネット範囲を選択する。各ネット範囲には任意のリストを設定できる。

インターフェースが複数あり、他の設定が存在しない場合は、**atalkd** は自動的にルーターとして動作することに注意してください。

# ファイル

*atalkd.conf* 設定ファイル

# 関連項目

atalkd.conf(5)

# 著者

[CONTRIBUTORS](https://netatalk.io/contributors) を参照
