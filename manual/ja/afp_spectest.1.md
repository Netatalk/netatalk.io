# 名前

afp_spectest — AFP仕様準拠テストスイート

# 概要

**afp_spectest** [-1234567aCilmVvX] [-h *host*] [-H *host2*] [-p *port*] [-s *volume*] [-c *path to volume*]
[-S *volume2*] [-u *user*] [-d *user2*] [-w *password*] [-f *test*]

# 説明

**afp_spectest** は、数百のテストケースを含む包括的な AFP 仕様テストスイートである。
テスト対象となる AFP コマンドごと、またはテストの前提条件ごとに分類されたテストセットで構成されている。

利用可能なテストセットは、**-l** オプションで一覧表示できる。**-f**
オプションを使用すると、単一のテストまたはテストセット全体を実行できる。

# オプション

**-1**
: AFP 2.1プロトコルバージョンを使用する

**-2**
: AFP 2.2プロトコルバージョンを使用する

**-3**
: AFP 3.0プロトコルバージョンを使用する

**-4**
: AFP 3.1プロトコルバージョンを使用する

**-5**
: AFP 3.2プロトコルバージョンを使用する

**-6**
: AFP 3.3プロトコルバージョンを使用する

**-7**
: AFP 3.4プロトコルバージョンを使用する

**-a**
: テスト対象のサーバーはファイルシステム拡張属性ではなく AppleDouble v2 メタデータを使用する

**-c** *パズ*
: テストボリュームへのローカルファイルシステムのパス（Tier 2 テストに必須）

**-C**
: 端末出力でANSIカラーをオフにする

**-d** *user*
: 認証用の2番目のユーザー名

**-f** *test*
: 実行するテストまたはテストセットを指定する

**-h** *host*
: サーバーのホスト名またはIPアドレス（デフォルト: localhost）

**-H** *ホスト*
: 2番目のホストのサーバーホスト名またはIPアドレス

**-i**
: 対話型モード – 各テストの前にユーザーにプロンプトを表示します（デバッグに使用）

**-l**
: 利用可能なすべてのテストセットを一覧表示して終了する

**-m**
: Mac OS ネイティブ AFP サーバー互換モードでテストを実行する

**-p** *port*
: サーバーポート番号（デフォルト: 548）

**-s** *ボリューム名*
: テスト用にマウントするボリューム名

**-S** *ボリューム名*
: テスト用にマウントする2番目のボリュームのボリューム名

**-u** *ユーザー名*
: 認証用のユーザー名（デフォルト: 現在のuid）

**-v**
: 詳細出力

**-V**
: 超詳細出力

**-w** *パスワード文字列*
: 認証用のパスワード

**-X**
: ビッグエンディアンと互換性のないテストをスキップする

# 使用法

spectest スイートのテストは、一般的な使用パターンとパラメータは同じですが、特定のテストには追加の要件がある。AFP プロトコルバージョン
(**-1** から **-7**) を設定し、次にテスト対象ホスト (localhost も可)
のアドレスと認証情報を設定する。一部のテストでは、2番目のユーザーと2番目のボリュームを定義する必要がある。

いわゆる *tier 2* (T2) テストは localhost から実行し、テスト対象ボリュームへのローカルパスを **-c**
で指定する必要がある。これは、テストの前提条件などを設定するために、システムコールを使用してファイルシステムを直接変更するためだ。

読み取り専用テストとスリープテストも別途実行する必要がある。

## ファイル名拡張子マッピングのテスト

FPGetFileDirParms
テストセット内のいくつかのテストでは、ファイル名拡張子とタイプ/クリエータのマッピングが有効になっていることが想定されている。netatalk
バージョン 3 以降では、extmap.conf(5)
を編集し、この設定ファイル内のすべてのコメント行をアンコメントすることで、この拡張子マッピングを明示的に有効にする必要がある。

## スリープテスト

