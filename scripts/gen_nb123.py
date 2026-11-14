import json, sys
def build(cells_spec, path):
    cells=[]
    for i,(kind,src) in enumerate(cells_spec):
        c={"cell_type":kind,"metadata":{},"id":f"c{i:02d}","source":src.strip('\n').splitlines(True)}
        if kind=="code": c.update({"execution_count":None,"outputs":[]})
        cells.append(c)
    nb={"cells":cells,"metadata":{"kernelspec":{"display_name":"Python 3","language":"python","name":"python3"},"language_info":{"name":"python"}},"nbformat":4,"nbformat_minor":5}
    json.dump(nb,open(path,'w',encoding='utf-8'),ensure_ascii=False,indent=1)

PREP = '''
import pandas as pd
import numpy as np
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline, make_pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier, export_text
from sklearn.dummy import DummyClassifier

DOEL = "terugbetaald"   # het label: betaalde de aanvrager terug?
ID = "aanvraag_id"      # een nummer zegt niets over de aanvrager, dus dit gebruiken we niet

def voorbewerking(kenmerken, data, schalen):
    tekst = [k for k in kenmerken if data[k].dtype == object]
    getal = [k for k in kenmerken if k not in tekst]
    stappen = [SimpleImputer(strategy="median")] + ([StandardScaler()] if schalen else [])
    return ColumnTransformer([
        ("tekst", make_pipeline(SimpleImputer(strategy="most_frequent"), OneHotEncoder(handle_unknown="ignore")), tekst),
        ("getal", make_pipeline(*stappen), getal)], verbose_feature_names_out=False)

def logistische_regressie(kenmerken, data):
    return Pipeline([("prep", voorbewerking(kenmerken, data, schalen=True)), ("model", LogisticRegression(max_iter=1000))])

def boom(kenmerken, data, diepte=None):
    return Pipeline([("prep", voorbewerking(kenmerken, data, schalen=False)),
                     ("model", DecisionTreeClassifier(max_depth=diepte, min_samples_leaf=2, min_samples_split=5, random_state=0))])

def kans_ja(model, data, kenmerken):
    ja = list(model.classes_).index("ja")
    return model.predict_proba(data[kenmerken])[:, ja]
'''

