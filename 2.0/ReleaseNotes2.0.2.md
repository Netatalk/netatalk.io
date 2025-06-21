# Netatalk 2.0.2

The Netatalk development team is proud to announce version 2.0.2 of the
Netatalk File Sharing suite. This is the latest stable version. It
contains several important bugfixes, therefore all users are encouraged
to upgrade their systems to 2.0.2.

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

## New in Netatalk 2.0.2

- NEW: cnid: Add an indexes check and rebuild, optional for dbd
  (parameter check default no), standalone program cnid_index for cdb.

- UPD: Enhanced afpd's -v command line switch and added -V for more
  verbose information

- UPD: uams_gss: build the principal used by uams_gss.so from afpd's
  configuration, don't use GSS_C_NT_HOSTBASED_SERVICE

- UPD: cnid_dbd: add process id in syslog and small clean up

- REM: remove netatalkshorternamelinks.pl cf. SF bug \[ 1061396 \]
  netatalkshorternamelinks.pl broken

- FIX: afpd: check for DenyRead on FPCopyFile

- FIX: afpd: add missing flush for AD2 Metadata on FPCopyFile, SF bug \[
  1055691 \] Word 98 OS 9 Saving an existing file

- FIX: afpd: Deal with AFP3 connection and type 2 (non-UTF8) names.
  reported by Gair Heaton, HI RESOLUTION SYSTEMS

- FIX: afpd: Broken 'crlf' option

- FIX: afpd: fix SF bug \[ 1079622 \] afpd/dhx memory bug, by Ralf
  Schuchardt

- FIX: afpd: Return an error if we cannot get the db stamp in
  afp_openvol.

- FIX: afpd: Fix slp registration with Solaris9 slpd, from hat at
  fa2.so-net.ne.jp

## Future Enhancements

Netatalk is an actively developed product and its functionality will be
enhanced in future versions. Some of the upcoming features include:

- Integrated Samba and NFS file locking

- Better integration of AppleDouble metadata and CNIDs with Samba

## Supported Platforms

As of Netatalk 2.0.2 the following operating systems are supported:

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
patches and reviews this project wouldn't be where it is.

- The Netatalk Development Team, January 2005
