# 名前

afp_spectest — AFP仕様準拠テストスイート

# 概要

**afp_spectest** [-1234567aCEimVvX] [-h *ホスト*] [-H *ホスト2*] [-p *ポート*] [-s *ボリューム*] [-c *ボリュームへのパス*]
[-S *ボリューム2*] [-u *ユーザー*] [-d *ユーザー2*] [-w *パスワード*] [-f *テスト*]

**afp_spectest** -l

# 説明

**afp_spectest** は、数百のテストケースを含む包括的なAFP仕様テストスイートである。
テスト対象となるAFPコマンドごと、またはテストの前提条件ごとに分類されたテストセットで構成されている。

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
: AFPサーバーの認証用の2番目のユーザー名

**-E**
: テストを実行する前にテストボリュームを空にする

> 【警告】 これにより、テストボリューム内のすべてのファイルとディレクトリが削除されてしまう!

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
: AppleShare (Mac) AFP サーバー互換モードでテストを実行する

**-p** *port*
: サーバーポート番号（デフォルト: 548）

**-s** *ボリューム名*
: テスト用にマウントするボリューム名

**-S** *ボリューム名*
: テスト用にマウントする2番目のボリュームのボリューム名

**-u** *ユーザー名*
: AFPサーバーの認証用のユーザー名（デフォルト: 現在のuid）

**-v**
: 詳細出力

**-V**
: 超詳細出力

**-w** *パスワード文字列*
: AFPサーバーの認証用のパスワード

**-X**
: ビッグエンディアンと互換性のないテストをスキップする

# 使用法

spectestのテスト項目は、一般的な使用パターンとパラメータは統一されているが、特定のテストには追加の要件がある。AFPプロトコルバージョン
(**-1** から **-7**) を設定し、次にテスト対象ホスト (localhost も可)
のアドレスと認証情報を設定する。一部のテストでは、2番目のユーザーと2番目のボリュームを定義する必要がある。

いわゆる *tier 2* (T2) テストは localhost から実行し、テスト対象ボリュームへのローカルパスを **-c**
で指定する必要がある。これは、テストの前提条件や結果検証などを設定しつつ、システムコールを使用してファイルシステムを直接弄るためである。

読み取り専用テストとスリープテストも別途実行する必要がある。

## ファイル名拡張子マッピングのテスト

FPGetFileDirParms テストセット内のいくつかのテストでは、ファイル名拡張子をClassic Mac
OS式の「Type/Creator」へのマッピングが有効になっていることが想定されている。netatalk バージョン 3
以降では、extmap.conf(5)
を編集し、この構成ファイルで有効にしたいマッピングの行のコメントを解除することで、この拡張マッピングを明示的に有効にする必要がある。

## スリープテスト

*FPzzz* テストセットは、AFP
スリープモードとタイムアウトを検証するテスト項目になっている。これらのテストは必然的に実行に時間がかかるため、spectest
スイートの実行時にはデフォルトでは実行されない。実行するには *-f* パラメータを使用する必要がある。

    afp_spectest -f FPzzz

## 読み取り専用テスト

名前が示すように、*Readonly* テストセットは、共有ボリュームが読み取り専用モードのときの netatalk の動作を検証する。

言うまでもなく、テストするボリュームは読み取り専用として設定されている必要がある。これは、例えば afp.conf で *read only =
yes* を設定することで実現できる。

    [test volume]
    path = /my/path
    volume name = test_volume
    read only = yes

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
- 2 NOT TESTED
- 3 SKIPPED

*NOT TESTED* は、テストセットアップステップまたは前提条件の検証に失敗したことを意味する。
この戻りコードは、テスト実行を失敗としてフラグ付けする。

*SKIPPED* は、テストがテスト対象の AFP サーバーに適用されないこと、またはテストに必要な特定のパラメータが欠落していることを意味する。
テストがスキップされた具体的な理由については、テストレポートを確認すること。
この戻りコードは、テスト結果を失敗としてフラグ付けしない。

## AppleShare AFP サーバーのテスト

このツール群は、主に Netatalk AFP サーバーをテストするために設計されているが、古い Mac OS X または Classic Mac OS
システムでホストされている AppleShare AFP サーバーをテストするためにも使用できる。

AppleShare AFP サーバーをテストする場合は、**-m** (Mac)
オプションを使用してテストランナーを起動する。このモードで実行すると、テストランナーは、AppleShare と Netatalk
の間の既知の現在または過去の相違点を持つテストを報告する。

AppleShare と Netatalk が異なる場合、または AppleShare の結果がバージョン間で異なる場合:

    header.dsi_code       -5000     AFPERR_ACCESS
    MAC RESULT: -5019 AFPERR_PARAM    -5010 AFPERR_BUSY
    Netatalk returns AFPERR_ACCESS when a Mac return AFPERR_PARAM or AFPERR_BUSY

AppleShare と Netatalk が以前は異なる結果を返していたが、現在は同じように動作する場合:

    Warning MAC and Netatalk now same RESULT!

上記の場合以外には、Mac OS 組み込みの AppleShare AFP サーバーまたは Netatalk
に対して実行されるかどうかにかかわらず、同じ結果を返すものとする。

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
