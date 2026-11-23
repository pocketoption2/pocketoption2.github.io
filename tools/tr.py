# Build a localized copy of an English page by applying exact string replacements.
import re, sys, json
def build(src, lang, pairs, dst):
    s = open(src).read()
    s = s.replace('from "../', 'from "../../').replace('import("../', 'import("../../')
    miss = []
    for a, b in pairs:
        if a not in s: miss.append(a[:70]); continue
        s = s.replace(a, b)
    for p in ["/review/", "/demo-account/", "/app/", "/deposit-withdrawal/", "/bonus-promo-code/", "/how-to-trade/", "/faq/"]:
        s = s.replace(f'href="{p}', f'href="/{lang}{p}')
    open(dst, "w").write(s)
    if miss: print("MISSING", dst, *miss, sep="\n  ")
