# 名前

papd.conf — Netatalk 印刷デーモンで使用されるプリンタの構成を決定するために papd によって使用される構成ファイル

# 説明

**papd.conf** は、netatalk が提供する印刷サービスを設定するために papd
が使用する設定ファイルである。 *papd* は、多くのシステムで lpd
と同じデフォルトを共有する。注目すべき例外の 1 つは Solaris である。

papd.conf の形式は、**printcap**(5) から派生したもので、1 つ以上のプリンタの設定を含めることができる。 *\#*
で始まっていない行はすべて解釈される。設定行は次のように構成される:

*printername:[options]*

System V 印刷システムを実行しているシステムでは、最も単純なケースは、papd.conf
がないか、有効な行はないか。この場合、**atalkd** はマシン上のローカル プリンタを自動検出する。行を *\\* (バックスラッシュ)
で分割できることに注意してください。

printername は単なる名前 (*Printer 1*) の場合もあれば、nbp_name 形式の完全な名前 (*Printer
1:LaserWriter@My Zone*) の場合もある。

BSD 印刷システムを使用するシステムでは、*pr* オプション内で該当する印刷コマンドへのパイプを使用する必要がある (例:
*pr=\|/usr/bin/lpr*)。

CUPS サポートがコンパイルされている場合、papd.conf の最初のエントリとして *cupsautoadd*
を使用すると、自動的に構成され、すべてのpapd で使用可能な CUPS プリンタ (カスタマイズ可能 - 以下を参照)。これは、CUPS キュー名を
*pr* エントリとして使用して、後で個々のエントリを追加することで、個々のプリンタに対して上書きできる。注意: CUPS サポートは、上記の
System V サポートとは相互に排他的である。

使用可能なオプションはコロンで区切られ (*:*)、行はコロンで終了する必要がある。使用可能なオプションとフラグは次のとおり。

**am=(uams list)**

**am** オプションを使用すると、特定のプリンタに対して特定の UAM
を指定できる。**au** フラグが存在しない場合は効果がない。注:
指定できる値は *uams_guest.so* と *uams_clrtxt.so*
のみ。最初の方法では有効なユーザー名が必要だが、パスワードは必要ない。
2 番目 には、有効なユーザー名と正しいパスワードの両方が必要。

**au**

> このフラグが存在する場合、プリンタの認証が有効になる。

*co=(CUPS オプション)*

> *co* オプションを使用すると、オプションを CUPS に渡すことができる (例:
*co="protocol=TBCP"* または *co="raw"*)。

**cupsautoadd[:type][@zone]**

> papd.conf の最初のエントリとして使用すると、papd を介してすべての CUPS プリンタが共有される。この特別な共有プリンタに割り当てられたタイプ/ゾーン設定とその他のパラメータは、すべての CUPS プリンタに適用される。*pd* オプションが設定されていない場合は、CUPS PPD が使用される。個々のプリンタのこれらのグローバル設定を上書きするには、後でそれらを papd.conf に追加し、異なる設定を割り当てるだけである。

**fo**

> このフラグが存在する場合、Mac OS X 以前の LaserWriter ドライバから生成された行末を変換するハックが有効になり、*foomatic-rip* がプリンタ ダイアログで設定された foomatic PPD オプションを認識できるようになる。注意: バイナリ印刷ジョブが破損する可能性があるため、注意して使用してください。

**op=(operator)**

> lpd スプールのオペレータ名を指定する。デフォルト値は「operator」である。

**pa=(appletalk address)**

> AppleTalk アドレスの指定を許可する。通常は必要ない。

*pd=(ppd ファイルへのパス)*

> 選択したプリンタに関連付ける特定の PPD (プリンタ記述ファイル)  を指定する。

*pr=(lpd/CUPS プリンタ名またはパイプ コマンド)*  

> スプール先の *lpd* または *CUPS* プリンタを設定する。デフォルト値は「lp」である。

# 例

CUPS サポートがコンパイルされていない場合 (Netatalk 2.0 以降ではデフォルト)、**pr**
パラメータをキュー名に設定することで、問題の lpd キューを定義する (次の例では「ps」)。**pr**
パラメータが設定されていない場合は、デフォルトのプリンタが使用される。

## 例： papd.conf System V 印刷システムの例

最初のスプーラは AppleTalk 名 Mac Printer Spooler で知られ、`/usr/share/lib/ppd` にある PPD
ファイルを使用する。さらに、ユーザー mcs は、スプールされるすべてのジョブの所有者になる。2 番目のスプーラは HP
プリンタと呼ばれ、すべてのオプションがデフォルトである。

    Mac Printer Spooler:\
       :pr=ps:\
       :pd=/usr/share/lib/ppd/HPLJ_4M.PPD:\
       :op=mcs:

    HP Printer:\
       :

上記の手法の代替として、papd の出力をパイプ経由で別のプログラムに送る方法がある。このメカニズムを使用して、ほぼすべての印刷システムを操作できる。

## 例： パイプを使用した papd.conf の例

最初のスプーラは HP 8100 と呼ばれている。印刷ジョブを */usr/bin/lpr* にパイプして印刷する。 PSSP
認証印刷が有効になっており、CAP スタイルの認証印刷も有効になっている。どちらの方法も、'**am**'
オプションで指定されたゲスト認証とクリアテキスト認証をサポートしている。使用される PPD は、*/etc/atalk/ppds/hp8100.ppd*
である。

    HP 8100:\
       :pr=|/usr/bin/lpr -Plp:\
       :sp:\
       :ca=/tmp/print:\
       :am=uams_guest.so,uams_clrtxt.so:\
       :pd=/etc/atalk/ppds/hp8100.ppd:

Netatalk 2.0 以降では、直接 CUPS 統合が使用可能。この場合、キュー名のみを **pr** パラメータとして定義すると、SysV lpd
デーモンは呼び出されず、代わりに CUPS が使用される。 **pd** スイッチを使用して特定の PPD が割り当てられていない限り、CUPS
で構成された PPD は **papd** でも使用される。

「cupsautoadd」という特別な共有が 1 つ存在する。これが最初のエントリとして存在する場合、使用可能なすべての CUPS
キューは、このグローバル共有に割り当てられたパラメータを使用して自動的に処理される。ただし、後続のプリンタ定義を使用して、個々のスプーラのこれらのグローバル設定を上書きできる。

## 例： papd.conf CUPS の例

最初のエントリは、すべての CUPS プリンタの自動共有を設定する。これらの共有はすべてゾーン「1st
floor」に表示され、追加の設定が行われていないため、CUPS プリンター名を NBP 名として使用し、CUPS で構成された PPD を使用する。2
番目のエントリは、1 つの CUPS プリンターに対して異なる設定を定義する。その NBP 名はプリンター名とは異なり、登録は別のゾーンで行われる。

    cupsautoadd@1st floor:op=root:

    Boss' LaserWriter@2nd floor:\
       :pr=laserwriter-chief:

# 注意事項

15 台を超えるプリンターをネットワークでは、papd プリンタ構成に AppleTalk ゾーンを指定する必要がある。そうでない場合、Mac
クライアントのセレクターには一部のプリンタしか表示されない場合がある。

# 関連項目

papd(8), atalkd.conf(5), lpd(8), lpoptions(8)

# 著者

[CONTRIBUTORS](https://netatalk.io/contributors) を参照
