# ソースコードから Netatalk をコンパイルする

本付録では、以下オペレーティング システムで Netatalk
のソースコードをコンパイルする手順が記載されている。開始する前に、まずインストールの章をお読みください。続行する前に、Netatalk のソース
コードのコピーが必要になる。

本手順書は自動的に生成されたため、ご使用のシステムに最適化されていない可能性があるのでご了承ください。また、技術的な制約により、一部の OS では
Netatalk を起動する手順が不完全である。

# オペレーティング システム一覧

## Alpine Linux

必要なパッケージをインストールする

```
apk add acl-dev avahi-compat-libdns_sd avahi-dev bison build-base cmark cracklib cracklib-dev cracklib-words cups cups-dev curl db-dev dbus-dev flex gcc iniparser-dev krb5-dev libevent-dev libgcrypt-dev libtirpc-dev libtracker linux-pam-dev localsearch mariadb-dev meson ninja openldap-dev openrc perl pkgconfig rpcsvc-proto-dev talloc-dev tinysparql-dev
```

コンフィグレーション

```
meson setup build -Dbuildtype=release -Dwith-appletalk=true -Dwith-dbus-sysconf-path=/usr/share/dbus-1/system.d -Dwith-tests=true
```

ビルド

```
meson compile -C build
```

組み込み試験を実行する

```
cd build && meson test && cd ..
```

インストールする

```
meson install -C build
```

netatalk の機能を確認する

```
netatalk -V
afpd -V
```

アンインストール

```
ninja -C build uninstall
```

## Arch Linux

必要なパッケージをインストールする

```
pacman -Sy --noconfirm avahi bison cmark-gfm cracklib cups db flex gcc iniparser localsearch mariadb-clients meson ninja perl pkgconfig rpcsvc-proto talloc tinysparql
```

コンフィグレーション

```
meson setup build -Dbuildtype=release -Dwith-appletalk=true -Dwith-dbus-sysconf-path=/usr/share/dbus-1/system.d -Dwith-init-hooks=false -Dwith-tests=true
```

ビルド

```
meson compile -C build
```

組み込み試験を実行する

```
cd build && meson test && cd ..
```

インストールする

```
meson install -C build
```

netatalk の機能を確認する

```
netatalk -V
afpd -V
```

アンインストール

```
ninja -C build uninstall
```

## Debian Linux

必要なパッケージをインストールする

```
apt-get update
apt-get install --assume-yes --no-install-recommends bison cmark-gfm cracklib-runtime file flex libacl1-dev libavahi-client-dev libcrack2-dev libcups2-dev libdb-dev libdbus-1-dev libevent-dev libgcrypt20-dev libglib2.0-dev libiniparser-dev libkrb5-dev libldap2-dev libmariadb-dev libpam0g-dev libtalloc-dev libtirpc-dev libtracker-sparql-3.0-dev libwrap0-dev meson ninja-build po4a quota systemtap-sdt-dev tcpd tracker tracker-miner-fs
```

コンフィグレーション

```
meson setup build -Dbuildtype=release -Dwith-appletalk=true -Dwith-dbus-sysconf-path=/usr/share/dbus-1/system.d -Dwith-docs-l10n=true -Dwith-init-hooks=false -Dwith-init-style=debian-sysv,systemd -Dwith-pkgconfdir-path=/etc/netatalk -Dwith-tests=true
```

ビルド

```
meson compile -C build
```

組み込み試験を実行する

```
cd build && meson test && cd ..
```

インストールする

```
meson install -C build
```

netatalk の機能を確認する

```
netatalk -V
afpd -V
```

アンインストール

```
ninja -C build uninstall
```

## Fedora Linux

必要なパッケージをインストールする

```
dnf --setopt=install_weak_deps=False --assumeyes install avahi-devel bison chkconfig cmark cracklib-devel cups-devel dbus-devel flex glib2-devel iniparser-devel krb5-devel libacl-devel libdb-devel libgcrypt-devel libtalloc-devel mariadb-connector-c-devel meson ninja-build openldap-devel pam-devel perl perl-Net-DBus quota-devel systemd systemtap-sdt-devel tracker tracker-devel
```

