# Netatalk 2.2.1

The Netatalk development team is proud to announce version 2.2.1 of the
Netatalk File Sharing suite. This is the first update to the new 2.2
release series. All users are encouraged to upgrade their systems to
2.2.1.

Netatalk is a freely-available Open Source AFP fileserver. It also
provides a kernel level implementation of the AppleTalk Protocol Suite.
A \*NIX/\*BSD system running Netatalk is capable of serving many
Macintosh clients simultaneously as an AppleShare file server (AFP),
AppleTalk router, \*NIX/\*BSD print server, and for accessing AppleTalk
printers via Printer Access Protocol (PAP). Included are a number of
minor printing and debugging utilities.

The suite contains:

- afpd - a file server that implements the Apple Filing Protocol,
  allowing clients running MacOS to access Unix file servers

- atalkd - an implementation of the AppleTalk protocol

- papd - a print server that enables Macintosh computers to access
  printers connected to Unix servers

- megatron - a tool to convert files in Macintosh specific formats like
  BinHex, AppleSingle, or MacBinary into files readable by Unix
  computers

- various supporting programs and utilities

## Summary of hot stuff and enhancements in 2.2

- AFP 3.3 support (necessary for TimeMachine and Lion)

- Robust network disconnect/reconnect, especially important for Time
  Machine

- Support for fast AFP searches (CNID backend "dbd" only)

- POSIX draft 1e ACL support

- Complete Netatalk volume compatible `ad`
  file utility suite

- Dynamic filesystem cache

- Builtin Zeroconf registration of the AFP server and TimeMachine
  volumes

- Support for ACLs without a common Directory Service between server and
  client

## Important

The enhancements for fast AFP searches are only implemented for the CNID
backend "dbd" and require changes to the underlying CNID database, ie an
additional index. This breaks drop-in compatibility between the CNID
backends "cdb" and "dbd". Once "dbd" has upgraded a CNID database of a
volume, "cdb" will reject to open it.

## License

Netatalk is a Free/Open Source Software project and is released under
the GNU General Public License (GPL). The full license text is available
at:

    http://www.gnu.org/licenses/gpl.html

## Changes in 2.2.1

- NEW: afpd: disable continous service feature by default, new option
  -keepsessions to enable it

- NEW: configure option "--enable-redhat-systemd" for Fedora15 and
  later. "--enable-redhat" is renamed "--enable-redhat-sysv".

- UPD: afpd: Enhance ACL support detection for volumes: enable them per
  volume if 1) ACL support compiled in, 2) the volume supports ACLs, 3)
  the new volume option "noacls" is not set for the volume. The previous
  behaviour was to enable ACL support for a volume if 1) it was compiled
  in and 2) the volume supported ACLs. There was no way to disable ACLs
  for a volume.

- UPD: afpd: add a configurable hold time option to FCE file
  modification event generation, default is 60 s, new option
  "fceholdfmod" to change it

- UPD: afpd: add support for new NetBSD quota subsystem, Bug ID 3249879

- FIX: afpd: increase BerkeleyDB locks and lockobjs

- FIX: afpd: create special folder as root

- FIX: afpd: fix compilation error if --enable-ddp is used

- FIX: afpd: More robust IPC reconnect error handling

- FIX: afpd: ACL access checking

- FIX: afpd: fix a possible race condition between SIGCHLD handler and
  new connection attempts

- FIX: afpd: fix undefined behaviour when more then ~510 connetions
  where established

- FIX: afpd: fix a crash when searching for a UUID that is not a special
  local UUID and LDAP support is not compiled in

- FIX: afpd: .volinfo file not created on first volume access if user in
  rolist

- FIX: afpd: possible crash at startup when registering with Avahi when
  Avahi is not running

- FIX: afpd: return correct user/group type when mapping UUIDs to names

- FIX: afpd: for directories add DARWIN_ACE_DELETE ACE if
  DARWIN_ACE_ADD_SUBDIRECTORY is set

- FIX: afpd: afpd crashed when it failed to register with Avahi because
  eg user service registration is disabled in the Avahi config

- FIX: dbd: function checking and removing malformed ad:ea header files
  failed to chdir back to the original working directory

- FIX: cnid_dbd: increase BerkeleyDB locks and lockobjs

- FIX: cnid_dbd: implement -d option, deletes CNID db

- FIX: dbd: better detection of local (or SMB/NFS) modifications on AFP
  volumes

- FIX: suse: initscript return better status

- FIX: Sourcecode distribution: add missing headers

- FIX: Solaris 10: missing dirfd replacement function

- FIX: case-conversion of surrogate pair

- FIX: Compilation error on GNU/kFreeBSD, fixes Bug ID 3392794 and
  Debian \#630349

- FIX: Fix Debian Bug#637025

- FIX: Multiple \*BSD compilation compatibility fixes, Bug ID 3380785

- FIX: precompose_w() failed if tail character is decomposed surrogate
  pair

## Changes in 2.2.0

- NEW: afpd: new volume option "nonetids"

- NEW: afpd: ACL access check caching

- NEW: afpd: FCE event notifications

- NEW: afpd: new option "-mimicmodel" for specifying Bonjour model
  registration

- UPD: Support for Berkeley DB 5.1

- UPD: case-conversion is based on Unicode 6.0.0

- UPD: cnid_metad: allow up to 4096 volumes

