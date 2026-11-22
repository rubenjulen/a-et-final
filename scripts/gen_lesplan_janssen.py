#!/usr/bin/env python3
"""Bouwt 'ICT A-ET Lesplan' in de Janssen-huisstijl (docx + pdf).

Stap 1 (eenmalig, of na wijzigingen in het lesplan-doc): python3 gen_lesplan_janssen.py --prepare
        zet de markdown-export (huisstijl/lesplan_bron_raw.md) om naar de Janssen-opbouw
        in huisstijl/lesplan_bron.md (koppen, vakbeschrijvingsmarker, figuur).
Stap 2: python3 gen_lesplan_janssen.py
        bouwt de docx, rendert naar pdf, bepaalt de paginanummers voor de inhoudsopgave
        en bouwt opnieuw met de juiste nummers.
"""
import os
import re
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from janssen_docx import JanssenDoc  # noqa: E402

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
HS = os.path.join(ROOT, "lesmateriaal", "huisstijl")
RAW = os.path.join(HS, "lesplan_bron_raw.md")
SRC = os.path.join(HS, "lesplan_bron.md")
OUT_DOCX = os.path.join(ROOT, "lesmateriaal", "ICT A-ET Lesplan.docx")
OUT_DIR = os.path.join(ROOT, "lesmateriaal")

CHAPTERS = {  # sectienummer in het doc -> hoofdstuk in Janssen-opbouw
    "2": "OPZET EN WERKWIJZE", "3": "METHODIEK", "4": "INSTRUMENTEN", "5": "WEEKOVERZICHT",
    "6": "PLANNING PER WEEK", "7": "AI-PRACTICA", "8": "BEGELEIDING EN VOORTGANG",
    "9": "TOETSING EN RAPPORT", "11": "LEEROMGEVING", "12": "PUNTEN TER AFSTEMMING",
}


def prepare():
    raw = open(RAW, encoding="utf-8").read()
    raw = raw.replace("&#91;", "[").replace("\\]", "]").replace("\\<", "<").replace("\\>", ">")
    parts = re.split(r"^## ", raw, flags=re.M)
    head, secs = parts[0], parts[1:]
    intro = [p for p in head.split("\n\n") if p.strip() and not p.startswith("#") and "@Ruben" not in p]
    out = ["# ALGEMEEN", ""]
    out += [p.replace("staan in sectie 12", "staan in het hoofdstuk Punten ter afstemming") for p in intro]
    sec10 = None
    for s in secs:
        title, _, body = s.partition("\n")
        m = re.match(r"(\d+)\.\s+(.*)", title.strip())
        body = body.strip("\n")
        body = re.sub(r"^### ", "## ", body, flags=re.M)
        body = re.sub(r"^\*\*([^*]+?)\.?\*\*\s*$", r"### \1", body, flags=re.M)   # losse vette groepskoppen
        body = body.replace("(sectie 8)", "(zie Begeleiding en voortgang)").replace("(sectie 12)", "(zie Punten ter afstemming)")
        body = re.sub(r"^\[embedded content:[^\n]*\]$", "![](lesplan_fasering.png)", body, flags=re.M)
        if m and m.group(1) == "1":
            out += ["", "## Uitgangspunten", "", body, "", "# AI & ETHICS (A-ET)", "", "<<vakbeschrijving>>"]
        elif m and m.group(1) == "10":
            sec10 = body
        elif m:
            out += ["", "# " + CHAPTERS[m.group(1)], "", body]
        else:  # Bronnen
            out += ["", "# BRONNEN", "", body]
    # toelichting studielast (tekst onder de tabel van §10) bewaren voor de vakbeschrijving
    expl = [p for p in sec10.split("\n\n") if not p.lstrip().startswith("|")]
    open(os.path.join(HS, "lesplan_studielast_toelichting.md"), "w", encoding="utf-8").write("\n\n".join(expl))
    open(SRC, "w", encoding="utf-8").write("\n".join(out).replace("\n\n\n", "\n\n") + "\n")
    print("bron geschreven:", SRC)


