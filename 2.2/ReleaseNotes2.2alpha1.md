# Netatalk 2.2alpha1

The Netatalk development team is proud to announce version 2.2alpha1 of
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

Netatalk is a Free/Open Source Software project and is released under
the GNU General Public License (GPL). The full license text is available
at:

    <http://www.gnu.org/licenses/gpl.html>

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

## Changes in not yet released 2.1.5

- UPD: afpd: support newlines in -loginmesg with \n escaping syntax

- UPD: afpd: support for changed chmod semantics on ZFS with ACLs in
  onnv145+

- FIX: afpd: fix leaking ressource when moving objects on the server

## Changes in 2.1.4

- FIX: afpd: Downstream fix for FreeBSD PR 148022

- FIX: afpd: Fixes for bugs 3074077 and 3074078

- FIX: afpd: Better handling of symlinks in combination with ACLs and
  EAs. Fixes bug 3074076.

- FIX: dbd: Adding a file with the CNID from it's adouble file did not
  work in case that CNID was alread occupied in the database

- FIX: macusers: add support for Solaris

- NEW: cnid_metad: use a PID lockfile

- NEW: afpd: prevent log flooding

- UPD: dbd: ignore ".zfs" snapshot directories

- UPD: dbd: support interrupting -re mode

## Changes in 2.1.3

- FIX: afpd: fix a serious error in networking IO code

- FIX: afpd: Solaris 10 compatibilty fix: don't use SO_SNDTIMEO, use
  non-blocking IO and select instead for writing/sending data.

- UPD: Support for BerkeleyDB 5.0.

## Changes in 2.1.2

- FIX: afpd: fix for possible crash in case more then one server is
  configured in afpd.conf.

- FIX: afpd: ExtendedAttributes in FreeBSD

- FIX: afpd: sharing home folders corrupted the per volume umask.

- UPD: afpd: umask for home folders is no longer taken from startup
  umask.

- UPD: afpd: dont and permissions with parent folder when creating new
  directories on "upriv" volumes.

- UPD: afpd: use 'afpserver@fqdn' instead of 'afpserver/fqdn@realm'.
  Prevents a crash in older GNU GSSAPI libs on eg. CentOS 5.x.

## Supported Platforms

As of Netatalk 2.1.4 the following operating systems are supported:

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

- The Netatalk Development Team, November 2010
