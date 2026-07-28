#!/usr/bin/env python3
"""Rename GMMT -> GLMT and Mindset -> Lens across the PPT slides + source docs + report.
Contextual fixes for the spine/case badges (only the Mindset column's M becomes L)."""
import os, re, shutil

SLIDES = "/Users/hongyangchun/Codebase/default/outputs/gmmt-ppt/frontend/src/slides"
DOCS = "/Users/hongyangchun/Codebase/default/outputs/gmmt-ppt/docs/product"
REPORT = "/Users/hongyangchun/Codebase/default/outputs/gmmt-ppt/../GMMT模型深度解读报告.md"

# per-file contextual (after global GMMT->GLMT and Mindset->Lens)
CONTEXT = {
    "slide-4.js": [
        (">M</div>\n        <p class=\"text-lg font-bold text-[#1F3A5F] mt-1\">Lens 思维</p>",
         ">L</div>\n        <p class=\"text-lg font-bold text-[#1F3A5F] mt-1\">Lens 视角</p>"),
    ],
    "slide-5.js": [
        ("心智是方法的生成器", "视角是方法的生成器"),
    ],
    "slide-8.js": [
        ("Lens 要点", "Lens 视角"),
    ],
    "slide-9.js": [
        (">M</div><p class=\"text-sm font-bold text-[#1F3A5F] mt-1\">思维方式</p>",
         ">L</div><p class=\"text-sm font-bold text-[#1F3A5F] mt-1\">视角思维</p>"),
    ],
    "slide-10.js": [
        (">M</div><p class=\"text-sm font-bold text-[#1F3A5F] mt-1\">思维方式</p>",
         ">L</div><p class=\"text-sm font-bold text-[#1F3A5F] mt-1\">视角思维</p>"),
    ],
    "slide-12.js": [
        (">M</div><p class=\"text-xs text-[#4A4A4A] mt-1\">收集≠理解；输出倒逼输入；卡片盒。</p>",
         ">L</div><p class=\"text-xs text-[#4A4A4A] mt-1\">收集≠理解；输出倒逼输入；卡片盒。</p>"),
    ],
}

def process(path, contextual):
    with open(path, "r", encoding="utf-8") as f:
        s = f.read()
    before = s
    s = s.replace("GMMT", "GLMT")
    s = s.replace("Mindset", "Lens")
    for old, new in contextual:
        if old in s:
            s = s.replace(old, new)
        else:
            print(f"  [WARN] contextual pattern not found in {os.path.basename(path)}: {old[:40]!r}")
    if s != before:
        with open(path, "w", encoding="utf-8") as f:
            f.write(s)
        print(f"  updated {os.path.basename(path)}")
    else:
        print(f"  (no change) {os.path.basename(path)}")

print("=== slides ===")
for fn in sorted(os.listdir(SLIDES)):
    if fn.endswith(".js"):
        process(os.path.join(SLIDES, fn), CONTEXT.get(fn, []))

print("=== docs ===")
for fn in os.listdir(DOCS):
    if fn.endswith(".md"):
        process(os.path.join(DOCS, fn), [])

print("=== report (rename + GMMT->GLMT only) ===")
if os.path.exists(REPORT):
    newp = REPORT.replace("GMMT模型深度解读报告.md", "GLMT模型深度解读报告.md")
    with open(REPORT, "r", encoding="utf-8") as f:
        rs = f.read()
    rs = rs.replace("GMMT", "GLMT")
    with open(newp, "w", encoding="utf-8") as f:
        f.write(rs)
    os.remove(REPORT)
    print(f"  renamed + replaced -> {os.path.basename(newp)}")
else:
    print("  report not found at expected path")
print("DONE")
