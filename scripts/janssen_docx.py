"""Janssen-huisstijl voor Word-documenten (python-docx).

Afgeleid van de Syllabus Minor AI 2026-2027 v1.0 (zie lesmateriaal/huisstijl/JANSSEN_HUISSTIJL.md).
Gebruik:

    from janssen_docx import JanssenDoc
    jd = JanssenDoc(footer_left="Collegejaar 2026-2027 v1.0")
    jd.cover(["LESPLAN", "AI & ETHICS (A-ET)"], sub="Minor Artificial Intelligence")
    jd.toc(entries)                      # [(niveau, tekst, pagina)], statisch
    jd.markdown(md_text, base_dir)       # koppen, alinea's, lijsten, tabellen, afbeeldingen
    jd.label_table(rows, widths)         # tabel met vetgedrukte labelkolom
    jd.save("uit.docx")

Alles in Calibri 11, donkerblauw #002060; tabelranden dun grijs #999999.
"""
import os
import re

from docx import Document
from docx.enum.section import WD_SECTION
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_BREAK, WD_TAB_ALIGNMENT, WD_TAB_LEADER
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Cm, Inches, Pt, RGBColor

NAVY = RGBColor(0x00, 0x20, 0x60)
GREY = "999999"
HERE = os.path.dirname(os.path.abspath(__file__))
LOGO = os.path.join(HERE, "..", "lesmateriaal", "huisstijl", "janssen_logo.png")


# ---------- kleine helpers ----------

def _font(run, size=None, bold=None, italic=None, color=NAVY, name="Calibri"):
    run.font.name = name
    rpr = run._element.get_or_add_rPr()
    rfonts = rpr.find(qn("w:rFonts"))
    if rfonts is None:
        rfonts = OxmlElement("w:rFonts")
        rpr.insert(0, rfonts)
    for a in ("w:ascii", "w:hAnsi", "w:cs", "w:eastAsia"):
        rfonts.set(qn(a), name)
    if size:
        run.font.size = Pt(size)
    if bold is not None:
        run.font.bold = bold
    if italic is not None:
        run.font.italic = italic
    if color is not None:
        run.font.color.rgb = color


def _field(paragraph, instr, size=9, name="Times New Roman"):
    """Voeg een Word-veld in (PAGE, NUMPAGES, ...)."""
    r = paragraph.add_run()
    _font(r, size=size, name=name)
    b = OxmlElement("w:fldChar"); b.set(qn("w:fldCharType"), "begin")
    t = OxmlElement("w:instrText"); t.set(qn("xml:space"), "preserve"); t.text = instr
    s = OxmlElement("w:fldChar"); s.set(qn("w:fldCharType"), "separate")
    v = OxmlElement("w:t"); v.text = "1"
    e = OxmlElement("w:fldChar"); e.set(qn("w:fldCharType"), "end")
    for el in (b, t, s, v, e):
        r._element.append(el)


def _cell_borders(cell, color=GREY, size=4):
    tcpr = cell._element.get_or_add_tcPr()
    borders = OxmlElement("w:tcBorders")
    for edge in ("top", "left", "bottom", "right"):
        el = OxmlElement(f"w:{edge}")
        el.set(qn("w:val"), "single"); el.set(qn("w:sz"), str(size)); el.set(qn("w:color"), color)
        borders.append(el)
    tcpr.append(borders)


def _cell_margins(table, top=40, bottom=40, left=80, right=80):
    tblpr = table._element.tblPr
    mar = OxmlElement("w:tblCellMar")
    for k, v in (("top", top), ("left", left), ("bottom", bottom), ("right", right)):
        el = OxmlElement(f"w:{k}"); el.set(qn("w:w"), str(v)); el.set(qn("w:type"), "dxa")
        mar.append(el)
    tblpr.append(mar)


def _keep_with_next(p):
    p.paragraph_format.keep_with_next = True


