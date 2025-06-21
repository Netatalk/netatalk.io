# Netatalk 1.3

netatalk is a kernel-level implementation of the AppleTalk Protocol
Suite for BSD-derived systems. netatalk's primary services are
routing, file service, print spooling, and outbound printing, in an
AppleTalk networking environment. The current release contains support
for EtherTalk Phase I and II.

netatalk-1.3 runs on the following machines:

| OS | Versions | Hardware | Notes |
|----|----------|----------|-------|
| SunOS | 4.1+ | | Sparc kernel must have VDDRV option installed |
| Ultrix | 4.[1-3] | 3100,5000 | |

## Changes

atalkd is completely rewritten for phase 2 support. atalkd.conf
from previous version will not work!

afpd now has better AFS support. In particular, the configuration
for AFS was made much easier; a number of Kerberos-related
byte-ordering and time problems were found; clear-text passwords
were added (thanks to <geeb@umich.edu>).

afpd now handles Unix permissions much better (thanks to
<metcalf@mit.edu>).

There are many, many more changes, but most are small bug fixes.

netatalk-1.3 is available via anonymous ftp from terminator.rs.itd.umich.edu,
in ~ftp/unix/netatalk/netatalk-1.3.tar.{Z,gz}.

Research Systems Unix Group  
The University of Michigan <netatalk@umich.edu>  
c/o Wesley Craig +1-313-764-2278  
535 W. William St.  
Ann Arbor, Michigan  
48103-4943

- Wesley Craig, January 1994
