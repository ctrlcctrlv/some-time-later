#!/bin/bash
set -x
fontforge -lang=py -script build.py
woff2_compress Some\ Time\ Later.otf
