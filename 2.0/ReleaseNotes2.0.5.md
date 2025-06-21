# Netatalk 2.0.5

The Netatalk development team is proud to announce version 2.0.5 of the
Netatalk File Sharing suite. This is the latest stable version. It
contains several important bugfixes, including a more complete security
fix for CVE-2008-5718. Time Machine support has been added with the new
volume option "tm". All users are encouraged to upgrade their systems to
2.0.5.

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
the GNU General Public License (GPL). The full license text is available
at:

    <http://www.gnu.org/licenses/gpl.html>

## Changes in 2.0.5

- NEW: afpd: Time Machine support with new volume option "tm".

- FIX: papd: Remove variable expansion for BSD printers. Fixes
  CVE-2008-5718.

- FIX: afpd: .AppleDxxx folders were user accessible if option 'usedots'
  was set

- FIX: afpd: vetoed files/dirs where still accessible

- FIX: afpd: cnid_resolve: don't return '..' as a valid name.

- FIX: uniconv: -d option wasn't working

## Supported Platforms

As of Netatalk 2.0.5 the following operating systems are supported:

- FreeBSD

- Linux

- OpenBSD

- NetBSD

- Solaris

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

    <http://sourceforge.net/projects/netatalk/>

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

- The Netatalk Development Team, November 2009
