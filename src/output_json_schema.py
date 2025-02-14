# Copyright (c) 2025 Robert Bosch GmbH
# SPDX-License-Identifier: AGPL-3.0

from __future__ import annotations
from typing import List
from enum import Enum
from pydantic import BaseModel, Field, field_validator

class SyscallSuccess(BaseModel):
    test_values: List[int] = Field(..., description="The test values to inject as system call successful return values")

    @field_validator("test_values")
    @classmethod
    def enforce_uint64_unique(cls, v: List[int]) -> List[int]:
        seen = set()
        out: List[int] = []
        for x in v:
            if not isinstance(x, int):
                continue
            if x < 0 or x > 18446744073709551615:
                continue
            if x in seen:
                continue
            seen.add(x)
            out.append(x)

        return out

class SyscallErrorCode(BaseModel):
    error_codes: List[Errno] = Field(..., description="The error codes to inject as system call error codes")

    @field_validator("error_codes")
    @classmethod
    def enforce_errno_unique(cls, v: List[Errno]) -> List[Errno]:
        seen = set()
        out: List[Errno] = []
        for x in v:
            if not isinstance(x, Errno):
                continue
            if x in seen:
                continue
            seen.add(x)
            out.append(x)

        return out
    
class Errno(str, Enum):
    E2BIG = "E2BIG"
    EACCES = "EACCES"
    EADDRINUSE = "EADDRINUSE"
    EADDRNOTAVAIL = "EADDRNOTAVAIL"
    EADV = "EADV"
    EAFNOSUPPORT = "EAFNOSUPPORT"
    EAGAIN = "EAGAIN"
    EALREADY = "EALREADY"
    EBADE = "EBADE"
    EBADF = "EBADF"
    EBADFD = "EBADFD"
    EBADMSG = "EBADMSG"
    EBADR = "EBADR"
    EBADRQC = "EBADRQC"
    EBADSLT = "EBADSLT"
    EBFONT = "EBFONT"
    EBUSY = "EBUSY"
    ECANCELED = "ECANCELED"
    ECHILD = "ECHILD"
    ECHRNG = "ECHRNG"
    ECOMM = "ECOMM"
    ECONNABORTED = "ECONNABORTED"
    ECONNREFUSED = "ECONNREFUSED"
    ECONNRESET = "ECONNRESET"
    EDEADLOCK = "EDEADLOCK"
    EDESTADDRREQ = "EDESTADDRREQ"
    EDOM = "EDOM"
    EDOTDOT = "EDOTDOT"
    EDQUOT = "EDQUOT"
    EEXIST = "EEXIST"
    EFAULT = "EFAULT"
    EFBIG = "EFBIG"
    EHOSTDOWN = "EHOSTDOWN"
    EHOSTUNREACH = "EHOSTUNREACH"
    EIDRM = "EIDRM"
    EILSEQ = "EILSEQ"
    EINPROGRESS = "EINPROGRESS"
    EINTR = "EINTR"
    EINVAL = "EINVAL"
    EIO = "EIO"
    EISCONN = "EISCONN"
    EISDIR = "EISDIR"
    EISNAM = "EISNAM"
    EKEYEXPIRED = "EKEYEXPIRED"
    EKEYREJECTED = "EKEYREJECTED"
    EKEYREVOKED = "EKEYREVOKED"
    EL2HLT = "EL2HLT"
    EL2NSYNC = "EL2NSYNC"
    EL3HLT = "EL3HLT"
    EL3RST = "EL3RST"
    ELIBACC = "ELIBACC"
    ELIBBAD = "ELIBBAD"
    ELIBEXEC = "ELIBEXEC"
    ELIBMAX = "ELIBMAX"
    ELIBSCN = "ELIBSCN"
    ELNRNG = "ELNRNG"
    ELOOP = "ELOOP"
    EMEDIUMTYPE = "EMEDIUMTYPE"
    EMFILE = "EMFILE"
    EMLINK = "EMLINK"
    EMSGSIZE = "EMSGSIZE"
    EMULTIHOP = "EMULTIHOP"
    ENAMETOOLONG = "ENAMETOOLONG"
    ENAVAIL = "ENAVAIL"
    ENETDOWN = "ENETDOWN"
    ENETRESET = "ENETRESET"
    ENETUNREACH = "ENETUNREACH"
    ENFILE = "ENFILE"
    ENOANO = "ENOANO"
    ENOBUFS = "ENOBUFS"
    ENOCSI = "ENOCSI"
    ENODATA = "ENODATA"
    ENODEV = "ENODEV"
    ENOENT = "ENOENT"
    ENOEXEC = "ENOEXEC"
    ENOKEY = "ENOKEY"
    ENOLCK = "ENOLCK"
    ENOLINK = "ENOLINK"
    ENOMEDIUM = "ENOMEDIUM"
    ENOMEM = "ENOMEM"
    ENOMSG = "ENOMSG"
    ENONET = "ENONET"
    ENOPKG = "ENOPKG"
    ENOPROTOOPT = "ENOPROTOOPT"
    ENOSPC = "ENOSPC"
    ENOSR = "ENOSR"
    ENOSTR = "ENOSTR"
    ENOSYS = "ENOSYS"
    ENOTBLK = "ENOTBLK"
    ENOTCONN = "ENOTCONN"
    ENOTDIR = "ENOTDIR"
    ENOTEMPTY = "ENOTEMPTY"
    ENOTNAM = "ENOTNAM"
    ENOTRECOVERABLE = "ENOTRECOVERABLE"
    ENOTSOCK = "ENOTSOCK"
    ENOTSUP = "ENOTSUP"
    ENOTTY = "ENOTTY"
    ENOTUNIQ = "ENOTUNIQ"
    ENXIO = "ENXIO"
    EOVERFLOW = "EOVERFLOW"
    EOWNERDEAD = "EOWNERDEAD"
    EPERM = "EPERM"
    EPFNOSUPPORT = "EPFNOSUPPORT"
    EPIPE = "EPIPE"
    EPROTO = "EPROTO"
    EPROTONOSUPPORT = "EPROTONOSUPPORT"
    EPROTOTYPE = "EPROTOTYPE"
    ERANGE = "ERANGE"
    EREMCHG = "EREMCHG"
    EREMOTE = "EREMOTE"
    EREMOTEIO = "EREMOTEIO"
    ERESTART = "ERESTART"
    ERFKILL = "ERFKILL"
    EROFS = "EROFS"
    ESHUTDOWN = "ESHUTDOWN"
    ESOCKTNOSUPPORT = "ESOCKTNOSUPPORT"
    ESPIPE = "ESPIPE"
    ESRCH = "ESRCH"
    ESRMNT = "ESRMNT"
    ESTALE = "ESTALE"
    ESTRPIPE = "ESTRPIPE"
    ETIME = "ETIME"
    ETIMEDOUT = "ETIMEDOUT"
    ETOOMANYREFS = "ETOOMANYREFS"
    ETXTBSY = "ETXTBSY"
    EUCLEAN = "EUCLEAN"
    EUNATCH = "EUNATCH"
    EUSERS = "EUSERS"
    EXDEV = "EXDEV"
    EXFULL = "EXFULL"
