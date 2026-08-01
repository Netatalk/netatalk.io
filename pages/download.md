# Download Netatalk

Here you can find the latest Netatalk source code releases for download,
which can be [built and installed](/install.html) on your system.

We also distribute a [Webmin module](/docs/Webmin-Module.html) for Netatalk, which can be installed directly from the Webmin interface.

Both have corresponding `.asc` files for GPG signature verification,
as well as `.sha256sum` and `.sha512sum` files for checksum verification.

NETATALK_DOWNLOADS

## GPG Signature Verification

To validate the integrity of the downloaded source code, you can download the corresponding GPG signature file.
The signatures are signed with the [GPG key of the Netatalk project](http://netatalk.io/NetatalkDistributionPublicKey.asc),
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

If you get a warning an untrusted signature, compare the key fingerprint
with the one above. If they match, you can trust the signature.

For older releases, go to [Netatalk Files on
SourceForge](https://sourceforge.net/projects/netatalk/files/).

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

See the [container documentation](/docker.html) for available options
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
