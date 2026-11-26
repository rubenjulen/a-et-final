import json, shutil, os
S=''  # draaien vanuit een map met een link out -> lesmateriaal
OUT=S+'out/week9/practicum5/'
def build(cells_spec, path):
    cells=[]
    for i,(kind,src) in enumerate(cells_spec):
        c={"cell_type":kind,"metadata":{},"id":f"c{i:02d}","source":src.strip('\n').splitlines(True)}
        if kind=="code": c.update({"execution_count":None,"outputs":[]})
        cells.append(c)
    nb={"cells":cells,"metadata":{"kernelspec":{"display_name":"Python 3","language":"python","name":"python3"},"language_info":{"name":"python"}},"nbformat":4,"nbformat_minor":5}
    json.dump(nb,open(path,'w',encoding='utf-8'),ensure_ascii=False,indent=1)

PREP = '''
import os
import warnings
import pandas as pd
import numpy as np
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline, make_pipeline
from sklearn.linear_model import LogisticRegression

DOEL = "terugbetaald"   # het label: betaalde de aanvrager terug?
ID = "aanvraag_id"      # een nummer zegt niets over de aanvrager, dus dit gebruiken we niet

def lees(naam):
    """Leest een csv uit dezelfde map als dit notebook."""
    if not os.path.exists(naam):
        raise FileNotFoundError(
            f"{naam} niet gevonden. Zet de drie csv-bestanden in dezelfde map als dit notebook. "
            "Werk je in Google Colab? Draai dan eerst de cel hierboven met files.upload().")
    return pd.read_csv(naam)

def voorbewerking(kenmerken, data):
    tekst = [k for k in kenmerken if data[k].dtype == object]
    getal = [k for k in kenmerken if k not in tekst]
    return ColumnTransformer([
        ("tekst", make_pipeline(SimpleImputer(strategy="most_frequent"), OneHotEncoder(handle_unknown="ignore")), tekst),
        ("getal", SimpleImputer(strategy="mean"), getal)], verbose_feature_names_out=False)

# Zelfde instellingen als de Logistic Regression-widget in Orange: geen schaling van de getallen,
# ontbrekende getallen aangevuld met het gemiddelde, en de standaard van 100 rekenstappen.
# Daardoor krijg je (vrijwel) dezelfde getallen als medestudenten met Orange.
# Python waarschuwt dat het model niet helemaal is uitgerekend; die melding zetten we uit.
warnings.filterwarnings("ignore", category=UserWarning)
from sklearn.exceptions import ConvergenceWarning
warnings.filterwarnings("ignore", category=ConvergenceWarning)

def logistische_regressie(kenmerken, data):
    return Pipeline([("prep", voorbewerking(kenmerken, data)), ("model", LogisticRegression(max_iter=100))])
'''

