# Netatalk, Open Source File Server for Macs

Netatalk is a Free and Open Source file server for Macs. The Netatalk
software runs on a UNIX-like operating system (such as Linux, BSD or
macOS) and allows Macintosh computers to easily connect with each other
and share files on a local network or over the Internet.

Written in pure C, it is light-weight, performant, and portable.
Conforming to the [Apple Filing
Protocol](https://developer.apple.com/library/archive/documentation/Networking/Conceptual/AFP/Introduction/Introduction.html#//apple_ref/doc/uid/TP40000854-CH1-SW1)
specification up to and including AFP 3.4, any macOS, Mac OS X, or Mac
OS system can talk to a Netatalk file server out of the box.

Since 1990, Netatalk has been leveraged by universities, enterprises,
and home users for collaboration and remote data backup on Macs. With
Netatalk, any UNIX-like host is able to integrate seamlessly with macOS
network file system services.

## Getting Started

There are roughly three ways to get started with Netatalk: Install a
pre-built binary package, pull a container image, or build the software
yourself from source. Knowledge of how to install packages, edit
configuration files, and starting/stopping system services are required.

### 1. Install a pre-built package for your distribution

Use your operating system's package manager to install the latest
available *netatalk* package. This is the recommended option for most
users. See [Repology](https://repology.org/project/netatalk/packages)
for a list of known packages.

### 2. Pull a container image

This option is either for users who already leverage containers in their
setup, or for when a binary package is outdated and you want to run the
latest Netatalk version. Running a docker image has a relatively lower
barrier to entry compared to building from source.

With Docker Engine or equivalent installed, do:

    $ docker pull netatalk/netatalk:latest

Then follow the
[instructions](https://hub.docker.com/r/netatalk/netatalk) on how to
configure the container.

### 3. Build from source

You want to build from source when neither of the previous options are
feasible, or when you want to do an optimized Netatalk deployment with
only a subset of features enabled.

Arrange a C compiler (we use *gcc* or *clang*), the
[Meson](https://mesonbuild.com/) build system with
[Ninja](https://ninja-build.org/), together with [required
libraries](https://netatalk.io/install).
Read more in the [Netatalk manual](stable/htmldocs/installation) or the
OS specific guides in the [wiki](docs).

## How to Use

By default, Netatalk shares the home directory of each authorized user,
with secure authentication methods compatible with macOS, Mac OS X, Mac
OS 9 and Mac OS 8.

If you need a different setup, you have to configure the host system
before starting Netatalk. Netatalk has a dizzying amount of options
which can be daunting initially. The
[Configuration](stable/htmldocs/configuration) chapter and
[afp.conf](https://netatalk.io/stable/htmldocs/afp.conf.5) page in the
Netatalk manual are good places to start.

Once Netatalk is up and running, in the macOS Finder, active Netatalk
file servers appear under *Locations*, or in the *Network* drawer. On
Classic Mac OS, you use the *AppleShare* client within the *Chooser*
desk accessory.

## Features

Below is an overview of the capabilities and bundled utilities that the
latest version of Netatalk provides.

| Feature | Details |
|----|----|
| Host OS Support | Linux (glibc & musl), DragonFlyBSD, FreeBSD, NetBSD, OpenBSD, macOS, OmniOS, Solaris 11 |
| Client OS Support | macOS, Mac OS X, Mac OS 8/9, Macintosh System Software 6.0.x/7.x, GS/OS, ProDOS |
| AFP Protocol Versions | 1.1, 2.0, 2.1, 2.2, 3.0, 3.1, 3.2, 3.3. 3.4 |
| AFP over TCP | Yes |
| AFP over [AppleTalk](https://en.wikipedia.org/wiki/AppleTalk) | Yes (supported on Linux, NetBSD) |
| Macintosh File System Metadata | macOS / OSX extended attributes, Classic Mac OS resource forks |
| Service Discovery | *[Bonjour](https://en.wikipedia.org/wiki/Bonjour_(software))*-compatible on macOS / OSX, *AppleTalk* on Classic Mac OS |
| Remote Backups | *[Time Machine](https://en.wikipedia.org/wiki/Time_Machine_(macOS))*-compatible |
| Indexed Search | *[Spotlight](https://en.wikipedia.org/wiki/Spotlight_(Apple))*-compatible on macOS / OSX, *CatalogSearch* on Classic Mac OS |
| Macintosh Network Booting | *[NetBoot](https://en.wikipedia.org/wiki/NetBoot)* 1.0-compatible (usage example: [kea-mboot](https://github.com/saybur/kea-mboot)) |
| Apple II Network Booting | Yes: //e and IIGS (via `a2boot`) |
| AppleTalk Printing to modern printers | Yes (via `papd`) |
| Printing to [LocalTalk](https://en.wikipedia.org/wiki/LocalTalk) printers | Yes (via `pap`) |
| AppleTalk Time Server | *[Timelord](https://web.archive.org/web/20010303220117/http://www.cs.mu.oz.au/appletalk/readmes/TMLD.README.html)*-compatible (via `timelord`) |
| AppleTalk Router | Yes (via `atalkd`) |
| [MacIP](https://en.wikipedia.org/wiki/MacIP) Gateway | Yes (via `macipgw`) |
| Administrative GUI | *[Webmin](https://webmin.com/)* module |

# Latest News

## Netatalk 4.1.2 is available

*10th of February 2025*

The Netatalk development team is proud to announce the latest version in
the Netatalk 4.1 release series. This fixes bugs in the Webmin module,
while also improving compatibility with MacPorts.

All users of previous Netatalk versions are encouraged to upgrade to
4.1.2.

For a summary of news and a detailed list of changes see the [Release
Notes](/4.1/ReleaseNotes4.1.2.html).

## Netatalk 4.1.1 is available

*20th of January 2025*

The Netatalk development team is proud to announce the latest version in
the Netatalk 4.1 release series. This is a bugfix release that also
improves compatibility with NetBSD and NixOS.

All users of previous Netatalk versions are encouraged to upgrade to
4.1.1.

For a summary of news and a detailed list of changes see the [Release
Notes](/4.1/ReleaseNotes4.1.1.html).

## End of Life policy published

*18th of January 2025*

The Netatalk Project has published its End of Life policy. We guarantee
that each release series will be supported with security patches for 12
months after the release of the superseding feature release.

Most urgently, this means that the long-running 3.1 release series will
be out of support after May 31st, 2025. Users and downstream packagers
are encouraged to upgrade to the latest Netatalk 4.1 release series.

For more information, see the [Security
Policy](/security.html).

## Older Stories

See the [News Archive](/archive.html)