- UPD: afpd: only forward SIGTERM and SIGUSR1 from parent to childs

- UPD: afpd: use internal function instead of popening du -sh in order
  to calculate the used size of a volume for option "volsizelimit"

- UPD: afpd: Add negative UUID caching, enhance local UUID handling

- FIX: afpd: configuration reload with SIGHUP

- FIX: afpd: crashes in the dircache

- FIX: afpd: Correct afp logout vs dsi eof behaviour

- FIX: afpd: new catsearch was broken

- FIX: afpd: only use volume UUIDs in master afpd

- FIX: dbd: Multiple fixes, reliable locking

- FIX: ad file suite: fix an error that resulted in CNID database
  inconsistencies

## Changes in 2.2-beta4

- NEW: afpd: new afpd.conf options "tcprcvbuf" and "tcpsndbuf" to
  customize the corresponding TCP socket options.

- NEW: afpd: new afpd.conf option "nozeroconf" which disabled automatic
  Zeroconf service registration.

- FIX: afpd: generate mersenne primes for DHX2 UAM once at startup, not
  for every login

- FIX: afpd: DSI streaming deadlock

- FIX: afpd: extended sleep

- FIX: afpd: directory cache

- FIX: Support for platforms that do not have the \*at functions

- UPD: afpd: put POSIX write lock on volume files while reading them

## Changes in 2.2-beta3

- FIX: afpd: fix option volsizelimit to return a usefull value for the
  volume free space using `du -sh` with
  popen

- FIX: afpd: fix idle connection disconnects

- FIX: afpd: don’t disconnect sessions for clients if boottimes don’t
  match

- FIX: afpd: better handling of very long filenames that contain many
  multibyte UTF-8 glyphs

## Changes in 2.2-beta2

- NEW: afpd: AFP 3.3

- UPD: afpd: AFP 3.x can’t be disabled

## Changes in 2.2-beta1

- FIX: composition of Surrogate Pair

- UPD: gentoo,suse,cobalt,tru64: inistscript name is "netatalk", not
  "atalk"

- UPD: gentoo: rc-update install don’t hook in the Makefile

## Changes in 2.2alpha5

- UPD: afpd: new option "searchdb" which enables fast catalog searches
  using the CNID db.

- UPD: Case-insensitive fast search with the CNID db

- UPD: cnid_dbd: afpd now passes the volume path, not the db path when
  connecting for a volume. cnid_dbd will read the
  ".AppleDesktop/.volinfo" file of the volume in order to figure out the
  CNID db path and the volume charset encoding.

## Changes in 2.2alpha4

- NEW: Enhanced CNID "dbd" database for fast name search support.
  Important: this makes cnidscheme "cdb" incompatible with "dbd".

- NEW: afpd: support for fast catalog searches

- NEW: ad utility: ad find

- UPD: afpd: CNID database versioning check for "cdb" scheme

- UPD: cnid_dbd: CNID database versioning and upgrading. Additional CNID
  database index for fast name searches.

## Changes in 2.2alpha3

- FIX: afpd: various fixes

- FIX: Any daemon did not run if atalkd doesn’t exist (redhat/debian)

## Changes in 2.2alpha2

- FIX: afpd: fix compilation error when ACL support is not available

- FIX: Ensure Appletalk manpages and config files are distributed

## Changes in 2.2alpha1

- NEW: ad utility: ad cp

- NEW: ad utility: ad rm

- NEW: ad utility: ad mv

- NEW: afpd: dynamic directoy and CNID cache (new config option
  -dircachesize)

- NEW: afpd: POSIX 1e ACL support

- NEW: afpd: automagic Zeroconf registration with avahi, registering
  both the service \_afpovertcp.\_tcp and TimeMachine volumes with
  \_adisk.\_tcp.

- UPD: afpd: ACLs usable (though not visible on the client side) without
  common directory service, by mapping ACLs to UARight

- UPD: afpd: performance improvements for ACL access calculations

- UPD: AppleTalk ist disabled by default at configuration time. If
  needed use configure switch --enable-ddp.

- FIX: afpd: Solaris 10 compatibilty fix: don’t use
  SO_SNDTIMEO/SO_RCVTIMEO, use non-blocking IO and select instead.

- FIX: cnid_dbd: Solaris 10 compatibilty fix: don’t use
  SO_SNDTIMEO/SO_RCVTIMEO, use non-blocking IO and select instead.

- REM: afile/achfile/apple_cm/apple_mv/apple_rm: use ad

## Supported Platforms

As of Netatalk 2.2 the following operating systems are supported:

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

Netatalk is also available via anonymous git. See the SourceForge
project site for anonymous git instructions.

## Contact

For more information about Netatalk, see its web page at:

<http://netatalk.sourceforge.net/>

The project is hosted at SourceForge. The SourceForge project page is
located at:

<http://sourceforge.net/projects/netatalk/>

The Netatalk development team can be reached via the mailing list
<netatalk-devel@lists.sourceforge.net>. For subscription information and
archives see Netatalk’s SourceForge project page.

<netatalk-admins@lists.sourceforge.net> is a mailing list for Netatalk
system administrators. For subscription information and archives see the
Netatalk web page.

## Acknowledgements

We would like to thank all contributors to the Netatalk project for
their commitment. Without the many suggestions, bug and problem reports,
patches, and reviews this project wouldn’t be where it is.

- The Netatalk Development Team, September 2011
