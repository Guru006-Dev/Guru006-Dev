"""
generate_banner.py  --  Pure CSS @keyframes animations for GitHub SVG rendering
"""
import base64, io, math, random
from pathlib import Path
import numpy as np
from PIL import Image, ImageOps, ImageFilter, ImageEnhance
from scipy.spatial import cKDTree

random.seed(42)
np.random.seed(42)

# ── Palette ────────────────────────────────────────────────────────────────
C_BG      = "#0A101F"
C_CHROME  = "#22D3EE"
C_CHTML   = "#0891B2"
C_PORT_D  = "#A78BFA"
C_PORT_L  = "#7C3AED"
C_MUTED   = "#94A3B8"
C_DIM     = "#64748B"
C_TEXT    = "#F8FAFC"
C_RED     = "#EF4444"

SVG_W, SVG_H = 1180, 610
PANEL_W      = int(SVG_W * 0.38)   # 448px
INFO_X       = PANEL_W + 32
COLS, ROWS   = 120, 145
DOT_R        = 1.2
PAD          = 14
OUT          = Path(r"c:\Users\Guru\Desktop\testing")
PHOTO        = OUT / "ChatGPT Image Jul 29, 2026, 12_06_33 AM No background.png"
HANDLE       = "Guru006-Dev"
EMAIL        = "dguru5079@gmail.com"

INFO_ROWS = [
    ("Subject",           "Guru.D",                  None),
    ("Role",              "Final Year CSE Student",  None),
    ("Origin",            "Vellore, Tamil Nadu",     None),
    ("Education",         "B.Tech CSE - Amrita VVP", None),
    ("Status",            "Debugging Life . One Commit at a Time", None),
    ("ToolChain",         "VS Code, Git, Docker, Figma, Playwright", None),
    None,
    ("Core.Lang",         "TypeScript, Java, Python, C, C++", None),
    ("Core.Frontend",     "React, Flutter, Vite, Tailwind", None),
    ("Core.Backend",      "Node.js, Express, Redis, Socket.io", None),
    ("Core.Database",     "MongoDB, PostgreSQL, Firebase", None),
    ("Core.Infra",        "Docker, AWS, k6, Gemini API", None),
    None,
    ("Contact",           "",                        None),
    ("Contact.Mail",      "dguru5079@gmail.com",     "mailto:dguru5079@gmail.com"),
    ("Contact.Portfolio", "coming soon",             "#"),
    ("Contact.LinkedIn",  "linkedin.com/in/gurud132", "https://www.linkedin.com/in/gurud132"),
    ("Contact.GitHub",    "@Guru006-Dev",            "https://github.com/Guru006-Dev"),
]

portrait_oy = 46.0
portrait_ox = float(PAD)
avail_w     = PANEL_W - PAD * 2
avail_h     = SVG_H - portrait_oy - 8
cell_w      = avail_w / COLS
cell_h      = avail_h / ROWS

def load_photo():
    img = Image.open(PHOTO).convert("RGB")
    w, h = img.size
    img = img.crop((0, 0, w, int(h * 0.75)))
    w2, h2 = img.size
    rt = COLS / ROWS
    rc = w2 / h2
    if rc > rt:
        nw = int(h2 * rt); l = (w2 - nw) // 2
        img = img.crop((l, 0, l + nw, h2))
    else:
        nh = int(w2 / rt); t = (h2 - nh) // 2
        img = img.crop((0, t, w2, t + nh))
    return img

img_raw = load_photo()
img_resized = img_raw.resize((COLS, ROWS), Image.LANCZOS)

img_hd = img_raw.resize((int(avail_w * 2), int(avail_h * 2)), Image.LANCZOS)
img_hd = ImageOps.autocontrast(img_hd, cutoff=1)
img_hd = ImageEnhance.Contrast(img_hd).enhance(1.15)
buf = io.BytesIO()
img_hd.save(buf, format="PNG", optimize=True)
B64_PHOTO = base64.b64encode(buf.getvalue()).decode("ascii")

