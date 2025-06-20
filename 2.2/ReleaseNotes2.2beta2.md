# Netatalk 2.2-beta2

The Netatalk development team is proud to announce version 2.2-beta2 of
the Netatalk File Sharing suite. This is an unstable version, published
for the sole purpose of receiving wider testing. Do not run this on
production systems.

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

## Summary of hot stuff and enhancements since 2.1

- AFP 3.3 support

- Support for fast AFP searches (CNID backend "dbd" only)

- POSIX draft 1e ACL support

- Complete Netatalk volume compatible \`ad\` file utility suite

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

    <http://www.gnu.org/licenses/gpl.html>

## Changes in 2.2beta2

- NEW: afpd: AFP 3.3

- UPD: afpd: AFP 3.x can't be disabled

## Changes in 2.2-beta1

- FIX: composition of Surrogate Pair

- UPD: gentoo,suse,cobalt,tru64: inistscript name is "netatalk", not
  "atalk"

- UPD: gentoo: rc-update install don't hook in the Makefile

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

- FIX: Any daemon did not run if atalkd doesn't exist (redhat/debian)

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

- FIX: afpd: Solaris 10 compatibilty fix: don't use
  SO_SNDTIMEO/SO_RCVTIMEO, use non-blocking IO and select instead.

- FIX: cnid_dbd: Solaris 10 compatibilty fix: don't use
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

- The Netatalk Development Team, March 2011
