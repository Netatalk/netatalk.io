# 以前の Netatalk バージョンからのアップグレード

## Netatalk 3 からのアップグレード

Netatalk 3 から Netatalk 4 へのアップグレードは簡単。古いバージョンの上に新しいバージョンをインストールするだけ。Netatalk
4 での主要な変更点は、Netatalk 2 と Netatalk 3 の間で削除された AppleTalk
サービス、構成ファイル、およびツールを一部復活させたことである。

主に、**atalkd** デーモンと **atalkd.conf** 設定ファイル、また **papd** デーモンと **papd.conf**
設定ファイルが追加された。

## Netatalk 2 からのアップグレード

Netatalk 4 の主要な変更は以下の3点：

1.  これまでの AFP 設定ファイルすべてが廃止され、AFP に関してのほぼ全オプション名を変更し、新しい設定ファイルを追加した：
    *afp.conf* と *extmap.conf*

2.  ファイルメタデータをファイルシステムの拡張属性に保存する新しいバックエンド。

3.  AppleTalk トランスポート層はデフォルトで無効になっている。非常に古い Mac で Netatalk
    を使用する場合は、*afp.conf* にて **appletalk = yes** オプションで有効にしてください。
    それから、**netatalk** を起動する前に **atalkd** デーモンを立ち上げてください。

### 設定まわりの変更点

#### afp.conf

- （Samba の smb.conf のような） "ini" スタイルの構文

- 一つで設定すべてを指示するという点： AFP 及びボリュームの構成を共に一つのファイルで設定することになるという点

- *afpd.conf*、 *netatalk.conf*、 *AppleVolumes.default* 及び、 *afp_ldap.conf*
の廃止

> **警告**

> ほとんどのオプション名は変更されたので、 詳細については
[afp.conf](afp.conf.html) の manpage 全体を読むこと

#### extmap.conf

- Classic Mac OS type/creator と拡張子の関連付け

- 2.x とは異なり、マッピングはデフォルトで無効になっている。有効にするには、ファイル内の行のコメントを解除する

- *AppleVolumes.system* の廃止

### 新たなメタデータバックエンド

macOS拡張属性およびClassic Mac OS リソースフォークをファイルシステムの拡張属性に保存する **ea = sys**
という新しいバックエンド。

- デフォルトのバックエンドである（！）

- 拡張属性のあるファイルシステムが必須。 さもなくば **ea = ad** オプションの使用が代替となる

- ファイルシステムを AppleDouble v2 から拡張属性への変換はアクセス時、その都度行われる（**convert appledouble**
オプションを無効にすることも可能）

- 一括で変換する場合 **dbd** を用いることができる

実装の詳細：

- Mac のメタデータ（すなわち FinderInfo、AFP フラグ、コメント、CNID）は “*org.netatalk.Metadata*”
という名前の拡張属性に保存される。

- さらに、Netatalk 4.1.0以降を実行しているmacOSホストでは、FinderInfo はファイルシステムにネイティブに保存され、"com.apple.FinderInfo" という名前の拡張属性として表示される。

- マックのリソースフォークは：

- ZFS を用いた Solaris では “*org.netatalk.ResourceFork*” という拡張属性に保存される。

- ないしは、ファイル名が “*file*” であるものに対して各々、“*._file*” という名の別の AppleDouble ファイルに保存される。

- Netatalk 4.1.0 以降、macOS ホスト上のリソース フォークにネイティブに保存されている。

- ".\_" ファイルのフォーマットは、 たとえそのファイルシステムに CIFS サーバー (Samba) 経由でアクセスした場合でも、 マックの
CIFS クライアントが想定しているフォーマットと全く同じである。 なので、データを失う危険性（リソースもメタデータも）なく、
マックから同じデータセットに AFP 経由と CIFS 経由と並行してアクセスすることができる。 一方、ウィンドウズから当該データセットに CIFS
経由でアクセスした場合は、未だに “*file*” と “*file*” の紐付けを失うこととなるであろう（非 ZFS
ファイルシステムの場合。上記参照）。 今のところその点で拡張 Samba VFS モジュールが必要である（改善中）。

