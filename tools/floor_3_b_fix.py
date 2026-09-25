# -*- coding: utf-8 -*-

fixes = {
    ("", "…이젠 살만 할지도…?"): "……如今说不定值得一买……？",
    ("오티스", "군자금은 많을수록 좋다. 특히나 어떤 위협이 닥칠지 모르는 이런 변수투성이 장소에선 더더욱."): "军资素来多多益善。尤其在这等危机四伏、波诡云谲的莫测险境之中更为如是。",
    ("오티스", "역시 노련하십니다. 음…?"): "当真老练敏捷。唔……？",
    ("오티스", "이게 무슨…? 관리자님, 조심하십시오!"): "这是何等变故……？！管理者大人，小心防范！",
    ("오티스", "괜찮으십니까? 혹시 이물질이 튀진 않으셨는지…"): "您没事吧？不知可有污秽异物溅落身上……",
}

with open("tools/assemble_floor_3_b.py", "r", encoding="utf-8") as f:
    c = f.read()

# Add fixes import
if "import floor_3_b_fix as fx" not in c:
    c = c.replace("import floor_3_b_part3 as p3", "import floor_3_b_part3 as p3\nimport floor_3_b_fix as fx")
    c = c.replace("all_translations.update(p3.translations)", "all_translations.update(p3.translations)\nall_translations.update(fx.fixes)")

with open("tools/assemble_floor_3_b.py", "w", encoding="utf-8") as f:
    f.write(c)

