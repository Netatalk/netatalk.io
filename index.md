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
users.

See [Repology](https://repology.org/project/netatalk/packages)
for a list of known packages.

### 2. Deploy a container image

The project publishes images on [Docker Hub](https://hub.docker.com/r/netatalk/netatalk)
that can be deployed with a container runtime such as docker or podman.

Refer to the [container documentation](/docker.html) for details on how to
configure the container.

### 3. Build from source

You want to build from source when neither of the previous options are
feasible, or when you want to do a hardened Netatalk deployment with
only a subset of features enabled.

You need a C compiler (we use *gcc* or *clang*), the
[Meson](https://mesonbuild.com/) build system with
[Ninja](https://ninja-build.org/), together with [required
libraries](/install.html).
Read more in the [Netatalk manual](/manual/en/Installation.html) or the
OS specific guides in the [wiki](/docs.html).

## How to Use

By default, Netatalk shares the home directory of each authorized user,
with secure authentication methods compatible with macOS, Mac OS X, Mac
OS 9 and Mac OS 8.

If you need a different setup, you have to configure the host system
before starting Netatalk. Netatalk has a dizzying amount of options
which can be daunting initially.
The [Configuration](/manual/en/Configuration.html) chapter and
[afp.conf](/manual/en/afp.conf.5.html) page in the Netatalk manual
are good places to start.

Once Netatalk is up and running, in the macOS Finder, active Netatalk
file servers appear under *Locations*, or in the *Network* drawer. On
Classic Mac OS, you use the *AppleShare* client within the *Chooser*
desk accessory.

## How to Contribute

If you found a bug or have an idea for a new feature,
please file a ticket at the [GitHub issue tracker](https://github.com/Netatalk/netatalk/issues/new/choose).

If you want to contribute code, please familiarize yourself with
the [Contributor Guidelines](https://netatalk.io/docs/Developer-Notes)
and then file a [Pull Request](https://github.com/Netatalk/netatalk/pulls)
with the project.

We are looking forward to your contribution!

## Latest News

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

## Older Stories

See the [News Archive](/archive.html)