def make_grey_dark(pil_img):
    g = pil_img.convert("L")
    g = ImageOps.autocontrast(g, cutoff=1)
    g = ImageEnhance.Contrast(g).enhance(1.8)
    g = g.filter(ImageFilter.UnsharpMask(radius=3, percent=160, threshold=2))
    g_arr = np.array(g, dtype=np.float32) / 255.0
    g_arr = np.power(g_arr, 0.4) * 255.0
    return g_arr.astype(np.float32)

def make_grey_light(pil_img):
    g = pil_img.filter(ImageFilter.GaussianBlur(radius=0.6)).convert("L")
    g = ImageOps.autocontrast(g, cutoff=1)
    g = ImageEnhance.Contrast(g).enhance(1.3)
    g = g.filter(ImageFilter.UnsharpMask(radius=3, percent=140, threshold=2))
    return np.array(g, dtype=np.float32)

def floyd_steinberg(grey):
    h, w = grey.shape
    buf  = grey.astype(np.float64) / 255.0
    res  = np.zeros((h, w), dtype=bool)
    ltr  = True
    for y in range(h):
        xs = range(w) if ltr else range(w - 1, -1, -1)
        for x in xs:
            old = buf[y, x]
            new = 1.0 if old > 0.5 else 0.0
            err = old - new
            res[y, x] = (new == 0.0)
            if ltr:
                if x + 1 < w:          buf[y, x + 1]     += err * 7 / 16
                if y + 1 < h:
                    if x - 1 >= 0:     buf[y + 1, x - 1] += err * 3 / 16
                    buf[y + 1, x]                         += err * 5 / 16
                    if x + 1 < w:      buf[y + 1, x + 1] += err * 1 / 16
            else:
                if x - 1 >= 0:         buf[y, x - 1]     += err * 7 / 16
                if y + 1 < h:
                    if x + 1 < w:      buf[y + 1, x + 1] += err * 3 / 16
                    buf[y + 1, x]                         += err * 5 / 16
                    if x - 1 >= 0:     buf[y + 1, x - 1] += err * 1 / 16
        ltr = not ltr
    return res

def to_xy(dither):
    r, c = np.where(dither)
    xs   = portrait_ox + (c + 0.5) * cell_w
    ys   = portrait_oy + (r + 0.5) * cell_h
    return np.column_stack([xs, ys]).astype(np.float32)

logo_cx = portrait_ox + avail_w * 0.72
logo_cy = portrait_oy + avail_h * 0.22
sc      = min(avail_w, avail_h) * 0.18

