# Name

extmap.conf — Configuration file used by afpd to specify file name extension mappings

# Description

**extmap.conf** is the configuration file used by **afpd** to specify file
name extension to Mac OS type/creator mappings.

On Classic Mac OS, type/creator is filesystem metadata that is used to
determine the file type and application used to open the file.
They consist of four characters each.

This scheme was partially supported up to Mac OS X 10.4 Tiger,
but removed in Mac OS X 10.5 Leopard in favor of looking
up the file extension directly.

The configuration lines are composed like:

    .extension [ type [ creator ] ]

The type is mandatory, but creator is optional.

Any line beginning with a hash (“#”) character is ignored. The
leading-dot lines specify file name extension mappings. The extension
'.' sets the default creator and type for otherwise untyped Unix files.

# Examples

## Example: Set both type and creator

Extension is jpg, type is "JPEG", creator is "ogle" which maps to
Preview.app on Mac OS X.

    .jpg "JPEG" "ogle"

## Example: Set only type

Extension is lzh, type is "LHA", creator is not defined.

    .lzh "LHA"

# See Also

afp.conf(5), afpd(8)

# Author

[Contributors to the Netatalk Project](https://netatalk.io/contributors)
