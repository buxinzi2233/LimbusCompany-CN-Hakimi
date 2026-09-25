# -*- coding: utf-8 -*-
import json, os, subprocess

with open("tools/translate_floor_2_b.py", "r", encoding="utf-8") as f:
    text = f.read()

# get the part up to the end of translations
# We know speaker_map starts with "speaker_map = {"
parts = text.split("speaker_map = {")
first_part = parts[0] # contains translations = { ...

# cut off from "if missing:"
first_part = first_part.split("if missing:")[0]

# Now let's extract all ("speaker", "korean"): "chinese" tuples from first_part and extra_dict
import re

# Let's import the translations dict cleanly by parsing or building it directly