cells = [
("markdown", """
# Practicum 5 (optioneel): het model een jaar later

AI & Ethics (A-ET), blok 3. Dit notebook doet dezelfde stappen als de Orange-versie in kennispakket 3. De tabellen en de vragen zijn hetzelfde.

**Ethische vraag:** wie merkt het als het model ongemerkt slechter wordt?

**Let op:** het model in dit notebook gebruikt dezelfde instellingen als de Logistic Regression-widget in Orange. Je getallen horen daarom (vrijwel) gelijk te zijn aan die van medestudenten met Orange; een verschil van één aanvraag kan voorkomen. De vragen gaan over wat je ziet, niet over het precieze getal.
"""),
("markdown", """
## Het scenario

> Dit scenario is verzonnen. Het is maart 2028. Snel Krediet draait sinds september 2026 op een logistisch regressiemodel zoals je dat in practicum 1 en 2 trainde, zonder hertraining. In de periode daarna stegen de prijzen in Suriname flink. Lonen stegen op papier mee, maar mensen konden er minder van kopen. Suribank is ook actiever klanten gaan werven in het binnenland. Inmiddels is bekend welke leningen uit die periode zijn terugbetaald.

## Bestanden

Zet deze drie bestanden in dezelfde map als dit notebook:

| Bestand | Wat het is |
| --- | --- |
| `suribank_kredietaanvragen.csv` | De 1.200 aanvragen waarop het model is getraind (uit practicum 1) |
| `suribank_2025_controle.csv` | 1.000 andere aanvragen uit dezelfde periode als de trainingsdata; het model heeft ze nooit gezien |
| `suribank_2027.csv` | 1.000 aanvragen uit de periode na de invoering |
"""),
("markdown", "**Alleen in Google Colab:** draai deze cel en kies de drie csv-bestanden. Werk je lokaal (Jupyter of VS Code), sla deze cel dan over."),
("code", '''
# Alleen in Google Colab: haal het #-teken weg voor de twee regels hieronder en draai de cel.
# from google.colab import files
# files.upload()
'''),
("markdown", "## Stap 0. Data inladen"),
("code", PREP + '''
leerdata = lees("suribank_kredietaanvragen.csv")
controle = lees("suribank_2025_controle.csv")
nieuw = lees("suribank_2027.csv")
kenmerken = [k for k in leerdata.columns if k not in (DOEL, ID)]
print(len(leerdata), "aanvragen om te leren,", len(controle), "in 2025 (controle),", len(nieuw), "in 2027")
print("Kenmerken:", kenmerken)
'''),
("markdown", """
## Deel 1: wat je meteen had kunnen zien (20 minuten)

In het echt weet je pas na een jaar of een lening is terugbetaald. Kijk daarom eerst alleen naar de **invoer**: wat aanvragers invullen op het moment dat ze aanvragen. De kolom `terugbetaald` gebruiken we in dit deel niet.
"""),
("code", '''
def invoer(d):
    return {
        "Mediaan maandinkomen (SRD)": d["maandinkomen_srd"].median(),
        "Mediaan gevraagd bedrag (SRD)": d["gevraagd_bedrag_srd"].median(),
        "Aandeel binnenland (%)": round((d["regio"] == "binnenland").mean() * 100, 1),
        "Aandeel informeel (%)": round((d["dienstverband"] == "informeel").mean() * 100, 1),
    }

pd.DataFrame({"2025 (controle)": invoer(controle), "2027": invoer(nieuw)})
'''),
("markdown", "Wil je het ook zien? Deze cel tekent het maandinkomen en het gevraagde bedrag naast elkaar, zoals de Box Plot in Orange."),
("code", '''
import matplotlib.pyplot as plt
fig, assen = plt.subplots(1, 2, figsize=(10, 4))
for as_, kolom in zip(assen, ["maandinkomen_srd", "gevraagd_bedrag_srd"]):
    as_.boxplot([controle[kolom].dropna(), nieuw[kolom].dropna()], showfliers=False)
    as_.set_xticks([1, 2])
    as_.set_xticklabels(["2025 (controle)", "2027"])
    as_.set_title(kolom)
plt.tight_layout()
plt.show()
'''),
("markdown", "**Schrijf op:** neem de vier getallen over in de tabel van deel 1 in je practicumverslag."),
("markdown", """
## Deel 2: wat er gebeurde (30 minuten)

Nu kijk je naar de uitkomsten. Je traint het model op alle 1.200 aanvragen, net als Snel Krediet deed, en test het daarna op 2025 en op 2027.
"""),
("code", '''
model = logistische_regressie(kenmerken, leerdata).fit(leerdata[kenmerken], leerdata[DOEL])
print("Model getraind op", len(leerdata), "aanvragen")
'''),
("markdown", """
Per testbestand rekenen we hetzelfde uit als in Orange:

- **CA**: het deel dat het model goed voorspelt.
- **Voorspeld "ja"**: het percentage dat het model goedkeurt.
- **Werkelijk "ja"**: het percentage dat echt terugbetaalde.
- **Onterecht goedgekeurd**: van wie *niet* terugbetaalde, het deel dat toch "ja" kreeg.
- **Onterecht afgewezen**: van wie *wel* terugbetaalde, het deel dat "nee" kreeg.
"""),
("code", '''
def uitkomsten(d):
    voorspeld = model.predict(d[kenmerken])
    echt = d[DOEL].values
    tg = int(((voorspeld == "ja") & (echt == "ja")).sum())   # terecht goedgekeurd
    og = int(((voorspeld == "ja") & (echt == "nee")).sum())  # onterecht goedgekeurd
    oa = int(((voorspeld == "nee") & (echt == "ja")).sum())  # onterecht afgewezen
    ta = int(((voorspeld == "nee") & (echt == "nee")).sum()) # terecht afgewezen
    rij = {
        "CA (%)": round((tg + ta) / len(echt) * 100, 1),
        "Voorspeld ja (%)": round((tg + og) / len(echt) * 100, 1),
        "Werkelijk ja (%)": round((tg + oa) / len(echt) * 100, 1),
        "Vakken (ja-ja / nee-ja / ja-nee / nee-nee)": f"{tg} / {og} / {oa} / {ta}",
        "Onterecht goedgekeurd (%)": round(og / (og + ta) * 100, 1),
        "Onterecht afgewezen (%)": round(oa / (oa + tg) * 100, 1),
    }
    for regio in ["kust", "binnenland"]:
        r = d["regio"].values == regio
        oa_r = int(((voorspeld == "nee") & (echt == "ja") & r).sum())
        tg_r = int(((voorspeld == "ja") & (echt == "ja") & r).sum())
        rij[f"Onterecht afgewezen, {regio} (%)"] = round(oa_r / (oa_r + tg_r) * 100, 1)
    return rij

pd.DataFrame({"2025 (controle)": uitkomsten(controle), "2027": uitkomsten(nieuw)})
'''),
("markdown", "De vakken staan als *werkelijk-voorspeld*: ja-ja is werkelijk ja en voorspeld ja, nee-ja is werkelijk nee maar voorspeld ja, enzovoort.\n\n**Schrijf op:** neem de getallen over in de tabel van deel 2 in je practicumverslag."),
("markdown", """
## Extra: per inkomensgroep

Deze cel deelt de aanvragers in vier even grote groepen naar maandinkomen in SRD (de grenzen komen uit 2025). Per groep zie je hoeveel er werd goedgekeurd en hoeveel er echt terugbetaalde. Gebruik dit bij vraag 2.
"""),
("code", '''
grenzen = controle["maandinkomen_srd"].quantile([0.25, 0.5, 0.75]).values
namen = ["laagste kwart", "tweede kwart", "derde kwart", "hoogste kwart"]

def per_inkomen(d, jaar):
    d = d.dropna(subset=["maandinkomen_srd"]).copy()
    d["inkomensgroep"] = pd.cut(d["maandinkomen_srd"], [-np.inf, *grenzen, np.inf], labels=namen)
    d["goedgekeurd"] = model.predict(d[kenmerken]) == "ja"
    d["terug"] = d[DOEL] == "ja"
    t = d.groupby("inkomensgroep", observed=False).agg(aanvragen=("terug", "size"),
                                                       goedgekeurd=("goedgekeurd", "mean"),
                                                       terugbetaald=("terug", "mean"))
    t[["goedgekeurd", "terugbetaald"]] = (t[["goedgekeurd", "terugbetaald"]] * 100).round(1)
    t.columns = pd.MultiIndex.from_product([[jaar], t.columns])
    return t

pd.concat([per_inkomen(controle, "2025 (controle)"), per_inkomen(nieuw, "2027")], axis=1)
'''),
("markdown", """
## Wat had de monitoring gezien?

Sommige getallen ken je op de dag van de aanvraag. Andere ken je pas als de leningen zijn afgelost of niet. Deze cel zet ze naast elkaar. Vergelijk het met jullie monitoringplan (K8, tabblad K8_Monitoring in het werkboek): welke indicator had al in 2027 een signaal gegeven?
"""),
("code", '''
def signalen(d):
    i, u = invoer(d), uitkomsten(d)
    return {
        "Direct zichtbaar | mediaan maandinkomen (SRD)": i["Mediaan maandinkomen (SRD)"],
        "Direct zichtbaar | aandeel binnenland (%)": i["Aandeel binnenland (%)"],
        "Direct zichtbaar | aandeel informeel (%)": i["Aandeel informeel (%)"],
        "Direct zichtbaar | goedgekeurd door het model (%)": u["Voorspeld ja (%)"],
        "Pas na een jaar | werkelijk terugbetaald (%)": u["Werkelijk ja (%)"],
        "Pas na een jaar | onterecht goedgekeurd (%)": u["Onterecht goedgekeurd (%)"],
        "Pas na een jaar | onterecht afgewezen, binnenland (%)": u["Onterecht afgewezen, binnenland (%)"],
    }

pd.DataFrame({"2025 (controle)": signalen(controle), "2027": signalen(nieuw)})
'''),
("markdown", """
## Vragen (één pagina, zoals bij elk practicum)

**Schrijf op** in je practicumverslag:

1. Welke veranderingen had Suribank in 2027 al kunnen zien, zonder te wachten op de uitkomsten? Welke indicator in jullie monitoringplan had dit opgemerkt?
2. Het model keurt in 2027 meer aanvragen goed, terwijl minder mensen hun lening terugbetalen. Hoe kan dat? Kijk naar het inkomen.
3. Het verschil in onterecht afwijzen tussen binnenland en kust is in 2027 bijna verdwenen. Is het model eerlijker geworden?
4. Wie draagt de schade als iemand onterecht een lening krijgt?
5. Je bent hoofd kredietverlening. Wat doe je, en wie moet daarover beslissen?

Sla het notebook op en lever een schermafdruk van je tabellen in bij je verslag.
"""),
]
build(cells, OUT+'practicum5.ipynb')
for f in ['out/week0/practicum1/suribank_kredietaanvragen.csv','out/week9/suribank_2025_controle.csv','out/week9/suribank_2027.csv']:
    shutil.copy(S+f, OUT)
print('ok')
