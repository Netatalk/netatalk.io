# Download Netatalk

## Netatalk Source Code Releases

The most recent stable Netatalk source code releases can be downloaded
from the **navbar to the left** on this website.

You can also find the release tarballs attached to the [release
notes](https://github.com/Netatalk/netatalk/releases) on GitHub.

To validate the integrity of the downloaded source code, you can
download the corresponding GPG signature file. The signatures are
signed with the GPG key of the Netatalk project, which can be fetched
from the keystore at [keys.openpgp.org](https://keys.openpgp.org)
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

## Webmin Module

As of Netatalk 4.0.0, the Webmin module is part of the Netatalk package.
Module tarballs are distributed with stable releases.

The Webmin modules for Netatalk 3.x and earlier can be downloaded from
[SourceForge
Files](https://sourceforge.net/projects/netatalk/files/Webmin/) section.

## AFP Test-Suite

As of Netatalk 4.0.2, the afptest test suite is part of the Netatalk
package.

Find historical afptest release tarballs in the [SourceForge
Files](https://sourceforge.net/projects/netatalk/files/Testsuite/)
section.
