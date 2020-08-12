import fontforge
import psMat
import unicodedata
font = fontforge.open("Some Time Later.sfd")

font.encoding = "UnicodeBMP"
font.selection.select(("unicode","ranges"),0xE000,0xE0FF)
font.clear()
font.selection.all()
font.unlinkReferences()
font.removeOverlap()
font.generate("Some Time Later.otf", flags=("opentype", "old-kern", "no-hints", "no-flex", "winkern", "omit-instructions"))
