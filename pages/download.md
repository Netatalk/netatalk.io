# Download Netatalk

Here you can find the latest source code releases of the Netatalk AFP file server
and the Netatalk Client for download.

Every release has a corresponding `.asc` file for GPG signature verification,
as well as a `.sha256sum` file for checksum verification.
The server release files also come with `.sha512sum` checksums.

## Netatalk Server

The Netatalk file server source code can be [built and installed](/install.html) on your system.

We also distribute a [Webmin module](/docs/Webmin-Module.html) for Netatalk, which can be installed directly from the Webmin interface.

NETATALK_DOWNLOADS

All Netatalk server releases are published on
[GitHub Releases](https://github.com/Netatalk/netatalk/releases).
For older releases, go to [Netatalk Files on
SourceForge](https://sourceforge.net/projects/netatalk/files/).

## Netatalk Client

The Netatalk Client is a Free and Open Source AFP file sharing client
for Linux, \*BSD, macOS and other Unix-like operating systems.
It can mount AFP volumes as local filesystems through FUSE,
browse them interactively with the *afpcmd* command line client,
and add AFP support to other applications through the *libafpclient* library.

See the [installation instructions](https://github.com/Netatalk/netatalk-client/blob/main/INSTALL.md)
and the [getting started guide](https://github.com/Netatalk/netatalk-client/blob/main/docs/GETTING_STARTED.md)
for how to build and use the client.

NETATALK_CLIENT_DOWNLOADS

All Netatalk Client releases are published on
[GitHub Releases](https://github.com/Netatalk/netatalk-client/releases).
Releases before 0.9.5 were published as *afpfs-ng* tarballs with checksums only, without GPG signatures.

## GPG Signature Verification

To validate the integrity of the downloaded source code, you can download the corresponding GPG signature file.
Both Netatalk server and Netatalk Client releases are signed with the [GPG key of the Netatalk project](http://netatalk.io/NetatalkDistributionPublicKey.asc),
which can also be fetched from the keystore at [keys.openpgp.org](https://keys.openpgp.org)
or [keys.mailvelope.com](https://keys.mailvelope.com).

The GPG key fingerprint is: **835A 6542 8C82 2F69 C45B  817A 7B13 E1BF E4DD E8BD**

    $ gpg --keyserver keys.openpgp.org --recv-keys 7B13E1BFE4DDE8BD
    gpg: key 7B13E1BFE4DDE8BD: public key "Netatalk Distribution <distribution@netatalk.io>" imported
    gpg: Total number processed: 1
    gpg:               imported: 1
    $ gpg --verify netatalk-x.y.z.tar.xz.asc netatalk-x.y.z.tar.xz
    gpg: Signature made Fri 08 Aug 2025 01:21:05 PM UTC
    gpg:                using RSA key 835A65428C822F69C45B817A7B13E1BFE4DDE8BD
    gpg: Good signature from "Netatalk Distribution <distribution@netatalk.io>"

The same procedure applies to the Netatalk Client tarball, `netatalk-client-x.y.z.tar.xz`.

If you get a warning about an untrusted signature, compare the key fingerprint
with the one above. If they match, you can trust the signature.

## Netatalk Binary Packages

This project relies on downstream packagers, for instance Linux or \*BSD
distributions, to package and distribute pre-built binary packages for
Netatalk.

Either use your operating system's package manager to search for a
*netatalk* package, or refer to the Repology reference below.

### Container Deployment

The Netatalk development team maintains a
[container image for Netatalk](https://hub.docker.com/r/netatalk/netatalk)
which is distributed on Docker Hub.

With Docker Engine or compatible container runtime installed, pull a
`netatalk/netatalk` tag from Docker Hub, for example:

    docker pull netatalk/netatalk:latest

See the [container documentation](/containers.html) for available options
and usage examples.

### Repology Reference

A list of [binary netatalk packages](https://repology.org/project/netatalk/packages) known to Repology.

![Repology package status](https://repology.org/badge/vertical-allrepos/netatalk.svg)

## AFP Test-Suite

The AFP Test-Suite used to be a separate project, but is now part of the Netatalk distribution since v4.0.
The test suite is used to verify the correct operation of an AFP server implementation.

Find historical afptest tarballs in the [SourceForge
Files](https://sourceforge.net/projects/netatalk/files/Testsuite/)
section.