# ---------- practicum 1 ----------
p1 = [
("markdown", """
# Practicum 1: opfrisser, een model trainen en de fouten lezen

AI & Ethics (A-ET), week 0. Dit notebook doet dezelfde stappen als de Orange-versie in de weekmodule. De vragen en de evidence card zijn hetzelfde.

Je hebt `suribank_kredietaanvragen.csv` nodig, in dezelfde map als dit notebook.

**Let op:** Python rekent op een paar punten anders dan Orange, bijvoorbeeld bij het splitsen van de data en het bouwen van de boom. Je getallen kunnen daardoor iets afwijken van die van medestudenten met Orange. De vragen gaan over wat je ziet, niet over het precieze getal.
"""),
("markdown", "## Stap 1. Data inladen en het label instellen"),
("code", PREP + '''
data = pd.read_csv("suribank_kredietaanvragen.csv")
kenmerken = [k for k in data.columns if k not in (DOEL, ID)]
print(len(data), "aanvragen")
print("Kenmerken:", kenmerken)
data.head()
'''),
("markdown", "## Stap 2. Terugbetalen per groep\n\nWelk deel betaalde terug, per regio? En hoe is het soort werk per regio verdeeld?"),
("code", '''
terug = pd.crosstab(data["regio"], data[DOEL], normalize="index").round(3) * 100
print("Terugbetaald per regio (procent):")
print(terug)
print()
werk = pd.crosstab(data["regio"], data["dienstverband"], normalize="index").round(3) * 100
print("Soort werk per regio (procent):")
print(werk)
'''),
("markdown", "## Stap 3. Data splitsen\n\n70% om te leren, 30% om te testen. `stratify` zorgt dat in beide delen ongeveer evenveel terugbetalers zitten, net als in Orange. `random_state=7` legt vast welke aanvragers in welk deel komen, zodat je bij opnieuw draaien dezelfde uitkomst krijgt."),
("code", '''
from sklearn.model_selection import train_test_split
leer, test = train_test_split(data, train_size=0.7, stratify=data[DOEL], random_state=7)
print(len(leer), "om te leren,", len(test), "om te testen, waarvan", (test[DOEL] == "ja").sum(), "terugbetaald")
'''),
("markdown", "## Stap 4. Drie modellen\n\nLogistische regressie, een beslisboom, en Constant: een model dat altijd het antwoord geeft dat het vaakst voorkomt. Dat is je ondergrens."),
("code", '''
modellen = {
    "Logistic Regression": logistische_regressie(kenmerken, data),
    "Tree": boom(kenmerken, data),
    "Constant": Pipeline([("prep", voorbewerking(kenmerken, data, schalen=False)), ("model", DummyClassifier(strategy="most_frequent"))]),
}
for naam, m in modellen.items():
    m.fit(leer[kenmerken], leer[DOEL])
print("Drie modellen geleerd")
'''),
("markdown", "## Stap 5 en 6. Testen en de verwarringsmatrix\n\nCA is het deel dat het model goed voorspelt. De vier vakken laten zien welke fouten het model maakt. Precisie: van alle goedgekeurde aanvragen, welk deel betaalde terug? Recall: van alle goede betalers, welk deel werd goedgekeurd?"),
("code", '''
rijen = []
for naam, m in modellen.items():
    voorspeld = m.predict(test[kenmerken])
    echt = test[DOEL].values
    tg = int(((voorspeld == "ja") & (echt == "ja")).sum())   # terecht goedgekeurd
    og = int(((voorspeld == "ja") & (echt == "nee")).sum())  # onterecht goedgekeurd
    oa = int(((voorspeld == "nee") & (echt == "ja")).sum())  # onterecht afgewezen
    ta = int(((voorspeld == "nee") & (echt == "nee")).sum()) # terecht afgewezen
    rijen.append({"model": naam, "CA": round((tg + ta) / len(echt) * 100, 1),
                  "terecht goedgekeurd": tg, "onterecht goedgekeurd": og,
                  "onterecht afgewezen": oa, "terecht afgewezen": ta,
                  "precisie ja": round(tg / (tg + og) * 100, 1) if tg + og else None,
                  "recall ja": round(tg / (tg + oa) * 100, 1)})
pd.DataFrame(rijen).set_index("model")
'''),
("markdown", "## Stap 7. Twijfelgevallen\n\nDe kans op *ja* per testaanvraag, volgens logistische regressie. We tonen de aanvragen met een kans dicht bij 50%."),
("code", '''
lr = modellen["Logistic Regression"]
t = test.copy()
t["kans op ja"] = kans_ja(lr, t, kenmerken).round(3)
twijfel = t.iloc[(t["kans op ja"] - 0.5).abs().argsort()[:8]]
twijfel[[ID, "regio", "dienstverband", "maandinkomen_srd", "gevraagd_bedrag_srd", "looptijd_maanden", "kans op ja", DOEL]]
'''),
("markdown", "## Extra bij vraag 6. District en regio weglaten\n\nWat gebeurt er als het model district en regio niet meer krijgt? Kijk naar de CA, en denk aan je antwoord op vraag 1. In practicum 2 (week 3) meet je de fouten per regio."),
("code", '''
zonder = [k for k in kenmerken if k not in ("district", "regio")]
lr2 = logistische_regressie(zonder, data).fit(leer[zonder], leer[DOEL])
print("CA met district en regio:   ", round((lr.predict(test[kenmerken]) == test[DOEL]).mean() * 100, 1), "%")
print("CA zonder district en regio:", round((lr2.predict(test[zonder]) == test[DOEL]).mean() * 100, 1), "%")
'''),
("markdown", "## Extra. Hoe stabiel is dit?\n\nDe uitkomst hangt af van welke aanvragers toevallig in de testset komen. Hieronder splitsen we tien keer anders en kijken we naar het gemiddelde en de spreiding. Wat betekent dit voor een organisatie die zegt: \"ons model haalt 70%\"?"),
("code", '''
uitkomsten = []
for seed in range(10):
    l, t = train_test_split(data, train_size=0.7, stratify=data[DOEL], random_state=seed)
    for naam, maak in [("Logistic Regression", lambda: logistische_regressie(kenmerken, data)), ("Tree", lambda: boom(kenmerken, data))]:
        m = maak().fit(l[kenmerken], l[DOEL])
        uitkomsten.append({"model": naam, "CA": (m.predict(t[kenmerken]) == t[DOEL]).mean() * 100})
pd.DataFrame(uitkomsten).groupby("model")["CA"].agg(["mean", "min", "max"]).round(1)
'''),
("markdown", """
## Stap 8. Opslaan en vragen

Sla het notebook op. Beantwoord de zeven vragen uit de weekmodule en vul evidence card 1 in. Lever een schermafdruk van je notebook in.

1. Welk deel van de aanvragers betaalde terug aan de kust, en welk deel in het binnenland? Hoe verschilt het soort werk tussen de twee regio's?
2. Welk deel van de testaanvragen voorspelt elk model goed (CA)? Hoeveel procentpunt zijn Tree en Logistic Regression beter dan Constant?
3. Vul voor Logistic Regression de vier vakken in.
4. Welk model wijst meer goede betalers onterecht af? Welk model zou de bank kiezen, en welk model zouden aanvragers kiezen? Gebruik precisie en recall.
5. Zoek een aanvraag met een kans rond 50%. Wat zou jij als bank met deze aanvraag doen, en wie zou erover moeten beslissen?
6. Stel dat de bank district en regio weglaat. Is het risico op ongelijke behandeling van mensen uit het binnenland dan weg?
7. Denk aan jullie eigen oplossing uit A-AI1 en A-AI2. Welke fout kan die maken, en wie merkt de gevolgen?
"""),
]

