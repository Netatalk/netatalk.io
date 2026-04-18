# AFP SRP User Authentication Method

This document is an open source community specification for the SRP (Secure Remote Password)
User Authentication Method as implemented by Apple's AFP clients and servers,
notably AirPort Time Capsule and the AFP client in macOS.
The protocol was reverse-engineered by the Netatalk development team using packet captures
from TimeCapsule8,119 which identifies itself as conforming to AFP 3.3,
then validated against the AFP client in macOS Tahoe 26.4.

## Overview

The SRP UAM implements the Secure Remote Password protocol (RFC 2945, RFC 5054)
over AFP's existing FPLoginExt/FPLoginCont authentication framework. It provides
mutual authentication and a shared session key without transmitting the password
or a password-equivalent value.

The exchange completes in two rounds:

1. **Client init** (FPLoginExt) -- client sends username; server responds with
   SRP group parameters, salt, and server public ephemeral B.
2. **Client proof** (FPLoginCont) -- client sends public ephemeral A and proof
   M1; server responds with proof M2.

## SRP Parameters

The server selects an SRP group from RFC 5054. In practice, Apple servers use
group #2 (1536-bit):

- **N**: 1536-bit prime from RFC 5054 section 3
- **g**: 2
- **Hash**: SHA-1

The group index is transmitted in the server's first response (field2), allowing
for future use of larger groups.

## Wire Format

All multi-byte integers are big-endian. Variable-length fields use 2-byte
big-endian length prefixes (SASL-style TLV encoding).

### Round 1: FPLoginExt (AFP command 0x3F)

#### FPLoginExt Request

| Offset | Size | Field |
| --- | --- | --- |
| 0 | 1 | Command (0x3F = FPLoginExt) |
| 1 | 1 | Pad (0x00) |
| 2 | 2 | Flags (0x0000) |
| 4 | 1+n | AFP version (Pascal string: length byte + ASCII), e.g. `06 "AFP3.3"` |
| 5+n | 1+m | UAM name (Pascal string: length byte + ASCII), e.g. `03 "SRP"` |
| 6+n+m | 1 | Username type (0x03 = UTF-8) |
| 7+n+m | 2 | Username length |
| 9+n+m | u | Username (UTF-8 bytes) |
| 9+n+m+u | 1 | Pathname type (0x03 = UTF-8) |
| 10+n+m+u | 2 | Pathname length (0x0000 = empty) |
| 12+n+m+u | 2 | UserAuthInfo: SRP init marker (0x0001) |

The UserAuthInfo value 0x0001 signals the start of an SRP exchange.

#### FPLoginExt Response (Success)

The server returns AFP error -5001 (kFPAuthContinue) with a 413-byte payload
(for the 1536-bit group):

