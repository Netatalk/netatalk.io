# Netatalk 2.1

The Netatalk development team is proud to announce version 2.1 of the
Netatalk File Sharing suite. This is the latest stable version.

Netatalk is a collection of server programs and utilities for handling
various protocols employed by Apple Macintosh computers on Unix
compatible systems. This allows Unix hosts to act as file, print, and
time servers for Apple Macintosh (classic MacOS as well as MacOS X)
computers.

The suite contains:

- afpd - a file server that implements the Apple Filing Protocol,
  allowing clients running MacOS to access Unix file servers

- atalkd - an implementation of the AppleTalk protocol

- papd - a print server that enables Macintosh computers to access
  printers connected to Unix servers

- timelord - a time server for synchronizing time over the network

- megatron - a tool to convert files in Macintosh specific formats like
  BinHex, AppleSingle, or MacBinary into files readable by Unix
  computers

- various supporting programs and utilities

Netatalk is a Free/Open Source Software project and is released under
the GNU General Public License (GPL). Please see

http://www.gnu.org/licenses/gpl.html

for the full license text.

## News

Netatalk 2.1 is a minor upgrade highlighting the following new features
and changes:

Protocol level:

- AFP 3.2

- IPv6

- Extended Attributes support

- ACL support with ZFS

- AppleTalk support in afpd and AppleTalk daemons (atalkd and papd) are
  disabled by default

afpd:

- default CNID backend is "dbd"

- enable live debugging with SIGINT

- afpd uses an in memory temporary DB if can't open the volume's
  database, but currently this only works with the "cdb" or "tdb"
  backends not with the default "dbd".

atalkd:

- atalkd: workaround for broken Linux 2.6 AT kernel module: Linux 2.6
  sends broadcast queries to the first available socket which is in our
  case the last configured one. atalkd now tries to find the right one.
  Note: now a misconfigured or plugged router can broadcast a wrong
  route !

Tools:

- dbd: "dbd" CNID database and volume maintanance and intergrity check
  utility

- apple_dump: dump AppleDouble files

### Upgrading from a 2.0 version

2.1 and 2.0 filenames encoding and adouble headers are compatible thus
it's possible to upgrade and downgrade between 2.0 and 2.1, you may have
to upgrade/downgrade (or delete) your .AppleDB folders in case the bdb
versions differ.

### Requirements

BerkeleyDB \>= 4.6

### configure

New default:

- sendfile is enabled on Linux

New options:

- --disable-sendfile

- --enable-nfsv4acls NFSv4 ACL Support (only Solaris?)

Webmin:

- --with-webmin path where webmin is installed \[$PKGCONFDIR/webmin\]

- --with-webminuser name for the webmin admin user

- --with-webminversion Webmin version to fetch from sf.net \[1.490\]

- --with-webminpass password for the webmin admin user

- --with-webminport TCP port for webmin

Removed options:

- --with-logfile

- --with-cnid-dbd-txn dbd always use transaction

- --with-cnid-db3-backend use dbd for transaction

- --with-cnid-hash-backend never really work

### afpd.conf

New defaults:

- slp is disable by default

- ddp is disable by default

New options:

- -slp advertise with SRVLOC

- -hostname

- -volnamelen

- -setuplog

- -closevol

- -ntdomain

- -ntseparator

Removed options:

- -noslp

### AppleVolume.default

Set default options via a :DEFAULT: line: "upriv" and "usedots".

New options:

- acl

- caseinsensitive volume is case insensitive (JFS in OS2 mode)

- nocnidcache

- ea:sys\|ad

Removed options:

- cachecnid

### Best Practices

Use a separate user group for cnid_dbd daemons:

   cnid_metad -u afpd -g afpd

All CNID databases in the same directory:

- AppleVolumes.default:

     :DEFAULT: dbpath:/var/lib/afpd/$v

- with /var/lib/afpd:

     drwxr-xr-x afpd afpd 4096 2009-11-24 15:12 /var/lib/afpd

afpd or cnid_metad will create the substituded subdirectory ($v is
replaced by the volume name)

## Changes in 2.1 since 2.1-beta2

- NEW: afpd: new volume option "volsizelimit" for limitting reported
  volume size. Useful for limitting TM backup size.

- UPD: dbd: -c option for rebuilding volumes which prevents the creation
  of .AppleDouble stuff, only removes orphaned files.

## Changes in 2.1-beta2 since 2.1-beta1

- NEW: afpd: static generated AFP signature stored in
  afp_signature.conf, cf man 5 afp_signature.conf

- NEW: afpd: clustering support: new per volume option "cnidserver".

