"""
generate_projects_card.py  --  3D / Colorful logo icons for Guru006-Dev projects
Matches arifhaxn's rich custom project icon styling.
"""
from pathlib import Path

OUT = Path(r"c:\Users\Guru\Desktop\testing")

def make_projects_svg(mode="dark"):
    dark = (mode == "dark")
    bg = "#0A101F" if dark else "#F8FAFC"
    card_bg = "#131D31" if dark else "#FFFFFF"
    card_stroke = "#22D3EE" if dark else "#CBD5E1"
    card_stroke_opacity = "0.5" if dark else "1.0"
    cc = "#22D3EE" if dark else "#0891B2"
    text_color = "#F8FAFC" if dark else "#0F172A"
    muted = "#94A3B8" if dark else "#64748B"
    dim = "#64748B" if dark else "#94A3B8"
    pill_bg = "#1E293B" if dark else "#F1F5F9"
    pill_text = "#A78BFA" if dark else "#7C3AED"

    projects = [
        {
            "name": "Guru006-Dev/Pariksha",
            "title": "Pariksha",
            "desc": "Secure AI Examination &amp; Anti-Cheat Portal",
            "pills": ["React", "Node.js", "MongoDB"],
            "pct": 86,
            "pct_breakdown": "TS 86% · React 9% · CSS 5%",
            "stars": 3,
            "updated": "updated 2d ago",
            "icon_bg": "linear-gradient(135deg, #0284C7, #22D3EE)",
            "icon_color": "#22D3EE",
            "icon_svg": '''
              <defs>
                <linearGradient id="g1" x1="0%" y1="0%" x2="100%" y2="100%">
                  <stop offset="0%" stop-color="#0284C7"/>
                  <stop offset="100%" stop-color="#22D3EE"/>
                </linearGradient>
              </defs>
              <rect width="50" height="50" rx="12" fill="url(#g1)"/>
              <path d="M25 10L14 15v8c0 7.55 4.7 14.6 11 16.35 6.3-1.75 11-8.8 11-16.35v-8L25 10zm-2 21l-6-6 2.12-2.12L23 24.76l8.88-8.88L34 18l-11 13z" fill="#FFFFFF"/>
            '''
        },
        {
            "name": "Guru006-Dev/HealthHub",
            "title": "HealthHub",
            "desc": "Healthcare Telemedicine &amp; Records Platform",
            "pills": ["Flutter", "Dart", "Firebase"],
            "pct": 78,
            "pct_breakdown": "Dart 78% · C++ 12% · HTML 10%",
            "stars": 4,
            "updated": "updated 5d ago",
            "icon_color": "#A78BFA",
            "icon_svg": '''
              <defs>
                <linearGradient id="g2" x1="0%" y1="0%" x2="100%" y2="100%">
                  <stop offset="0%" stop-color="#7C3AED"/>
                  <stop offset="100%" stop-color="#A78BFA"/>
                </linearGradient>
              </defs>
              <rect width="50" height="50" rx="12" fill="url(#g2)"/>
              <path d="M34 13H16c-1.65 0-3 1.35-3 3v18c0 1.65 1.35 3 3 3h18c1.65 0 3-1.35 3-3V16c0-1.65-1.35-3-3-3zm-2 12h-5v5h-4v-5h-5v-4h5v-5h4v5h5v4z" fill="#FFFFFF"/>
            '''
        },
        {
            "name": "Guru006-Dev/SecurePass",
            "title": "SecurePass",
            "desc": "Zero-Knowledge Password Manager &amp; Vault",
            "pills": ["Python", "C++", "SQLite"],
            "pct": 92,
            "pct_breakdown": "Python 92% · C++ 5% · SQL 3%",
            "stars": 5,
            "updated": "updated 1w ago",
            "icon_color": "#10B981",
            "icon_svg": '''
              <defs>
                <linearGradient id="g3" x1="0%" y1="0%" x2="100%" y2="100%">
                  <stop offset="0%" stop-color="#059669"/>
                  <stop offset="100%" stop-color="#10B981"/>
                </linearGradient>
              </defs>
              <rect width="50" height="50" rx="12" fill="url(#g3)"/>
              <path d="M33 20h-2v-4c0-3.87-3.13-7-7-7s-7 3.13-7 7v4h-2c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h18c1.1 0 2-.9 2-2V22c0-1.1-.9-2-2-2zm-9 12c-1.66 0-3-1.34-3-3s1.34-3 3-3 3 1.34 3 3-1.34 3-3 3zm4.1-12H18.9v-4c0-2.81 2.29-5.1 5.1-5.1 2.81 0 5.1 2.29 5.1 5.1v4z" fill="#FFFFFF"/>
            '''
        },
        {
            "name": "Guru006-Dev/NitroStack",
            "title": "NitroStack",
            "desc": "High-Performance Full-Stack Starter Engine",
            "pills": ["TypeScript", "Express", "Redis"],
            "pct": 84,
            "pct_breakdown": "TS 84% · Docker 10% · JS 6%",
            "stars": 2,
            "updated": "updated 2w ago",
            "icon_color": "#F59E0B",
            "icon_svg": '''
              <defs>
                <linearGradient id="g4" x1="0%" y1="0%" x2="100%" y2="100%">
                  <stop offset="0%" stop-color="#D97706"/>
                  <stop offset="100%" stop-color="#F59E0B"/>
                </linearGradient>
              </defs>
              <rect width="50" height="50" rx="12" fill="url(#g4)"/>
              <path d="M16 11v14h5v14l13-18h-7l7-10z" fill="#FFFFFF"/>
            '''
        },
        {
            "name": "Guru006-Dev/Zoomcab",
            "title": "Zoomcab",
            "desc": "Real-time Ride Hailing &amp; Fleet Tracker",
            "pills": ["Flutter", "Node.js", "Socket.io"],
            "pct": 74,
            "pct_breakdown": "Dart 74% · JS 16% · HTML 10%",
            "stars": 2,
            "updated": "updated 3w ago",
            "icon_color": "#3B82F6",
            "icon_svg": '''
              <defs>
                <linearGradient id="g5" x1="0%" y1="0%" x2="100%" y2="100%">
                  <stop offset="0%" stop-color="#2563EB"/>
                  <stop offset="100%" stop-color="#60A5FA"/>
                </linearGradient>
              </defs>
              <rect width="50" height="50" rx="12" fill="url(#g5)"/>
              <path d="M34.84 17.02c-.34-1.01-1.29-1.72-2.42-1.72H17.58c-1.13 0-2.08.71-2.42 1.72L12 25v13c0 .92.75 1.67 1.67 1.67h1.67c.92 0 1.66-.75 1.66-1.67v-1.67h16V38c0 .92.75 1.67 1.67 1.67h1.67c.92 0 1.66-.75 1.66-1.67V25l-3.17-7.98zM18.42 18.67h13.16l1.75 5H16.67l1.75-5z" fill="#FFFFFF"/>
            '''
        },
        {
            "name": "Guru006-Dev/CareerLogic-AI",
            "title": "CareerLogic-AI",
            "desc": "AI Resume Analyzer &amp; Assessment System",
            "pills": ["React", "Python", "Gemini"],
            "pct": 88,
            "pct_breakdown": "Python 88% · TS 8% · CSS 4%",
            "stars": 6,
            "updated": "updated 1mo ago",
            "icon_color": "#EC4899",
            "icon_svg": '''
              <defs>
                <linearGradient id="g6" x1="0%" y1="0%" x2="100%" y2="100%">
                  <stop offset="0%" stop-color="#DB2777"/>
                  <stop offset="100%" stop-color="#F472B6"/>
                </linearGradient>
              </defs>
              <rect width="50" height="50" rx="12" fill="url(#g6)"/>
              <path d="M25 10l4.47 10.53L40 22l-8.68 7.53L33.94 40 25 34.07 16.06 40l2.62-10.47L10 22l10.53-1.47L25 10z" fill="#FFFFFF"/>
            '''
        }
    ]

    card_w, card_h = 570, 160
    svg_w, svg_h = 1180, 570

    cards_xml = []
    for idx, p in enumerate(projects):
        row = idx // 2
        col = idx % 2
        x = 10 + col * (card_w + 20)
        y = 55 + row * (card_h + 16)

        r = 28
        circ = 2 * 3.14159 * r
        dash = (p['pct'] / 100.0) * circ
        offset = circ - dash

        pills_xml = []
        px = 85
        for pill in p['pills']:
            pw = len(pill) * 7 + 16
            pills_xml.append(f'''
              <rect x="{px}" y="95" width="{pw}" height="20" rx="10" fill="{pill_bg}"/>
              <text x="{px + pw/2}" y="109" font-family="monospace" font-size="10" fill="{pill_text}" text-anchor="middle">{pill}</text>
            ''')
            px += pw + 8

        cards_xml.append(f'''
        <g transform="translate({x}, {y})">
          <rect width="{card_w}" height="{card_h}" rx="10" fill="{card_bg}" stroke="{card_stroke}" stroke-width="1.2" stroke-opacity="{card_stroke_opacity}"/>
          <circle cx="20" cy="22" r="3" fill="{cc}"/>
          <text x="32" y="25" font-family="monospace" font-size="11" fill="{muted}">{p['name']}</text>
          
          <!-- 3D Colorful Logo Icon -->
          <g transform="translate(20, 42)">
            {p['icon_svg']}
          </g>
          
          <text x="85" y="55" font-family="monospace" font-size="15" font-weight="bold" fill="{text_color}">{p['title']}_</text>
          <text x="85" y="75" font-family="monospace" font-size="11" fill="{muted}">{p['desc']}</text>
          
          {"".join(pills_xml)}
          
          <g transform="translate(500, 75)">
            <circle cx="0" cy="0" r="{r}" fill="none" stroke="{card_stroke}" stroke-width="6" stroke-opacity="0.3"/>
            <circle cx="0" cy="0" r="{r}" fill="none" stroke="{cc}" stroke-width="6"
                    stroke-dasharray="{circ:.1f}" stroke-dashoffset="{offset:.1f}"
                    transform="rotate(-90)"/>
            <text x="0" y="5" font-family="monospace" font-size="12" font-weight="bold" fill="{text_color}" text-anchor="middle">{p['pct']}%</text>
          </g>
          <text x="500" y="122" font-family="monospace" font-size="9" fill="{dim}" text-anchor="middle">{p['pct_breakdown']}</text>
          
          <text x="85" y="138" font-family="monospace" font-size="10" fill="{cc}">★ {p['stars']}</text>
          <text x="120" y="138" font-family="monospace" font-size="10" fill="{dim}">{p['updated']}</text>
        </g>
        ''')

    return f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {svg_w} {svg_h}" width="{svg_w}" height="{svg_h}">
  <rect width="{svg_w}" height="{svg_h}" rx="12" fill="{bg}" stroke="{cc}" stroke-width="1.5"/>
  <text x="24" y="32" font-family="monospace" font-size="14" font-weight="bold" fill="{cc}">PROJECTS.LIST</text>
  <text x="160" y="32" font-family="monospace" font-size="12" fill="{muted}">./projects.sh --all</text>
  {"".join(cards_xml)}
</svg>'''

if __name__ == "__main__":
    (OUT / "projects_dark.svg").write_text(make_projects_svg("dark"), encoding="utf-8")
    (OUT / "projects_light.svg").write_text(make_projects_svg("light"), encoding="utf-8")
    print("Generated 3D colorful projects_dark.svg and projects_light.svg!")
