# News Archive

Netatalk release announcements and other news.

### Netatalk 4.5.1 is available

*16th of July 2026*

The Netatalk development team is proud to announce the latest release of the Netatalk 4.5 release series.

This is a bugfix release that includes patches for the below four security vulnerabilities, big-endian support in SpotlightRPC, and a handful of other improvements.

[CVE-2026-62318](/security/CVE-2026-62318.html),
[CVE-2026-62319](/security/CVE-2026-62319.html),
[CVE-2026-62320](/security/CVE-2026-62320.html),
[CVE-2026-62321](/security/CVE-2026-62321.html)

For a summary of news and a detailed list of changes see the [Release Notes](/4.5/ReleaseNotes4.5.1.html).

### Introducing the Netatalk Client

*6th of July 2026*

The Netatalk development team is proud to announce the first release of the Netatalk Client,
a new project that provides a modern AFP client for Unix-like operating systems.

The Netatalk Client got started in 2024 as a fork of the [afpfs-ng](https://sourceforge.net/projects/afpfs-ng/)
project, which had been dormant for over a decade at the time. It has now been thoroughtly
overhauled with countless features added, including support for the latest AFP protocol versions,
modern authentication methods, and improved performance and reliability.

Netatalk Client is still considered beta level software, but early adopters are encouraged to test it and report any issues to the Netatalk development team.

See the [Netatalk Client v0.9.5 release notes and tarball](https://github.com/Netatalk/netatalk-client/releases/tag/0.9.5).

### Netatalk 4.5.0 is available

*30th of May 2026*

The Netatalk development team is proud to announce the first stable release of the Netatalk 4.5 release series.

All new features in the beta release have been refined and stabilized, notably the new directory caching optimizations
with ARC cache, 1M entries, rfork cache, and more.

Support for the SRP (*Secure Remote Password*) authentication method has been added, which is a modern and secure alternative to DHX2, supported in Mac OS X 10.7 Lion through macOS 26 Tahoe.

The Spotlight search feature has been modularized, overhauled and works out of the box. We now support three different indexing backends: the original LocalSearch backend,
a backend that uses Netatalk's native CNID database (the new default), and a new experimental backend that uses the Xapian search engine library.

The AFP statistics framework has been rewritten from D-Bus to Unix sockets, which is more lightweight and portable.
We have now retired the old `macusers` utility in favor of `afpstats` for getting AFP user and session information.

In addition, a wide range of security fixes and hardening has been introduced, including fixes for the following vulnerabilities:

[CVE-2026-7835](/security/CVE-2026-7835.html),
[CVE-2026-7836](/security/CVE-2026-7836.html),
[CVE-2026-7837](/security/CVE-2026-7837.html),
[CVE-2026-44053](/security/CVE-2026-44053.html),
[CVE-2026-44056](/security/CVE-2026-44056.html),
[CVE-2026-44058](/security/CVE-2026-44058.html),
[CVE-2026-44059](/security/CVE-2026-44059.html),
[CVE-2026-44061](/security/CVE-2026-44061.html),
[CVE-2026-44063](/security/CVE-2026-44063.html),
[CVE-2026-44065](/security/CVE-2026-44065.html),
[CVE-2026-44067](/security/CVE-2026-44067.html),
[CVE-2026-44069](/security/CVE-2026-44069.html),
[CVE-2026-44070](/security/CVE-2026-44070.html),
[CVE-2026-44071](/security/CVE-2026-44071.html),
[CVE-2026-44072](/security/CVE-2026-44072.html),
[CVE-2026-44073](/security/CVE-2026-44073.html),
[CVE-2026-44074](/security/CVE-2026-44074.html),
[CVE-2026-44075](/security/CVE-2026-44075.html),
[CVE-2026-49387](/security/CVE-2026-49387.html),
[CVE-2026-49388](/security/CVE-2026-49388.html),
[CVE-2026-49389](/security/CVE-2026-49389.html),
[CVE-2026-49390](/security/CVE-2026-49390.html)

For a summary of news and a detailed list of changes see the [Release Notes](/4.5/ReleaseNotes4.5.0.html).

### Netatalk 4.4.3 is available

*13th of May 2026*

The Netatalk development team is proud to announce a security focused release of the Netatalk 4.4 release series.

In addition to the following security fixes, this release contains a handful of UAM and container hardening improvements.

[CVE-2026-44047](/security/CVE-2026-44047.html),
[CVE-2026-44048](/security/CVE-2026-44048.html),
[CVE-2026-44049](/security/CVE-2026-44049.html),
[CVE-2026-44050](/security/CVE-2026-44050.html),
[CVE-2026-44051](/security/CVE-2026-44051.html),
[CVE-2026-44052](/security/CVE-2026-44052.html),
[CVE-2026-44054](/security/CVE-2026-44054.html),
[CVE-2026-44055](/security/CVE-2026-44055.html),
[CVE-2026-44057](/security/CVE-2026-44057.html),
[CVE-2026-44060](/security/CVE-2026-44060.html),
[CVE-2026-44062](/security/CVE-2026-44062.html),
[CVE-2026-44064](/security/CVE-2026-44064.html),
[CVE-2026-44066](/security/CVE-2026-44066.html),
[CVE-2026-44068](/security/CVE-2026-44068.html),
[CVE-2026-44076](/security/CVE-2026-44076.html),
[CVE-2026-45354](/security/CVE-2026-45354.html),
[CVE-2026-45355](/security/CVE-2026-45355.html),
[CVE-2026-45356](/security/CVE-2026-45356.html),
[CVE-2026-45698](/security/CVE-2026-45698.html),
[CVE-2026-45699](/security/CVE-2026-45699.html)

Note that there are another outstanding 18 CVEs that are not fixed in this release,
because the Netatalk team deemed them to be of lower severity.
These will be addressed in a future feature release.

For a summary of news and a detailed list of changes see the [Release Notes](/4.4/ReleaseNotes4.4.3.html).

### Netatalk 4.4.2 is available

*17th of April 2026*

The Netatalk development team is proud to announce the latest release of the Netatalk 4.4 release series.

This fixes a build breakage on certain 32 bit systems that was introduced between v4.3 and v4.4,
plus a range of stability and reliability fixes to afpd and the SQLite CNID backend.

For a summary of news and a detailed list of changes see the [Release Notes](/4.4/ReleaseNotes4.4.2.html).

### Netatalk 4.5.0 beta is available

*3rd of April 2026*

The Netatalk development team is proud to announce a beta release of
Netatalk 4.5.0.

This release introduces an ARC (Adaptive Replacement Cache) for the directory cache,
along with enumerate caching, AppleDouble support in cache, inter-process cache sync,
and a Resource Fork caching framework.
Together with other optimizations, this results in a significant reduction of file system I/O
and improved performance on workloads with many small files,
which speeds up both file operations and directory listings.

A new feature synthesizes a virtual *Icon\r* file in the volume root,
enabling Classic Mac OS clients to display custom color volume icons
over the wire with the *legacy icon* setting.

Other highlights include a default global 'cnid scheme' option,
static volume UUID configuration, mkdir and rmdir commands in the nad utility,
and important improvements to the SQLite CNID backend.

Early adopters are encouraged to test the new beta release and report any
issues to the Netatalk development team.

For a detailed list of changes, see the [Release Notes](/4.5/ReleaseNotes4.5.0beta.html).

### Netatalk 4.4.1 is available

*21st of January 2026*

The Netatalk development team is proud to announce the latest release of the Netatalk 4.4 release series.

This release contains primarily a range of bugfixes and reliability improvements for the SQLite CNID backend.

Also of note is that as of this version, we bundle the subprojects (currently: *bstring*) in the release tarball.
This is handy when building from tarball in an environment without internet access.

For a summary of news and a detailed list of changes see the [Release Notes](/4.4/ReleaseNotes4.4.1.html).

### Netatalk 4.4.0 is available

*4th of January 2026*

The Netatalk development team is proud to announce the first release of
the Netatalk 4.4 release series.

In this release, we introduce sophisticated directory cache optimization
which drastically reduces file system I/O by properly using the pre-existing caching architecture.

Early adopters are encouraged to test the new release and report any
issues to the Netatalk development team.

For a summary of news and a detailed list of changes see the [Release
Notes](/4.4/ReleaseNotes4.4.0.html).

### Netatalk 4.3.2 is available

*7th of September 2025*

The Netatalk development team is proud to announce the latest release of
the Netatalk 4.3 release series.

A critical bug preventing authentication with an AD domain via PAM has been
fixed.

All users of previous Netatalk versions are encouraged to upgrade to 4.3.2.

For a summary of news and a detailed list of changes see the [Release
Notes](/4.3/ReleaseNotes4.3.2.html).

### Netatalk 4.3.1 is available

*29th of August 2025*

The Netatalk development team is proud to announce the latest release of
the Netatalk 4.3 release series.

The afp_lantest utility has been given a major overhaul,
and is now capable of thoroughly testing caching in the AFP server.

All users of previous Netatalk versions are encouraged to upgrade to 4.3.1.

For a summary of news and a detailed list of changes see the [Release
Notes](/4.3/ReleaseNotes4.3.1.html).

### Netatalk 4.3.0 is available

*5th of August 2025*

The Netatalk development team is proud to announce the first release of
the Netatalk 4.3 release series.

Notable in this release, is the addition of an experimental SQLite
CNID backend, as well as a new AppleTalk tool called *rtmpqry*.

A major breaking change is the mandatory dependency on a shared [bstring](https://github.com/msteinert/bstring)
library. This library was previously vendored in the Netatalk source tree.
In the absense of a packaged version of *bstring* for your operating system,
the Meson build system can build it on the fly as a subproject.

Early adopters are encouraged to test the new release and report any
issues to the Netatalk development team.

For a summary of news and a detailed list of changes see the [Release
Notes](/4.3/ReleaseNotes4.3.0.html).

### Netatalk 4.2.4 is available

*31st of May 2025*

The Netatalk development team is proud to announce the latest version in
the Netatalk 4.2 release series.
This release has fixes for building on macOS with MacPorts,
as well as the latest Solaris 11.4.81 CBE release.
All users of previous Netatalk versions are encouraged to upgrade to 4.2.4.

For a summary of news and a detailed list of changes see the [Release
Notes](/4.2/ReleaseNotes4.2.4.html).

### Netatalk 4.2.3 is available

*7th of May 2025*

The Netatalk development team is proud to announce the latest version in
the Netatalk 4.2 release series.

In this version, we ship a handful of bug fixes and improvements to the
documentation.
All users of previous Netatalk versions are encouraged to upgrade to
4.2.3.

For a summary of news and a detailed list of changes see the [Release
Notes](/4.2/ReleaseNotes4.2.3.html).

### Netatalk 4.2.2 is available

*27th of April 2025*

The Netatalk development team is proud to announce the latest version in
the Netatalk 4.2 release series.

This release contains overhauled documentation,
improvements to the netatalk webmin module,
and significant new containerization capabilities.

All users of previous Netatalk versions are encouraged to upgrade to
4.2.2.

For a summary of news and a detailed list of changes see the [Release
Notes](/4.2/ReleaseNotes4.2.2.html).

### Netatalk 4.2.1 is available

*14th of April 2025*

The Netatalk development team is proud to announce the latest version in
the Netatalk 4.2 release series.
This release contains a range of important bug fixes,
new options for downstream packaging, and improvements to testing.
All users of previous Netatalk versions are encouraged to upgrade to 4.2.1.

For a summary of news and a detailed list of changes see the [Release
Notes](/4.2/ReleaseNotes4.2.1.html).

### Netatalk 4.2.0 is available

*31st of March 2025*

The Netatalk development team is proud to announce the first release of
the Netatalk 4.2 release series. The theme for this release is
security and reliability.

There are a number of breaking changes and new dependencies in this release.
Please read the [Release Notes](/4.2/ReleaseNotes4.2.0.html) carefully
before upgrading.

Early adopters are encouraged to test the new release and report any
issues to the Netatalk development team.

For a summary of news and a detailed list of changes see the [Release
Notes](/4.2/ReleaseNotes4.2.0.html).

### Netatalk 4.1.2 is available

*10th of February 2025*

The Netatalk development team is proud to announce the latest version in
the Netatalk 4.1 release series. This fixes bugs in the Webmin module,
while also improving compatibility with MacPorts.

All users of previous Netatalk versions are encouraged to upgrade to
4.1.2.

For a summary of news and a detailed list of changes see the [Release
Notes](/4.1/ReleaseNotes4.1.2.html).

### Netatalk 4.1.1 is available

*20th of January 2025*

The Netatalk development team is proud to announce the latest version in
the Netatalk 4.1 release series. This is a bugfix release that also
improves compatibility with NetBSD and NixOS.

All users of previous Netatalk versions are encouraged to upgrade to
4.1.1.

For a summary of news and a detailed list of changes see the [Release
Notes](/4.1/ReleaseNotes4.1.1.html).

### End of Life policy published

*18th of January 2025*

The Netatalk Project has published its End of Life policy. We guarantee
that each release series will be supported with security patches for 12
months after the release of the superseding feature release.

Most urgently, this means that the long-running 3.1 release series will
be out of support after May 31st, 2025. Users and downstream packagers
are encouraged to upgrade to the latest Netatalk 4.1 release series.

For more information, see the [Security
Policy](/security.html).

### Netatalk 4.1.0 is available

*11th of January 2025*

The Netatalk development team is proud to announce the first release of
the Netatalk 4.1 release series. This is a minor feature release that
further improves interoperability on macOS hosts, makes the MacIP
Gateway deamon more usable, and introduces a number of bugfixes and
build system improvements.

All users of previous Netatalk versions are encouraged to upgrade to
4.1, with a few caveats outlined in the Release Notes.

For a summary of news and a detailed list of changes see the [Release
Notes](/4.1/ReleaseNotes4.1.0.html).

### Netatalk 4.0.8 is available

*9th of December 2024*

The Netatalk development team is proud to announce the latest release of
the Netatalk 4.0 release series. This release improves interoperability
with macOS hosts, in particular.

See the [upgrade chapter](/4.0/htmldocs/upgrade) of the manual for
instructions how to upgrade existing 3.x or 2.x deployments. All users
of previous Netatalk versions are encouraged to upgrade to 4.0!

For a summary of news and a detailed list of changes see the [Release
Notes](/4.0/ReleaseNotes4.0.8.html).

### Netatalk 4.0.7 is available

*24th of November 2024*

The Netatalk development team is proud to announce the latest release of
the Netatalk 4.0 release series. We have fixed a range of build system
bugs for \*BSD hosts in particular.

See the [upgrade chapter](/4.0/htmldocs/upgrade) of the manual for
instructions how to upgrade existing 3.x or 2.x deployments. All users
of previous Netatalk versions are encouraged to upgrade to 4.0!

For a summary of news and a detailed list of changes see the [Release
Notes](/4.0/ReleaseNotes4.0.7.html).

### Netatalk 4.0.6 is available

*15th of November 2024*

The Netatalk development team is proud to announce the latest release of
the Netatalk 4.0 release series. This release contains fixes for older
AppleShare Clients, the Webmin module, and the Meson build system.

See the [upgrade chapter](/4.0/htmldocs/upgrade) of the manual for
instructions how to upgrade existing 3.x or 2.x deployments. All users
of previous Netatalk versions are encouraged to upgrade to 4.0!

For a summary of news and a detailed list of changes see the [Release
Notes](/4.0/ReleaseNotes4.0.6.html).

### Netatalk 4.0.5 is available

*10th of November 2024*

The Netatalk development team is proud to announce the latest release of
the Netatalk 4.0 release series. This release contains fixes for
AppleTalk (atalkd, macipgw), the Webmin module, and the Meson build
system, among other things.

See the [upgrade chapter](/4.0/htmldocs/upgrade) of the manual for
instructions how to upgrade existing 3.x or 2.x deployments. All users
of previous Netatalk versions are now encouraged to upgrade!

For a summary of news and a detailed list of changes see the [Release
Notes](/4.0/ReleaseNotes4.0.5.html).

### Netatalk 4.0.4 is available

*2nd of November 2024*

The Netatalk development team is proud to announce the latest release of
the Netatalk 4.0 release series. This is a minor bugfix release that
addresses build and distribution specific issues. Additionally, the
bundled test suite has seen major refinement.

See the [upgrade chapter](/4.0/htmldocs/upgrade) of the manual for
instructions how to upgrade existing 3.x or 2.x deployments. Early
adopters are encouraged to upgrade to the 4.0 release series. We look
forward to your feedback!

For a summary of news and a detailed list of changes see the [Release
Notes](/4.0/ReleaseNotes4.0.4.html).

### Netatalk 4.0.3 is available

*26th of October 2024*

The Netatalk development team is proud to announce the latest release of
the Netatalk 4.0 release series. This release contains a number of minor
bugfixes in afpd, improvements to the build system, as well as a major
overhaul to the afptest test suite.

See the [upgrade chapter](/4.0/htmldocs/upgrade) of the manual for
instructions how to upgrade existing 3.x or 2.x deployments. Early
adopters are encouraged to upgrade to the 4.0 release series. We look
forward to your feedback!

For a summary of news and a detailed list of changes see the [Release
Notes](/4.0/ReleaseNotes4.0.3.html).

### Netatalk 4.0.2 is available

*18th of October 2024*

The Netatalk development team is proud to announce the latest release of
the Netatalk 4.0 release series. This release expands integration and
end to end testing capabilities greatly. In addition, a host of build
system and other improvements are included.

See the [upgrade chapter](/4.0/htmldocs/upgrade) of the manual for
instructions how to upgrade existing 3.x or 2.x deployments. Early
adopters are encouraged to upgrade to the 4.0 release series. We look
forward to your feedback!

For a summary of news and a detailed list of changes see the [Release
Notes](/4.0/ReleaseNotes4.0.2.html).

### Netatalk 4.0.1 is available

*6th of October 2024*

The Netatalk development team is proud to announce the latest release of
the Netatalk 4.0 release series. This is a minor bugfix release that
addresses build and distribution specific issues.

See the [upgrade chapter](/4.0/htmldocs/upgrade) of the manual for
instructions how to upgrade existing 3.x or 2.x deployments. Early
adopters are encouraged to upgrade to the 4.0 release series. We look
forward to your feedback!

For a summary of news and a detailed list of changes see the [Release
Notes](/4.0/ReleaseNotes4.0.1.html).

### Netatalk 4.0.0 is available

*29th of September 2024*

The Netatalk development team is proud to announce the first release of
the Netatalk 4.0 release series. In this release series, we are bringing
back the entire AppleTalk networking suite that was removed in Netatalk
3.0.

See the [upgrade chapter](/4.0/htmldocs/upgrade) of the manual for
instructions how to upgrade existing 3.x or 2.x deployments. Early
adopters are encouraged to upgrade to the 4.0 release series. We look
forward to your feedback!

For a summary of news and a detailed list of changes see the [Release
Notes](/4.0/ReleaseNotes4.0.0.html).

### Netatalk 2.4.10 is available

*24th of September 2024*

The Netatalk development team is proud to announce the latest release of
the Netatalk 2.4 release series. This release contains a handful of
minor bug fixes and build system improvements. All users of Netatalk 2.4
are encouraged to upgrade their systems to 2.4.10.

For a summary of news and a detailed list of changes see the [Release
Notes](/2.4/ReleaseNotes2.4.10.html).

### Netatalk 3.2.10 is available

*24th of September 2024*

The Netatalk development team is proud to announce the latest release of
the Netatalk 3.2 release series. This release contains a handful of
minor bug fixes and build system improvements. All users of Netatalk 3.2
are encouraged to upgrade their systems to 3.2.10.

For a summary of news and a detailed list of changes see the [Release
Notes](/3.2/ReleaseNotes3.2.10.html).

### Netatalk 2.4.9 is available

*15th of September 2024*

The Netatalk development team is proud to announce the latest release of
the Netatalk 2.4 release series. This release contains bug fixes for the
DHX2 and DHX user authentication modules. All users of Netatalk 2.4 are
encouraged to upgrade their systems to 2.4.9.

For a summary of news and a detailed list of changes see the [Release
Notes](/2.4/ReleaseNotes2.4.9.html).

### Netatalk 3.2.9 is available

*15th of September 2024*

The Netatalk development team is proud to announce the latest release of
the Netatalk 3.2 release series. This release contains bug fixes for the
DHX2 and DHX user authentication modules. All users of Netatalk 3.2 are
encouraged to upgrade their systems to 3.2.9.

For a summary of news and a detailed list of changes see the [Release
Notes](/3.2/ReleaseNotes3.2.9.html).

### Netatalk 2.4.8 is available

*8th of September 2024*

The Netatalk development team is proud to announce the latest release of
the Netatalk 2.4 release series. This release contains security fixes
for the bundled WolfSSL library. All users of Netatalk 2.4 who use the
bundled WolfSSL library are strongly encouraged to upgrade their systems
to 2.4.8.

For a summary of news and a detailed list of changes see the [Release
Notes](/2.4/ReleaseNotes2.4.8.html).

### Netatalk 3.2.8 is available

*8th of September 2024*

The Netatalk development team is proud to announce the latest release of
the Netatalk 3.2 release series. This release contains security fixes
for the bundled WolfSSL library. All users of Netatalk 3.2 who use the
bundled WolfSSL library are strongly encouraged to upgrade their systems
to 3.2.8.

For a summary of news and a detailed list of changes see the [Release
Notes](/3.2/ReleaseNotes3.2.8.html).

### Netatalk 2.4.7 is available

*19th of August 2024*

The Netatalk development team is proud to announce the latest release of
the Netatalk 2.4 release series. This release contains bug fixes for the
Meson build system. All users of Netatalk 2.4 who use Meson are
encouraged to upgrade their systems to 2.4.7.

For a summary of news and a detailed list of changes see the [Release
Notes](/2.4/ReleaseNotes2.4.7.html).

### Netatalk 3.2.7 is available

*19th of August 2024*

The Netatalk development team is proud to announce the latest release of
the Netatalk 3.2 release series. This release contains bug fixes for the
Meson build system. All users of Netatalk 3.2 who use Meson are
encouraged to upgrade their systems to 3.2.7.

For a summary of news and a detailed list of changes see the [Release
Notes](/3.2/ReleaseNotes3.2.7.html).

### Netatalk 2.4.6 is available

*11th of August 2024*

The Netatalk development team is proud to announce the latest release of
the Netatalk 2.4 release series. This release contains bug fixes for the
Meson build system. All users of Netatalk 2.4 who use Meson are
encouraged to upgrade their systems to 2.4.6.

For a summary of news and a detailed list of changes see the [Release
Notes](/2.4/ReleaseNotes2.4.6.html).

### Netatalk 3.2.6 is available

*11th of August 2024*

The Netatalk development team is proud to announce the latest release of
the Netatalk 3.2 release series. This release contains bug fixes for the
Meson build system. All users of Netatalk 3.2 who use Meson are
encouraged to upgrade their systems to 3.2.6.

For a summary of news and a detailed list of changes see the [Release
Notes](/3.2/ReleaseNotes3.2.6.html).

### Netatalk 2.4.5 is available

*1st of August 2024*

The Netatalk development team is proud to announce the latest release of
the Netatalk 2.4 release series. This release contains primarily bug
fixes for the Meson build system. All users of Netatalk 2.4 are
encouraged to upgrade their systems to 2.4.5.

For a summary of news and a detailed list of changes see the [Release
Notes](/2.4/ReleaseNotes2.4.5.html).

### Netatalk 3.2.5 is available

*1st of August 2024*

The Netatalk development team is proud to announce the latest release of
the Netatalk 3.2 release series. This release contains primarily bug
fixes for the Meson build system. All users of Netatalk 3.2 are
encouraged to upgrade their systems to 3.2.5.

For a summary of news and a detailed list of changes see the [Release
Notes](/3.2/ReleaseNotes3.2.5.html).

### Netatalk 2.4.4 is available

*19th of July 2024*

The Netatalk development team is proud to announce the latest release of
the Netatalk 2.4 release series. This release contains primarily bug
fixes for the Meson build system. All users of Netatalk 2.4 are
encouraged to upgrade their systems to 2.4.4.

For a summary of news and a detailed list of changes see the [Release
Notes](/2.4/ReleaseNotes2.4.4.html).

### Netatalk 3.2.4 is available

*19th of July 2024*

The Netatalk development team is proud to announce the latest release of
the Netatalk 3.2 release series. This release contains primarily bug
fixes for the Meson build system. All users of Netatalk 3.2 are
encouraged to upgrade their systems to 3.2.4.

For a summary of news and a detailed list of changes see the [Release
Notes](/3.2/ReleaseNotes3.2.4.html).

### Netatalk 2.4.3 is available

*14th of July 2024*

The Netatalk development team is proud to announce the latest release of
the Netatalk 2.4 release series. This release contains primarily bug
fixes for the Meson build system. Notably, the with-rpath option now
correctly enables or disables runpath for all compiled binaries. All
users of Netatalk 2.4 are encouraged to upgrade their systems to 2.4.3.

For a summary of news and a detailed list of changes see the [Release
Notes](/2.4/ReleaseNotes2.4.3.html).

### Netatalk 3.2.3 is available

*12th of July 2024*

The Netatalk development team is proud to announce the latest release of
the Netatalk 3.2 release series. This release contains primarily bug
fixes for the Meson build system. Notably, the with-rpath option now
correctly enables or disables runpath for all compiled binaries. All
users of Netatalk 3.2 are encouraged to upgrade their systems to 3.2.3.

For a summary of news and a detailed list of changes see the [Release
Notes](/3.2/ReleaseNotes3.2.3.html).

### Netatalk 2.4.2 is available

*6th of July 2024*

The Netatalk development team is proud to announce the latest release of
the Netatalk 2.4 release series. This version reintroduces
OpenSSL/LibreSSL as a required library when building with the bundled
SSL provider. This addresses a potential obstacle to redistribution of
Netatalk binaries. All users of Netatalk 2.4 are encouraged to upgrade
their systems to 2.4.2.

For a summary of news and a detailed list of changes see the [Release
Notes](/2.4/ReleaseNotes2.4.2.html).

### Netatalk 3.2.2 is available

*6th of July 2024*

The Netatalk development team is proud to announce the latest release of
the Netatalk 3.2 release series. This version reintroduces
OpenSSL/LibreSSL as a required library when building with the bundled
SSL provider. This addresses a potential obstacle to redistribution of
Netatalk binaries. All users of Netatalk 3.2 are encouraged to upgrade
their systems to 3.2.2.

For a summary of news and a detailed list of changes see the [Release
Notes](/3.2/ReleaseNotes3.2.2.html).

### Netatalk 2.4.1 is available

*29th of June 2024*

The Netatalk development team is proud to announce the latest release of
the Netatalk 2.4 release series. It includes a patch for security issues
[CVE-2024-38439](/security/CVE-2024-38439.html),
[CVE-2024-38440](/security/CVE-2024-38440.html), and
[CVE-2024-38441](/security/CVE-2024-38441.html). All users of Netatalk
2.4 are encouraged to upgrade their systems to 2.4.1.

For a summary of news and a detailed list of changes see the [Release
Notes](/2.4/ReleaseNotes2.4.1.html).

### Netatalk 3.2.1 is available

*29th of June 2024*

The Netatalk development team is proud to announce the latest release of
the Netatalk 3.2 release series. It includes a patch for security issues
[CVE-2024-38439](/security/CVE-2024-38439.html),
[CVE-2024-38440](/security/CVE-2024-38440.html), and
[CVE-2024-38441](/security/CVE-2024-38441.html). Additionally, the Meson
build system options have been completely reworked for ease of use. All
users of Netatalk 3.2 are encouraged to upgrade their systems to 3.2.1.

For a summary of news and a detailed list of changes see the [Release
Notes](/3.2/ReleaseNotes3.2.1.html).

### Netatalk 3.1.19 is available

*29th of June 2024*

The Netatalk development team is proud to announce the latest release of
the Netatalk 3.1 release series. It includes a patch for security issues
[CVE-2024-38439](/security/CVE-2024-38439.html),
[CVE-2024-38440](/security/CVE-2024-38440.html), and
[CVE-2024-38441](/security/CVE-2024-38441.html). All users of Netatalk
3.1 are encouraged to upgrade their systems to 3.1.19.

For a summary of news and a detailed list of changes see the [Release
Notes](/3.1/ReleaseNotes3.1.19.html).

### Netatalk 2.4.0 is available

*22nd of June 2024*

The Netatalk development team is proud to announce version 2.4.0 of
Netatalk. This is the first stable release of the new 2.4 series. Early
adopters are encouraged to upgrade their systems to 2.4.0.

The standout new feature in this version, is a bundled WolfSSL library
which enables support for the older DHX and Random Number UAMs on modern
systems. The Meson build system is also introduced, which is what
enables the former.

A companion release of the Netatalk 2 Webmin Module, version 2.0, is
also available now. Find more information in the [Release
Notes](https://github.com/Netatalk/netatalk-webmin/releases/tag/netatalk2-2.0).

For a summary of news and a detailed list of changes see the [Release
Notes](/2.4/ReleaseNotes2.4.0.html).

### Netatalk 3.2.0 is available

*1st of June 2024*

The Netatalk development team is proud to announce version 3.2.0 of
Netatalk. This is the first stable release of the new 3.2 series. Early
adopters are encouraged to upgrade their systems to 3.2.0.

The standout new feature in this version, is a bundled WolfSSL library
which enables support for the older DHX and Random Number UAMs on modern
systems. The Meson build system is also introduced, which is what
enables the former.

A companion release of the Netatalk 3 Webmin Module, version 1.1, is
also available now. Find more information in the [Release
Notes](https://github.com/Netatalk/netatalk-webmin/releases/tag/netatalk3-1.1).

For a summary of news and a detailed list of changes see the [Release
Notes](/3.2/ReleaseNotes3.2.0.html).

### Netatalk 3 Webmin Module 1.0 Released

*20th of April 2024*

The first stable and fully compliant version of the Netatalk 3 Webmin
Module is now available. A large number of supported options and help
text has been added.

For more information and to download the module, see the [Release
Notes](https://github.com/Netatalk/netatalk-webmin/releases/tag/netatalk3-1.0).

Simultaneously, a bugfix [v1.3 release of the Netatalk 2
module](https://github.com/Netatalk/netatalk-webmin/releases/tag/netatalk2-1.3)
is also available now.

### Netatalk 2.3.2 is available

*31st of March 2024*

The Netatalk development team is proud to announce version 2.3.2 of the
Netatalk File Sharing suite. This release comes with improvements for
AppleTalk and pap, as well as native init scripts for modern macOS. All
users of previous Netatalk v2 releases are encouraged to upgrade their
installations to 2.3.2.

For a summary of news and a detailed list of changes see the [Release
Notes](/2.3/ReleaseNotes2.3.2.html).

### Netatalk 2.3.1 is available

*3rd of February 2024*

The Netatalk development team is proud to announce version 2.3.1 of the
Netatalk File Sharing suite. This release comes with a range of
compatibility and stability improvements. All users of previous Netatalk
v2 releases are encouraged to upgrade their installations to 2.3.1.

A [companion release of the Webmin
module](https://github.com/Netatalk/netatalk-webmin/releases/tag/netatalk2-1.2)
is also available which adds functionality and fixes bugs.

For a summary of news and a detailed list of changes see the [Release
Notes](/2.3/ReleaseNotes2.3.1.html).

### Netatalk 3 Webmin Module 0.3 Released

*8th of January 2024*

Version 0.3 of the Netatalk 3 Webmin Module is now available. It
introduces a range of minor improvements which makes usage of the module
more convenient.

For more information, see the [Release
Notes](https://github.com/Netatalk/netatalk-webmin/releases/tag/netatalk3-0.3).

### Netatalk 2 Webmin Module 1.1 Released

*6th of January 2024*

Version 1.1 of the Netatalk 2 Webmin Module is a companion to Netatalk
2.3.0. In addition, it includes a range of UX improvements and bugfixes.

For more information, see the [Release
Notes](https://github.com/Netatalk/netatalk-webmin/releases/tag/netatalk2-1.1).

### Netatalk 2.3.0 is available

*28th of December 2023*

The Netatalk development team is proud to announce version 2.3.0 of the
Netatalk File Sharing suite. This is the first stable release of the new
2.3 series. Early adopters are encouraged to upgrade their systems to
2.3.0.

The theme for this release is security and code quality. Long-obsoleted
features have been removed, bugs have been fixed, and documentation
improved.

For a summary of news and a detailed list of changes see the [Release
Notes](/2.3/ReleaseNotes2.3.0.html).

### Netatalk 3.1.18 is available

*5th of October 2023*

The Netatalk development team is proud to announce the latest release of
the Netatalk 3.1 release series. It includes a patch for security issue
[CVE-2022-22995](/security/CVE-2022-22995.html). All users of Netatalk
3.1 are encouraged to upgrade their systems to 3.1.18.

For a summary of news and a detailed list of changes see the [Release
Notes](/3.1/ReleaseNotes3.1.18.html).

### Netatalk Webmin modules updated

*22nd of September 2023*

The Webmin modules for Netatalk 3 as well as Netatalk 2 have been
updated for Webmin v2. Also included is numerous bugfixes as well as
broader support for server settings.

For more information, see the release notes for [Netatalk 3 module
v0.2](https://github.com/Netatalk/netatalk-webmin/releases/tag/netatalk3-0.2)
and [Netatalk 2 module
v1.0](https://github.com/Netatalk/netatalk-webmin/releases/tag/netatalk2-1.0).

### Netatalk 3.1.17 is available

*16th of September 2023*

The Netatalk development team is proud to announce the latest release of
the Netatalk 3.1 release series. It includes a 0-day fix for security
issue [CVE-2023-42464](/security/CVE-2023-42464.html). All users of
Netatalk 3.1 are encouraged to upgrade their systems to 3.1.17.

For a summary of news and a detailed list of changes see the [Release
Notes](/3.1/ReleaseNotes3.1.17.html).

### Netatalk 3.1.16 is available

*11th of September 2023*

The Netatalk development team is proud to announce the latest release of
the Netatalk 3.1 release series. It includes fixes for the "Invalid
metadata EA" error, among other improvements. All users of Netatalk 3.1
are encouraged to upgrade their systems to 3.1.16.

For a summary of news and a detailed list of changes see the [Release
Notes](/3.1/ReleaseNotes3.1.16.html).

### Netatalk 2.2.10 is available

*17th of August 2023*

The Netatalk development team is proud to announce version 2.2.10 of the
Netatalk File Sharing suite. This release contains a range of bugfixes
and quality of life improvements. Additionally, Netatalk now runs on
macOS Ventura hosts. All Netatalk 2.2 users are encouraged to upgrade
their systems to 2.2.10.

For a summary of news and a detailed list of changes see the [Release
Notes](/2.2/ReleaseNotes2.2.10.html).

### Netatalk 3.1.15 is available

*28th of April 2023*

The Netatalk development team is proud to announce the latest release of
the Netatalk 3.1 release series. It includes fixes for security issues
[CVE-2022-43634](/security/CVE-2022-43634.html) and
[CVE-2022-45188](/security/CVE-2022-45188.html), as well as a range of
other bug fixes. Additionally, Netatalk now runs on macOS Ventura hosts.

For a summary of news and a detailed list of changes see the [Release
Notes](/3.1/ReleaseNotes3.1.15.html).

### Netatalk 2.2.9 is available

*26th of April 2023*

The Netatalk development team is proud to announce version 2.2.9 of the
Netatalk File Sharing suite. This release contains a fix for security
issue [CVE-2022-45188](/security/CVE-2022-45188.html) in addition to
other minor bug fixes. All Netatalk 2.2 users are encouraged to upgrade
their systems to 2.2.9.

For a summary of news and a detailed list of changes see the [Release
Notes](/2.2/ReleaseNotes2.2.9.html).

### Netatalk 2.2.8 is available

*25th of February 2023*

The Netatalk development team is proud to announce version 2.2.8 of the
Netatalk File Sharing suite. This release contains a range of bugfixes
and quality of life improvements. All Netatalk 2.2 users are encouraged
to upgrade their systems to 2.2.8.

For a summary of news and a detailed list of changes see the [Release
Notes](/2.2/ReleaseNotes2.2.8.html).

### Netatalk 3.1.14 is available

*10th of January 2023*

The Netatalk development team is proud to announce the latest release of
the Netatalk 3.1 release series. Please update to this latest release as
soon as possible, since it includes fixes for a critical crash in afpd
that was introduced with the security improvements in 3.1.13, in
addition to a range of other minor improvements.

For a summary of news and a detailed list of changes see the [Release
Notes](/3.1/ReleaseNotes3.1.14.html).

### Netatalk 2.2.7 is available

*10th of January 2023*

The Netatalk development team is proud to announce version 2.2.7 of the
Netatalk File Sharing suite. This release fixes the following major
security issues: [CVE-2018-1160](/security/CVE-2018-1160.html),
[CVE-2022-23121](/security/CVE-2022-23121.html),
[CVE-2022-23123](/security/CVE-2022-23123.html), and
[CVE-2022-23125](/security/CVE-2022-23125.html). In addition, it
restores full compatibility with Linux, while introducing cross-platform
systemd service support. Finally, a large number of 3.1 backports and
community patches have been adopted for improved usability and
stability. All Netatalk 2.2 users are encouraged to upgrade their
systems to 2.2.7.

For a summary of news and a detailed list of changes see the [Release
Notes](/2.2/ReleaseNotes2.2.7.html).

### Netatalk releases moving to GitHub

*10th of January 2023*

Future Netatalk releases and release notes will be hosted on
[GitHub](https://github.com/Netatalk/netatalk). Over the last several
years, the git repository, wiki, and issue tracker have been gradually
moved to GitHub. This last move represents the next step in this
process. Legacy release archives will remain on SourceForge, and so will
this website as well as the mailing lists.

### Netatalk 3.1.13 is available

*22th of March 2022*

The Netatalk development team is proud to announce the latest release of
the Netatalk 3.1 release series. Please update to this latest release as
soon as possible as this releases fixes the following major security
issues: [CVE-2021-31439](/security/CVE-2021-31439.html),
[CVE-2022-23121](/security/CVE-2022-23121.html),
[CVE-2022-23122](/security/CVE-2022-23122.html),
[CVE-2022-23123](/security/CVE-2022-23123.html),
[CVE-2022-23124](/security/CVE-2022-23124.html),
[CVE-2022-23125](/security/CVE-2022-23125.html) and
[CVE-2022-0194.html](/security/CVE-2022-0194).

For a summary of news and a detailed list of changes see the [Release
Notes](/3.1/ReleaseNotes3.1.13.html).

### Netatalk 3.1.12 is available

*20th of December 2018*

The Netatalk development team is proud to announce the latest release of
the Netatalk 3.1 release series. Please update to this latest release as
soon as possible as this releases fixes a major security issue
([CVE-2018-1160](/security/CVE-2018-1160.html)).

For a summary of news and a detailed list of changes see the [Release
Notes](/3.1/ReleaseNotes3.1.12.html).

### Netatalk 2.2.6 is available

*9rd of July 2017*

The Netatalk development team is proud to announce version 2.2.6 of the
Netatalk File Sharing suite. This release contains critical fixes for
AppleTalk networks coexisting with TCP/IP networks. In addition, it
improves compatibility with NetBSD. All Netatalk 2.2 users are
encouraged to upgrade their systems to 2.2.6.

For a summary of news and a detailed list of changes see the [Release
Notes](/2.2/ReleaseNotes2.2.6.html).

### Netatalk 3.1.11 is available

*15th of March 2017*

The Netatalk development team is proud to announce the latest release of
the Netatalk 3.1 release series. Users are encouraged to update their
servers to the 3.1 release series which is the stable and supported
version for production systems.

For a summary of news and a detailed list of changes see the [Release
Notes](/3.1/ReleaseNotes3.1.11.html).

### Netatalk 3.1.10 is available

*12th of September 2016*

The Netatalk development team is proud to announce the latest release of
the Netatalk 3.1 release series. Users are encouraged to update their
servers to the 3.1 release series which is the stable and supported
version for production systems.

For a summary of news and a detailed list of changes see the [Release
Notes](/3.1/ReleaseNotes3.1.10.html).

### Netatalk 3.1.9 is available

*19th of July 2016*

The Netatalk development team is proud to announce the latest release of
the Netatalk 3.1 release series. Users are encouraged to update their
servers to the 3.1 release series which is the stable and supported
version for production systems.

For a summary of news and a detailed list of changes see the [Release
Notes](/3.1/ReleaseNotes3.1.9.html).

### Netatalk 3.1.8 is available

*29th of December 2015*

The Netatalk development team is proud to announce the latest release of
the Netatalk 3.1 release series. Users are encouraged to update their
servers to the 3.1 release series which is the stable and supported
version for production systems.

For a summary of news and a detailed list of changes see the [Release
Notes](/3.1/ReleaseNotes3.1.8.html).

### Netatalk 3.1.7 is available

*28th of November 2014*

The Netatalk development team is proud to announce the latest release of
the Netatalk 3.1 release series. Users are encouraged to update their
servers to the 3.1 release series which is the stable and supported
version for production systems.

For a summary of news and a detailed list of changes see the [Release
Notes](/3.1/ReleaseNotes3.1.7.html).

### Netatalk 3.1.6 is available

*12th of August 2014*

The Netatalk development team is proud to announce the latest release of
the Netatalk 3.1 release series. Users are encouraged to update their
servers to the 3.1 release series which is the stable and supported
version for production systems.

For a summary of news and a detailed list of changes see the [Release
Notes](/3.1/ReleaseNotes3.1.6.html).

### Netatalk 3.1.5 is available

*12th of August 2014*

The Netatalk development team is proud to announce the latest release of
the Netatalk 3.1 release series. Users are encouraged to update their
servers to the 3.1 release series which is the stable and supported
version for production systems.

For a summary of news and a detailed list of changes see the [Release
Notes](/3.1/ReleaseNotes3.1.5.html).

### Netatalk 3.1.4 is available

*7th of August 2014*

The Netatalk development team is proud to announce the latest release of
the Netatalk 3.1 release series. Users are encouraged to update their
servers to the 3.1 release series which is the stable and supported
version for production systems.

For a summary of news and a detailed list of changes see the [Release
Notes](/3.1/ReleaseNotes3.1.4.html).

### Netatalk 3.1.3 is available

*3rd of July 2014*

The Netatalk development team is proud to announce the latest release of
the Netatalk 3.1 release series. Users are encouraged to update their
servers to the 3.1 release series which is the stable and supported
version for production systems.

For a summary of news and a detailed list of changes see the [Release
Notes](/3.1/ReleaseNotes3.1.3.html).

### Netatalk 3.1.2 is available

*3rd of June 2014*

The Netatalk development team is proud to announce the third release of
the Netatalk 3.1 release series. Users are encourage to update their
servers to the 3.1 release series which can be considered stable enough
for production systems.

For a summary of news and a detailed list of changes see the [Release
Notes](/3.1/ReleaseNotes3.1.2.html).

### Netatalk 3.1.1 is available

*13th of Mar 2014*

The Netatalk development team is proud to announce version 3.1.1 of the
Netatalk File Sharing suite. This is the second release of the 3.1
release series. Early adopters are encouraged to upgrade their systems
to 3.1.1.

For a summary of news and a detailed list of changes see the [Release
Notes](/3.1/ReleaseNotes3.1.1.html).

### Netatalk 3.0.8 is available

*21st of Feb 2014*

The Netatalk development team is proud to announce version 3.0.8 of the
Netatalk File Sharing suite. This is the first update to the 3.0 release
series. All users are encouraged to upgrade their systems to 3.0.8.

For a summary of news and a detailed list of changes see the [Release
Notes](/3.0/ReleaseNotes3.0.8.html).

### Netatalk 3.0.7 is available

*2nd of Feb 2014*

The Netatalk development team is proud to announce version 3.0.7 of the
Netatalk File Sharing suite. This is the first update to the 3.0 release
series. All users are encouraged to upgrade their systems to 3.0.7.

For a summary of news and a detailed list of changes see the [Release
Notes](/3.0/ReleaseNotes3.0.7.html).

### Netatalk 3.1.0 is available

*28th of Oct 2013*

The Netatalk development team is proud to announce version 3.1.0 of the
Netatalk File Sharing suite. This is the first release of the 3.1
release series. Early adopters are encouraged to upgrade their systems
to 3.1.0.

For a summary of news and a detailed list of changes see the [Release
Notes](/3.1/ReleaseNotes3.1.0.html).

### Netatalk 3.0.6 is available

*25th of Oct 2013*

The Netatalk development team is proud to announce version 3.0.6 of the
Netatalk File Sharing suite. This is the first update to the 3.0 release
series. All users are encouraged to upgrade their systems to 3.0.6.

For a summary of news and a detailed list of changes see the [Release
Notes](/3.0/ReleaseNotes3.0.6.html).

### Netatalk 3.1-beta2 is available

*16th of September 2013*

The Netatalk development team is proud to announce the second beta
release of the next Netatalk version 3.1. This release is intended for
testing only.

For a summary of news and a detailed list of changes see the [Release
Notes](/3.1/ReleaseNotes3.1beta2.html).

### Netatalk 3.0.5 is available

*14th of Aug 2013*

The Netatalk development team is proud to announce version 3.0.5 of the
Netatalk File Sharing suite. This is the first update to the 3.0 release
series. All users are encouraged to upgrade their systems to 3.0.5.

For a summary of news and a detailed list of changes see the [Release
Notes](/3.0/ReleaseNotes3.0.5.html).

### Netatalk 3.1-beta1 is available

*7th of August 2013*

The Netatalk development team is proud to announce the first beta
release of the next Netatalk version 3.1. This release is intended for
testing only.

For a summary of news and a detailed list of changes see the [Release
Notes](/3.1/ReleaseNotes3.1beta1.html).

### Netatalk 2.2.5 is available

*23rd of July 2013*

The Netatalk development team is proud to announce version 2.2.5 of the
Netatalk File Sharing suite. This is the third update to the 2.2 release
series. All users are encouraged to upgrade their systems to 2.2.5.

For a summary of news and a detailed list of changes see the [Release
Notes](/2.2/ReleaseNotes2.2.5.html).

### Netatalk 3.1-alpha1 is available

*1st of July 2013*

The Netatalk development team is proud to announce the first alpha
release of the next Netatalk version 3.1. This release is intended for
testing only.

For a summary of news and a detailed list of changes see the [Release
Notes](/3.1/ReleaseNotes3.1alpha1.html).

### Netatalk 3.0.4 is available

*24nd of May 2013*

The Netatalk development team is proud to announce version 3.0.4 of the
Netatalk File Sharing suite. This is the first update to the 3.0 release
series. All users are encouraged to upgrade their systems to 3.0.4.

For a summary of news and a detailed list of changes see the [Release
Notes](/3.0/ReleaseNotes3.0.4.html).

### Netatalk 3.0.3 is available

*26nd of March 2013*

The Netatalk development team is proud to announce version 3.0.3 of the
Netatalk File Sharing suite. This is the first update to the 3.0 release
series. All users are encouraged to upgrade their systems to 3.0.3.

For a summary of news and a detailed list of changes see the [Release
Notes](/3.0/ReleaseNotes3.0.3.html).

### Netatalk 3.0.2 is available

*22nd of January 2013*

The Netatalk development team is proud to announce version 3.0.2 of the
Netatalk File Sharing suite. This is the first update to the 3.0 release
series. All users are encouraged to upgrade their systems to 3.0.2.

For a summary of news and a detailed list of changes see the [Release
Notes](/3.0/ReleaseNotes3.0.2.html).

### Netatalk 3.0.1 is available

*28nd of September 2012*

The Netatalk development team is proud to announce version 3.0.1 of the
Netatalk File Sharing suite. This is the first update to the 3.0 release
series. All users are encouraged to upgrade their systems to 3.0.1.

For a summary of news and a detailed list of changes see the [Release
Notes](/3.0/ReleaseNotes3.0.1.html).

### Netatalk 2.2.4 is available

*28nd of September 2012*

The Netatalk development team is proud to announce version 2.2.4 of the
Netatalk File Sharing suite. This is the third update to the 2.2 release
series. All users are encouraged to upgrade their systems to 2.2.4.

For a summary of news and a detailed list of changes see the [Release
Notes](/2.2/ReleaseNotes2.2.4.html).

### Netatalk 3.0 is available

*9th of July 2012*

The Netatalk development team is proud to announce the release of
Netatalk 3.0. Early adopters are encouraged to upgrade their systems to
3.0.

For a summary of news and a detailed list of changes see the [Release
Notes](/3.0/ReleaseNotes3.0.html).

### Netatalk 3.0 beta2 is available

*1st of June 2012*

The Netatalk development team is proud to announce version 3.0 beta2 of
the Netatalk File Sharing suite. This is the second beta release to the
new 3.0 release series. This release is not intended for production
systems, but for testing only.

For a summary of news and a detailed list of changes see the [Release
Notes](/3.0/ReleaseNotes3.0beta2.html).

### Netatalk 3.0 beta1 is available

*22nd of May 2012*

The Netatalk development team is proud to announce version 3.0 beta1 of
the Netatalk File Sharing suite. This is the first beta release to the
new 3.0 release series. This release is not intended for production
systems, but for testing only.

For a summary of news and a detailed list of changes see the [Release
Notes](/3.0/ReleaseNotes3.0beta1.html).

### Netatalk 2.2.3 is available

*22nd of May 2012*

The Netatalk development team is proud to announce version 2.2.3 of the
Netatalk File Sharing suite. This is the third update to the 2.2 release
series. All users are encouraged to upgrade their systems to 2.2.3.

For a summary of news and a detailed list of changes see the [Release
Notes](/2.2/ReleaseNotes2.2.3.html).

### Netatalk 3.0 alpha3 is available

*20th of April 2012*

The Netatalk development team is proud to announce version 3.0 alpha3 of
the Netatalk File Sharing suite. This is the third alpha release to the
new 3.0 release series. This release is not intended for production
systems, but for testing only.

For a summary of news and a detailed list of changes see the [Release
Notes](/3.0/ReleaseNotes3.0alpha3.html).

### Netatalk 3.0 alpha2 is available

*4th of April 2012*

The Netatalk development team is proud to announce version 3.0 alpha2 of
the Netatalk File Sharing suite. This is the second alpha release to the
new 3.0 release series. This release is not intended for production
systems, but for testing only.

For a summary of news and a detailed list of changes see the [Release
Notes](/3.0/ReleaseNotes3.0alpha2.html).

### Netatalk 3.0 alpha1 is available

*27th of March 2012*

The Netatalk development team is proud to announce version 3.0 alpha1 of
the Netatalk File Sharing suite. This is the first alpha release to the
new 3.0 release series. This release is not intended for production
systems, but for testing only.

For a summary of news and a detailed list of changes see the [Release
Notes](/3.0/ReleaseNotes3.0alpha1.html).

### Netatalk 2.2.2 is available

*16th of January 2012*

The Netatalk development team is proud to announce version 2.2.2 of the
Netatalk File Sharing suite. This is the second update to the new 2.2
release series. All users are encouraged to upgrade their systems to
2.2.2.

For a summary of news and a detailed list of changes see the [Release
Notes](/2.2/ReleaseNotes2.2.2.html).

### Netatalk 2.2.1 is available

*6th of September 2011*

The Netatalk development team is proud to announce version 2.2.1 of the
Netatalk File Sharing suite. This is the first update to the new 2.2
release series. All users are encouraged to upgrade their systems to
2.2.1.

For a summary of news and a detailed list of changes see the [Release
Notes](/2.2/ReleaseNotes2.2.1.html).

### Netatalk 2.1.6 is available

*5th of September 2011*

The Netatalk development team is proud to announce version 2.1.6 of the
Netatalk File Sharing suite. This is the last update to the 2.1 series.
All users are encouraged to upgrade their systems to 2.1.6.

For a summary of news and a detailed list of changes see the [Release
Notes](/2.1/ReleaseNotes2.1.6.html).

### Netatalk 2.2.0 is available for testing!

*27th of July 2011*

The Netatalk development team is proud to announce version 2.2.0 of the
Netatalk File Sharing suite. This is the first stable release of the new
2.2 series. Early adopters are encouraged to upgrade their systems to
2.2.0.

For a summary of news and a detailed list of changes see the [Release
Notes](/2.2/ReleaseNotes2.2.0.html).

### Netatalk 2.1.5 is available

*21st of December 2010*

The Netatalk development team is proud to announce version 2.1.5 of the
Netatalk File Sharing suite. This is the latest stable version. All
users are encouraged to upgrade their systems to 2.1.5.

For a summary of news and a detailed list of changes see the [Release
Notes](/2.1/ReleaseNotes2.1.5.html).

### Netatalk 2.1.4 is available

*15th of October 2010*

The Netatalk development team is proud to announce version 2.1.4 of the
Netatalk File Sharing suite. This is the latest stable version. All
users are encouraged to upgrade their systems to 2.1.4.

For a summary of news and a detailed list of changes see the [Release
Notes](/2.1/ReleaseNotes2.1.4.html).

### Netatalk 2.1.3 is available

*12th of July 2010*

The Netatalk development team is proud to announce version 2.1.3 of the
Netatalk File Sharing suite. This is the latest stable version. All
users are encouraged to upgrade their systems to 2.1.3.

For a summary of news and a detailed list of changes see the [Release
Notes](/2.1/ReleaseNotes2.1.3.html).

### Netatalk 2.1.2 is available

*18th of June 2010*

The Netatalk development team is proud to announce version 2.1.2 of the
Netatalk File Sharing suite. This is the latest stable version. All
users are encouraged to upgrade their systems to 2.1.2.

For a summary of news and a detailed list of changes see the [Release
Notes](/2.1/ReleaseNotes2.1.2.html).

### Netatalk 2.1.1 is available

*26th of May 2010*

The Netatalk development team is proud to announce version 2.1.1 of the
Netatalk File Sharing suite. This is the latest stable version. All
users are encouraged to upgrade their systems to 2.1.1.

For a summary of news and a detailed list of changes see the [Release
Notes](/2.1/ReleaseNotes2.1.1.html).

### Netatalk 2.1 is available

*26th of April 2010*

The Netatalk development team is proud to announce version 2.1 of the
Netatalk File Sharing suite.

For a summary of news and a detailed list of changes see the [Release
Notes](/2.1/ReleaseNotes2.1.html).

In case, you want to upgrade an existing Netatalk 1.x installation,
ensure you carefully read the upgrade guide before and follow the steps
outlined there.

### Netatalk 2.0.5 is available

*10th of November 2009*

The Netatalk development team is proud to announce version 2.0.5 of the
Netatalk File Sharing suite. This is the latest stable version. It
contains several important bugfixes, including a more complete security
fix for [CVE-2008-5718](/security/CVE-2008-5718.html). Time Machine
support has been added with the new volume option "tm". All users are
encouraged to upgrade their systems to 2.0.5.

For a summary of news and a detailed list of changes see the [Release
Notes](/2.0/ReleaseNotes2.0.5.html).

### Netatalk 2.0.4 is available!

*29th of May 2009*

The Netatalk development team is proud to announce version 2.0.4 of the
Netatalk File Sharing suite. This is the latest stable version. It
contains several important bugfixes, including a security fix for papd
(see [CVE-2008-5718](/security/CVE-2008-5718.html)), therefore *all
users are encouraged to upgrade their systems to 2.0.4.*

For a summary of news and a detailed list of changes see the [Release
Notes](/2.0/ReleaseNotes2.0.4.html).

### Netatalk 2.0.3 is available!

*18th of May 2005*

The Netatalk development team is proud to announce version 2.0.3 of the
Netatalk File Sharing suite. This is the latest stable version. It
contains several important bugfixes, therefore *all users are encouraged
to upgrade their systems to 2.0.3.*

For a summary of news and a detailed list of changes see the [Release
Notes](/2.0/ReleaseNotes2.0.3.html).

### Netatalk 2.0.2 is available!

*3rd of January 2005*

The Netatalk development team is proud to announce version 2.0.2 of the
Netatalk File Sharing suite. This is the latest stable version. It
contains several important bugfixes, therefore *all users are encouraged
to upgrade their systems to 2.0.2.*

For a summary of news and a detailed list of changes see the [Release
Notes](/2.0/ReleaseNotes2.0.2.html).

### Netatalk 1.6.4a released

*28th of October 2004*

This release is a security fix for the etc2ps.sh script. See
[CAN-2004-0974](/security/CVE-2004-0974.html) for details. No other
changes were made from Netatalk 1.6.4.

### Netatalk 2.0.1 is available!

*27th of October 2004*

The Netatalk development team is proud to announce version 2.0.1 of the
Netatalk File Sharing suite. This is the latest stable version. It
contains several important bugfixes, therefore *all users are encouraged
to upgrade their systems to 2.0.1.*

The etc2ps.sh script delivered with all Netatalk versions prior to 2.0.1
has been found to be vulnerable to symlink attacks. See
[CAN-2004-0974](/security/CVE-2004-0974.html) for details.

For a summary of news and a detailed list of changes see the [Release
Notes](/2.0/ReleaseNotes2.0.1.html).

### Netatalk 2.0.0 is available!

*11th of October 2004*

The Netatalk development team is proud to present the new stable 2.0.0
release. Major improvements over the 1.6 series are:

- Netatalk's AFP 3.1 compliant file server allows long filenames, UTF-8
  names, large file support and full Mac OS X compatibility
- The print server task can directly interact with CUPS, automagically
  sharing all CUPS queues
- Kerberos V support, allowing true "Single Sign On"
- Whole rework of the CNID subsystem, providing reliable and persistant
  storage of file and directory IDs
- Huge improvements regarding product documentation making Netatalk's
  features accessible more easily
- countless bugs fixed compared to previous versions

In case, you want to upgrade an existing Netatalk 1.x installation,
ensure you carefully read the upgrade guide before and follow the steps
outlined there. If you made use of symlinks inside Netatalk shares
consider setting up a test installation with 2.0 before migrating since
Netatalk 2.0 provides no support for symlinks any longer.

For a summary of news and a detailed list of changes see the [Release
Notes](/2.0/ReleaseNotes2.0.0.html).