### そのほかの主要な変更点

- AFP 及び CNID デーモンの起動・再起動を担う新しいサービスコントローラデーモン [netatalk](netatalk.html)
の導入。バンドルされているスタートスクリプトが すべて更新されているため、自分の環境でもアップデートされているか確認する必要あり！

- CNID データベースはデフォルトで *$prefix/var/netatalk/CNID/*
以下に保存される。以前は各共有ボリュームにて保存されていた。

- Netatalk 2.x のボリュームオプション “**usedots**” 及び “**upriv**” はデフォルトとなった。

- SLP 及び AFP プロキシのサポート機能は削除。

### アップグレード手段

1.  Netatalk 2.x を停止する

2.  Netatalk 4 をインストールする

3.  設定 *afp.conf* 及び *extmap.conf* を自力で書き換える

4.  **afpd** と **cnid_metad** の代わりに **netatalk** 起動にのみ関連している、 Netatalk
    起動スクリプトを更新するか、標準の起動スクリプトに置き換える。

5.  *afp_voluuid.conf* 及び *afp_signature.conf* を localstate ディレクトリ （デフォルトでは
    *$prefix/var/netatalk/*）、に移動。 正しいパスを見つけるために **afpd -v** コマンドが有用

6.  Netatalk 4 を起動する

### 新旧設定ファイル名

| 旧ファイル名 | 新ファイル名 | 注記 |
|----|----|----|
| \- | `etc/afp.conf` | 新しい "ini" 様式のフォーマット |
| \- | `etc/extmap.conf` | netatalk 3.0.2 から採用 |
| `etc/netatalk/afp_signature.conf` | `var/netatalk/afp_signature.conf` | 厳密には $localstatedir に移動 |
| `etc/netatalk/afp_voluuid.conf` | `var/netatalk/afp_voluuid.conf` | 厳密には $localstatedir に移動 |
| `etc/netatalk/netatalk.conf` (`/etc/default/netatalk`) | \- | 廃止 |
| `etc/netatalk/afpd.conf` | \- | 廃止 |
| `etc/netatalk/afp_ldap.conf` | \- | 廃止 |
| `etc/netatalk/AppleVolumes.default` | \- | 廃止 |
| `etc/netatalk/AppleVolumes.system` | \- | 廃止 |
| `~/.AppleVolumes` | \- | 廃止 |

### 新旧オプション対応表

**netatalk.conf (/etc/default/netatalk) から afp.conf**

| 旧 netatalk.conf | 新 afp.conf | 旧デフォルト値 | 新デフォルト値 | セクション | 詳細 |
|----|----|----|----|----|----|
| ATALK_NAME | hostname | \- | \- | \(G\) | デフォルトでは gethostname() を使用 |
| ATALK_UNIX_CHARSET | unix charset | LOCALE | UTF8 | \(G\) | \- |
| ATALK_MAC_CHARSET | mac charset | MAC_ROMAN | MAC_ROMAN | (G)/(V) | \- |
| CNID_METAD_RUN | \- | yes | \- | \- | netatalk(8) で制御 |
| AFPD_RUN | \- | yes | \- | \- | netatalk(8) で制御 |
| AFPD_MAX_CLIENTS | max connections | 20 | 200 | \(G\) | \- |
| AFPD_UAMLIST | uam list | -U uams_dhx.so,uams_dhx2.so | uams_dhx.so uams_dhx2.so | \(G\) | \- |
| AFPD_GUEST | guest account | nobody | nobody | \(G\) | \- |
| CNID_CONFIG | log level | -l log_note | cnid:note | \(G\) | \- |
| CNID_CONFIG | log file | \- | \- | \(G\) | \- |
| ATALKD_RUN | \- | no | \- | \- | 独自起動スクリプトで制御 |
| PAPD_RUN | \- | no | \- | \- | 独自起動スクリプトで制御 |
| TIMELORD_RUN | \- | no | \- | \- | 独自起動スクリプトで制御 |
| A2BOOT_RUN | \- | no | \- | \- | 独自起動スクリプトで制御 |
| ATALK_BGROUND | \- | no | \- | \- | 独自起動スクリプトで制御 |
| ATALK_ZONE | ddp zone | \- | \- | \(G\) | 4.0.0で復活 |

**afpd.conf から afp.conf**

| 旧 afpd.conf | 新 afp.conf | 旧デフォルト値 | 新デフォルト値 | セクション | 詳細 |
|----|----|----|----|----|----|
| 一番目のフィールド（"-" あるいは“サーバー名”) | hostname | \- | \- | \(G\) | 4.2.0で新規追加、デフォルトでは hostname を使用 |
| -uamlist | uam list | uams_dhx.so,uams_dhx2.so | uams_dhx.so uams_dhx2.so | \(G\) | \- |
| -nozeroconf | zeroconf | \- | （サポートされていれば） yes | \(G\) | \- |
| -advertise_ssh | advertise ssh | \- | no | \(G\) | \- |
| -\[no\]savepassword | save password | -savepassword | yes | \(G\) | \- |
| -\[no\]setpassword | set password | -nosetpassword | no | \(G\) | \- |
| -client_polling | client polling | \- | no | \(G\) | \- |
| -hostname | hostname | \- | \- | \(G\) | デフォルトでは gethostname() を使用 |
| -loginmesg | login message | \- | \- | (G)/(V) | \- |
| -guestname | guest account | nobody | nobody | \(G\) | \- |
| -passwdfile | passwd file | afppasswd | afppasswd | \(G\) | \- |
| -passwdminlen | passwd minlen | \- | \- | \(G\) | \- |
| -tickleval | tickleval | 30 | 30 | \(G\) | \- |
| -timeout | timeout | 4 | 4 | \(G\) | \- |
| -sleep | sleep time | 10 | 10 | \(G\) | \- |
| -dsireadbuf | dsireadbuf | 12 | 12 | \(G\) | \- |
| -server_quantum | server quantum | 303840 | 1048576 | \(G\) | \- |
| -volnamelen | volnamelen | 80 | 80 | \(G\) | \- |
| -setuplog | log level | default log_note | default:note | \(G\) | \- |
| -setuplog | log file | \- | \- | \(G\) | \- |
| -admingroup | admingroup | \- | \- | \(G\) | \- |
| -k5service | k5 service | \- | \- | \(G\) | \- |
| -k5realm | k5 realm | \- | \- | \(G\) | \- |
| -k5keytab | k5 keytab | \- | \- | \(G\) | \- |
| -uampath | uam path | etc/netatalk/uams/ | lib/netatalk/ | \(G\) | 厳密には $libdir に移動 |
| -ipaddr | afp listen | \- | \- | \(G\) | \- |
| -cnidserver | cnid server | localhost:4700 | localhost:4700 | (G)/(V) | \- |
| -port | port | 548 | 548 | \(G\) | \- |
| -signature | signature | auto | \- | \(G\) | \- |
| -fqdn | fqdn | \- | \- | \(G\) | \- |
| -unixcodepage | unix charset | LOCALE | UTF8 | \(G\) | \- |
| -maccodepage | mac charset | MAC_ROMAN | MAC_ROMAN | (G)/(V) | \- |
| -closevol | close vol | \- | no | \(G\) | \- |
| -ntdomain | nt domain | \- | \- | \(G\) | \- |
| -ntseparator | nt separator | \- | \- | \(G\) | \- |
| -dircachesize | dircachesize | 8192 | 8192 | \(G\) | \- |
| -tcpsndbuf | tcpsndbuf | \- | \- | \(G\) | OS のデフォルト |
| -tcprcvbuf | tcprcvbuf | \- | \- | \(G\) | OS のデフォルト |
| -fcelistener | fce listener | \- | \- | \(G\) | \- |
| -fcecoalesce | fce coalesce | \- | \- | \(G\) | \- |
| -fceevents | fce events | \- | \- | \(G\) | \- |
| -fceholdfmod | fce holdfmod | 60 | 60 | \(G\) | \- |
| -mimicmodel | mimic model | \- | \- | \(G\) | \- |
| -adminauthuser | admin auth user | \- | \- | \(G\) | \- |
| -noacl2maccess | map acls | \- | rights | \(G\) | \- |
| -\[no\]tcp | \- | -tcp | \- | \- | 常に TCP を有効 |
| -\[no\]ddp | appletalk | -ddp | no | \(G\) | 4.0.0で復活 |
| -\[no\]transall | \- | -transall | \- | \- | 常に TCP を有効 |
| -nodebug | \- | \- | \- | \- | 廃止 |
| -\[no\]slp | \- | -noslp | \- | \- | SLP サポートが廃止 |
| -\[no\]uservolfirst | \- | -nouservolfirst | \- | \- | uservol が廃止 |
| -\[no\]uservol | \- | -uservol | \- | \- | uservol が廃止 |
| -proxy | \- | \- | \- | \- | 廃止 |
| -defaultvol | \- | AppleVolumes.default | \- | \- | afp.conf のみ |
| -systemvol | \- | AppleVolumes.system | \- | \- | extmap.conf のみ |
| -loginmaxfail | \- | \- | \- | \- | そもそも最初からサポートされていない |
| -unsetuplog | \- | \- | \- | \- | 廃止 |
| -authprintdir | \- | \- | \- | \- | CAP スタイル認証印刷が廃止 |
| -ddpaddr | ddp address | 0.0 | 0.0 | \(G\) | 4.0.0で復活 |
| -\[no\]icon | legacy icon | -noicon | \- | \(G\) | 4.0.2で復活 |
| -keepsessions | \- | \- | \- | \- | 廃止。kill -HUP を使用 |

**from afp_ldap.conf から afp.conf**

| 旧 afp_ldap.conf | 新 afp.conf | 旧デフォルト値 | 新デフォルト値 | セクション | 詳細 |
|----|----|----|----|----|----|
| ldap_server | ldap server | \- | \- | \(G\) | \- |
| ldap_auth_method | ldap auth method | \- | \- | \(G\) | \- |
| ldap_auth_dn | ldap auth dn | \- | \- | \(G\) | \- |
| ldap_auth_pw | ldap auth pw | \- | \- | \(G\) | \- |
| ldap_userbase | ldap userbase | \- | \- | \(G\) | \- |
| ldap_userscope | ldap userscope | \- | \- | \(G\) | \- |
| ldap_groupbase | ldap groupbase | \- | \- | \(G\) | \- |
| ldap_groupscope | ldap groupscope | \- | \- | \(G\) | \- |
| ldap_uuid_attr | ldap uuid attr | \- | \- | \(G\) | \- |
| ldap_uuid_string | ldap uuid string | \- | \- | \(G\) | \- |
| ldap_name_attr | ldap name attr | \- | \- | \(G\) | \- |
| ldap_group_attr | ldap group attr | \- | \- | \(G\) | \- |

**AppleVolumes.\* から afp.conf**

| 旧 AppleVolumes.\* | 新 afp.conf | 旧デフォルト値 | 新デフォルト値 | セクション | 詳細 |
|----|----|----|----|----|----|
| （ピリオドで始まる行） | \- | \- | \- | \- | extmap.conf で使用する |
| :DEFAULT: | \- | options:upriv,usedots | \- | \- | "vol preset" を使用する |
| 一番目のフィールド ("~") | \- | \- | \- | \- | \[Homes\] セクションを使用する |
| 一番目のフィールド ("/path") | path | \- | \- | \(V\) | \- |
| 二番目のフィールド | \- | \- | \- | \- | セクション名を使用する |
| allow: | valid users | \- | \- | \(V\) | \- |
| deny: | invalid users | \- | \- | \(V\) | \- |
| rwlist: | rwlist | \- | \- | \(V\) | \- |
| rolist: | rolist | \- | \- | \(V\) | \- |
| volcharset: | vol charset | UTF8 | （unix charset と同じ） | (G)/(V) | \- |
| maccharset: | mac charset | MAC_ROMAN | MAC_ROMAN | (G)/(V) | \- |
| veto: | veto files | \- | \- | \(V\) | \- |
| cnidscheme: | cnid scheme | dbd | dbd | \(V\) | \- |
| casefold: | casefold | \- | \- | \(V\) | \- |
| adouble: | appledouble | v2 | ea | \(V\) | 4.2.0で廃止 |
| cnidserver: | cnid server | localhost:4700 | localhost:4700 | (G)/(V) | \- |
| dbpath: | vol dbpath | （ボリュームディレクトリ） | $prefix/var/netatalk/CNID/ | \(G\) | 厳密には $localstatedir に移動 |
| umask: | umask | 0000 | 0000 | \(V\) | \- |
| dperm: | directory perm | 0000 | 0000 | \(V\) | \- |
| fperm: | file perm | 0000 | 0000 | \(V\) | \- |
| password: | password | \- | \- | \(V\) | \- |
| root_preexec: | \- | \- | \- |  | 4.1.0で廃止 |
| preexec: | preexec | \- | \- | \(V\) | \- |
| root_postexec: | \- | \- | \- | \- | 4.1.0で廃止 |
| postexec: | postexec | \- | \- | \(V\) | \- |
| allowed_hosts: | hosts allow | \- | \- | \(V\) | \- |
| denied_hosts: | hosts deny | \- | \- | \(V\) | \- |
| ea: | ea | auto | auto | \(V\) | \- |
| volsizelimit: | vol size limit | \- | \- | \(V\) | 4.0.0で復活 |
| perm: | \- | \- | \- | \- | "directory perm" 及び "file perm" を使用する |
| forceuid: | \- | \- | \- | \- | 廃止 |
| forcegid: | \- | \- | \- | \- | 廃止 |
| options:ro | read only | \- | no | \(V\) | \- |
| options:invisibledots | invisible dots | \- | no | \(V\) | \- |
| options:nostat | stat vol | \- | yes | \(V\) | \- |
| options:preexec_close | preexec close | \- | no | \(V\) | \- |
| options:root_preexec_close | \- | \- | \- | \- | 4.1.0で廃止 |
| options:upriv | unix priv | \- | yes | \(V\) | \- |
| options:nodev | cnid dev | \- | yes | \(V\) | \- |
| options:illegalseq | illegal seq | \- | no | \(V\) | \- |
| options:tm | time machine | \- | no | \(V\) | \- |
| options:searchdb | search db | \- | no | \(V\) | \- |
| options:nonetids | network ids | \- | yes | \(V\) | \- |
| options:noacls | acls | \- | yes | \(V\) | \- |
| options:followsymlinks | follow symlinks | \- | no | \(V\) | \- |
| options:nohex | \- | \- | \- | \- | ":2f" は ":" に自動変換される |
| options:usedots | \- | \- | \- | \- | ":2e" は "." に自動変換される |
| options:nofileid | \- | \- | \- | \- | 廃止 |
| options:prodos | prodos | \- | no | \(V\) | 4.0.0で復活 |
| options:mswindows | \- | \- | \- | \- | 廃止 |
| options:crlf | \- | \- | \- | \- | 廃止 |
| options:noadouble | \- | \- | \- | \- | 廃止 |
| options:limitsize | legacy volume size | \- | no | \(V\) | 4.0.0で復活 |
| options:dropbox | \- | \- | \- | \- | 廃止 |
| options:dropkludge | \- | \- | \- | \- | 廃止 |
| options:nocnidcache | \- | \- | \- | \- | 廃止 |
| options:caseinsensitive | \- | \- | \- | \- | 廃止 |