# ---------- practicum 2 en 3 ----------
p23 = [
("markdown", """
# Practicum 2 en 3: fouten per groep en uitlegbaarheid

AI & Ethics (A-ET), week 3. Dit notebook doet dezelfde stappen als de Orange-versie in de weekmodule. Deel 1 is practicum 2 (het bias-experiment), deel 2 is practicum 3 (uitlegbaarheid).

Je hebt drie bestanden nodig, in dezelfde map als dit notebook: `suribank_versie_A.csv`, `suribank_versie_B.csv` en `suribank_testset.csv`.

**Het verhaal achter versie B.** Tot 2022 werden betalingen van klanten uit het binnenland via het kantoor in Albina met de hand ingeboekt. Een deel van de klanten die gewoon betaalden, staat daardoor in de historische data als wanbetaler. Versie B bevat die scheve labels. De testset bevat de echte uitkomsten.

**Let op:** Python rekent op een paar punten anders dan Orange. Je getallen kunnen iets afwijken. Het patroon bij practicum 2 is hetzelfde. Bij practicum 3 scoort logistische regressie in Python hoger dan in Orange; de les blijft: de lange boom doet het slechter dan de korte, en de korte boom is bijna even goed en wel te begrijpen.
"""),
("code", PREP + '''
versie_A = pd.read_csv("suribank_versie_A.csv")
versie_B = pd.read_csv("suribank_versie_B.csv")
testset = pd.read_csv("suribank_testset.csv")
alle_kenmerken = [k for k in versie_A.columns if k not in (DOEL, ID)]
GEVOELIG = ["geslacht", "district", "regio"]
print(len(versie_A), "aanvragen om te leren,", len(testset), "om te testen")
'''),
("markdown", """
## Deel 1. Practicum 2: het bias-experiment

We leren logistische regressie op de leerdata en testen apart voor de kust en het binnenland. Per regio rekenen we uit:

- **Goedgekeurd:** voorspeld ja, gedeeld door het totaal.
- **Onterecht afgewezen:** goede betalers met voorspelling nee, gedeeld door alle goede betalers.
- **Onterecht goedgekeurd:** slechte betalers met voorspelling ja, gedeeld door alle slechte betalers.
"""),
("code", '''
def per_regio(leerdata, kenmerken, naam):
    m = logistische_regressie(kenmerken, leerdata).fit(leerdata[kenmerken], leerdata[DOEL])
    rijen = []
    for regio in ["kust", "binnenland"]:
        t = testset[testset["regio"] == regio]
        v = m.predict(t[kenmerken]); e = t[DOEL].values
        rijen.append({"versie": naam, "regio": regio,
                      "CA": round((v == e).mean() * 100, 1),
                      "goedgekeurd": round((v == "ja").mean() * 100, 1),
                      "onterecht afgewezen": round(((v == "nee") & (e == "ja")).sum() / (e == "ja").sum() * 100, 1),
                      "onterecht goedgekeurd": round(((v == "ja") & (e == "nee")).sum() / (e == "nee").sum() * 100, 1)})
    return rijen
'''),
("markdown", "### Stap 1 tot en met 4. Versie A"),
("code", '''
tabel = per_regio(versie_A, alle_kenmerken, "A")
pd.DataFrame(tabel)
'''),
("markdown", "### Stap 5. Versie B, met de scheve labels"),
("code", '''
tabel += per_regio(versie_B, alle_kenmerken, "B")
pd.DataFrame(tabel)
'''),
("markdown", "### Stap 6. Versie B zonder gevoelige kenmerken\n\nGeslacht, district en regio gaan eruit, net als met Select Columns in Orange."),
("code", '''
zonder = [k for k in alle_kenmerken if k not in GEVOELIG]
tabel += per_regio(versie_B, zonder, "B zonder gevoelige kenmerken")
uitkomst2 = pd.DataFrame(tabel)
uitkomst2
'''),
("markdown", """
### Vragen bij practicum 2

1. Versie A: hoe groot is het verschil in onterecht afwijzen tussen kust en binnenland? Waar komt dat verschil vandaan, als woonplaats in deze data geen directe rol speelt bij terugbetalen?
2. Versie B: wat gebeurt er met goede betalers uit het binnenland? Wat gebeurt er met de CA voor het binnenland? Hoe kan dat?
3. Zonder gevoelige kenmerken: wat verandert er? Waarom kom je niet terug op het niveau van versie A?
4. Wie is verantwoordelijk voor het verschil: de bank die de data vastlegde, de leverancier die alle velden gebruikte, of de bank die niet per groep testte? Gebruik minstens één ethische lens.
5. Wat zou jij van Suribank eisen voordat zo'n model live mag? Formuleer één eis die je kunt controleren.

Vul daarna evidence card 2 in.
"""),
("markdown", """
## Deel 2. Practicum 3: uitlegbaarheid

### Stap 1 en 2. Drie modellen vergelijken

We leren op versie A, zonder geslacht, district en regio: een korte boom (3 niveaus), een lange boom en logistische regressie.
"""),
("code", '''
k = [x for x in alle_kenmerken if x not in GEVOELIG]
modellen3 = {
    "Korte boom (3 niveaus)": boom(k, versie_A, diepte=3),
    "Lange boom": boom(k, versie_A),
    "Logistic Regression": logistische_regressie(k, versie_A),
}
rijen = []
for naam, m in modellen3.items():
    m.fit(versie_A[k], versie_A[DOEL])
    ca = (m.predict(testset[k]) == testset[DOEL]).mean() * 100
    rijen.append({"model": naam, "CA op de testset": round(ca, 1),
                  "eindpunten": m.named_steps["model"].get_n_leaves() if "boom" in naam else None})
pd.DataFrame(rijen).set_index("model")
'''),
("markdown", "### Stap 3. In de korte boom kijken\n\nLees de regels van boven naar beneden. `class: ja` betekent: het model voorspelt terugbetalen."),
("code", '''
korte = modellen3["Korte boom (3 niveaus)"]
print(export_text(korte.named_steps["model"], feature_names=list(korte.named_steps["prep"].get_feature_names_out())))
'''),
("markdown", "### Stap 4. In logistische regressie kijken\n\nIn Orange gebruik je hiervoor het Nomogram. Hier kijken we naar de gewichten. Positief betekent: meer kans op ja. Omdat de getallen geschaald zijn, kun je de gewichten met elkaar vergelijken."),
("code", '''
lr3 = modellen3["Logistic Regression"]
namen = lr3.named_steps["prep"].get_feature_names_out()
richting = -1 if lr3.classes_[1] == "nee" else 1   # scikit-learn rekent richting de tweede klasse
gewichten = pd.Series(richting * lr3.named_steps["model"].coef_[0], index=namen)
gewichten.sort_values(key=abs, ascending=False).round(3).head(10)
'''),
("markdown", "### Stap 5. Eén aanvrager: TB0046\n\nWat voorspelt elk model voor deze aanvrager, met welke kans, en wat gebeurde er werkelijk?"),
("code", '''
aanvrager = testset[testset[ID] == "TB0046"]
print(aanvrager[k + [DOEL]].T)
print()
for naam, m in modellen3.items():
    p = kans_ja(m, aanvrager, k)[0]
    print(f"{naam:24s} voorspelt {'ja' if p >= 0.5 else 'nee'}, kans op ja {p:.0%}")
print("Werkelijk terugbetaald:", aanvrager[DOEL].iloc[0])
'''),
("markdown", """
### Vragen bij practicum 3

1. Welke CA hebben de drie modellen op de testset? Welk model is het best? Verrast je dat?
2. Schrijf de korte boom op als drie of vier regels in gewone taal, zoals: "Bij een looptijd van meer dan 24 maanden en geen eerdere achterstand …"
3. Welke drie kenmerken wegen bij logistische regressie het zwaarst? Vind je dat redelijk?
4. Wat voorspelt elk model voor aanvraag TB0046, en met welke kans? Wat gebeurde er werkelijk?
5. Leg de uitkomst van de korte boom voor TB0046 uit aan drie doelgroepen, elk in hooguit 60 woorden: de aanvrager, de kredietmedewerker en een toezichthouder.
6. Rudin zegt: kies bij grote gevolgen een model dat zelf te begrijpen is. Ben je het daarmee eens voor Suribank? Wanneer zou je toch een complexer model kiezen?

Vul daarna evidence card 3 in.
"""),
]
build(p1, sys.argv[1]); build(p23, sys.argv[2])
