# Netatalk 1.5 The New Year's Release

The Netatalk development team is proud to announce the final 1.5 release
of the Netatalk File Sharing suite. Netatalk is a collection of server
programs and utilities for handling various protocols employed by Apple
Macintosh computers on Unix compatible systems. The suite contains

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

## News in Netatalk 1.5.0

Since the early pre-release versions of Netatalk 1.5, Netatalk has been
hosted and developed on SourceForge ( <http://sourceforge.net/>). This
offers a great variety of resources and tools to the project and helped
to open up the development process.

Starting with version 1.5pre7, Netatalk is now licensed under the GNU
General Public License (GPL), which is used by many Open Source/Free
Software projects as their license of choice. We chose this license to
allow us to develop Netatalk as freely as possible and to ensure that
Netatalk will stay free in the future.

Netatalk now makes use of the GNU autotools (autoconf, automake, and
libtool) for building. This increases the portability of Netatalk as
well as the flexibility of the build system, and helps make the whole
build process more transparent. Ports to new platforms and enhancement
to the source code can now be handled much easier.

Netatalk 1.5 features a new experimental DID tracking system, based on
Berkeley DB3 files. The scheme, known as CNID-DB, is intended to end
various problems concerning aliases and disappearing files encountered
in earlier versions of Netatalk. This new DID scheme is scheduled to
become the default DID in future Netatalk versions.

Apart from these larger changes, a lot of work has gone into the
Netatalk source code and build process and we feel that the quality of
the code base has greatly improved since earlier releases.

## Future Enhancements

Netatalk is an actively developed product and its functionality will be
enhanced in future versions. Some of the upcoming features include:

- Further improvements in the build system for enhanced portability

- AFP 3.0 support, including long file names

- A new universal logging system

- Persistent DID support (stable alias support) by default

- Integrated Samba and NFS file locking

- Long file name handling ("mangling") for older AppleShare clients

- 100% QuarkXPress compatibility

- Server-side find capability ("FPCatSearch")

- Improved Documentation

## Supported Platforms

As of Netatalk 1.5.0 the following operating systems are supported:

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

Netatalk tar-balls can be found at
<http://me.in-berlin.de/~jroger/netatalk/>. Binaries for Debian GNU/Linux
will be added to the unstable distribution soon and will be available at
every Debian non-US mirror. Binaries for other operating systems will be
made available at the SourceForge site
<http://sourceforge.net/projects/netatalk/> as time permits.

Netatalk is also available via anonymous CVS. See the SourceForge
project site for anonymous CVS instructions. The main development is
happening in the trunk. Well-tested patches are back-ported to
branch-1-5-prep branch, from which the tar-balls are created.

## Contact

For more information about Netatalk, see its web page at:
<http://netatalk.sourceforge.net/>

The project is hosted at SourceForge. The SourceForge project page is
located at: <http://sourceforge.net/projects/netatalk/>

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

- The Netatalk Development Team, New Year's Eve 2001