| Offset | Size | Field |
| --- | --- | --- |
| 0 | 2 | Transaction context (echoed from client, or server-assigned) |
| 2 | 2 | Group index (0x0002 = RFC 5054 group #2, 1536-bit) |
| 4 | 2 | N_len (0x00C0 = 192) |
| 6 | 192 | N (prime, big-endian) |
| 198 | 2 | g_len (0x0001) |
| 200 | 1 | g (0x02) |
| 201 | 2 | salt_len (0x0010 = 16) |
| 203 | 16 | salt |
| 219 | 2 | B_len (0x00C0 = 192) |
| 221 | 192 | B (server public ephemeral, big-endian) |

#### FPLoginExt Response (Unknown User)

If the username is not recognized, the server returns AFP error -5023
(kFPUserNotAuth) with a 2-byte payload:

| Offset | Size | Field |
| --- | --- | --- |
| 0 | 2 | SRP init marker (0x0001), echoed from request |

The DSI header for this response:

| Offset | Size | Field |
| --- | --- | --- |
| 0 | 1 | Flags (0x01 = reply) |
| 1 | 1 | Command (0x02 = FPLoginExt) |
| 2 | 2 | Request ID |
| 4 | 4 | Error code (0xFFFFEC61 = -5023) |
| 8 | 4 | Total data length (0x00000002) |
| 12 | 4 | Reserved (0x00000000) |

### Round 2: FPLoginCont (AFP command 0x13)

#### FPLoginCont Request

| Offset | Size | Field |
| --- | --- | --- |
| 0 | 1 | Command (0x13 = FPLoginCont) |
| 1 | 1 | Pad (0x00) |
| 2 | 2 | AFP ID (0x0000) |
| 4 | 2 | SRP step marker (0x0003) |
| 6 | 2 | A_len (0x00C0 = 192) |
| 8 | 192 | A (client public ephemeral, big-endian) |
| 200 | 2 | M1_len (0x0014 = 20) |
| 202 | 20 | M1 (client proof, SHA-1) |

#### FPLoginCont Response (Success)

AFP error 0 (kFPNoErr) with a 24-byte payload:

| Offset | Size | Field |
| --- | --- | --- |
| 0 | 2 | SRP step marker (0x0004) |
| 2 | 2 | M2_len (0x0014 = 20) |
| 4 | 20 | M2 (server proof, SHA-1) |

#### FPLoginCont Response (Authentication Failure)

If the client proof M1 is invalid - e.g. incorrect or empty password -
the server returns error -6754 with no payload.

**Note:** -6754 does *not* correspond to a standard AFP return code.

The DSI header for this response:

| Offset | Size | Field |
| --- | --- | --- |
| 0 | 1 | Flags (0x01 = reply) |
| 1 | 1 | Command (0x02 = DSICommand) |
| 2 | 2 | Request ID |
| 4 | 4 | Error code (0xFFFFE59E = -6754) |
| 8 | 4 | Total data length (0x00000000) |
| 12 | 4 | Reserved (0x00000000) |

## Cryptographic Operations

All hash operations use SHA-1 unless otherwise noted. `PAD(x)` denotes
zero-padding a big-endian integer to the byte length of the prime N (192 bytes
for the 1536-bit group). `strip(x)` denotes removing leading zero bytes from a
big-endian integer (minimum 1 byte).

### Password Verifier Input (x)

Standard RFC 2945:

    x = SHA1(salt | SHA1(username | ":" | password))

Username and password are UTF-8 encoded. No SASLprep normalization or PBKDF2
key stretching is applied.

### Client Ephemeral (A)

    a = random in [1, N-1]
    A = g^a mod N

A is transmitted as a 192-byte big-endian integer (zero-padded).

### Scrambling Parameter (u)

SRP-6a with padded inputs:

    u = SHA1(PAD(A) | PAD(B))

### Multiplier (k)

SRP-6a with padded inputs:

    k = SHA1(N | PAD(g))

N is already the full byte length of the prime. g is zero-padded to the same
length.

### Shared Secret (S)

Standard SRP client computation:

    S = (B - k * g^x mod N) ^ (a + u * x) mod N

### Session Key (K)

MGF1 mask generation function (PKCS#1 v2.1) with SHA-1, producing 40 bytes.
Leading zeros are stripped from S before input to MGF1:

    K = MGF1-SHA1(strip(S), 40)

Where MGF1 is defined as:

    MGF1(seed, length):
        output = empty
        for counter = 0, 1, 2, ...:
            output = output | SHA1(seed | I2OSP(counter, 4))
            if len(output) >= length:
                return output[0:length]

I2OSP(counter, 4) is the counter as a 4-byte big-endian integer.

### Client Proof (M1)

    M1 = SHA1(H(N) XOR H(g) | H(username) | salt | A | B | K)

Where:

- `H(N)` = `SHA1(strip(N))`
- `H(g)` = `SHA1(strip(g))` -- g as minimal bytes (0x02 for g=2)
- `H(N) XOR H(g)` = bytewise XOR of the two 20-byte digests
- `H(username)` = `SHA1(username)` -- UTF-8 bytes
- `salt` = raw salt bytes (not length-prefixed)
- `A` = `strip(A)` -- leading zeros removed
- `B` = `strip(B)` -- leading zeros removed
- `K` = all 40 bytes of the session key

### Server Proof (M2)

    M2 = SHA1(A | M1 | K)

Where A uses the same stripped representation as in M1.

The client verifies M2 to confirm the server also knows the password verifier.

## Padding Summary

The protocol uses two different padding conventions depending on context:

| Context | Padding |
| --- | --- |
| Computing u (scrambling parameter) | PAD to N length |
| Computing k (multiplier) | PAD to N length |
| Computing K (session key via MGF1) | Strip leading zeros |
| M1/M2 proof: N, g, A, B | Strip leading zeros |

## Server Advertisement

The SRP UAM is advertised in the AFP GetStatus (FPGetSrvrInfo) response as the
string "SRP" in the UAM list.

## Addendum: Unverified Edge Case in M1 / M2

This specification was reverse-engineered from packet captures of an Apple
Time Capsule (TimeCapsule8,119, AFP 3.3) and subsequently cross-checked
against the macOS Tahoe AFP client interoperating with the Netatalk
server-side implementation. Both peers agreed on every field listed above
in every exchange that was observed -- with one caveat that has not yet
been resolved by direct evidence.

For the `A` and `B` fields fed into the `M1` and `M2` SHA-1 inputs, this
spec prescribes `strip(A)` and `strip(B)` (leading zero bytes removed).
However:

- `strip(x)` and `PAD(x)` produce byte-for-byte identical inputs whenever
  the high byte of `x` is non-zero. For uniformly random `A` and `B` in
  the 1536-bit group, the high byte is zero with probability roughly
  `1/256` (~0.4%) per value.
- All exchanges captured against Time Capsule, and all exchanges observed
  between macOS Tahoe and the Netatalk server, have happened to use
  values of `A` and `B` whose high bytes were non-zero. For these
  exchanges, an implementation that fed `PAD(A)` / `PAD(B)` into M1
  instead of `strip(A)` / `strip(B)` would have produced the exact same
  M1 digest, and the protocol would have appeared to work identically.
- Therefore the choice of `strip` over `PAD` for `A` and `B` in M1/M2 is
  not yet directly verified against an Apple peer. It is the convention
  used by Tom Wu's reference SRP-6a derivation and by RFC 5054's `u` and
  `k` examples (where `PAD` is explicit), so `strip` is the more likely
  choice if Apple is following standard SRP-6a literature, but this is
  inference rather than observation.

The same ambiguity does **not** apply to `H(N)`, `H(g)`, `PAD(g)` in `k`,
`PAD(A)`/`PAD(B)` in `u`, or `strip(S)` in `K`: those formulas have either
been confirmed against the Time Capsule via differential testing, or are
unambiguous because the values they operate on do contain leading zeros
in the captured exchanges.

If a future implementation observes intermittent M1 verification failures
at roughly a 1-in-256 rate where the failing exchanges all have a leading
zero byte in either the wire-format `A` or the wire-format `B`, this
addendum is the first place to look. Resolving the ambiguity in that case
is straightforward: capture one such failing exchange, recompute M1 once
with `strip(A)` / `strip(B)` and once with `PAD(A)` / `PAD(B)`, and see
which one matches the M1 the Apple peer actually sent. The Padding
Summary table above should then be updated accordingly.

## References

- [RFC 2945: The SRP Authentication and Key Exchange System](https://tools.ietf.org/html/rfc2945)
- [RFC 5054: Using the Secure Remote Password (SRP) Protocol for TLS Authentication](https://tools.ietf.org/html/rfc5054)
- [Apple Filing Protocol Programming Guide (Apple Developer, 2012)](https://developer.apple.com/library/archive/documentation/Networking/Conceptual/AFP/Introduction/Introduction.html)