def _add_hyperlink(paragraph, text, url, bold=False, italic=False, size=None):
    part = paragraph.part
    r_id = part.relate_to(url, "http://schemas.openxmlformats.org/officeDocument/2006/relationships/hyperlink", is_external=True)
    h = OxmlElement("w:hyperlink"); h.set(qn("r:id"), r_id)
    r = OxmlElement("w:r"); rpr = OxmlElement("w:rPr")
    rf = OxmlElement("w:rFonts")
    for a in ("w:ascii", "w:hAnsi", "w:cs"):
        rf.set(qn(a), "Calibri")
    rpr.append(rf)
    c = OxmlElement("w:color"); c.set(qn("w:val"), "002060"); rpr.append(c)
    u = OxmlElement("w:u"); u.set(qn("w:val"), "single"); rpr.append(u)
    if bold:
        rpr.append(OxmlElement("w:b"))
    if italic:
        rpr.append(OxmlElement("w:i"))
    if size:
        sz = OxmlElement("w:sz"); sz.set(qn("w:val"), str(int(size * 2))); rpr.append(sz)
    r.append(rpr)
    t = OxmlElement("w:t"); t.text = text; t.set(qn("xml:space"), "preserve"); r.append(t)
    h.append(r)
    paragraph._p.append(h)


INLINE = re.compile(r"(\*\*[^*]+\*\*|\*[^*\s][^*]*\*|\[[^\]]+\]\([^)]+\))")


def add_inline(paragraph, text, size=11, bold=False, italic=False):
    """Zet tekst met **vet**, *cursief* en [link](url) in een alinea."""
    text = text.replace("\\<", "<").replace("\\>", ">").replace("\\[", "[").replace("\\]", "]").replace("&#91;", "[")
    for part in INLINE.split(text):
        if not part:
            continue
        if part.startswith("**") and part.endswith("**"):
            add_inline(paragraph, part[2:-2], size, True, italic)
        elif part.startswith("[") and "](" in part:
            m = re.match(r"\[([^\]]+)\]\(([^)]+)\)", part)
            _add_hyperlink(paragraph, m.group(1), m.group(2), bold, italic, size)
        elif part.startswith("*") and part.endswith("*") and len(part) > 2:
            add_inline(paragraph, part[1:-1], size, bold, True)
        else:
            r = paragraph.add_run(part)
            _font(r, size=size, bold=bold, italic=italic)


# ---------- document ----------

