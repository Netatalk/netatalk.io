# 名前

afp_lantest – AFP LAN パフォーマンスおよびディレクトリキャッシュのテストツール

# 概要

**afp_lantest** [-34567bcGgKVv] [-h *host*] [-p *port*] [-s *volume*] [-u *user*] [-w *password*]
[-n *iterations*] [-f *tests*] [-F *bigfile*]

# 説明

**afp_lantest** は、ディレクトリキャッシュのパフォーマンスを含めて AFP (Apple Filing Protocol) サーバーの
様々な側面をベンチマークするために設計された包括的な AFP パフォーマンステストツールである。

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

**-c**
: Output results in CSV format (default: tabular)

**-F** *ビッグファイル*
: 読み取りテストにはボリュームのルート内の既存のファイルを使用する (ファイルサイズは -g/-G オプションと一致する必要がある)

**-f** *テスト*
: 実行する特定のテストを数字で指定する（例：「134」はテスト 1、3、4 を実行する）

**-G**
: 10ギガビットネットワーク向けに最適化 (ファイルのテストサイズが10GBに増加)

**-g**
: ギガビットネットワーク向けに最適化 (ファイルのテストサイズを1GBに増加)

**-h** *host*
: サーバーのホスト名またはIPアドレス（デフォルト: localhost）

**-K**
: キャッシュに重点を置いたテストのみを実行する（テスト9～12）

**-n** *回数*
: 実行するテスト反復回数（デフォルト: 2）。反復回数が5回を超える場合、外れ値は削除される

**-p** *port*
: サーバーポート番号（デフォルト: 548）

**-s** *ボリューム名*
: テスト用にマウントするボリューム名

**-u** *ユーザー名*
: 認証用のユーザー名（デフォルト: 現在のuid）

**-V**
: 超詳細出力

**-v**
: 詳細出力

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

テスト9～12は、netatalkにおけるディレクトリキャッシュのパフォーマンス向上に焦点を当てて設計されている。これらのテストは、最適化されたキャッシュ検証機能と確率的検証機能の恩恵を大きく受けている。これらのキャッシュ重視のテストのみを実行するには、**-K**
オプションを使用してください。

# 例

すべてのテストをデフォルト設定で実行する

    afp_lantest -h server.example.com -u testuser -w password -s TestVolume

キャッシュに重点を置いたテストのみを実行する

    afp_lantest -K -h server.example.com -u testuser -w password -s TestVolume

特定のテストを実行する（ファイル操作）

    afp_lantest -f 123 -h server.example.com -u testuser -w password -s TestVolume

ギガビットネットワークに最適化されたテストを実行する

    afp_lantest -g -h server.example.com -u testuser -w password -s TestVolume

統計分析のために複数の反復を実行する

    afp_lantest -n 5 -h server.example.com -u testuser -w password -s TestVolume

# IO監視の例

IO監視 (Linuxのみ) には、hidepid=0 で /proc_io にマウントされた proc ファイルシステムが必要である。*gid* を
afp_lantest を実行するユーザーのグループIDに設定する。

