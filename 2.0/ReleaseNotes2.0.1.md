# Netatalk 2.0.1

The Netatalk development team is proud to announce version 2.0.1 of the
Netatalk File Sharing suite. This is the latest stable version. It
contains several important bugfixes, therefore all users are encouraged
to upgrade their systems to 2.0.1.

The etc2ps.sh script delivered with all Netatalk versions prior to 2.0.1
has been found to be vulnerable to symlink attacks. See CAN-2004-0974
for details.

Please note that the handling of the default type/creator has changed
with 2.0.1. As a side effect, users upgrading from earlier versions,
including 2.0.0, will have to remove the default type/creator from the
AppleVolumes.System file. The install process will not modify this file
automatically. Please remove the line starting with '.         "????"'
manually.

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

## New in Netatalk 2.0.1

- NEW: --enable-debian configure option. Will install /etc/init.d/atalk
  to get not in conflict with standard debian /etc/init.d/netatalk.
  Reads netatalk.conf from $ETCDIR and not from /etc/default/

- UPD: Disable logger code by default. Log to syslog instead

- UPD: changed netatalk.conf default settings to prevent problems with
  AppleTalk zone names containing spaces

- FIX: insecure tempfile handling bug in etc2ps.sh, found by Trustix,
  CAN-2004-0974.

- REM: remove add_netatalk_printer and netatalk.template from stable
  branch until fixed. (possible symlink vulnerabilities)

- FIX: afpd: set hasBeenInited in default finder info. This bug caused
  endless finder refreshes with OS9 finder if the noadouble option was
  used. From TSUBAKIMOTO Hiroya.

- FIX: afpd: fix a bug in default CREATOR/TYPE handling. Due to this bug
  the type/creator mappings in AppleVolumes.system were ignored, causing
  problems i.e. with OS9 clients.

- FIX: AppleVolumes.system: By default don't define a CREATOR/TYPE for a
  file of unknown type.

- FIX: fix two Tru64 UNIX compilation errors, from Burkhard Schmidt bs
  AT cpfs.mpg.de

- FIX: afpd: FPMapId wasn't using UTF8 for groups if requested by
  client.

## Future Enhancements

Netatalk is an actively developed product and its functionality will be
enhanced in future versions. Some of the upcoming features include:

- Integrated Samba and NFS file locking

- Better integration of AppleDouble metadata and CNIDs with Samba

## Supported Platforms

As of Netatalk 2.0.1 the following operating systems are supported:

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

- The Netatalk Development Team, October 2004