# ---------- vakbeschrijving A-ET (letterlijk uit de syllabus, aangevuld met de uitwerking) ----------

LEERDOELEN = [
    "**Begrijpen van ethische kwesties in AI:** studenten leren de belangrijkste ethische dilemma's die AI oproept, zoals privacy, bias en discriminatie, en de sociale impact van AI-toepassingen (kennis).",
    "**Analyseren van ethische implicaties in AI-oplossingen:** studenten ontwikkelen de vaardigheid om ethische overwegingen in hun AI-projecten te identificeren, en leren hoe ze deze kunnen aanpakken bij het ontwikkelen van AI-oplossingen (toepassing).",
    "**Integreren van ethische normen in AI-oplossingen:** studenten leren hoe ze ethische normen, zoals transparantie en verantwoording, kunnen integreren in de ontwikkeling van AI-toepassingen (toepassing).",
    "**Discussie en debatteren over ethische AI-thema's:** studenten nemen actief deel aan debatten over ethische dilemma's in AI en leren hoe ze onderbouwde standpunten innemen over ethische kwesties (oordeelsvorming).",
    "**Voorstellen voor ethische verbeteringen in AI-oplossingen:** studenten ontwikkelen voorstellen om ethische kwesties in hun AI-oplossingen aan te pakken, en presenteren deze aan experts of stakeholders (oordeelsvorming).",
]
TC = [
    ("TC1: Analyseren (niveau 3)", "Studenten kunnen ethische vraagstukken in AI identificeren en analyseren, zoals bias, privacy en de maatschappelijke impact van AI-oplossingen."),
    ("TC2: Adviseren (niveau 3)", "Studenten kunnen organisaties adviseren over het implementeren van ethische richtlijnen en normen voor AI-systemen en zorgen voor naleving van wet- en regelgeving."),
    ("TC3: Ontwerpen (niveau 3)", "Studenten kunnen AI-oplossingen ontwerpen die voldoen aan ethische normen en richtlijnen, en tegelijkertijd de effectiviteit van de oplossing waarborgen."),
    ("TC4: Realiseren (niveau 3)", "Studenten kunnen de ethische componenten van AI-oplossingen implementeren en testen, en zorgen dat deze oplossingen voldoen aan de ethische en juridische eisen."),
    ("TC5: Manage & Control (niveau 3)", "Studenten kunnen de ethische uitvoering van AI-projecten beheren, inclusief het controleren van de impact van AI-oplossingen op ethische vraagstukken en het implementeren van verbeteringen."),
]
GC = [
    ("GC1: Toekomstgericht organiseren (niveau 3)", "Studenten kunnen de ethische implicaties van AI-oplossingen beoordelen en integreren in strategische besluitvormingsprocessen voor toekomstige toepassingen van AI."),
    ("GC2: Onderzoekend probleemoplossen (niveau 3)", "Studenten gebruiken een kritische en onderzoekende benadering om ethische dilemma's in AI te identificeren, mogelijke oplossingen te analyseren en deze oplossingen te implementeren in real-world toepassingen."),
    ("GC3: Persoonlijk leiderschap (niveau 3)", "Studenten tonen leiderschap in het integreren van ethische normen in hun AI-projecten, verantwoordelijkheid nemen voor het naleven van wet- en regelgeving en actief pleiten voor ethische AI-principes."),
    ("GC4: Doelgericht interacteren (niveau 3)", "Studenten kunnen effectief en ethisch communiceren met verschillende stakeholders, zowel intern als extern, om bewustzijn te creëren over de ethische implicaties van AI-oplossingen."),
    ("GC5: Creativiteit (niveau 3)", "Studenten tonen creatief en innovatief denken door AI-oplossingen te ontwerpen die zowel technisch effectief als ethisch verantwoord zijn, en door bestaande ethische frameworks aan te passen aan nieuwe AI-uitdagingen."),
]


def comp(items):
    return "\n".join(f"• **{t}**\n  {d}" for t, d in items)


