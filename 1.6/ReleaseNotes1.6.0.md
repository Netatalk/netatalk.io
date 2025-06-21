# Netatalk 1.6.0

The Netatalk development team is proud to announce version 1.6.0 of the
Netatalk File Sharing suite. Netatalk is a collection of server programs
and utilities for handling various protocols employed by Apple Macintosh
computers on Unix compatible systems. This allows Unix hosts to act as
file, print, and time servers for Apple Macintosh (classic MacOS as well
as MacOS X) computers.

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

- various other utilities

Netatalk is a Free/Open Source Software project and is released under
the GNU General Public License (GPL). Please see
<http://www.gnu.org/licenses/gpl.html> for the full license text.

## News in Netatalk 1.6.0

Netatalk 1.6.0 is a new major release that greatly enhances Netatalk's
usefulness. Especially noteworthy are the improved compatibility with
MacOS X as well as industry-standard programs like Photoshop and
QuarkXPress.

The changes in detail:

- Long file name mangling support
- Improved log file support
- CNID DID handling by default
- The CDB data store for CNID is enabled by default
- Server-side find capability ("FPCatSearch")
- Bug fixes, build fixes, code cleanup

## Future Enhancements

Netatalk is an actively developed product and its functionality will be
enhanced in future versions. Some of the upcoming features include:

- AFP 3.0 support, including long file names

- Integrated Samba and NFS file locking

- Improved Documentation

## Supported Platforms

As of Netatalk 1.6.0 the following operating systems are supported:

- FreeBSD

- Linux (Debian, Mandrake, RedHat, SuSE, others should work as well)

- OpenBSD

- Solaris

- Tru64 (TCP only)

Netatalk may compile and run on other operating systems as well, but it
is not well-tested on those. We welcome patches and suggestions for
enhancing the portability of Netatalk as well as success and failure
stories. Please write to <netatalk-devel@lists.sourceforge.net>.

## Availability

Netatalk tar-balls can be found at:

    <http://sourceforge.net/project/showfiles.php?group_id=8642>

Binaries for Debian GNU/Linux will be added to the unstable distribution
soon and will be available at every Debian non-US mirror. Binaries for
other operating systems will be made available at the SourceForge site
<http://sourceforge.net/projects/netatalk/> as time permits.

Netatalk is also available via anonymous CVS. See the SourceForge
project site for anonymous CVS instructions. Main development is
happening in the trunk. Well-tested patches are back-ported to
branch-netatalk-1-6, which is also the basis for official releases.

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

- The Netatalk Development Team, December 2002
