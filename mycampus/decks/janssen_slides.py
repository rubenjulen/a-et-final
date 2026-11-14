"""Bouwstenen voor A-ET-decks in de Janssen-huisstijl (Slides-artefact, inline stijlen, 1920x1080).

Gebruik vanuit een generator per college (bijv. gen_c1.py):
    from janssen_slides import *
    S = Deck(logo='/_blob/...', footer='ICT A-ET · College 1 · donderdag 7 januari 2027', parts=[...])
    S.add('id', html, notes)
Palet (WCAG-contrast op wit / navy berekend):
    navy #002060 (15,3) · donkerblauw #2E5597 (7,3) · logoblauw #3F82BA (alleen vlakken/lijnen)
    ijsblauw #EAF0F8 · antraciet #25282A · leigrijs #5B6B7F (5,5) · goud #C8A24A (alleen op navy, 6,3)
    groen #1F7A4D (5,3) · rood #B3261E (6,5)
"""
import html as _h
import json
import os

NAVY, BLUE_T, BLUE, ICE, BG = '#002060', '#2E5597', '#3F82BA', '#EAF0F8', '#FBFCFE'
INK, MUTED, GOLD, GREEN, RED = '#25282A', '#5B6B7F', '#C8A24A', '#1F7A4D', '#B3261E'
ON_NAVY, ON_NAVY_MUTED, LINE, CARD = '#F5F8FC', '#C5D3E8', '#C9D6E8', '#FFFFFF'
FONT = "'Carlito', Calibri, 'Source Sans 3', Arial, sans-serif"
FACES = {
    'carlito': {'family': 'Carlito', 'href': 'https://fonts.googleapis.com/css2?family=Carlito:ital,wght@0,400;0,700;1,400;1,700&display=swap'},
    'source-sans-3': {'family': 'Source Sans 3', 'href': 'https://fonts.googleapis.com/css2?family=Source+Sans+3:ital,wght@0,400;0,600;0,700;1,400&display=swap'},
}


def e(t):
    """Escape platte tekst; **vet** wordt <b>."""
    t = _h.escape(t, quote=False)
    parts = t.split('**')
    return ''.join(f'<b>{p}</b>' if i % 2 else p for i, p in enumerate(parts))


def qr_svg(url, size=220, dark=NAVY, light='#FFFFFF', label='QR-code'):
    import segno
    q = segno.make(url, error='m')
    m = q.matrix
    n = len(m) + 8
    d = ''.join(f'M{x + 4} {y + 4}h1v1h-1z' for y, row in enumerate(m) for x, v in enumerate(row) if v)
    return (f'<svg aria-label="{_h.escape(label)}" viewBox="0 0 {n} {n}" width="{size}" height="{size}" '
            f'style="width:{size}px;height:{size}px;flex:none"><rect width="{n}" height="{n}" fill="{light}"/>'
            f'<path d="{d}" fill="{dark}"/></svg>')


