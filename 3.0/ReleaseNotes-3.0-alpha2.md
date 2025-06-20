# Netatalk 3.0 alpha2

The Netatalk development team is proud to announce the release of the
second alpha version of the new major Netatalk release 3.0. This release
is NOT intended for production systems.

Netatalk is a freely-available Open Source AFP fileserver. A \*NIX/\*BSD
system running Netatalk is capable of serving many Macintosh clients
simultaneously as an AppleShare file server (AFP).

The suite contains:

- netatalk - the main server service controller

- afpd - the AFP file server daemin

- cnid_metad - the CNID database multiplexing daemon

- cnid_dbd - the CNID database daemon serving CNIDs for AFP volumes

- various supporting programs and utilities

## Summary of major new features and enhancements in 3.0

- New ini style configuration file afp.conf which replaces all previous
  configuration files

- New default AppleDouble backend using filesytem Extended Attributes,
  conversion from AppleDouble v2 is done automatically on access

- New service controller process "netatalk" responsible for starting and
  restarting afpd and cnid_metad as necessary

- AppleTalk support has been removed

Please make sure to read the upgrading section in the Netatalk online
manual before trying to upgrade your system to 3.0!

## License

Netatalk is a Free/Open Source Software project and is released under
the GNU General Public License (GPLv2). The full license text is
available at:

    <http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt>

## Changes in 3.0 alpha2

- UPD: afpd: Store *.* as is and */* as *:* on the server, don’t CAP
  hexencode as "2e" and "2f" respectively

- UPD: afdp: Automatic name conversion, renaming files and directories
  containing CAP sequences to their not enscaped forms

- UPD: afpd: Correct handling of user homes and users without homes

- UPD: afpd: Perform complete automatic adouble:v2 to adouble:ea
  conversion as root. Previously only unlinking the adouble:v2 file was
  done as root

- UPD: dbd: -C option removes CAP encoding

- UPD: Add graceful option to RedHat init script

- UPD: Add --disable-bundled-libevent configure options When set to yes,
  we rely on a properly installed version on libevent CPPFLAGS and
  LDFLAGS should be set properly to pick that up

- UPD: Run ldconfig on Linux at the end of make install

- FIX: afpd: ad cp on appledouble = ea volumes

- FIX: dbd: ignore .\_ appledouble files

- REM: Volumes options "use dots" and "hex encoding"

## Changes in 3.0 alpha1

- NEW: Central configuration file afp.conf which replaces all previous
  files

- NEW: netatalk: service controller starting and restarting afpd and
  cnid_metad as necessary

- NEW: afpd: Extended Attributes AppleDouble backend (default)

- UPD: CNID databases are stored in $localstatedir/netatalk/CNID
  (default: /var/netatalk/CNID), databases found in AFP volumes are
  automatically moved

- UPD: Start scripts and service manifests have been changed to only
  start the new netatalk service controller process

- UPD: afpd: UNIX privileges and use dots enabled by default

- UPD: afpd: Support for arbitrary AFP volumes using variable expansion
  has been removed

- UPD: afpd: afp_voluuid.conf and afp_signature.conf location has been
  changed to $localstatedir/netatalk/ (default: /var/netatalk/)

- UPD: afpd: default server messages dir changed to
  $localstatedir/netatalk/msg/

- UPD: dbd: new option -C for conversion from AppleDouble v2 to ea

- REM: AppleTalk support has been removed

- REM: afpd: SLP and AFP proxy support have been removed

- REM: afpd: legacy file extension to type/creator mapping has been
  removed

- REM: afpd: AppleDouble backends v1, osx and sfm have been removed

## Supported Platforms

As of Netatalk 3.0 the following operating systems are supported:

- FreeBSD

- Linux

- OpenBSD

- NetBSD

- \[Open\]Solaris

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

<http://sourceforge.net/projects/netatalk/>

The Netatalk development team can be reached via the mailing list
<netatalk-devel@lists.sourceforge.net>. For subscription information and
archives see Netatalk’s SourceForge project page.

<netatalk-admins@lists.sourceforge.net> is a mailing list for Netatalk
system administrators. For subscription information and archives see the
Netatalk web page.

## Acknowledgements

We would like to thank all contributors to the Netatalk project for
their commitment. Without the many suggestions, bug and problem reports,
patches, and reviews this project wouldn’t be where it is.

- The Netatalk Development Team, April 2012
