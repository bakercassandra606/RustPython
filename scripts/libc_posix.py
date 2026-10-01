#!/usr/bin/env python
import collections
import re
import urllib.request
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Iterator

CONSTS_PAT = re.compile(r"\b_*[A-Z]+(?:_+[A-Z]+)*_*\b")
OS_CONSTS_PAT = re.compile(r"\bos\.(_*[A-Z]+(?:_+[A-Z]+)*_*)")


LIBC_VERSION="0.2.177"


EXCLUDE = frozenset()
