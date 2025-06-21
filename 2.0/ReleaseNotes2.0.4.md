# Netatalk 2.0.4

The Netatalk development team is proud to announce version 2.0.4 of the
Netatalk File Sharing suite. This is the latest stable version. It
contains several important bugfixes, including a security fix for papd
(see CVE-2008-5718), therefore all users are encouraged to upgrade their
systems to 2.0.4.

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

## New in Netatalk 2.0.4

- REM: remove timeout

- NEW: afpd: DHX2 uams using GNU libgcrypt.

- NEW: afpd: volume options 'illegalseq', 'perm' and 'invisibledots'
  'ilegalseq' encode illegal sequence in filename asis, ex "\217-",
  which is not a valid SHIFT-JIS char, is encoded as U\217 -. 'perm'
  value OR with the client requested permissions. (help with OSX 10.5
  strange permissions). Make dot files visible by default with
  'usedots', use 'invisibledots' for keeping the old behavior, ie for
  OS9 (OSX hide dot files on its own).

- NEW: afpd: volume options allow_hosts/denied hosts

- NEW: afpd: volume options dperm/fperm default directory and file
  permissions or with server requests.

- NEW: afpd: afpd.conf, allow line continuation with \\

- NEW: afpd: AppleVolumes.default allow line continuation with \\

- NEW: afpd: Mac greek encoding.

- NEW: afpd: CJK encoding.

- UPD: afpd: Default UAMs: DHX + DHX2

- FIX: afpd: return the right error in createfile and copyfile if the
  disk is full.

- FIX: afpd: resolveid return the same error code than OSX if it's a
  directory

- FIX: afpd: server name check, test for the whole loopback subnet not
  only 127.0.0.1.

- UPD: afpd: limit comments size to 128 bytes, (workaround for Adobe CS2
  bug).

- UPD: afpd: no more daemon icon.

- UPD: usedots, return an invalide name only for .Applexxx files used by
  netatalk not all files starting with .apple.

- UPD: cnid: increase the number of cnid_dbd slots to 512.

- FIX: cnid: dbd detach the daemon from the control terminal.

- UPD: cnid: never ending Berkeley API changes…

- UPD: cnid: dbd add a timeout when reading data from afpd client.

- UPD: cnid: Don't wait five second after the first error when speaking
  to the dbd backend.

- FIX: papd: vars use % not $

- FIX: papd: quote chars in popen variables expansion. security fix.

- FIX: papd: papd -d didn't write to stderr.

- FIX: papd: ps comments don't always use ()

- FIX: many compilation errors (solaris, AFS, Tru64, xfs quota…).

## Supported Platforms

As of Netatalk 2.0.4 the following operating systems are supported:

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

- The Netatalk Development Team, May 2009
