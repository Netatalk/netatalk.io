# 名前

afp_lantest – AFP LAN パフォーマンスおよびディレクトリキャッシュのテストツール

# 概要

**afp_lantest** [-34567GgVvbC] [-h *host*] [-p *port*] [-s *volume*] [-u *user*] [-w *password*]
[-n *iterations*] [-f *tests*] [-F *bigfile*]

# 説明

**afp_lantest** は、AFP (Apple Filing Protocol) サーバーの様々な側面をベンチマークするために
設計された包括的な AFP パフォーマンステストツールである。
特に netatalk におけるディレクトリキャッシュのパフォーマンス改善に重点を置いている。

このツールは、ファイル操作、ディレクトリトラバーサル、キャッシュ効率を測定する一連のテストを実行する。従来のファイルシステムベンチマークに加え、最適化されたディレクトリキャッシュ検証と確率的検証機能の利点を強調する、キャッシュに特化したテストも含まれている。

# オプション

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

**-b**
: デバッグモード

**-C**
: キャッシュに重点を置いたテストのみを実行する（テスト9～12）

**-f** *テスト*
: 実行する特定のテストを数字で指定する（例：「134」はテスト 1、3、4 を実行する）

**-F** *ビッグファイル*
: 読み取りテストにはボリュームのルート内の既存のファイルを使用する (ファイルサイズは -g/-G オプションと一致する必要がある)

**-g**
: ギガビットネットワーク向けに最適化 (ファイルのテストサイズを1GBに増加)

**-G**
: 10ギガビットネットワーク向けに最適化 (ファイルのテストサイズが10GBに増加)

**-h** *host*
: サーバーのホスト名またはIPアドレス（デフォルト: localhost）

**-n** *回数*
: 実行するテスト反復回数（デフォルト: 1）

**-p** *port*
: サーバーポート番号（デフォルト: 548）

**-s** *ボリューム名*
: テスト用にマウントするボリューム名

**-u** *ユーザー名*
: 認証用のユーザー名（デフォルト: 現在のuid）

**-v**
: 詳細出力

**-V**
: 超詳細出力

**-w** *パスワード文字列*
: 認証用のパスワード

# 設定

テストランナーの AFP クライアントは現在 ClearTxt UAM のみをサポートしている。netatalk の afp.conf で UAM
を設定する。

    [Global]
    uam list = uams_clrtxt.so

# 利用可能なテスト

以下のテストが利用可能

**(1) 1000個のファイルを開き、512バイトを読み出す**
: 多数の小さな操作を伴う基本的なファイルアクセスパターンをテストする

**(2) 1つの大きなファイルを書き込む**
: 持続的な書き込みパフォーマンスを測定する

**(3) 1つの大きなファイルを読み取る**
: 持続的な読み取りパフォーマンスを測定する

**(4) ロック/ロック解除をそれぞれ10000回行う**
: ファイルのロックパフォーマンスをテストする

**(5) 2000個のファイルを含むディレクトリを作成する**
: ディレクトリ作成とファイル作成のパフォーマンスをテストする

**(6) 2000個のファイルを含むディレクトリを列挙する**
: 多数のファイルを含むディレクトリ列挙をテストする

**(7) 2000個のファイルを含むディレクトリを削除する**
: ディレクトリとファイルの削除のパフォーマンスをテストする

**(8) 1000個のディレクトリを含むディレクトリツリーを作成する**
: ネストされたディレクトリの作成をテストする

**(9) ディレクトリキャッシュヒット [CACHE]**
: ディレクトリとファイルの検索パフォーマンスをテストする。 (1000ディレクトリ + 10000ファイル)

**(10) 混合キャッシュ操作 [CACHE]**
: create/stat/enum/delete の各操作をテストする

**(11) ディープパストラバーサル [CACHE]**
: 深いディレクトリ構造でのパフォーマンスをテストする

**(12) キャッシュ検証 [CACHE]**
: ディレクトリキャッシュの検証メカニズムをテストする

## キャッシュ重視のテスト

テスト9～12は、netatalkにおけるディレクトリキャッシュのパフォーマンス向上に焦点を当てて設計されている。これらのテストは、最適化されたキャッシュ検証機能と確率的検証機能の恩恵を大きく受けている。これらのキャッシュ重視のテストのみを実行するには、**-C**
オプションを使用してください。

# 例

すべてのテストをデフォルト設定で実行する

    afp_lantest -h server.example.com -u testuser -w password -s TestVolume

キャッシュに重点を置いたテストのみを実行する

    afp_lantest -C -h server.example.com -u testuser -w password -s TestVolume

特定のテストを実行する（ファイル操作）

    afp_lantest -f 123 -h server.example.com -u testuser -w password -s TestVolume

