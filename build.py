#!/usr/bin/env python3

import fontforge
import psMat
import unicodedata
font = fontforge.open("Some Time Later.sfd")

font.encoding = "UnicodeBMP"
font.selection.all()
font.unlinkReferences()
font.removeOverlap()
font.generate("Some Time Later.otf", flags=("opentype", "old-kern", "no-hints", "no-flex", "winkern", "omit-instructions", "no-FFTM-table"))
