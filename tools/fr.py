# Build French pages: English keys come from the RU tables in tools/<page>.py,
# French values from tools/fr_<page>.py (same order).
import sys, io, re, os, contextlib, importlib
sys.path.insert(0, "tools")
import tr
real_build = tr.build
PAGES = {"home": "index", "demo": "demo-account", "app": "app", "deposit": "deposit-withdrawal",
         "bonus": "bonus-promo-code", "howto": "how-to-trade", "review": "review", "faqp": "faq"}
NB = "\u00a0"

def keys(page):
    g = {}
    tr.build = lambda *a, **k: None
    with contextlib.redirect_stdout(io.StringIO()):
        exec(compile(open(f"tools/{page}.py").read(), page, "exec"), g)
    tr.build = real_build
    return [a for a, b in g["RU"]]

def typo(v):
    v = re.sub(r"(\d) (\d{3})\b", r"\1" + NB + r"\2", v)
    v = re.sub(r"(\d) ([$%])", r"\1" + NB + r"\2", v)
    v = re.sub(r"(\S) ([?!;:»])(?=\s|$|<|\"|')", r"\1" + NB + r"\2", v)
    v = v.replace("« ", "«" + NB)
    return v

def fit(k, v):
    lead = k[: len(k) - len(k.lstrip())]
    trail = k[len(k.rstrip()):]
    return lead + typo(v.strip()) + trail

only = sys.argv[1:] or list(PAGES)
os.makedirs("src/pages/fr", exist_ok=True)
for page in only:
    ks = keys(page)
    fr = importlib.import_module(f"fr_{page}").FR
    assert len(ks) == len(fr), (page, len(ks), len(fr))
    mod = importlib.import_module(f"fr_{page}")
    pairs = [(k, fit(k, v)) for k, v in zip(ks, fr)] + [(a, typo(b)) for a, b in getattr(mod, "EXTRA", [])]
    real_build(f"src/pages/{PAGES[page]}.astro", "fr", pairs, f"src/pages/fr/{PAGES[page]}.astro")
