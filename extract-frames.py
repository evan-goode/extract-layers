#!/usr/bin/env python3

import sys
from xml.dom.minidom import parse

dom = parse(sys.stdin)
print(dom)