def vakbeschrijving(jd):
    jd.heading("Vakbeschrijving A-ET", 2)
    jd.label_table([
        ("Vak:", "AI & Ethics", "Vakcode:", "A-ET"),
        ("Opleiding:", "Minor AI (HBO-Bedrijfskunde/HBO-ICT)", "Studiepunten:", "3"),
        ("Studiebelasting:", "84 sbu", "Aantal colleges:", "3"),
        ("Voorkennis:", "HBO werk-en denkniveau"),
        ("Leerdoelen:", "\n".join("• " + l for l in LEERDOELEN)),
        ("Taakcompetenties:", comp(TC)),
        ("Generieke competenties:", comp(GC)),
        ("Inhoud:", "AI roept belangrijke ethische vraagstukken op. In deze module leren studenten hoe ze ethische dilemma's kunnen identificeren en aanpakken. Ze verdiepen zich in kwesties zoals privacy, transparantie en sociale impact, en leren hoe ze deze ethische normen kunnen integreren in hun AI-oplossingen.\n\n"
                    "Uitwerking: studenten beoordelen hun eigen AI-oplossing uit A-AI2 op ethiek, risico's en regelgeving, ontwerpen verbeteringen, bouwen die via A-AI2 in en testen ze. Het eindproduct beantwoordt de vraag: is deze AI-oplossing verantwoord inzetbaar, en onder welke voorwaarden?"),
        ("Werkvormen:",
         "• **Gastcollege en debat:** studenten nemen deel aan debatten over ethische kwesties in AI, ondersteund door experts uit het werkveld. De gastspreker (bijvoorbeeld uit de sectoren technologie, recht of beleid) worden door de coach uitgenodigd en gecoördineerd, zodat studenten verschillende praktijkperspectieven krijgen aangereikt. De studenten bereiden zich voor op het debat door middel van literatuur, casussen en kritische vragen.\n"
         "• **Ethiek in praktijk:** studenten analyseren de ethische implicaties van hun AI-oplossing en stellen voorstellen voor verbetering.\n"
         "• **Drie colleges en vier blokken:** drie colleges van 3 uur (week 1, 2 en 8); daartussen zelfstudie en groepswerk in vier blokken (voorbereiden, analyseren, ontwerpen, verantwoorden), elk met een kennispakket en een kennischeck. Er zijn geen online lessen.\n"
         "• **Feedback op vaste momenten:** feedforward op K1 (11 januari) en op het concept van K2 tot en met K4 (25 januari), schriftelijke feedback op Assessment 1 (18 februari) en de Design Review in college 3.\n"
         "• **AI-practica:** practicum 1 in blok 0 en practicum 4 (de eigen oplossing testen) als bewijs; practicum 2, 3 en 5 als verdieping, in Orange of Python.\n"
         "• **Design Review en peerfeedback:** in college 3 presenteert elke groep de maatregelen aan een panel; in blok 3 geven groepen elkaar feedback op het concept eindrapport."),
        ("Toetsing:",
         "**Week 5: Assessment 1 (weging 30%)**\n"
         "Inleveren tussenproduct bij docent: ethiek analyse + beschrijving aanpak. Uitwerking: op donderdag 4 februari het tussenrapport van de groep (maximaal 8 pagina's, 60%) en één individueel uitgewerkt ethisch dilemma (800 tot 1.000 woorden, 40%).\n\n"
         "**Week 10: Assessment 2 (weging 70%)**\n"
         "Ethiekanalyse en reflectie-opdracht (70%): studenten schrijven een reflectie over ethische dilemma's die ze hebben geïdentificeerd in hun AI-oplossing en hoe ze deze hebben aangepakt. Studenten leveren een eindverslag over de ethische overwegingen binnen hun AI-project en geven aan uit hoe ze ethische normen hebben geïntegreerd. Uitwerking: op donderdag 11 maart het eindrapport van de groep met beslismemo (maximaal 12 pagina's, 60%) en de individuele reflectie (1.500 tot 2.000 woorden, 40%).\n\n"
         "**Bijzonderheden**\n"
         "-Dit vak moet minimaal met een voldoende (5,5) worden beoordeeld.\n"
         "-De eindbeoordeling is individueel en wordt bepaald op basis van de gewogen resultaten.\n"
         "-Peerbeoordeling van de inzet kan het groepscijfer per student verlagen bij aantoonbaar te weinig bijdrage."),
        ("Duur:", "10 weken, met een voorbereidingsblok vanaf 14 december"),
        ("Literatuur:", "Verstrekte lesmateriaal tijdens de les: vier kennispakketten met studieteksten, kennisclips en kaderclips en casussen, het casusdossier Suribank, het voorbeeldrapport en de kaders (zie Bronnen)."),
    ])
    # studiebelasting en collegetabel, in het format van de syllabus
    jd.table([
        ["Studie activiteiten", "SBU"],
        ["Voorbereiding (Lezen over ethische concepten in AI, zoals bias, privacy, en maatschappelijke impact. Lezen van artikelen over data-ethiek, algoritmische bias en verantwoording.)\n  A-ET: blok 0 met kennispakket 0, beginquiz en practicum 1.", "4"],
        ["Colleges (groepsbijeenkomsten in aanwezigheid van de docent)\n  A-ET: drie colleges van 3 uur.", "9"],
        ["Huiswerkopdrachten (Bespreken ethische verbeteringen binnen AI-toepassingen. Analyse van gesprekken en verwerken van feedback over hoe ethische integratie kan bijdragen aan de AI-oplossing).\n  A-ET: K1 tot en met K4 en gesprekken met de partner (20), risico's, maatregelen, governance en monitoring (16), voorbereiding gastcollege en Design Review (5), practicum 4 en peerfeedback (4).", "45"],
        ["Zelfstudie (bestuderen van literatuur, reflecteren over teamrol en persoonlijke inzichten in ethische kwesties in AI, feedback in de groep.)\n  A-ET: kennispakketten 1 tot en met 3, kennischecks en reflectie in de groep.", "10"],
        ["Toets (maken en inleveren tussenopdracht, eindrapportage en reflectieverslag).\n  A-ET: Assessment 1 (7) en Assessment 2 (9).", "16"],
        ["**Uren totaal**", "**84**"],
    ], header=True, widths=[14.7, 1.8], size=10)
    expl = open(os.path.join(HS, "lesplan_studielast_toelichting.md"), encoding="utf-8").read()
    jd.markdown(expl)
    jd.table([
        ["College", "Inhoud", "Huiswerk"],
        ["1\n(7 januari)",
         "• Opening met een dilemma: een Surinaamse bank wil een kredietmodel dat sneller beslist maar aanvragers uit het binnenland vaker afwijst\n"
         "• Werkt het, mag het, is het verantwoord; ethiek, recht en compliance; lessen uit eerdere technologie\n"
         "• Echte casussen: de e-visumchatbot van BIBIS en het fraudealgoritme van Rotterdam\n"
         "• De vier ethische lenzen, met hun theorienaam, in groepjes toegepast\n"
         "• Het kader in vier lagen, de Surinaamse context, de opbouw van module en rapport\n"
         "• Groepen (zie groep A-AI1) bakenen hun eigen oplossing af als casus (K1)",
         "K1 afronden; vragen voor de gastspreker en debatstellingen voorbereiden; kennispakket 1."],
        ["2\n(14 januari)",
         "**Gastcollege en debat**\n• Gastspreker met één echte casus en vraaggesprek\n• Debat in Lagerhuisvorm over de stellingen van de groepen\n"
         "**College**\n• Minicollege: bronnen van bias, waarom perfecte eerlijkheid niet bestaat, de black box en uitlegbaarheid, privacy en verantwoording\n• Vertaling naar de eigen casus: K2, K3 en het plan voor bewijsverzameling",
         "K2 tot en met K4 en gesprekken met de partner; bevindingen uit gesprekken en interviews verwerken in het tussenproduct (Assessment 1)."],
        ["3\n(25 februari)",
         "**Interactieve feedbacksessie over de tussenresultaten**\n"
         "• Feedback op Assessment 1\n"
         "• Minicollege: veiligheid en agents, macht en regelgeving, werk en ongelijkheid, professionele praktijk\n"
         "• Design Review: elke groep presenteert de maatregelen aan een panel\n"
         "• Plan naar Assessment 2: monitoring, stopcriterium en beslismemo",
         "Feedback verwerken in de verwerkingslijst en in het voorstel voor ethische integratie (maatregelen, governance, monitoring, beslismemo); individuele reflectie."],
    ], header=True, widths=[2.4, 9.6, 4.5], size=10)


