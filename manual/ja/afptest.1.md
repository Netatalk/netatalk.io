# 名前

afp_lantest, afp_logintest, afp_spectest, afp_speedtest, afparg, fce_listen
— AFP プロトコルテスト一式

# 概要

`afp_lantest [-34567GgVv] [-h host] [-p port] [-s volume] [-u user] [-w
password] [-n iterations] [-t tests] [-F bigfile]`

`afp_logintest [-1234567CmVv] [-h host] [-p port] [-s volume] [-u user] [-w
password]`

`afp_spectest [-1234567aCiLlmVvXx] [-h host] [-H host2] [-p port] [-s
volume] [-c path to volume] [-S volume2] [-u user] [-d user2] [-w password]
[-f test]`

`afp_speedtest [-1234567aeiLnVvy] [-h host] [-p port] [-s volume] [-S
volume2] [-u user] [-w password] [-n iterations] [-d size] [-q quantum] [-F
file] [-f test]`

`afparg [-1234567lVv] [-h host] [-p port] [-s volume] [-u user] [-w
password] [-f command]`

`fce_listen [-h host] [-p port]`

# 説明

このスイートには、AFP サーバーをテストするためのいくつかのユーティリティが含まれている。適合性テスト、ベンチマーク、ヘルパーに大別される。

*afptest*
ツール群は大体同じ一般的な使用パターンとパラメータに従う。AFP プロトコル リビジョン (**-1** から **-7**)
を設定し、次にテストするホストのアドレスと資格情報 (localhost も可)
を設定する。一部のテストでは、2番目のユーザーと2番目のボリュームを定義する必要がある。さらに別のテスト セットを localhost
から実行し、テスト対象のボリュームへのローカル パスを指定する必要がある。 単一のテストまたはテスト セクションは、**-f**
オプションで実行できる。使用可能なテストは、**-l** オプションで一覧表示できる。

各オプションの正確な使用方法については、各ツールのヘルプテキストを参照してください。

## 復帰コード

テストスイート内の各テストは、次の復帰コードのいずれかを返す。

- 0 PASSED
- 1 FAILED
- 2 NOT TESTED - テストの準備または前提条件チェックに失敗した
- 3 SKIPPED - テストの前提条件が満たされていない

NOT TESTED の結果はテスト実施全体の失敗として扱われるが、SKIPPED はそうではない。

テスト対象 AFP サーバーは Mac か Netatalk のどちらでもよく、spectest と logintest
の結果は同じでなければならない。

## 適合性テスト

**afp_spectest** は、数百個のテスト項目を含む AFP 仕様テスト スイートの中核を 構成する。これは、テストする AFP コマンド別、またはテストの前提条件別に分けられたテストセットに編成されている。 たとえば、Tier 2 (T2) テストは、共有ボリュームへのパスを示す **-c** オプションを使用してホスト上で 実行する必要がある。また、読み取り専用テストとスリープ テストも別々に実行する必要がある。

**afp_logintest** は、DSI セッションと認証のテスト スイートである。

## ベンチマーク

**afp_lantest**は、AFP サーバーのファイル転送ベンチマークです。さまざまなファイル転送パターンのバッチを実行する *HELIOS LanTest* にヒントを得たものである。

**afp_speedtest**は、読み•書き•コピー操作のベンチマークツールである。他のファイル転送プロトコルとの比較テストを行うために、AFP
コマンドまたは POSIX システムコールを使用して実行できる。

## ヘルパー

**afparg** は、オプションの引数を持つ特定のコマンドを受け取り、AFP サーバーにアクションを送信する対話型 AFP クライアントである。サーバの問題検討やシステム管理などに活用できる。`afparg -l` を実行して利用可能なコマンドを一覧表示する。

**fce_listen** は、Netatalk のファイルシステム変更イベント (FCE) プロトコルのシンプルなリスナーである。これは、AFP サーバーから受信した UDP データグラムを出力する。

## Mac AFP サーバーのテスト

