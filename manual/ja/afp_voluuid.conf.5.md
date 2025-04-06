# 名前

afp_voluuid.conf — AFP ボリュームの UUID を指定するために afpd が利用する設定ファイル

# 説明

**afp_voluuid.conf** は全てのAFPボリュームのUUIDを魔法のように自動的に指定するために **afpd** が利用する設定ファイルである。設定行は以下のように構成される。

<"volume-name"\> <uuid-string\>

最初のフィールドはボリューム名である。ボリューム名がスペースを含む場合、それを引用符で囲まなければならない。第二のフィールドは36文字からなるUUIDの16進数ASCII文字列表現である。

先頭のスペースとタブは無視される。空行は無視される。頭に#が付いた行は無視される。不正な行は無視される。

> **注記**

> このUUIDはTime
Machineボリュームの強固な曖昧さ除去を提供する目的でZeroconfによって宣伝される。

> MySQL CNIDバックエンドにも使用されている。

> このファイルを軽率に編集すべきでないし、他のサーバにコピーすべきでもない。

# 例

## 例： 3つのボリュームは程がされた afp_voluuid.conf

    # This is a comment.
    "Backup for John Smith" 1573974F-0ABD-69CC-C40A-8519B681A0E1
    "bob" 39A487F4-55AA-8240-E584-69AA01800FE9
    mary 6331E2D1-446C-B68C-3066-D685AADBE911

# 参照

afpd(8), afp.conf(5), avahi-daemon(8), mDNSResponder(8)

# 著者

[CONTRIBUTORS](https://netatalk.io/contributors) を参照