# ---------- opbouw en twee-staps inhoudsopgave ----------

def build(toc_entries):
    md = open(SRC, encoding="utf-8").read()
    jd = JanssenDoc(footer_left="Collegejaar 2026-2027 v1.0")
    jd.cover(["LESPLAN", "AI & ETHICS (A-ET)"], sub="Minor Artificial Intelligence · Collegejaar 2026-2027")
    jd.toc(toc_entries, note="Waar in dit document in de hij-vorm wordt gesproken wordt nadrukkelijk ook de zij-vorm bedoeld.")
    jd.markdown(md, base_dir=HS, hooks={"vakbeschrijving": vakbeschrijving})
    jd.save(OUT_DOCX)


def headings():
    md = open(SRC, encoding="utf-8").read()
    hs = []
    for ln in md.split("\n"):
        m = re.match(r"^(#{1,2})\s+(.*)$", ln)
        if m:
            hs.append((len(m.group(1)), m.group(2).strip()))
        if ln.strip() == "<<vakbeschrijving>>":
            hs.append((2, "Vakbeschrijving A-ET"))
    return hs


def render_pdf():
    subprocess.run(["soffice", "--headless", "--convert-to", "pdf", "--outdir", OUT_DIR, OUT_DOCX],
                   check=True, capture_output=True, timeout=240)
    return OUT_DOCX[:-5] + ".pdf"