ギガビットネットワークに最適化されたテストを実行する

    afp_lantest -g -h server.example.com -u testuser -w password -s TestVolume

統計分析のために複数の反復を実行する

    afp_lantest -n 5 -h server.example.com -u testuser -w password -s TestVolume

AFP 3.4 を使用して afp_lantest ベンチマークを実行する

    % afp_lantest -7 -h localhost -p 548 -u test -w test -s "File Sharing" -n 2
    Run 0 => Opening, stating and reading 512 bytes from 1000 files   3237 ms
    Run 0 => Writing one large file                                    146 ms for 100 MB (avg. 718 MB/s)
    Run 0 => Reading one large file                                     36 ms for 100 MB (avg. 2912 MB/s)
    Run 0 => Locking/Unlocking 10000 times each                        772 ms
    Run 0 => Creating dir with 2000 files                             3615 ms
    Run 0 => Enumerate dir with 2000 files                             755 ms
    Run 0 => Deleting dir with 2000 files                             1245 ms
    Run 0 => Create directory tree with 10^3 dirs                     1724 ms
    Run 0 => Directory cache hits (1000 dir + 10000 file lookups)     3056 ms
    Run 0 => Mixed cache operations (create/stat/enum/delete)          484 ms
    Run 0 => Deep path traversal (nested directory navigation)         377 ms
    Run 0 => Cache validation efficiency (metadata changes)           8822 ms
    Run 1 => Opening, stating and reading 512 bytes from 1000 files   3448 ms
    Run 1 => Writing one large file                                     79 ms for 100 MB (avg. 1327 MB/s)
    Run 1 => Reading one large file                                     37 ms for 100 MB (avg. 2833 MB/s)
    Run 1 => Locking/Unlocking 10000 times each                        779 ms
    Run 1 => Creating dir with 2000 files                             3731 ms
    Run 1 => Enumerate dir with 2000 files                             587 ms
    Run 1 => Deleting dir with 2000 files                             1156 ms
    Run 1 => Create directory tree with 10^3 dirs                     1802 ms
    Run 1 => Directory cache hits (1000 dir + 10000 file lookups)     3006 ms
    Run 1 => Mixed cache operations (create/stat/enum/delete)          463 ms
    Run 1 => Deep path traversal (nested directory navigation)         247 ms
    Run 1 => Cache validation efficiency (metadata changes)           8565 ms

    Netatalk Lantest Results (average times across 2 iterations)
    ===================================

    Test 1: Opening, stating and reading 512 bytes from 1000 files
     Average:   3342 ms ± 149.2 ms (std dev)

    Test 2: Writing one large file
     Average:    112 ms ± 47.4 ms (std dev)
     Throughput: 936 MB/s (Write, 100 MB file)

    Test 3: Reading one large file
     Average:     36 ms ± 1.0 ms (std dev)
     Throughput: 2912 MB/s (Read, 100 MB file)

    Test 4: Locking/Unlocking 10000 times each
     Average:    775 ms ± 5.0 ms (std dev)

    Test 5: Creating dir with 2000 files
     Average:   3673 ms ± 82.0 ms (std dev)

    Test 6: Enumerate dir with 2000 files
     Average:    671 ms ± 118.8 ms (std dev)

    Test 7: Deleting dir with 2000 files
     Average:   1200 ms ± 62.9 ms (std dev)

    Test 8: Create directory tree with 1000 dirs
     Average:   1763 ms ± 55.2 ms (std dev)

    Test 9: Directory cache hits (1000 dir + 10000 file lookups)
     Average:   3031 ms ± 35.4 ms (std dev)

    Test 10: Mixed cache operations (create/stat/enum/delete)
     Average:    473 ms ± 14.9 ms (std dev)

    Test 11: Deep path traversal (nested directory navigation)
     Average:    312 ms ± 91.9 ms (std dev)

    Test 12: Cache validation efficiency (metadata changes)
     Average:   8693 ms ± 181.7 ms (std dev)

# 復帰コード

**0**
: すべてのテストは成功した

**1**
: 1つ以上のテストが失敗した

# 注記

- 大容量ファイル操作を伴うテスト（テスト2および3）では、テストボリュームに一時ファイルが作成される。
- **-g** および **-G** オプションは、テストファイルのサイズとテスト時間を大幅に増加させる。
- キャッシュに重点を置いたテスト（8～11）は、netatalk のディレクトリキャッシュのパフォーマンスに関する最も詳細な情報を提供する。
- 一貫したパフォーマンス測定には、複数回の反復（**-n**）が推奨される。
- このツールは、指定された AFP ボリュームへの書き込みアクセスを必要とする。

# 関連項目

**afp_speedtest**(1), **afpd**(8), **netatalk**(8)