- UPD: afpd: set volume defaults options "upriv" and "usedots" in the
  volume config file AppleVolumes.default. This will only affect new
  installations, but not upgrades.

- FIX: afpd: prevent security attack guessing valid server accounts.
  afpd now returns error -5023 for unknown users, as does
  AppleFileServer.

### Detailed list of changes in 2.1-beta1

- NEW: afpd: AFP 3.2 support

- NEW: afpd: Extended Attributes support using native attributes or
  using files inside .AppleDouble directories.

- NEW: afpd: ACL support with ZFS

- NEW: cnid_metad: options -l and -f to configure logging

- NEW: IPv6 support

- NEW: AppleDouble compatible UNIX files utility suite \`ad …\`. With
  2.1 only \`ad ls\`.

- NEW: CNID database maintanance utility dbd

- NEW: support BerkeleyDB upgrade. Starting with the next release after
  2.1 in case of BerkeleyDB library updates, Netatalk will be able to
  upgrade the CNID databases.

- NEW: afpd: store and read CNIDs to/from AppleDouble files by default.
  This is used as a cache and as a backup in case the database is
  deleted or corrupted. It can be disabled with a new volume option
  "nocnidcache".

- NEW: afpd: sending SIGINT to a child afpd process enables debug
  logging to /tmp/afpd.PID.XXXXXX.

- NEW: configure args to download and install a "private" Webmin
  instance including only basic Webmin modules plus our netatalk.wbm.

- NEW: fallback to a temporary in memory tdb CNID database if the volume
  database can't be opened.

- NEW: support for Unicode characters in the range above U+010000 using
  internal surrogate pairs

- NEW: apple_dump: utility to dump AppleSingle and AppleDouble files

- NEW: afpldaptest: utility to check afp_ldap.conf.

- UPD: atalkd and papd are now disabled by default. AppleTalk is legacy.

- UPD: slp advertisement is now disabled by default. server option -slp
  SRVLOC is legacy.

- UPD: cdb/dbd CNID backend requires BerkeleyDB \>= 4.6

- UPD: afpd: default CNID backend is "dbd"

- UPD: afpd: try to install PAM config that pulls in system\|common auth

- UPD: afpd: symlink handling: never followed server side, client
  resolves them, so it's safe to use them now.

- UPD: afpd: Comment out all extension-\>type/creator mappings in
  AppleVolumes.system. They're unmaintained, possibly wrong and do not
  fit for OS X.

- FIX: rewritten logger

- FIX: afpd: UNIX permissions handling

- FIX: cnid_dbd: always use BerkeleyDB transactions

- FIX: initscripts installation now correctly uses autoconf paths, ie
  they're installed to --sysconfdir.

- FIX: UTF-8 volume name length

- FIX: atalkd: workaround for broken Linux 2.6 AT kernel module: Linux
  2.6 sends broadcast queries to the first available socket which is in
  our case the last configured one. atalkd now tries to find the right
  one. Note: now a misconfigured or plugged router can broadcast a wrong
  route !

- REM: afpd: removed CNID backends "db3", "hash" and "mtab"

- REM: cnid_maint: use dbd

- REM: cleanappledouble.pl: use dbd

- REM: nu: use \`macusers\` instead

## Supported Platforms

As of Netatalk 2.1 the following operating systems are supported:

- FreeBSD

- Linux

- OpenBSD

- NetBSD

- \[Open\]Solaris

- Tru64 (TCP only)

Netatalk may compile and run on other operating systems as well, but it
is not well-tested on those. We welcome patches and suggestions for
enhancing the portability of Netatalk as well as success and failure
stories. Please write to <netatalk-devel@lists.sourceforge.net>.

## Availability

Netatalk tar-balls can be found at:

    <http://sourceforge.net/project/showfiles.html?group_id=8642>

Netatalk is also available via anonymous CVS. See the SourceForge
project site for anonymous CVS instructions.

## Contact

For more information about Netatalk, see its web page at:

    <http://netatalk.sourceforge.net/>

The project is hosted at SourceForge. The SourceForge project page is
located at:

    <http://sourceforge.net/projects/netatalk>

The Netatalk development team can be reached via the mailing list
<netatalk-devel@lists.sourceforge.net>. For subscription information and
archives see Netatalk's SourceForge project page.

<netatalk-admins@lists.sourceforge.net> is a mailing list for Netatalk
system administrators. For subscription information and archives see the
Netatalk web page.

## Acknowledgements

We would like to thank all contributors to the Netatalk project for
their commitment. Without the many suggestions, bug and problem reports,
patches, and reviews this project wouldn't be where it is.

- The Netatalk Development Team, April 2010
