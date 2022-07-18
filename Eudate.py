#!/usr/bin/env python3

import re
import os
import shutil

datePatern = re.compile(r"""
    ^(.*?)                      # all text before the date
    ((0|1)?\d)-                 # one or two digits for the month
    ((0|1|2|3)?\d)-             # one or two digits for the day
    ((19|20)\d\d)               # four digits for the year
    (.*?)$                      # all text after the date
    """, re.ASCII | re.VERBOSE)  # '\d'会匹配Unicode中所有数字字符，不止[0-9], re.ASCII限定只匹配ASCII字符
# TODO: Loop over the files in the working directory.
for amerFilename in os.listdir("."):
    mo = datePatern.search(amerFilename)
    # TODO: Skip files without a date.
    if mo is None:
        continue
    # TODO: Get the different parts of the filename.
    beforePart = mo.group(1)
    monthPart  = mo.group(2)
    dayPart    = mo.group(4)
    yearPart   = mo.group(6)
    afterPart  = mo.group(8)
    # TODO: Form the European-style filename.
    euroFilename = beforePart + dayPart + '-' + monthPart + '-' + yearPart + afterPart
    # TODO: Get the full, absolute file paths.
    absWorkingDir = os.path.abspath('.')
    amerFilename = os.path.join(absWorkingDir, amerFilename)
    euroFilename = os.path.join(absWorkingDir, euroFilename)
    # TODO: Rename the files.
    print('Renaming "%s" to "%s"...' % (amerFilename, euroFilename))
    shutil.move(amerFilename, euroFilename) # uncomment after testing