def flutter_pts(n=300):
    pts = []
    for t in np.linspace(0, 1, n // 3):
        pts.append([logo_cx + sc * (-0.5 + t), logo_cy + sc * (0.3 - 0.7 * t)])
    for t in np.linspace(0, 1, n // 3):
        pts.append([logo_cx + sc * (-0.3 + 0.7 * t), logo_cy + sc * (0.5 - 0.6 * t)])
    while len(pts) < n:
        t = random.random()
        pts.append([logo_cx + sc * (-0.4 + 0.9 * t), logo_cy + sc * (-0.2 + 0.5 * random.random())])
    return np.array(pts[:n], dtype=np.float32)

def react_pts(n=300):
    pts = []
    for ang in [0, math.pi / 3, 2 * math.pi / 3]:
        for i in range(n // 3):
            t  = 2 * math.pi * i / (n // 3)
            ex = sc * math.cos(t)
            ey = sc * 0.38 * math.sin(t)
            rx = ex * math.cos(ang) - ey * math.sin(ang)
            ry = ex * math.sin(ang) + ey * math.cos(ang)
            pts.append([logo_cx + rx, logo_cy + ry])
    while len(pts) < n:
        a = random.random() * 2 * math.pi
        r = random.random() * sc * 0.1
        pts.append([logo_cx + r * math.cos(a), logo_cy + r * math.sin(a)])
    return np.array(pts[:n], dtype=np.float32)

def node_pts(n=300):
    pts = []
    per = n // 6
    for side in range(6):
        a0 = math.pi / 6 + side * math.pi / 3
        a1 = math.pi / 6 + (side + 1) * math.pi / 3
        for i in range(per):
            t = i / per
            pts.append([
                logo_cx + sc * (math.cos(a0) * (1 - t) + math.cos(a1) * t),
                logo_cy + sc * (math.sin(a0) * (1 - t) + math.sin(a1) * t),
            ])
    while len(pts) < n:
        a = random.random() * 2 * math.pi
        r = random.random() * sc * 0.35
        pts.append([logo_cx + r * math.cos(a), logo_cy + r * math.sin(a)])
    return np.array(pts[:n], dtype=np.float32)

def ot_match(src, dst):
    _, idx = cKDTree(dst).query(src)
    return dst[idx]

def intro_groups(pts, n=60):
    idx = np.arange(len(pts))
    np.random.default_rng(42).shuffle(idx)
    grps = [[] for _ in range(n)]
    for i, d in enumerate(idx):
        grps[i % n].append(int(d))
    return grps

def dpath(xy, r=DOT_R):
    if not len(xy):
        return ""
    order = np.lexsort((xy[:, 0], xy[:, 1]))
    xy    = xy[order]
    s     = 2 * r
    return " ".join(f"M{x - r:.1f},{y - r:.1f}h{s:.1f}v{s:.1f}h-{s:.1f}z" for x, y in xy)

def info_panel(mode):
    dark   = (mode == "dark")
    cc     = C_CHROME if dark else C_CHTML
    cv     = C_TEXT   if dark else "#1E293B"
    pr     = SVG_W - 28
    lbl_x  = INFO_X
    val_x  = pr
    ldr_x  = INFO_X + 138

    lines  = [
        f'<text x="{lbl_x}" y="65" font-family="monospace" font-size="12"'
        f' fill="{cc}" font-weight="bold" letter-spacing="2">SYSTEM.INFO<tspan fill="{C_PORT_D}" class="blink-cursor">_</tspan></text>'
    ]

    y = 95
    for row in INFO_ROWS:
        if row is None:
            y += 8
            continue
        lbl, val, url = row
        if lbl == "Contact":
            lines.append(
                f'<text x="{lbl_x}" y="{y}" font-family="monospace" font-size="10"'
                f' fill="{C_DIM}">- Contact</text>'
            )
            y += 20
            continue

        if len(val) > 42:
            val = val[:41] + "..."
        dots_str = ". " * max(1, 28 - len(lbl) // 2 - len(val) // 2)
        
        row_content = (
            f'<text x="{lbl_x}" y="{y}" font-family="monospace" font-size="10.5" fill="{cc}">{lbl}</text>'
            f'<text x="{ldr_x}" y="{y}" font-family="monospace" font-size="10.5" fill="{C_DIM}" opacity="0.35">{dots_str}</text>'
            f'<text x="{val_x}" y="{y}" font-family="monospace" font-size="10.5" fill="{cv}" text-anchor="end">{val}</text>'
        )

        if url:
            lines.append(f'<a href="{url}" target="_blank" style="cursor: pointer;">{row_content}</a>')
        else:
            lines.append(row_content)
            
        y += 22

    lines.append(
        f'<text x="{lbl_x}" y="{SVG_H - 22}" font-family="monospace" font-size="10.5"'
        f' fill="{cc}">▸ More about me &amp; projects below in README ↓<tspan fill="{cc}" class="blink-cursor">_</tspan></text>'
    )
    return "\n".join(lines)

def chrome(mode):
    dark = (mode == "dark")
    cc   = C_CHROME if dark else C_CHTML
    cbg  = C_BG     if dark else "#F8FAFC"
    cf   = "#0D1A2F" if dark else "#E2EEF9"

    parts = [
        f'<rect width="{SVG_W}" height="{SVG_H}" rx="10" fill="{cbg}"'
        f' stroke="{cc}" stroke-width="1.5"/>',
        f'<rect width="{SVG_W}" height="36" rx="10" fill="{cf}"/>',
        f'<rect y="18" width="{SVG_W}" height="18" fill="{cf}"/>',
    ]

    for i, col in enumerate(["#FF5F57", "#FEBC2E", "#28C840"]):
        cx_dot = 18 + i * 22
        parts.append(f'<circle cx="{cx_dot}" cy="18" r="6" fill="{col}"/>')

    parts.append(
        f'<text x="{SVG_W // 2}" y="23" font-family="monospace" font-size="11"'
        f' fill="{C_MUTED}" text-anchor="middle">{EMAIL} - % ./profile.sh --live</text>'
    )
    parts.append(
        f'<line x1="{PANEL_W}" y1="36" x2="{PANEL_W}" y2="{SVG_H}"'
        f' stroke="{cc}" stroke-width="1" stroke-dasharray="4,4" opacity="0.35"/>'
    )
    parts.append(
        f'<text x="{PANEL_W // 2 - 140}" y="56" font-family="monospace" font-size="10"'
        f' fill="{cc}" opacity="0.6">VISUAL.MAP</text>'
    )

    bx, by, bl = 14, 44, 18
    bw = PANEL_W - 28
    bh = SVG_H - 52
    for px, py, dx, dy in [(bx, by, 1, 1), (bx + bw, by, -1, 1),
                            (bx, by + bh, 1, -1), (bx + bw, by + bh, -1, -1)]:
        parts.append(
            f'<path d="M{px},{py + dy * bl} L{px},{py} L{px + dx * bl},{py}"'
            f' fill="none" stroke="{cc}" stroke-width="1.5" opacity="0.55"/>'
        )

    # Pure CSS Animated Radar Beam
    parts.append(
        f'<line x1="14" y1="44" x2="{PANEL_W - 14}" y2="44" stroke="{cc}" stroke-width="2" class="scan-beam"/>'
    )

    lx = SVG_W - 55
    ly = 20
    # Pure CSS Animated LIVE Pulse Badge
    parts.append(
        f'<circle cx="{lx}" cy="{ly}" r="4" fill="{C_RED}" class="live-pulse"/>'
        f'<circle cx="{lx}" cy="{ly}" r="4" fill="{C_RED}"/>'
        f'<text x="{lx + 10}" y="{ly + 4}" font-family="monospace" font-size="10"'
        f' fill="{C_RED}" font-weight="bold">LIVE</text>'
    )
    return "\n".join(parts)

def make_svg(mode, pts, ig, logos_list, pcol):
    dark  = (mode == "dark")
    T     = 14.2
    intro = 3.2
    fade  = 0.6
    n_g   = len(ig)

    def kt(s):
        return f"{s / T:.4f}"

    isv = []
    for gi, mem in enumerate(ig):
        if not mem:
            continue
        tb = (gi / n_g) * (intro - fade)
        pd = dpath(pts[mem])
        if pd:
            isv.append(
                f'<path d="{pd}" fill="{pcol}" shape-rendering="crispEdges" opacity="0">'
                f'<animate attributeName="opacity" values="0;1;0.25;0.25;1" keyTimes="0;0.22;0.35;0.90;1"'
                f' dur="{T}s" repeatCount="indefinite"/>'
                f'</path>'
            )

    cx2 = portrait_ox
    cy2 = portrait_oy
    cw  = avail_w
    ch  = avail_h

    filter_id = f"dt-filter-{mode}"
    if dark:
        fe_matrix = (
            '<feColorMatrix type="matrix" values="'
            ' 0.55 0    0    0 0.04'
            ' 0.40 0    0    0 0.06'
            ' 0.85 0    0    0 0.12'
            ' 0    0    0    1 0"/>'
        )
    else:
        fe_matrix = (
            '<feColorMatrix type="matrix" values="'
            ' 0.48 0    0    0 0.10'
            ' 0.22 0    0    0 0.05'
            ' 0.90 0    0    0 0.20'
            ' 0    0    0    1 0"/>'
        )

    photo_layer = f"""
    <defs>
      <filter id="{filter_id}" x="0%" y="0%" width="100%" height="100%">
        {fe_matrix}
      </filter>
    </defs>
    <image x="{cx2:.1f}" y="{cy2:.1f}" width="{cw:.1f}" height="{ch:.1f}"
           href="data:image/png;base64,{B64_PHOTO}"
           preserveAspectRatio="xMidYMid slice"
           filter="url(#{filter_id})" opacity="0">
      <animate attributeName="opacity" values="0;0;1;1;0" keyTimes="0;0.20;0.32;0.92;1"
               dur="{T}s" repeatCount="indefinite"/>
    </image>"""

    wins = [(4.3, 6.3), (7.6, 9.6), (10.9, 12.9)]
    tsv  = []
    sp   = logos_list[0]
    for lp, (ts, te) in zip(logos_list, wins):
        m2 = ot_match(sp, lp)
        pd = dpath(m2, r=1.6)
        ok = f"0;{kt(ts - 1.3)};{kt(ts)};{kt(te)};{kt(te + 1.3)};{kt(T)}"
        ov = "0;0;1;1;0;0"
        tsv.append(
            f'<path d="{pd}" fill="{pcol}" shape-rendering="crispEdges" opacity="0">'
            f'<animate attributeName="opacity" values="{ov}" keyTimes="{ok}"'
            f' dur="{T}s" begin="0s" repeatCount="indefinite"/>'
            f'</path>'
        )
        sp = m2

    intro_str = "\n    ".join(isv)
    trav_str  = "\n    ".join(tsv)

    return f"""<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg"
     viewBox="0 0 {SVG_W} {SVG_H}" width="{SVG_W}" height="{SVG_H}"
     role="img" aria-label="Guru.D - GitHub Profile Banner">
  <style>
    @keyframes cursorBlink {{
      0%, 49% {{ opacity: 1; }}
      50%, 100% {{ opacity: 0; }}
    }}
    .blink-cursor {{
      animation: cursorBlink 0.8s infinite;
    }}
    @keyframes livePulse {{
      0%, 100% {{ transform: scale(1); opacity: 0.3; }}
      50% {{ transform: scale(2.4); opacity: 0.9; }}
    }}
    .live-pulse {{
      animation: livePulse 1.8s infinite ease-in-out;
      transform-box: fill-box;
      transform-origin: center;
    }}
    @keyframes scanBeam {{
      0% {{ transform: translateY(0px); opacity: 0.2; }}
      50% {{ opacity: 0.7; }}
      100% {{ transform: translateY(540px); opacity: 0.2; }}
    }}
    .scan-beam {{
      animation: scanBeam 4s infinite ease-in-out;
    }}
  </style>
  <defs>
    <clipPath id="pc">
      <rect x="{cx2:.1f}" y="{cy2:.1f}" width="{cw:.1f}" height="{ch:.1f}" rx="6"/>
    </clipPath>
  </defs>

  {chrome(mode)}

  {photo_layer}

  <g clip-path="url(#pc)" id="intro-dots">
    {intro_str}
  </g>

  <g clip-path="url(#pc)" id="travellers">
    {trav_str}
  </g>

  <g id="info">
    {info_panel(mode)}
  </g>
</svg>"""

if __name__ == "__main__":
    print("Generating pure CSS keyframe animated terminal banner SVGs...")
    grey_dark  = make_grey_dark(img_resized)
    grey_light = make_grey_light(img_resized)

    d_dark  = floyd_steinberg(grey_dark)
    d_light = floyd_steinberg(grey_light)

    pts_d = to_xy(d_dark)
    pts_l = to_xy(d_light)
    logos = [flutter_pts(), react_pts(), node_pts()]
    ig_d  = intro_groups(pts_d)
    ig_l  = intro_groups(pts_l)

    for mode, pts, ig, pcol, fname in [
        ("dark",  pts_d, ig_d, C_PORT_D, "hero_banner_dark.svg"),
        ("light", pts_l, ig_l, C_PORT_L, "hero_banner_light.svg"),
    ]:
        svg = make_svg(mode, pts, ig, logos, pcol)
        p   = OUT / fname
        p.write_text(svg, encoding="utf-8")
        print(f"  {fname}: {p.stat().st_size/1024:.0f} KB")
    print("Done!")
