# Docentnotitie practicum 5: verwachte uitkomsten Python-notebook

Alleen voor de docent. Het notebook `practicum5.ipynb` gebruikt dezelfde instellingen als de Logistic Regression-widget in Orange 3.40: geen schaling, ontbrekende getallen aangevuld met het gemiddelde, lbfgs met 100 rekenstappen, getraind op alle 1.200 rijen van `suribank_kredietaanvragen.csv`. Daardoor komen de getallen overeen met de docentnotitie in week 9 (sectie 11); in 2027 wijkt één aanvraag af.

## Deel 1: invoer (gelijk aan Orange)

|  | 2025 (controle) | 2027 |
| --- | --- | --- |
| Mediaan maandinkomen | SRD 14.850 | SRD 18.800 |
| Mediaan gevraagd bedrag | SRD 106.000 | SRD 145.500 |
| Aandeel binnenland | 16,7% | 28,3% |
| Aandeel informeel | 15,0% | 24,1% |

## Deel 2: uitkomsten (Python)

|  | 2025 (controle) | 2027 | Orange (week 9) |
| --- | --- | --- | --- |
| CA | 66,9% | 62,5% | 66,9% / 62,6% |
| Voorspeld "ja" | 70,7% | 75,6% | 70,7% / 75,5% |
| Werkelijk "ja" | 56,0% | 47,1% | gelijk |
| Vakken (ja-ja / nee-ja / ja-nee / nee-nee) | 468 / 239 / 92 / 201 | 426 / 330 / 45 / 199 | 2027 in Orange: 426 / 329 / 45 / 200 |
| Onterecht goedgekeurd | 54,3% | 62,4% | 54,3% / 62,2% |
| Onterecht afgewezen | 16,4% | 9,6% | gelijk |
| Onterecht afgewezen, kust | 15,3% | 9,5% | gelijk |
| Onterecht afgewezen, binnenland | 23,7% | 9,7% | gelijk |

## Extra in het notebook: per inkomensgroep (grenzen uit 2025)

| Inkomensgroep | 2025 goedgekeurd | 2025 terugbetaald | 2027 aanvragen | 2027 goedgekeurd | 2027 terugbetaald |
| --- | --- | --- | --- | --- | --- |
| Laagste kwart | 55,5% | 41,3% | 131 | 64,1% | 35,9% |
| Tweede kwart | 65,1% | 50,2% | 179 | 72,1% | 35,2% |
| Derde kwart | 77,1% | 64,9% | 242 | 73,6% | 45,0% |
| Hoogste kwart | 84,0% | 67,1% | 394 | 81,5% | 58,1% |

In 2027 valt een veel groter deel van de aanvragers in het hoogste nominale kwart (394 tegenover 237), terwijl in elke groep minder mensen terugbetalen. Dat ondersteunt vraag 2 (inflatie: op papier rijker).

## Kanttekening voor de docent

Het Orange-model is formeel niet volledig uitgerekend (geen schaling, 100 stappen). Een goed geschaald en volledig uitgerekend model (StandardScaler, 1.000 stappen) laat dezelfde richting zien, maar minder extreem: goedgekeurd 61,1% → 65,2%, onterecht goedgekeurd 35,7% → 46,1%, en onterecht afgewezen kust/binnenland 16,7%/32,9% → 12,3%/16,8%. Het regioverschil wordt dan kleiner maar verdwijnt niet. Bruikbaar als verdiepingsvraag: "hangt je fairnessconclusie af van hoe het model is ingesteld?"
