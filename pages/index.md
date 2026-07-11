# Netatalk, Free and Open Source File Server

Netatalk is a Free and Open Source file server that uses the AFP protocol.
The Netatalk software runs on a UNIX-like operating system (such as Linux, *BSD or
macOS) and allows any computer with an AFP client to easily connect with each other
and share files on a local network or over the Internet.

The Netatalk file server software is light-weight, performant, and portable.
Conforming to the [Apple Filing
Protocol](https://developer.apple.com/library/archive/documentation/Networking/Conceptual/AFP/Introduction/Introduction.html#//apple_ref/doc/uid/TP40000854-CH1-SW1)
specification, any macOS, Mac OS X, or Classic Mac OS system can connect to a Netatalk file server out of the box.

Since its launch in 1990, Netatalk has been leveraged by universities, enterprises,
and home users for collaboration and remote data backup on Macs.
With Netatalk, any UNIX-like host is able to integrate seamlessly with networked
macOS systems, act as centralized file storage, and provide data backup services.

## Getting Started

There are three ways to get started with Netatalk: Install a pre-built binary package,
deploy a container image, or build the software yourself from source code.
Knowledge of basic system administration is required, including installing packages,
editing configuration files, and starting/stopping system services.

### 📦 Install a binary package for your distribution

Use your operating system's package manager to install the latest
available *netatalk* package. This is the recommended option for most
users.

See [Repology](https://repology.org/project/netatalk/packages)
for a list of known packages.

### 🐳 Deploy a container image

The project publishes images on [Docker Hub](https://hub.docker.com/r/netatalk/netatalk)
and [GHCR](https://github.com/Netatalk/netatalk/pkgs/container/netatalk)
that can be deployed with a container runtime such as docker or podman.

Refer to the [container documentation](containers.html) for details on how to
configure the container.

### 🛠️ Build from source

You want to build from source when neither of the previous options are
feasible, or when you want to do a hardened Netatalk deployment with
only a subset of features enabled.

See the [getting started guide](/install.html) for instructions how to prepare the build environment,
and read more about dependencoes in the [Netatalk manual](/manual/en/Installation.html).

## How to Use

By default, Netatalk shares the home directory of each authorized user,
with a secure authentication method for modern AFP clients.
It is recommended to start and stop the Netatalk AFP server through your operating systems's init system.

If you need a different setup, for instance sharing a specific directory or allowing very old AFP clients access,
you have to configure the host system and then restart Netatalk.
Netatalk has a dizzying amount of options which can be daunting initially.
The [Configuration](/manual/en/Configuration.html) chapter and
[afp.conf](/manual/en/afp.conf.5.html) page in the Netatalk manual
are good places to start.

Once Netatalk is up and running, use an [AFP client to connect to the file server](https://netatalk.io/docs/Connect-to-AFP-Server).

## Latest News

NETATALK_NEWS

## Older Stories

See the [News Archive](/archive.html)