例えば、rootとして実行するには、`mkdir -p /proc_io && mount -t proc -o hidepid=0,gid=0
proc /proc_io` とする。

    afp_lantest -n 2 -7 -h 127.0.0.1 -p 548 -u test -w test -s 'File Sharing'
    Connecting to host 127.0.0.1:548
    IO monitoring: /proc_io is available
    Looking for cnid_dbd processes with -u test in command line
    Found cnid_dbd process: PID 40
    Looking for afpd processes owned by user 'test' (UID: 1000)
    Found privilege-dropped afpd process: PID 36
    IO monitoring enabled (afpd: 36, cnid_dbd: 40)

    Run 1 => Open, stat and read 512 bytes from 1000 files [8,000 AFP ops]        1923 ms
            IO Operations; afpd: 6000 READs, 7002 WRITEs | cnid_dbd: 0 READs, 2 WRITEs
    Run 1 => Writing one large file [103 AFP ops]                                  136 ms for 100 MB (avg. 771 MB/s)
            IO Operations; afpd: 0 READs, 299 WRITEs | cnid_dbd: 0 READs, 0 WRITEs
    Run 1 => Reading one large file [102 AFP ops]                                   39 ms for 100 MB (avg. 2688 MB/s)
            IO Operations; afpd: 100 READs, 100 WRITEs | cnid_dbd: 0 READs, 0 WRITEs
    Run 1 => Locking/Unlocking 10000 times each [20,000 AFP ops]                   799 ms
            IO Operations; afpd: 0 READs, 20000 WRITEs | cnid_dbd: 0 READs, 0 WRITEs
    Run 1 => Creating dir with 2000 files [4,000 AFP ops]                         4061 ms
            IO Operations; afpd: 2000 READs, 10005 WRITEs | cnid_dbd: 4 READs, 6150 WRITEs
    Run 1 => Enumerate dir with 2000 files [~51 AFP ops]                           637 ms
            IO Operations; afpd: 1960 READs, 49 WRITEs | cnid_dbd: 0 READs, 0 WRITEs
    Run 1 => Deleting dir with 2000 files [2,000 AFP ops]                         3176 ms
            IO Operations; afpd: 4000 READs, 4004 WRITEs | cnid_dbd: 2 READs, 6104 WRITEs
    Run 1 => Create directory tree with 1000 dirs [1,110 AFP ops]                 1885 ms
            IO Operations; afpd: 0 READs, 4445 WRITEs | cnid_dbd: 4 READs, 2351 WRITEs
    Run 1 => Directory cache hits (100 dirs + 1000 files) [11,000 AFP ops]        3625 ms
            IO Operations; afpd: 10000 READs, 11100 WRITEs | cnid_dbd: 0 READs, 100 WRITEs
    Run 1 => Mixed cache operations (create/stat/enum/delete) [820 AFP ops]       1134 ms
            IO Operations; afpd: 820 READs, 1621 WRITEs | cnid_dbd: 0 READs, 1201 WRITEs
    Run 1 => Deep path traversal (nested directory navigation) [3,500 AFP ops]     965 ms
            IO Operations; afpd: 2500 READs, 3550 WRITEs | cnid_dbd: 0 READs, 50 WRITEs
    Run 1 => Cache validation efficiency (metadata changes) [30,000 AFP ops]      8529 ms
            IO Operations; afpd: 30000 READs, 30100 WRITEs | cnid_dbd: 0 READs, 100 WRITEs
    Run 2 => Open, stat and read 512 bytes from 1000 files [8,000 AFP ops]        2453 ms
            IO Operations; afpd: 6000 READs, 7002 WRITEs | cnid_dbd: 0 READs, 2 WRITEs
    Run 2 => Writing one large file [103 AFP ops]                                   87 ms for 100 MB (avg. 1205 MB/s)
            IO Operations; afpd: 0 READs, 299 WRITEs | cnid_dbd: 0 READs, 0 WRITEs
    Run 2 => Reading one large file [102 AFP ops]                                   36 ms for 100 MB (avg. 2912 MB/s)
            IO Operations; afpd: 100 READs, 100 WRITEs | cnid_dbd: 0 READs, 0 WRITEs
    Run 2 => Locking/Unlocking 10000 times each [20,000 AFP ops]                   769 ms
            IO Operations; afpd: 0 READs, 20000 WRITEs | cnid_dbd: 0 READs, 0 WRITEs
    Run 2 => Creating dir with 2000 files [4,000 AFP ops]                         3442 ms
            IO Operations; afpd: 2000 READs, 10005 WRITEs | cnid_dbd: 7 READs, 6140 WRITEs
    Run 2 => Enumerate dir with 2000 files [~51 AFP ops]                           805 ms
            IO Operations; afpd: 1960 READs, 49 WRITEs | cnid_dbd: 0 READs, 0 WRITEs
    Run 2 => Deleting dir with 2000 files [2,000 AFP ops]                         2475 ms
            IO Operations; afpd: 4000 READs, 4003 WRITEs | cnid_dbd: 4 READs, 6180 WRITEs
    Run 2 => Create directory tree with 1000 dirs [1,110 AFP ops]                 1701 ms
            IO Operations; afpd: 0 READs, 4442 WRITEs | cnid_dbd: 2 READs, 2267 WRITEs
    Run 2 => Directory cache hits (100 dirs + 1000 files) [11,000 AFP ops]        2962 ms
            IO Operations; afpd: 10000 READs, 11100 WRITEs | cnid_dbd: 0 READs, 100 WRITEs
    Run 2 => Mixed cache operations (create/stat/enum/delete) [820 AFP ops]        598 ms
            IO Operations; afpd: 820 READs, 1621 WRITEs | cnid_dbd: 2 READs, 1242 WRITEs
    Run 2 => Deep path traversal (nested directory navigation) [3,500 AFP ops]     796 ms
            IO Operations; afpd: 2500 READs, 3550 WRITEs | cnid_dbd: 0 READs, 50 WRITEs
    Run 2 => Cache validation efficiency (metadata changes) [30,000 AFP ops]      8431 ms
            IO Operations; afpd: 30000 READs, 30100 WRITEs | cnid_dbd: 0 READs, 100 WRITEs

    Netatalk Lantest Results (Averages and standard deviations (±) for all tests, across 2 iterations (default))
    ============================================================================================================

    Test                                                                Time_ms  Time± AFPD_R AFPD_R± AFPD_W AFPD_W± CNID_R CNID_R± CNID_W CNID_W±   MB/s
    ------------------------------------------------------------------ -------- ------ ------ ------- ------ ------- ------ ------- ------ ------- ------
    Open, stat and read 512 bytes from 1000 files [8,000 AFP ops]          2188  374.8   6000     0.0   7002     0.0      0     0.0      2     0.0      0
    Writing one large file [103 AFP ops]                                    111   34.7      0     0.0    299     0.0      0     0.0      0     0.0    900
    Reading one large file [102 AFP ops]                                     37    2.2    100     0.0    100     0.0      0     0.0      0     0.0   2702
    Locking/Unlocking 10000 times each [20,000 AFP ops]                     784   21.2      0     0.0  20000     0.0      0     0.0      0     0.0      0
    Creating dir with 2000 files [4,000 AFP ops]                           3751  437.7   2000     0.0  10005     0.0      5     2.2   6145     7.1      0
    Enumerate dir with 2000 files [~51 AFP ops]                             721  118.8   1960     0.0     49     0.0      0     0.0      0     0.0      0
    Deleting dir with 2000 files [2,000 AFP ops]                           2825  495.7   4000     0.0   4003     1.0      3     1.4   6142    53.7      0
    Create directory tree with 1000 dirs [1,110 AFP ops]                   1793  130.1      0     0.0   4443     2.2      3     1.4   2309    59.4      0
    Directory cache hits (100 dirs + 1000 files) [11,000 AFP ops]          3293  468.8  10000     0.0  11100     0.0      0     0.0    100     0.0      0
    Mixed cache operations (create/stat/enum/delete) [820 AFP ops]          866  379.0    820     0.0   1621     0.0      2     0.0   1221    29.0      0
    Deep path traversal (nested directory navigation) [3,500 AFP ops]       880  119.5   2500     0.0   3550     0.0      0     0.0     50     0.0      0
    Cache validation efficiency (metadata changes) [30,000 AFP ops]        8480   69.3  30000     0.0  30100     0.0      0     0.0    100     0.0      0
    ------------------------------------------------------------------ -------- ------ ------ ------- ------ ------- ------ ------- ------ ------- ------
    Sum of all AFP OPs = 80686                                            25729         57380          92272             13          16069               

    Aggregates Summary:
    -------------------
    Average Time per AFP OP: 0.319 ms
    Average AFPD Reads per AFP OP: 0.711
    Average AFPD Writes per AFP OP: 1.144

