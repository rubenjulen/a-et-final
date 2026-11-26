import json
cells=[]
def md(s): cells.append({"cell_type":"markdown","metadata":{},"source":s.strip('\n').splitlines(True)})
def code(s): cells.append({"cell_type":"code","metadata":{},"execution_count":None,"outputs":[],"source":s.strip('\n').splitlines(True)})
md("""
# Practicum 4: gepaarde test, grensgevallen en uitlegtest (Suribank)

AI & Ethics (A-ET), practicum 4. Dit notebook doet hetzelfde als de Orange-workflow `practicum4_suribank.ows`.

Je hebt drie bestanden nodig, in dezelfde map als dit notebook:
- `suribank_versie_A.csv` (de leerdata uit practicum 2)
- `suribank_paren.csv` (100 regioparen en 100 geslachtsparen)
- `suribank_testset.csv` (voor de grensgevallen)

Werk je met je eigen oplossing? Vervang de bestanden door die van jullie model, en pas in stap 1 de kolomnamen aan.

**Let op:** scikit-learn bouwt een beslisboom op een andere manier dan Orange. Je aantallen kunnen een paar paren verschillen van die van groepen die Orange gebruiken. Het patroon is hetzelfde.
""")
code("""
import pandas as pd
import numpy as np
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.pipeline import Pipeline, make_pipeline
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier, export_text

DOEL = "terugbetaald"     # de kolom die het model voorspelt
ID = "aanvraag_id"
leer = pd.read_csv("suribank_versie_A.csv")
paren = pd.read_csv("suribank_paren.csv")
testset = pd.read_csv("suribank_testset.csv")

kenmerken = [k for k in leer.columns if k not in (DOEL, ID)]
tekst = [k for k in kenmerken if leer[k].dtype == object]
getal = [k for k in kenmerken if k not in tekst]
print("Tekstkenmerken:", tekst)
print("Getallen:", getal)
""")
md("""
## Stap 1. Twee modellen leren

Dezelfde twee modellen als in practicum 2 en 3: logistische regressie en een beslisboom, op versie A (alle velden, ook geslacht, district en regio). Ontbrekend inkomen vullen we aan met de mediaan, zoals Kredimo doet.
""")
code("""
def voorbewerking(schalen):
    stappen = [SimpleImputer(strategy="median")] + ([StandardScaler()] if schalen else [])
    return ColumnTransformer([
        ("tekst", make_pipeline(SimpleImputer(strategy="most_frequent"), OneHotEncoder(handle_unknown="ignore")), tekst),
        ("getal", make_pipeline(*stappen), getal)], verbose_feature_names_out=False)

modellen = {
    "Logistic Regression": Pipeline([("prep", voorbewerking(schalen=True)), ("model", LogisticRegression(max_iter=1000))]),
    "Tree": Pipeline([("prep", voorbewerking(schalen=False)), ("model", DecisionTreeClassifier(min_samples_leaf=2, min_samples_split=5, random_state=0))]),
}
X, y = leer[kenmerken], leer[DOEL]
for naam, m in modellen.items():
    m.fit(X, y)
    print(naam, "geleerd")
""")
md("""
## Stap 2. De gepaarde test

Elk paar bestaat uit twee rijen: `R001-orig` en `R001-wijz`. Ze zijn gelijk, op één kenmerk na: regio (R) of geslacht (G). We kijken of het besluit verandert en hoeveel de kans op *ja* verschuift.
""")
code("""
def kans_ja(model, data):
    ja = list(model.classes_).index("ja")
    return model.predict_proba(data[kenmerken])[:, ja]

uitkomst = paren[[ID, "geslacht", "district", "regio"]].copy()
for naam, m in modellen.items():
    uitkomst[naam] = kans_ja(m, paren)

uitkomst["paar"] = uitkomst[ID].str.split("-").str[0]
uitkomst["versie"] = uitkomst[ID].str.split("-").str[1]
orig = uitkomst[uitkomst.versie == "orig"].set_index("paar")
wijz = uitkomst[uitkomst.versie == "wijz"].set_index("paar")

rijen = []
for naam in modellen:
    for soort, letter in [("regio", "R"), ("geslacht", "G")]:
        p = [k for k in orig.index if k.startswith(letter)]
        o, w = orig.loc[p, naam], wijz.loc[p, naam]
        gewisseld = ((o >= 0.5) != (w >= 0.5))
        rijen.append({"model": naam, "kenmerk": soort, "paren": len(p),
                      "ander besluit": int(gewisseld.sum()),
                      "gemiddeld verschil in kans": round(float((w - o).abs().mean()), 3),
                      "voorbeelden": ", ".join(list(gewisseld[gewisseld].index[:5]))})
samenvatting = pd.DataFrame(rijen)
samenvatting
""")
md("""
**Vraag.** Bij welk model en welk kenmerk wisselt het besluit? Wat betekent het als er *geen enkel* paar wisselt? Leg je antwoord naast de foutpercentages per regio uit practicum 2.
""")
code("""
# Waarom wisselt er bij logistische regressie (bijna) niets? Bekijk de gewichten.
lr = modellen["Logistic Regression"]
namen = lr.named_steps["prep"].get_feature_names_out()
# scikit-learn geeft de gewichten richting de tweede klasse ("nee"); we draaien ze om naar "ja".
richting = -1 if lr.classes_[1] == "nee" else 1
gewichten = pd.Series(richting * lr.named_steps["model"].coef_[0], index=namen).sort_values(key=abs, ascending=False)
print("Grootste gewichten (positief = meer kans op ja):")
print(gewichten.head(8).round(3))
print()
print("Gewichten van geslacht, district en regio:")
print(gewichten[[n for n in namen if any(s in n for s in ("geslacht", "district", "regio"))]].round(3))
""")
md("""
## Stap 3. Grensgevallen

We zoeken 10 aanvragers met een kans dicht bij 0,5. Dan verhogen we het maandinkomen met SRD 500. Hoe vaak slaat het besluit om? Is dat eerlijk tegenover de aanvrager?
""")
code("""
naam = "Logistic Regression"   # probeer ook "Tree"
m = modellen[naam]
t = testset.copy()
t["kans"] = kans_ja(m, t)
grens = t.iloc[(t["kans"] - 0.5).abs().argsort()[:10]].copy()
hoger = grens.copy()
hoger["maandinkomen_srd"] = hoger["maandinkomen_srd"] + 500
grens["kans na +500"] = kans_ja(m, hoger)
grens["omgeslagen"] = (grens["kans"] >= 0.5) != (grens["kans na +500"] >= 0.5)
grens[[ID, "regio", "maandinkomen_srd", "kans", "kans na +500", "omgeslagen"]].round(3)
""")
md("""
## Stap 4. Uitlegtest

Kies drie afgewezen aanvragers. Kun je in gewone woorden zeggen waarom het model ze afwees? Voor de beslisboom kun je de regels lezen (eerste drie lagen). Voor logistische regressie gebruik je de gewichten uit stap 2.
""")
code("""
boom = modellen["Tree"]
regels = export_text(boom.named_steps["model"], feature_names=list(boom.named_steps["prep"].get_feature_names_out()), max_depth=3)
print(regels)
""")
code("""
afgewezen = t[t["kans"] < 0.5].head(3)
afgewezen[[ID] + kenmerken + ["kans"]]
""")
md("""
## Stap 5. Opslaan voor het testlogboek

Dit schrijft `practicum4_uitkomst.csv` met per rij `aanvraag_id` en de kans op ja per model. Plak die kolommen in het tabblad **B_import** van het testlogboek. Bewaar het bestand: bij een hertest (optioneel) doen jullie dezelfde test opnieuw.
""")
code("""
uitkomst[[ID] + list(modellen)].to_csv("practicum4_uitkomst.csv", index=False)
print("Opgeslagen:", len(uitkomst), "rijen")
""")
nb={"cells":cells,"metadata":{"kernelspec":{"display_name":"Python 3","language":"python","name":"python3"},"language_info":{"name":"python"}},"nbformat":4,"nbformat_minor":5}
for i,c in enumerate(nb["cells"]): c["id"]=f"c{i:02d}"
json.dump(nb,open('out/week4/practicum4/practicum4_paren.ipynb','w',encoding='utf-8'),ensure_ascii=False,indent=1)
