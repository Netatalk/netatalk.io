# 名前

atalk_aton — AppleTalk アドレス解析

# 概要

    #include <sys/types.h>
    #include <netatalk/at.h>

    atalk_aton(	cp, 	 
        ata);	 
    char * cp;
    struct at_addr * ata;

# 説明

**atalk_aton()** ルーチンは、AppleTalk アドレスの ASCII 表現をシステム コールに適した形式に変換する。許容される
ASCII 表現には、16 進数と 10 進数の両方が含まれ、3 桁または 2 桁になる。たとえば、アドレス \`0x1f6b.77'
のネットワーク部分は \`8043' で、ノード部分は \`119'
になる。この同じアドレスは、\`8043.119'、\`31.107.119'、または \`0x1f.6b.77' と表記できる。アドレスが 16
進数で、最初の桁が \`A-F' のいずれかである場合、先頭の \`0x' が 10 進数は冗長。

# 関連項目

atalk(4)

# 著者

[CONTRIBUTORS](https://netatalk.io/contributors) を参照