class JanssenDoc:
    """Een Word-document in de Janssen-huisstijl."""

    def __init__(self, footer_left="Collegejaar 2026-2027 v1.0", logo=LOGO):
        self.doc = Document()
        self.logo = logo
        sec = self.doc.sections[0]
        sec.page_width, sec.page_height = Inches(8.5), Inches(11)
        sec.left_margin = sec.right_margin = Cm(2.5)
        sec.top_margin, sec.bottom_margin = Cm(2.8), Cm(2.2)
        sec.header_distance, sec.footer_distance = Cm(1.0), Cm(1.0)
        self._styles()
        self._header_footer(sec, footer_left)

    # stijlen
    def _styles(self):
        st = self.doc.styles
        normal = st["Normal"]
        normal.font.name = "Calibri"; normal.font.size = Pt(11); normal.font.color.rgb = NAVY
        normal.element.rPr.rFonts.set(qn("w:eastAsia"), "Calibri")
        pf = normal.paragraph_format
        pf.space_before = Pt(0); pf.space_after = Pt(6); pf.line_spacing = 1.08
        for lvl, size in ((1, 16), (2, 14), (3, 11)):
            h = st[f"Heading {lvl}"]
            h.font.name = "Calibri"; h.font.size = Pt(size); h.font.bold = True; h.font.italic = False
            h.font.color.rgb = NAVY
            rpr = h.element.get_or_add_rPr()
            rf = rpr.find(qn("w:rFonts"))
            if rf is None:
                rf = OxmlElement("w:rFonts"); rpr.insert(0, rf)
            for a in ("w:ascii", "w:hAnsi", "w:cs", "w:eastAsia"):
                rf.set(qn(a), "Calibri")
            for a in ("w:asciiTheme", "w:hAnsiTheme", "w:cstheme", "w:eastAsiaTheme"):
                if rf.get(qn(a)) is not None:
                    del rf.attrib[qn(a)]
            h.paragraph_format.space_before = Pt({1: 12, 2: 12, 3: 8}[lvl])
            h.paragraph_format.space_after = Pt({1: 6, 2: 4, 3: 0}[lvl])
            h.paragraph_format.keep_with_next = True
            if lvl == 1:
                h.font.all_caps = True

    def _header_footer(self, sec, footer_left):
        hp = sec.header.paragraphs[0]
        hp.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        hp.add_run().add_picture(self.logo, width=Cm(7.0))
        fp = sec.footer.paragraphs[0]
        fp.paragraph_format.tab_stops.add_tab_stop(Cm(16.5), WD_TAB_ALIGNMENT.RIGHT)
        r = fp.add_run(footer_left); _font(r, size=9, name="Times New Roman")
        r = fp.add_run("\tPagina "); _font(r, size=9, name="Times New Roman")
        _field(fp, "PAGE")
        r = fp.add_run(" van "); _font(r, size=9, name="Times New Roman")
        _field(fp, "NUMPAGES")

    # bouwstenen
    def page_break(self):
        self.doc.add_paragraph().add_run().add_break(WD_BREAK.PAGE)

    def cover(self, lines, sub=None):
        """Omslag: titelregels gecentreerd in hoofdletters op ca. 1/3 van de pagina."""
        for _ in range(9):
            self.doc.add_paragraph()
        for i, line in enumerate(lines):
            p = self.doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p.paragraph_format.space_after = Pt(18)
            _font(p.add_run(line.upper()), size=20, bold=True)
        if sub:
            p = self.doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            _font(p.add_run(sub), size=13)
        self.page_break()

    def heading(self, text, level=1):
        h = self.doc.add_heading(level=level)
        add_inline(h, text, size={1: 16, 2: 14, 3: 11}[level], bold=True)
        return h

    def para(self, text, italic=False, align=None, size=11):
        p = self.doc.add_paragraph()
        add_inline(p, text, size=size, italic=italic)
        if align == "center":
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        return p

    def bullets(self, items, numbered=False, start=1):
        """Opsomming; items mogen **vet lead-in** bevatten. numbered=True geeft 1., 2., ..."""
        for i, it in enumerate(items):
            p = self.doc.add_paragraph()
            pf = p.paragraph_format
            pf.left_indent = Cm(0.95); pf.first_line_indent = Cm(-0.6); pf.space_after = Pt(3)
            pf.tab_stops.add_tab_stop(Cm(0.95))
            mark = f"{start + i}." if numbered else "•"
            _font(p.add_run(mark + "\t"), size=11)
            add_inline(p, it)

    def toc(self, entries, title="INHOUDSOPGAVE", note=None):
        """Statische inhoudsopgave: entries = [(niveau, tekst, paginanummer)]."""
        h = self.doc.add_paragraph(); _font(h.add_run(title), size=16, bold=True)
        h.paragraph_format.space_after = Pt(24)
        for lvl, text, page in entries:
            p = self.doc.add_paragraph()
            pf = p.paragraph_format
            pf.left_indent = Cm({1: 0, 2: 0.5, 3: 1.0}[lvl]); pf.space_after = Pt(4 if lvl == 1 else 2)
            pf.tab_stops.add_tab_stop(Cm(16.0), WD_TAB_ALIGNMENT.RIGHT, WD_TAB_LEADER.DOTS)
            _font(p.add_run(f"{text}\t{page}"), size=11 if lvl < 3 else 10, bold=(lvl == 1))
        if note:
            for _ in range(4):
                self.doc.add_paragraph()
            p = self.doc.add_paragraph(); add_inline(p, note, size=11, italic=True)
        self.page_break()

    def table(self, rows, header=True, widths=None, label_col=False, size=10):
        """Tabel met dunne grijze randen. rows = lijst van lijsten met tekst (inline opmaak mag).
        header=True: eerste rij vet; label_col=True: eerste kolom vet."""
        ncol = max(len(r) for r in rows)
        t = self.doc.add_table(rows=0, cols=ncol)
        t.alignment = WD_TABLE_ALIGNMENT.CENTER
        t.autofit = False
        _cell_margins(t)
        for ri, row in enumerate(rows):
            cells = t.add_row().cells
            for ci in range(ncol):
                txt = row[ci] if ci < len(row) else ""
                c = cells[ci]; _cell_borders(c)
                if widths:
                    c.width = Cm(widths[ci])
                self._cell_text(c, txt, size, bold=(header and ri == 0) or (label_col and ci == 0))
            if header and ri == 0:
                trpr = t.rows[ri]._tr.get_or_add_trPr()
                th = OxmlElement("w:tblHeader"); th.set(qn("w:val"), "true"); trpr.append(th)
        self.doc.add_paragraph().paragraph_format.space_after = Pt(2)
        return t

    def _cell_text(self, cell, txt, size, bold=False):
        """Celtekst; regels die met '• ' of '- ' beginnen worden opsommingstekens binnen de cel."""
        cell.paragraphs[0].paragraph_format.space_after = Pt(0)
        first = True
        for line in str(txt).split("\n"):
            p = cell.paragraphs[0] if first else cell.add_paragraph()
            first = False
            p.paragraph_format.space_after = Pt(1)
            if line.startswith(("• ", "- ")):
                p.paragraph_format.left_indent = Cm(0.5); p.paragraph_format.first_line_indent = Cm(-0.4)
                p.paragraph_format.tab_stops.add_tab_stop(Cm(0.5))
                _font(p.add_run("•\t"), size=size)
                line = line[2:]
            add_inline(p, line, size=size, bold=bold)

    def label_table(self, rows, widths=(3.4, 13.1), size=11):
        """Vakbeschrijvingstabel: rij = (label, inhoud) of (label, inhoud, label2, inhoud2)."""
        t = self.doc.add_table(rows=0, cols=4)
        t.alignment = WD_TABLE_ALIGNMENT.CENTER; t.autofit = False
        _cell_margins(t)
        w = [Cm(3.4), Cm(6.6), Cm(3.3), Cm(3.2)]
        for row in rows:
            cells = t.add_row().cells
            for c, wd in zip(cells, w):
                c.width = wd; _cell_borders(c)
            if len(row) == 4:
                self._cell_text(cells[0], row[0], size, bold=True)
                self._cell_text(cells[1], row[1], size)
                cells[2].merge(cells[3])
                self._cell_text(cells[2], f"**{row[2]}** {row[3]}" if row[3] else f"**{row[2]}**", size)
            else:
                self._cell_text(cells[0], row[0], size, bold=True)
                m = cells[1].merge(cells[2]).merge(cells[3])
                self._cell_text(m, row[1], size)
        self.doc.add_paragraph().paragraph_format.space_after = Pt(2)
        return t

    def image(self, path, width_cm=16.0, caption=None):
        p = self.doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.add_run().add_picture(path, width=Cm(width_cm))
        if caption:
            self.para(caption, italic=True, size=9)

    def markdown(self, md, base_dir=".", hooks=None):
        """Zet markdown-blokken om: # ## ### koppen, alinea's, '- ' en '1. ' lijsten,
        tabellen met |, afbeeldingen ![](pad) en hook-markers <<naam>> (hooks[naam](self))."""
        hooks = hooks or {}
        lines = md.split("\n")
        i = 0
        while i < len(lines):
            ln = lines[i].rstrip()
            if not ln.strip():
                i += 1; continue
            m = re.match(r"^<<(\w+)>>$", ln.strip())
            if m:
                hooks[m.group(1)](self); i += 1; continue
            m = re.match(r"^(#{1,3})\s+(.*)$", ln)
            if m:
                self.heading(m.group(2), len(m.group(1))); i += 1; continue
            m = re.match(r"^!\[(.*?)\]\((.+?)\)$", ln.strip())
            if m:
                self.image(os.path.join(base_dir, m.group(2)), caption=m.group(1) or None); i += 1; continue
            if ln.lstrip().startswith("|"):
                rows = []
                while i < len(lines) and lines[i].lstrip().startswith("|"):
                    cells = [c.strip() for c in lines[i].strip().strip("|").split("|")]
                    if not all(re.fullmatch(r":?-{2,}:?", c) for c in cells if c):
                        rows.append(cells)
                    i += 1
                self.table(rows, header=True)
                continue
            if re.match(r"^(- |\* )", ln):
                items = []
                while i < len(lines) and re.match(r"^(- |\* )", lines[i]):
                    items.append(re.sub(r"^(- |\* )", "", lines[i]).strip()); i += 1
                self.bullets(items); continue
            m = re.match(r"^(\d+)\.\s", ln)
            if m:
                items, start = [], int(m.group(1))
                while i < len(lines) and re.match(r"^\d+\.\s", lines[i]):
                    items.append(re.sub(r"^\d+\.\s+", "", lines[i]).strip()); i += 1
                self.bullets(items, numbered=True, start=start); continue
            para = [ln.strip()]
            i += 1
            while i < len(lines) and lines[i].strip() and not re.match(r"^(#|\||- |\* |\d+\.\s|!\[|<<)", lines[i].lstrip()):
                para.append(lines[i].strip()); i += 1
            self.para(" ".join(para))

    def save(self, path):
        self.doc.save(path)
