# Netatalk 2.1.5

The Netatalk development team is proud to announce version 2.1.5 of the
Netatalk File Sharing suite. This is the latest stable version. All
users are encouraged to upgrade their systems to 2.1.5.

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

## License

Netatalk is a Free/Open Source Software project and is released under
the GNU General Public License (GPL). The full license text is available
at:

    <http://www.gnu.org/licenses/gpl.html>

## Changes in 2.1.5

- UPD: afpd: support newlines in -loginmesg with \n escaping syntax

- UPD: afpd: support for changed chmod semantics on ZFS with ACLs in
  onnv145+

- FIX: afpd: fix leaking ressource when moving objects on the server

- FIX: afpd: backport Solaris 10 compatibilty fix from 2.2: don't use
  SO_SNDTIMEO/SO_RCVTIMEO, use non-blocking IO and select instead.

- FIX: afpd: misaligned memory access on Sparc in ad_setattr, fixes bug
  3110004.

- FIX: cnid_dbd: backport Solaris 10 compatibilty fix from 2.2: don't
  use SO_SNDTIMEO/SO_RCVTIMEO, use non-blocking IO and select instead.

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

- The Netatalk Development Team, December 2010