このツール群は、主に Netatalk AFP サーバーをテストするために設計されているが、古い Mac OS X または Classic Mac OS
システムでホストされている Mac OS AFP サーバーをテストするためにも使用できる。

Mac AFP サーバーをテストする場合は、`-m` オプションを使用してテストランナーを起動する。Mac モードで実行すると、テストランナーは、Mac
と Netatalk の間の既知の現在または過去の相違点を持つテストを報告する。

Mac と Netatalk が異なる場合、または Mac の結果がバージョン間で異なる場合:

    header.dsi_code       -5000     AFPERR_ACCESS
    MAC RESULT: -5019 AFPERR_PARAM    -5010 AFPERR_BUSY
    Netatalk returns AFPERR_ACCESS when a Mac return AFPERR_PARAM or AFPERR_BUSY

Mac と Netatalk が以前は異なる結果を返していたが、現在は同じように動作する場合:

    Warning MAC and Netatalk now same RESULT!

# 例

## 環境設定

以下は、APF 仕様テストを実行するためのサンプル設定です。

- 2人のユーザー: <user1> <user2> は同じパスワードを持つ。
- 1つのグループ: <afpusers>
- user1, user2 は afpusers グループに割り当てられる。
- clear text UAM + guest UAM
- 2つの空のボリューム:

>    drwxrwsr-x    5 user1   afpusers       176 avr 27 23:56 /tmp/afptest1
>    drwxrwsr-x    5 user1   afpusers       176 avr 27 23:56 /tmp/afptest2

*注意:* テストボリュームに残ったファイルがあると、いくつかのテストが失敗する。

afp.confオプションは次の通り。

    [Global]
    uam list = uams_clrtxt.so uams_guest.so

    [testvol1]
    ea = sys
    path = /tmp/afptest1
    valid users = @afpusers
    volume name = testvol1

    [testvol2]
    ea = sys
    path = /tmp/afptest2
    valid users = @afpusers
    volume name = testvol2

## テストを実行する

afp_spectest の FPSetForkParms_test テストセットを AFP 3.4 で実行する。

    % afp_spectest -h 127.0.0.1 -p 548 -u user1 -d user2 -w passwd -s testvol1 -S testvol2 -c /srv/afptest1 -7 -f FPSetForkParms_test
    ===================
    FPSetForkParms_test
    -------------------
    FPSetForkParms:test62: SetForkParams errors - PASSED
    FPSetForkParms:test141: Setforkmode error - PASSED
    FPSetForkParms:test217: Setfork size 64 bits - PASSED
    FPSetForkParms:test306: set fork size, new size > old size - PASSED

AFP 3.0 を使用して afp_lantest ベンチマークを実行する。

    % afp_lantest -h 192.168.0.2 -s testvol1 -u user1 -w passwd -3
    Run 0 => Opening, stating and reading 512 bytes from 1000 files   1799 ms
    Run 0 => Writing one large file                                     30 ms for 100 MB (avg. 3495 MB/s)
    Run 0 => Reading one large file                                      8 ms for 100 MB (avg. 13107 MB/s)
    Run 0 => Locking/Unlocking 10000 times each                       1959 ms
    Run 0 => Creating dir with 2000 files                             1339 ms
    Run 0 => Enumerate dir with 2000 files                             217 ms
    Run 0 => Create directory tree with 10^3 dirs                      496 ms

    Netatalk Lantest Results (averages)
    ===================================

    Opening, stating and reading 512 bytes from 1000 files   1799 ms
    Writing one large file                                     30 ms for 100 MB (avg. 3495 MB/s)
    Reading one large file                                      8 ms for 100 MB (avg. 13107 MB/s)
    Locking/Unlocking 10000 times each                       1959 ms
    Creating dir with 2000 files                             1339 ms
    Enumerate dir with 2000 files                             217 ms
    Create directory tree with 10^3 dirs                      496 ms

# 参照

afpd(8)

# 著者

[CONTRIBUTORS](https://netatalk.io/contributors) を参照
