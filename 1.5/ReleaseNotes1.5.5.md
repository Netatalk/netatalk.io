# Netatalk 1.5.5

The Netatalk development team is proud to announce version 1.5.5 of the
Netatalk File Sharing suite. Netatalk is a collection of server programs
and utilities for handling various protocols employed by Apple Macintosh
computers on Unix compatible systems. The suite contains

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

## News in Netatalk 1.5.5

This release of Netatalk features various bug fixes. It is reported to
work well with Photoshop and QuarkXPress.

## Future Enhancements

Netatalk is an actively developed product and its functionality will be
enhanced in future versions. Some of the upcoming features include:

- AFP 3.0 support, including long file names

- A new universal logging system

- Persistent DID support (stable alias support) by default

- Integrated Samba and NFS file locking

- Long file name handling ("mangling") for older AppleShare clients

- 100% QuarkXPress compatibility

- Server-side find capability ("FPCatSearch")

- Improved Documentation

## Supported Platforms

As of Netatalk 1.5.5 the following operating systems are supported:

- FreeBSD

- Linux (Debian, Mandrake, RedHat, SuSE, others should work as well)

- OpenBSD

- Solaris (32bit flavors)

- Tru64

Netatalk may compile and run on other operating systems as well, but it
is not well-tested on those. We welcome patches and suggestions for
enhancing the portability of Netatalk, though.

## Availability

Netatalk tar-balls can be found at:

    <http://sourceforge.net/project/showfiles.php?group_id=8642>

Binaries for Debian GNU/Linux will be added to the unstable distribution
soon and will be available at every Debian non-US mirror. Binaries for
other operating systems will be made available at the SourceForge site
<http://sourceforge.net/projects/netatalk/> as time permits.

Netatalk is also available via anonymous CVS. See the SourceForge
project site for anonymous CVS instructions. The main development is
happening in the trunk. Well-tested patches are back-ported to
branch-1-5-prep branch, from which the tar-balls are created.

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

- The Netatalk Development Team, September 2002