## IO監視結果の列

    Time(ms) = Test runtime in milliseconds
    Time±    = Test runtime standard deviation
    AFPD_R   = afpd process IO Read operations
    AFPD_R±  = afpd process IO Read operation standard deviation
    AFPD_W   = afpd process IO Write operations
    AFPD_W±  = afpd process IO Write operation standard deviation

    CNID_*   = IO measurements for the cnid_dbd process (optional)

注意: afp_lantest でパフォーマンステストを行う場合、afp.conf の `log level` を `default:severe`
に設定してください。これより詳細に設定すると、カウントされた AFPD_W IO 値にログ書き込みが含まれる可能性がある。

## IO監視集計サマリー

集計値は純粋に内在的な指標であり、AFP操作は読み取り、書き込み、および接続関連の操作の混合である。

したがって、測定値はそれ自体のコンテキスト内でのみ意味がある。これらは、それ自体に対する変更を評価する方法を提供するが、他のシステムとの比較のための外部の一貫性や参照点を欠いている。

一般に、1未満の値は効率的な操作を示し（例えば、バッチ処理やキャッシュなどによる）、1を超える値は最適でない操作を示す（例えば、単一の操作の増幅により、追加の下流操作が発生する）。

注意: 総AFP操作は読み取り、書き込み、その他の操作の混合であるため、効果的な1:1 (AFP:IO)
閾値は1と等しくない。正確な閾値は、テストごとにテストウィキに示されている情報を使用して計算し、関連するAFP読み取り/書き込み操作を関連するAFPD_R/AFPD_W値と比較することで求めることができる。

理想的には、コードの変更により集計値が減少することを確認する必要がある。

詳細については、[Testing ウィキページ](https://netatalk.io/docs/Testing) を参照してください。

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
