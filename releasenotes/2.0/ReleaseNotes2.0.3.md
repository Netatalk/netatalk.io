# Netatalk 2.0.3

The Netatalk development team is proud to announce version 2.0.3 of the
Netatalk File Sharing suite. This is the latest stable version. It
contains several important bugfixes, therefore all users are encouraged
to upgrade their systems to 2.0.3.

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

## New in Netatalk 2.0.3

- NEW: afpd: add a cachecnid option that controls if afpd should use the
  IDs stored in the AD2 files as cache. Defaults to off.

- UPD: afpd: deal with more than 32 groups.

- FIX: afpd: several catsearch fixes, based on patch from TSUBAKIMOTO
  Hiroya.

- FIX: afpd: fix a race when a client very quickly reconnects and tries
  to kill its old session.

- FIX: afpd: OSX style symlink caused problems with Panther clients.

- FIX: afpd: old files with default type didn't show the right icon in
  finder, from Shlomi Yaakobovich, slightly modified.

- FIX: cnid_check: disable cnid_check if CNID db was configured with
  transactions and really bail out after the first error.

- FIX: admin-group configure option was broken.

- FIX: several problems with IDs cached in AD2 files.

- FIX: Ignore BIDI in UTF8 hints from OSX.

- FIX: Lots of gcc warning fixes.

- FIX: small configure script changes.

## Future Enhancements

Netatalk is an actively developed product and its functionality will be
enhanced in future versions. Some of the upcoming features include:

- Integrated Samba and NFS file locking

- Better integration of AppleDouble metadata and CNIDs with Samba

## Supported Platforms

As of Netatalk 2.0.3 the following operating systems are supported:

- FreeBSD

- Linux (Debian, Mandrake, RedHat, Suse, others should work as well)

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

- The Netatalk Development Team, May 2005
