"""
generate_individual_social_badges.py  --  Generates 4 separate SVG badges
(LinkedIn, Email, GitHub, Portfolio) so each button is 100% clickable in GitHub markdown.
"""
from pathlib import Path

OUT = Path(r"c:\Users\Guru\Desktop\testing")

def make_badge_svg(item_key, mode="dark"):
    dark = (mode == "dark")
    bg = "#0A101F" if dark else "#F8FAFC"
    card_bg = "#131D31" if dark else "#FFFFFF"
    card_stroke = "#22D3EE" if dark else "#0891B2"
    text_color = "#F8FAFC" if dark else "#0F172A"
    cyan = "#22D3EE" if dark else "#0891B2"

    badges = {
        "linkedin": {
            "label": "LINKEDIN",
            "icon": '<path d="M19 3a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h14m-.5 15.5v-5.3a3.26 3.26 0 0 0-3.26-3.26c-.85 0-1.84.52-2.28 1.3v-1.11h-2.79v8.37h2.79v-4.93c0-.77.62-1.4 1.39-1.4a1.4 1.4 0 0 1 1.4 1.4v4.93h2.75M6.46 10.9v8.37H9.25V10.9H6.46M7.86 6.78a1.62 1.62 0 1 0 0 3.24 1.62 1.62 0 0 0 0-3.24z" fill="' + cyan + '"/>'
        },
        "email": {
            "label": "EMAIL",
            "icon": '<path d="M20 4H4c-1.1 0-1.99.9-1.99 2L2 18c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 4l-8 5-8-5V6l8 5 8-5v2z" fill="' + cyan + '"/>'
        },
        "github": {
            "label": "GITHUB",
            "icon": '<path d="M12 2A10 10 0 0 0 2 12c0 4.42 2.87 8.17 6.84 9.5.5.08.66-.23.66-.5v-1.69c-2.77.6-3.36-1.34-3.36-1.34-.46-1.16-1.11-1.47-1.11-1.47-.91-.62.07-.6.07-.6 1 .07 1.53 1.03 1.53 1.03.87 1.52 2.34 1.07 2.91.83.1-.65.35-1.09.63-1.34-2.22-.25-4.55-1.11-4.55-4.92 0-1.11.38-2 1.03-2.71-.1-.25-.45-1.29.1-2.64 0 0 .84-.27 2.75 1.02.79-.22 1.65-.33 2.5-.33.85 0 1.71.11 2.5.33 1.91-1.29 2.75-1.02 2.75-1.02.55 1.35.2 2.39.1 2.64.65.71 1.03 1.6 1.03 2.71 0 3.82-2.34 4.66-4.57 4.91.36.31.69.92.69 1.85V21c0 .27.16.59.67.5C19.14 20.16 22 16.42 22 12A10 10 0 0 0 12 2z" fill="' + cyan + '"/>'
        },
        "portfolio": {
            "label": "PORTFOLIO",
            "icon": '<path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-1 17.93c-3.95-.49-7-3.85-7-7.93 0-.62.08-1.21.21-1.79L9 15v1c0 1.1.9 2 2 2v1.93zm6.9-2.54c-.26-.81-1-1.39-1.9-1.39h-1v-3c0-.55-.45-1-1-1H8v-2h2c.55 0 1-.45 1-1V7h2c1.1 0 2-.9 2-2v-.41c2.93 1.19 5 4.06 5 7.41 0 2.08-.8 3.97-2.1 5.39z" fill="' + cyan + '"/>'
        }
    }

    item = badges[item_key]
    w, h = 240, 48

    return f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}">
  <rect width="{w}" height="{h}" rx="8" fill="{card_bg}" stroke="{card_stroke}" stroke-width="1.5"/>
  <g transform="translate(20, 12) scale(1.0)">
    {item['icon']}
  </g>
  <text x="135" y="29" font-family="monospace" font-size="13" font-weight="bold" fill="{text_color}" text-anchor="middle" letter-spacing="2">{item['label']}</text>
</svg>'''

if __name__ == "__main__":
    for key in ["linkedin", "email", "github", "portfolio"]:
        (OUT / f"badge_{key}_dark.svg").write_text(make_badge_svg(key, "dark"), encoding="utf-8")
        (OUT / f"badge_{key}_light.svg").write_text(make_badge_svg(key, "light"), encoding="utf-8")
    print("Generated 8 individual badge SVGs (dark & light)!")