class Deck:
    def __init__(self, logo, footer, parts):
        self.logo, self.footer, self.parts = logo, footer, parts  # parts: lijst van korte titels
        self.slides = []  # (id, html)

    # ---------- frame ----------
    def frame(self, sid, body, notes='', dark=False, part=None, bg=None, footer=True, pad='128px 128px 168px'):
        bg = bg or (NAVY if dark else BG)
        col = ON_NAVY if dark else INK
        out = [f'<section id="{sid}" data-transition="fade" style="background:{bg};color:{col};'
               f'font-family:{FONT};padding:{pad};display:flex;flex-direction:column;gap:40px">']
        out.append(body)
        if part:
            out.append(self.progress(part, dark))
        if footer:
            out.append(self.foot(dark))
        if notes:
            out.append(f'<aside>{_h.escape(notes, quote=False)}</aside>')
        out.append('</section>')
        html = '\n'.join(out)
        assert len(notes) <= 4000, (sid, len(notes))
        self.slides.append((sid, html))
        return html

    def progress(self, part, dark=False):
        n = len(self.parts)
        lab = ON_NAVY_MUTED if dark else MUTED
        on, off = (GOLD, '#33507F') if dark else (BLUE, LINE)
        bars = ''.join(f'<div style="width:44px;height:8px;border-radius:4px;background:{on if i < part else off}"></div>'
                       for i in range(n))
        return (f'<div style="position:absolute;top:52px;right:128px;width:900px;display:flex;align-items:center;'
                f'justify-content:flex-end;gap:16px"><p style="font-size:24px;font-weight:700;color:{lab};'
                f'letter-spacing:1px;text-transform:uppercase">Deel {part}/{n} · {e(self.parts[part - 1])}</p>'
                f'<div style="display:flex;gap:6px">{bars}</div></div>')

    def foot(self, dark=False):
        col = ON_NAVY_MUTED if dark else MUTED
        logo = '' if dark else f'<img src="{self.logo}" alt="Janssen University of Applied Sciences" style="width:290px;height:34px;object-fit:contain">'
        return (f'<div style="position:absolute;left:128px;bottom:52px;width:1664px;display:flex;'
                f'justify-content:space-between;align-items:center"><p style="font-size:24px;color:{col}">{e(self.footer)}</p>{logo}</div>')

    # ---------- tekstblokken ----------
    @staticmethod
    def kicker(t, dark=False, color=None):
        c = color or (GOLD if dark else BLUE_T)
        return f'<p style="font-size:26px;font-weight:700;color:{c};text-transform:uppercase;letter-spacing:2px">{e(t)}</p>'

    @staticmethod
    def h2(t, dark=False, size=64):
        c = ON_NAVY if dark else NAVY
        return f'<h2 style="font-size:{size}px;font-weight:700;line-height:1.08;color:{c}">{e(t)}</h2>'

    @staticmethod
    def p(t, size=32, color=INK, weight=400, extra=''):
        return f'<p style="font-size:{size}px;line-height:1.35;color:{color};font-weight:{weight};{extra}">{e(t)}</p>'

    @staticmethod
    def ul(items, size=30, color=INK, ordered=False):
        tag = 'ol' if ordered else 'ul'
        li = ''.join(f'<li>{e(i)}</li>' for i in items)
        return f'<{tag} style="font-size:{size}px;line-height:1.45;color:{color};padding-left:44px">{li}</{tag}>'

    @staticmethod
    def card(title, body, label=None, dark=False, accent=BLUE, size=28, flex=1, bg=None):
        bgc = bg or (NAVY if dark else CARD)
        tc, bc = (ON_NAVY, ON_NAVY_MUTED) if dark else (NAVY, INK)
        lab = f'<p style="font-size:24px;font-weight:700;color:{GOLD if dark else BLUE_T};text-transform:uppercase;letter-spacing:1px">{e(label)}</p>' if label else ''
        ttl = f'<h3 style="font-size:36px;font-weight:700;line-height:1.15;color:{tc}">{e(title)}</h3>' if title else ''
        bd = body if body.startswith('<') else f'<p style="font-size:{size}px;line-height:1.38;color:{bc}">{e(body)}</p>'
        border = '' if dark else f'border:1px solid {LINE};border-top:6px solid {accent};'
        return (f'<div style="flex:{flex};background:{bgc};{border}border-radius:14px;padding:32px 36px;'
                f'display:flex;flex-direction:column;gap:12px">{lab}{ttl}{bd}</div>')

    @staticmethod
    def row(*cols, gap=28):
        return f'<div style="display:flex;gap:{gap}px;align-items:stretch">{"".join(cols)}</div>'

    @staticmethod
    def grid(cells, cols, gap=24):
        return f'<div style="display:grid;grid-template-columns:repeat({cols}, 1fr);gap:{gap}px">{"".join(cells)}</div>'

    @staticmethod
    def klaar(t, size=30):
        return (f'<div style="background:{NAVY};border-radius:14px;padding:24px 36px;display:flex;gap:24px;align-items:baseline">'
                f'<p style="font-size:28px;font-weight:700;color:{GOLD};letter-spacing:2px;white-space:nowrap">KLAAR =</p>'
                f'<p style="font-size:{size}px;line-height:1.35;color:{ON_NAVY}">{e(t)}</p></div>')

    @staticmethod
    def statement(t, dark=False, size=40):
        c = ON_NAVY if dark else NAVY
        bar = GOLD if dark else BLUE
        return (f'<div style="border-left:8px solid {bar};padding:4px 0 4px 32px">'
                f'<p style="font-size:{size}px;line-height:1.3;font-weight:700;color:{c}">{e(t)}</p></div>')

    @staticmethod
    def werkblok(tijd, vorm):
        return (f'<div style="display:flex;gap:16px">'
                f'<p style="font-size:26px;font-weight:700;color:{ON_NAVY};background:{NAVY};border-radius:999px;padding:8px 24px">Werkblok · {e(tijd)}</p>'
                f'<p style="font-size:26px;font-weight:700;color:{NAVY};background:{ICE};border:2px solid {BLUE};border-radius:999px;padding:6px 24px">{e(vorm)}</p></div>')

    @staticmethod
    def table(head, rows, size=28, widths=None):
        w = widths or [None] * len(head)
        th = ''.join(f'<th style="background:{ICE};color:{NAVY};text-align:left;padding:12px 16px;border:1px solid {LINE};font-weight:700{";width:" + x if x else ""}">{e(h)}</th>' for h, x in zip(head, w))
        trs = ''.join('<tr>' + ''.join(
            f'<td style="padding:12px 16px;border:1px solid {LINE};vertical-align:top;color:{NAVY if i == 0 else INK};font-weight:{700 if i == 0 else 400}">{e(c)}</td>'
            for i, c in enumerate(r)) + '</tr>' for r in rows)
        return f'<table style="font-size:{size}px;line-height:1.3;border-collapse:collapse;width:100%"><tr>{th}</tr>{trs}</table>'

    # ---------- wegschrijven ----------
    def write(self, root, index_path_in, title, sections, keep):
        os.makedirs(os.path.join(root, 'project/slides'), exist_ok=True)
        for sid, html in self.slides:
            with open(os.path.join(root, f'project/slides/{sid}.html'), 'w', encoding='utf-8') as f:
                f.write(html + '\n')
        idx = json.load(open(index_path_in, encoding='utf-8'))
        idx['title'] = title
        idx['order'] = [s for s, _ in self.slides]
        idx['sections'] = sections
        idx['faces'] = FACES
        for k, v in keep.items():
            idx[k] = v
        with open(os.path.join(root, 'project/deck.json'), 'w', encoding='utf-8') as f:
            json.dump(idx, f, ensure_ascii=False, separators=(',', ':'))
        return idx
