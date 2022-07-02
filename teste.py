#!/usr/bin/env python3

import pandas as pd

df = pd.read_xml('./zeppelin-site.xml')
print(df)