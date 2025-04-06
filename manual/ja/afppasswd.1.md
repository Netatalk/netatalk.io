# 名前

afppasswd — AFP パスワード保守ユーティリティ

# 概要

`afppasswd [-acfn] [-p afppasswd file] [-u minimum uid] [-w password
string]`

# 説明

**afppasswd** は、「Randnum exchange」および「2-Way Randnum exchange」ユーザー認証モジュールのユーザー資格情報を提供する afppasswd ファイルを作成および管理する。

**afppasswd**は、rootがパラメータ付きで呼び出すことも、一般のユーザが自分のAFPパスワードを変更するためにパラメータなしで呼び出すこともできる。

> **注記**

> このユーティリティでは、Random Number UAM
の2種類が利用するパスワードのみ変更できる。かなり弱いパスワード暗号化を提供するため、非常に古いAFPクライアントをサポートしなければならない限り、より安全な"DHX"
("DHCAST128") 及び "DHX2" UAMを推奨する。

# 例

ローカルユーザが自分のパスワードを変更する:

    example% afppasswd
    Enter NEW AFP password: (非表示)
    Enter NEW AFP password again: (非表示)
    afppasswd: updated password.

# オプション

**-a**

> *afppasswd*ファイルに新しいユーザを追加する。

**-c**

> *afppasswd*ファイルまたは特定ユーザを作成する。(さらに/または)初期化する。

**-f**

> 現在の動作を強制する。

**-p** <パス\>

> *afppasswd*ファイルのパス。

**-n**

> もしcracklibサポートが*netatalk*に組み込まれており、cracklib辞書に対して実行されたパスワードを持つことをスーパユーザが望まないなら、このオプションはcracklibチェックを無効にできるだろう。

**-u** <minimum uid\>

> これは、**afppasswd**がユーザを作成するときに使う最小の*ユーザid*
(uid)である。

**-w** <パスワード文字列\>

> パスワードを対話形式で入力するのではなく、文字列をパスワードとして使用する。
パスワードは平文で端末履歴に残るため、このオプションは絶対に必要な場合にのみ使用してください。

# 関連項目

afpd(8), afp.conf(5)

# 著者

[CONTRIBUTORS](https://netatalk.io/contributors) を参照