def page_numbers(pdf, hs):
    n = int(re.search(r"Pages:\s+(\d+)", subprocess.run(["pdfinfo", pdf], capture_output=True, text=True).stdout).group(1))
    pages = [subprocess.run(["pdftotext", "-f", str(i), "-l", str(i), pdf, "-"], capture_output=True, text=True).stdout for i in range(1, n + 1)]
    norm = lambda s: re.sub(r"\s+", " ", s).strip().lower()
    res, start = [], 3            # inhoud begint na omslag en inhoudsopgave
    for lvl, text in hs:
        key = norm(re.sub(r"\*\*", "", text))
        found = None
        for i in range(start - 1, n):
            lines = [norm(l) for l in pages[i].split("\n")]
            if any(l == key or (len(key) > 25 and l.startswith(key[:40])) for l in lines):
                found = i + 1; break
        if found is None:
            raise SystemExit(f"kop niet gevonden in pdf: {text}")
        res.append((lvl, text, found)); start = found
    return res, n


def main():
    if "--prepare" in sys.argv:
        prepare(); return
    hs = headings()
    entries = [(l, t, "0") for l, t in hs]
    build(entries)
    pdf = render_pdf()
    for _ in range(2):                  # tweede ronde: paginanummers kunnen verschuiven door de toc zelf
        found, n = page_numbers(pdf, hs)
        entries = [(l, t, str(p)) for l, t, p in found]
        build(entries); pdf = render_pdf()
    check, n = page_numbers(pdf, hs)
    assert [p for *_, p in check] == [int(e[2]) for e in entries], "inhoudsopgave klopt niet"
    print(f"klaar: {OUT_DOCX} en pdf, {n} pagina's")
    for l, t, p in check:
        print(("  " if l == 2 else "") + f"{t} .... {p}")


if __name__ == "__main__":
    main()