コンフィグレーション

```
meson setup build -Dbuildtype=release -Dwith-appletalk=true -Dwith-dbus-sysconf-path=/usr/share/dbus-1/system.d -Dwith-init-hooks=false -Dwith-tests=true
```

ビルド

```
meson compile -C build
```

組み込み試験を実行する

```
cd build && meson test && cd ..
```

インストールする

```
sudo meson install -C build
```

netatalk の機能を確認する

```
netatalk -V
afpd -V
```

アンインストール

```
sudo ninja -C build uninstall
```

## Ubuntu Linux

必要なパッケージをインストールする

```
sudo apt-get update
sudo apt-get install --assume-yes --no-install-recommends bison cmark-gfm cracklib-runtime file flex libacl1-dev libavahi-client-dev libcrack2-dev libcups2-dev libdb-dev libdbus-1-dev libevent-dev libgcrypt20-dev libglib2.0-dev libiniparser-dev libkrb5-dev libldap2-dev libmariadb-dev libpam0g-dev libtalloc-dev libtirpc-dev libtracker-sparql-3.0-dev libwrap0-dev meson ninja-build quota systemtap-sdt-dev tcpd tracker tracker-miner-fs
```

コンフィグレーション

```
meson setup build -Dbuildtype=release -Dwith-appletalk=true -Dwith-dbus-sysconf-path=/usr/share/dbus-1/system.d -Dwith-init-hooks=false -Dwith-tests=true
```

ビルド

```
meson compile -C build
```

配布テストを実行

```
cd build && meson dist && cd ..
```

インストールする

```
sudo meson install -C build
```

netatalk の機能を確認する

```
netatalk -V
afpd -V
```

netatalk を起動する

```
sudo systemctl start netatalk
sleep 1
asip-status localhost
```

netatalk を停止させる

```
sudo systemctl stop netatalk
```

アンインストール

```
sudo ninja -C build uninstall
```

## macOS

必要なパッケージをインストールする

```
brew update
brew install cmark-gfm cracklib iniparser mariadb meson openldap
```

コンフィグレーション

```
meson setup build -Dbuildtype=release -Dwith-tests=true
```

ビルド

```
meson compile -C build
```

組み込み試験を実行する

```
cd build && meson test && cd ..
```

インストールする

```
sudo meson install -C build
```

netatalk の機能を確認する

```
netatalk -V
afpd -V
```

netatalk を起動する

```
sudo netatalkd start
sleep 1
asip-status localhost
```

netatalk を停止させる

```
sudo netatalkd stop
```

アンインストール

```
sudo ninja -C build uninstall
```

## DragonflyBSD

必要なパッケージをインストールする

```
pkg install -y avahi bison cmark db5 iniparser libevent libgcrypt meson mysql80-client openldap26-client perl5 pkgconf py39-gdbm py39-sqlite3 py39-tkinter talloc tracker3
```

コンフィグレーションとビルド

```
set -e
meson setup build -Dbuildtype=release -Dwith-appletalk=true -Dwith-tests=true
meson compile -C build
meson install -C build
netatalk -V
afpd -V
ninja -C build uninstall
```

## FreeBSD

必要なパッケージをインストールする

```
pkg install -y avahi bison cmark db5 flex iniparser libevent libgcrypt meson mysql84-client openldap26-client p5-Net-DBus perl5 pkgconf talloc tracker3
```

コンフィグレーションとビルド

```
set -e
meson setup build -Dbuildtype=release -Dpkg_config_path=/usr/local/libdata/pkgconfig -Dwith-tests=true
meson compile -C build
cd build
meson test
cd ..
meson install -C build
netatalk -V
afpd -V
/usr/local/etc/rc.d/netatalk start
sleep 1
asip-status localhost
/usr/local/etc/rc.d/netatalk stop
/usr/local/etc/rc.d/netatalk disable
ninja -C build uninstall
```

## NetBSD

必要なパッケージをインストールする

