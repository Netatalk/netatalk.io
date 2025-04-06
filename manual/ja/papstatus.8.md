# 名前

papstatus — AppleTalk 接続プリンタのステータスを取得する

# 概要

`papstatus [-d] [-p printer] [retrytime]`

# 説明

**papstatus** は、AppleTalk に接続されたプリンタから現在のステータス
メッセージを取得するために使用される。プリンタ アクセス プロトコル
(PAP) を使用してステータス情報を取得する。

コマンド ラインでプリンタが指定されていない場合、**papstatus** は現在のディレクトリで *.paprc*
というファイルを検索し、それを読み取ってプリンタの名前を取得する。 *.paprc* ファイルには、*object:type@zone* という形式の
1 行が含まれている必要がある。ここで、*object*、*:type、*、*@zone* はそれぞれオプションである。 *type* と *zone*
の前にはそれぞれ \`*:*' と \`*@*' を付ける必要がある。空白行と \`*\#*' で始まる行は無視される。 *type* と *zone*
のデフォルトはそれぞれ *LaserWriter* とローカル ホストのゾーンである。

# オプション

**-d**

> デバッグ モードをオンにして、標準エラーに追加情報を出力する。

**-p** <printer\>

> *printer* からステータスを取得する (他の*.paprc*
ファイルでプリンタ名を検索する)。 *printer* の構文は、*.paprc*
ファイルで上で説明したものと同じ。

*retrytime*

> 通常、**papstatus** はプリンタからステータスを 1 回だけ取得する。
*retrytime* が指定されている場合は、プリンタの問い合わせの間に
*retrytime* 秒のスリープを挟んで、ステータスが繰り返し取得される。

# ファイル

*.paprc*

> プリンタ名を含むファイル

# 関連項目

nbp(1), pap(1)

# 著者

[CONTRIBUTORS](https://netatalk.io/contributors) を参照