*FPzzz* テストセットには、AFP
スリープモードとタイムアウトのテストが含まれている。これらのテストは必然的に実行に時間がかかるため、spectest
スイートの実行時にはデフォルトでは実行されない。代わりに、*-f* パラメータを使用して明示的にテストセットを実行する必要がある。

    afp_spectest -f FPzzz

## 読み取り専用テスト

名前が示すように、*Readonly* テストセットは、共有ボリュームが読み取り専用モードのときの netatalk の動作を検証する。

言うまでもなく、テストするボリュームは読み取り専用として設定されている必要がある。これは、例えば afp.conf で *rolist*
を設定することで実現できる。

    [test volume]
    path = /my/path
    volume name = test_volume
    rolist = myuser

テストでは、読み取り専用の共有ボリュームに少なくとも2つのファイルと1つのディレクトリが存在することを想定している。

    echo "testfile uno" > /my/path/first.txt
    echo "testfile dos" > /my/path/second.txt
    mkdir /my/path/third

最後に、*Readonly* テストセットを実行する。

    afp_spectest -s test_volume -f Readonly

## 復帰コード

テストスイート内の各テストは、次のいずれかの戻りコードを返す。

- 0 PASSED
- 1 FAILED
- 2 NOT TESTED - テストのセットアップ手順または前提条件チェックに失敗した
- 3 SKIPPED - テストの要件が満たされていない

なお、「NOT TESTED」の結果はテスト実行全体の失敗として扱われますが、「SKIPPED」はそうではない。

Spectest は、ネイティブ Mac OS AFP サーバーに対して実行した場合も Netatalk
に対して実行した場合も同じ結果を返すが、前者の場合は、Mac との互換性を有効にするために **-m** パラメータを指定して Spectest
を実行する必要がある。

## Mac AFPサーバーのテスト

このツール群は、主に Netatalk AFP サーバーをテストするために設計されているが、古い Mac OS X または Classic Mac OS
システムでホストされている Mac OS AFP サーバーをテストするためにも使用できる。

Mac AFP サーバーをテストする場合は、**-m** オプションを使用してテストランナーを起動する。Mac
モードで実行すると、テストランナーは、Mac と Netatalk の間の既知の現在または過去の相違点を持つテストを報告する。

Mac と Netatalk が異なる場合、または Mac の結果がバージョン間で異なる場合:

    header.dsi_code       -5000     AFPERR_ACCESS
    MAC RESULT: -5019 AFPERR_PARAM    -5010 AFPERR_BUSY
    Netatalk returns AFPERR_ACCESS when a Mac return AFPERR_PARAM or AFPERR_BUSY

Mac と Netatalk が以前は異なる結果を返していたが、現在は同じように動作する場合:

    Warning MAC and Netatalk now same RESULT!

# 例

## 環境設定

以下は、AFP仕様テストを実行するためのサンプル設定です。現在、テストランナーでは ClearTxt とゲスト認証のみがサポートされている。

- 2つのユーザー: user1, user2 は同じパスワードを持つ
- 1つのグループ: afpusers
- user1, user2 は afpusers グループに割り当てられる

2つの空のディレクトリを用意する。テストディレクトリに残ったファイルがあると、いくつかのテストが失敗する。

    drwxrwsr-x    5 user1   afpusers       176 avr 27 23:56 /tmp/afptest1
    drwxrwsr-x    5 user1   afpusers       176 avr 27 23:56 /tmp/afptest2

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

    % afp_spectest -h 10.0.0.10 -u user1 -d user2 -w passwd -s testvol1 -S testvol2 -c /srv/afptest1 -7 -f FPSetForkParms_test
    ===================
    FPSetForkParms_test
    -------------------
    FPSetForkParms:test62: SetForkParams errors - PASSED
    FPSetForkParms:test141: Setforkmode error - PASSED
    FPSetForkParms:test217: Setfork size 64 bits - PASSED
    FPSetForkParms:test306: set fork size, new size > old size - PASSED

# 関連項目

**afp_logintest**(1), **afparg**(1), **afpd**(8)