```
export PKG_PATH="http://ftp.NetBSD.org/pub/pkgsrc/packages/NetBSD/$(uname -p)/$(uname -r|cut -f '1 2' -d.)/All/"
pkg_add bison cmark db5 flex gcc13 gnome-tracker heimdal iniparser libcups libevent libgcrypt meson mysql-client p5-Net-DBus perl pkg-config talloc
```

コンフィグレーションとビルド

```
set -e
meson setup build -Dbuildtype=release -Dwith-appletalk=true -Dwith-dtrace=false -Dwith-tests=true
meson compile -C build
cd build
meson test
cd ..
meson install -C build
netatalk -V
afpd -V
service netatalk onestart
sleep 1
asip-status localhost
service netatalk onestop
ninja -C build uninstall
```

## OpenBSD

必要なパッケージをインストールする

```
pkg_add -I avahi bison cmark db-4.6.21p7v0 dbus gcc-11.2.0p14 heimdal iniparser libevent libgcrypt libtalloc mariadb-client meson openldap-client-2.6.8v0 p5-Net-DBus pkgconf tracker3
```

コンフィグレーションとビルド

```
set -e
meson setup build -Dbuildtype=release -Dpkg_config_path=/usr/local/lib/pkgconfig -Dwith-gssapi-path=/usr/local/heimdal -Dwith-kerberos-path=/usr/local/heimdal -Dwith-pam=false -Dwith-tests=true
meson compile -C build
meson install -C build
netatalk -V
afpd -V
rcctl -d start netatalk
sleep 1
asip-status localhost
rcctl -d stop netatalk
rcctl -d disable netatalk
ninja -C build uninstall
```

## OmniOS

必要なパッケージをインストールする

```
pkg install build-essential pkg-config
curl -O https://pkgsrc.smartos.org/packages/SmartOS/bootstrap/bootstrap-trunk-x86_64-20240116.tar.gz
tar -zxpf bootstrap-trunk-x86_64-20240116.tar.gz -C /
export PATH=/opt/local/sbin:/opt/local/bin:/usr/gnu/bin:/usr/bin:/usr/sbin:/sbin:$PATH
pkgin -y install avahi cmark gnome-tracker iniparser libevent libgcrypt meson mysql-client talloc
```

コンフィグレーションとビルド

```
set -e
export PATH=/opt/local/sbin:/opt/local/bin:/usr/gnu/bin:/usr/bin:/usr/sbin:/sbin:$PATH
meson setup build --prefix=/opt/local -Dbuildtype=release -Dpkg_config_path=/opt/local/lib/pkgconfig -Dwith-dbus-sysconf-path=/usr/share/dbus-1/system.d -Dwith-ldap-path=/opt/local -Dwith-tests=true
meson compile -C build
cd build
meson test
cd ..
meson install -C build
netatalk -V
afpd -V
sleep 1
svcadm enable svc:/network/netatalk:default
sleep 1
asip-status localhost
svcadm disable svc:/network/netatalk:default
ninja -C build uninstall
```

## Solaris

必要なパッケージをインストールする

```
pkg install bison cmake flex gcc libevent libgcrypt ninja pkg-config python/pip
pip install meson
curl -O https://gitlab.com/iniparser/iniparser/-/archive/v4.2.5/iniparser-v4.2.5.tar.gz
tar xzf iniparser-v4.2.5.tar.gz
cd iniparser-v4.2.5
mkdir build
cd build
cmake ..
make all
make install
```

コンフィグレーションとビルド

```
set -e
export PATH=/usr/local/sbin:/usr/local/bin:$PATH
meson setup build --prefix=/usr/local -Dbuildtype=release -Dpkg_config_path=/usr/lib/amd64/pkgconfig -Dwith-dbus-sysconf-path=/usr/share/dbus-1/system.d -Dwith-iniparser-path=/usr/local -Dwith-tests=true
meson compile -C build
cd build
meson test
cd ..
meson install -C build
netatalk -V
afpd -V
sleep 1
svcadm -v enable svc:/network/netatalk:default
sleep 1
asip-status localhost
svcadm -v disable svc:/network/netatalk:default
ninja -C build uninstall
```
