# Netatalk 2.0.0

The Netatalk development team is proud to announce the first stable
release of the new netatalk 2.0 codebase!

## Major improvements over the 1.6 series are:

- Netatalk's AFP 3.1 compliant file server allows long filenames, UTF-8
  names, large file support and full Mac OS X compatibility
- The print server task can directly interact with CUPS, automagically
  sharing all CUPS queues
- Kerberos V support, allowing true "Single Sign On"
- Whole rework of the CNID subsystem, providing reliable and persistant
  storage of file and directory IDs
- Huge improvements regarding product documentation, making Netatalk's
  features accessible more easily
- countless bugs fixed compared to previous versions

In case, you want to upgrade an existing Netatalk 1.x installation,
ensure you carefully read the upgrade guide before and follow the steps
outlined there. If you made use of symlinks inside Netatalk shares
consider setting up a test installation with 2.0 before migrating since
Netatalk 2.0 provides no support for symlinks any longer.

Netatalk is a collection of server programs and utilities for handling
various protocols employed by Apple Macintosh computers on Unix
compatible systems. This allows Unix hosts to act as file, print, and
time servers for Apple Macintosh (classic MacOS as well as MacOS X)
computers. Additionally Unix hosts using Netatalk can print to
AppleTalk-only printers.

The suite contains:

- afpd - a file server that implements the Apple Filing Protocol,
  allowing clients running MacOS to access Unix file servers

- atalkd - an implementation of the various AppleTalk protocols

- papd - a print server that enables Macintosh computers to access
  printers connected to Unix servers

- timelord - a time server for synchronizing time over the network

- megatron - a tool to convert files in Macintosh specific formats like
  BinHex, AppleSingle, or MacBinary into files readable by Unix
  computers

- various other utilities

Netatalk is a Free/Open Source Software project and is released under
the GNU General Public License (GPL). Please see

    <http://www.gnu.org/licenses/gpl.html>

for the full license text.

## New in Netatalk 2.0.0

Netatalk 2.0.0 is the first stable release for Netatalk 2.0 which is a
major upgrade for Netatalk 1.6.x. Please see the NEWS file contained in
the distribution for more detailed information.

## Future Enhancements

Netatalk is an actively developed product and its functionality will be
enhanced in future versions. Some of the upcoming features include:

- Integrated Samba and NFS file locking

- Better integration of AppleDouble metadata and CNIDs with Samba

## Supported Platforms

As of Netatalk 2.0.0 the following operating systems are supported:

- FreeBSD

- Linux (Debian, Mandrake, RedHat, SuSE, others should work as well)

- MacOS X (TCP only)

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

    <http://sourceforge.net/project/showfiles.php?group_id=8642>

Netatalk is also available via anonymous CVS. See the SourceForge
project site for anonymous CVS instructions.

## Contact

For more information about Netatalk, see its web page at:

    <http://netatalk.sourceforge.net/>

The project is hosted at SourceForge. The SourceForge project page is
located at:

    <http://sourceforge.net/projects/netatalk/>

<netatalk-admins@lists.sourceforge.net> is a mailing list for Netatalk
system administrators. For subscription information and archives see the
Netatalk web page.

The Netatalk development team can be reached via the mailing list
<netatalk-devel@lists.sourceforge.net>. For subscription information and
archives see Netatalk's SourceForge project page.

## Acknowledgements

We would like to thank all contributors to the Netatalk project for
their commitment. Without the many suggestions, bug and problem reports,
patches, and reviews this project wouldn't be where it is.

- The Netatalk Development Team, October 2004
