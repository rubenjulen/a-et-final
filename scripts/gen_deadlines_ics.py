#!/usr/bin/env python3
"""Maakt 'ICT A-ET Deadlines.ics': alle deadlines en contactmomenten van A-ET 2026-2027.
Bron: de deadlinetabel in de studiewijzer en de planningstabellen in de studentversies (mycampus/md).
Tijden in Surinaamse tijd (America/Paramaribo, UTC-3, geen zomertijd)."""
import datetime as dt, os, hashlib

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(REPO, 'lesmateriaal', 'algemeen', 'ICT A-ET Deadlines.ics')
TZ = 'America/Paramaribo'

D = lambda m, d: dt.date(2027 if m < 6 else 2026, m, d)
# (datum, starttijd|None, eindtijd|None, titel, omschrijving)  — None = hele dag
DEADLINE = '23:59'
items = [
    # contactmomenten en vaste momenten
    (D(12, 14), None, None, 'Week 0 opent', 'Online opfrisser: kennisclips, practicum 1, intake en beginquiz. Lees eerst de studiewijzer.'),
    (D(1, 5), '19:00', '20:00', 'Online inloopmoment week 0', 'Vragen over installatie (Orange, Python, Colab) en week 0.'),
    (D(1, 7), None, None, 'College 1 (op locatie)', 'Wat staat er op het spel bij jullie oplossing? Groepen bakenen hun casus af (K1).'),
    (D(1, 14), None, None, 'College 2 met gastspreker (op locatie)', 'Data-ethiek, bias, privacy en verantwoording; debat over de stellingen.'),
    (D(1, 21), None, None, 'Online sessie week 3', 'Fouten per groep, uitlegbaarheid en generatieve AI.'),
    (D(1, 25), None, None, 'Laatste dag om van casus te wisselen', 'Daarna blijft de casus vast.'),
    (D(1, 28), None, None, 'Online sessie week 4', 'Van dilemma naar risico.'),
    (D(2, 2), None, None, 'Online vragenuur Assessment 1', 'Vragen over het tussenrapport en het dilemma-canvas.'),
    (D(2, 11), None, None, 'Online sessie week 6', 'Algemene feedback op Assessment 1; van risico naar ontwerp.'),
    (D(2, 18), None, None, 'Online sessie week 7', 'Menselijke controle, met de toeslagenaffaire als casus.'),
    (D(2, 25), None, None, 'College 3: Design Review (op locatie)', 'Elke groep presenteert 8 minuten aan het panel.'),
    (D(3, 4), None, None, 'Online sessie week 9', 'Monitoring, de hertest en het beslismemo.'),
    (D(3, 9), None, None, 'Online vragenuur eindrapport en reflectie', 'Laatste vragen voor Assessment 2.'),
    # deadlines
    (D(1, 6), DEADLINE, None, 'Week 0 afronden', 'Intake, practicum 1 met evidence card 1, beschrijving van de eigen oplossing (groep) en beginquiz.'),
    (D(1, 10), DEADLINE, None, 'K1-canvas en weekcheck week 1', 'K1-canvas met teamafspraken (groep); weekcheck met standpunt (individueel).'),
    (D(1, 12), DEADLINE, None, 'Vragen gastspreker en debatstellingen', 'Drie vragen voor de gastspreker en twee debatstellingen met bronnen (groep).'),
    (D(1, 13), DEADLINE, None, 'Weekcheck week 2', 'Vijf kennisvragen, logboekregel en standpunt (individueel; telt niet mee).'),
    (D(1, 17), DEADLINE, None, 'Rapportstuk week 2: K2, K3 en bewijsplan', 'Groep.'),
    (D(1, 20), DEADLINE, None, 'Weekcheck week 3', 'Met de eigen uitkomsten van practicum 2; practicum 2 moet dus af zijn.'),
    (D(1, 24), DEADLINE, None, 'Rapportstuk week 3: practicum 3 en K4 snelle scan', 'Practicum 3 en evidence cards 2 en 3 (individueel); K4 snelle scan (groep).'),
    (D(1, 27), DEADLINE, None, 'Weekcheck week 4', 'Individueel; telt niet mee.'),
    (D(1, 31), DEADLINE, None, 'Concept K4, K5 en K6 naar de peergroep', 'Conceptronde vóór Assessment 1; dilemma-canvas in concept klaar.'),
    (D(2, 1), DEADLINE, None, 'Peerfeedback terug (week 4)', 'Eén pagina met de drie vaste vragen en de checklist.'),
    (D(2, 3), '18:00', None, 'Uiterste moment uitstel aanvragen Assessment 1', 'Uitstel alleen met een reden; de docent spreekt een nieuwe datum af.'),
    (D(2, 3), DEADLINE, None, 'Weekcheck week 5', 'Licht: drie vragen, een logboekregel en een standpunt.'),
    (D(2, 4), DEADLINE, None, 'Assessment 1 inleveren (30%)', 'Tussenrapport met testverslag practicum 4 (groep), dilemma-canvas (individueel), AI-verklaring en peerbeoordeling.'),
    (D(2, 10), DEADLINE, None, 'Weekcheck week 6', 'Individueel; telt niet mee.'),
    (D(2, 14), DEADLINE, None, 'Rapportstuk week 6: K4 doelniveau en K7 deel 1', 'K4 met doelniveau, gap en prioriteit; K7 deel 1 voor de top 5 risico\'s (groep).'),
    (D(2, 17), DEADLINE, None, 'Weekcheck week 7', 'Individueel; telt niet mee.'),
    (D(2, 21), DEADLINE, None, 'Concept K7 naar de peergroep', 'K7 deel 1 herzien en deel 2; docent in cc.'),
    (D(2, 22), DEADLINE, None, 'Peerfeedback terug (week 7)', 'Eén pagina met de drie vaste vragen en de checklist.'),
    (D(2, 23), DEADLINE, None, 'Presentatie en concept K7 voor de Design Review', 'Maximaal 8 dia\'s (groep).'),
    (D(2, 24), DEADLINE, None, 'Weekcheck week 8', 'Individueel; telt niet mee.'),
    (D(2, 28), DEADLINE, None, 'Rapportstuk week 8: herzien K7 en verwerkingslijst', 'Groep.'),
    (D(3, 3), DEADLINE, None, 'Weekcheck week 9', 'Individueel; telt niet mee.'),
    (D(3, 7), DEADLINE, None, 'Concept eindrapport naar de peergroep', 'Met hertest, K8 en beslismemo; docent in cc.'),
    (D(3, 8), DEADLINE, None, 'Peerfeedback terug (week 9)', 'Gericht op het beslismemo, de keten en het plan.'),
    (D(3, 10), '18:00', None, 'Uiterste moment uitstel aanvragen Assessment 2', 'Ook het laatste moment voor vragen.'),
    (D(3, 10), DEADLINE, None, 'Laatste weekcheck en module-evaluatie', 'Logboekregel, laatste standpunt en module-evaluatie.'),
    (D(3, 11), DEADLINE, None, 'Assessment 2 inleveren (70%)', 'Eindrapport (groep), reflectie (individueel), AI-verklaring en peerbeoordeling.'),
]

VTZ = ['BEGIN:VTIMEZONE', f'TZID:{TZ}', 'BEGIN:STANDARD', 'DTSTART:19700101T000000',
       'TZOFFSETFROM:-0300', 'TZOFFSETTO:-0300', 'TZNAME:SRT', 'END:STANDARD', 'END:VTIMEZONE']


def esc(t):
    return t.replace('\\', '\\\\').replace(';', '\\;').replace(',', '\\,').replace('\n', '\\n')


def fold(line):
    b = line.encode('utf-8'); out = []
    while len(b) > 75:
        cut = 75
        while (b[cut] & 0xC0) == 0x80:
            cut -= 1
        out.append(b[:cut].decode()); b = b' ' + b[cut:]
    out.append(b.decode()); return '\r\n'.join(out)


stamp = dt.datetime.now(dt.timezone.utc).strftime('%Y%m%dT%H%M%SZ')
lines = ['BEGIN:VCALENDAR', 'VERSION:2.0', 'PRODID:-//A-ET 2026-2027//Deadlines//NL', 'CALSCALE:GREGORIAN',
         'METHOD:PUBLISH', 'X-WR-CALNAME:ICT A-ET deadlines 2026-2027', f'X-WR-TIMEZONE:{TZ}'] + VTZ
for day, start, end, title, desc in sorted(items, key=lambda x: (x[0], x[1] or '')):
    uid = hashlib.sha1(f'{day}{start}{title}'.encode()).hexdigest()[:16] + '@a-et-2026-2027'
    ev = ['BEGIN:VEVENT', f'UID:{uid}', f'DTSTAMP:{stamp}']
    if start is None:
        ev += [f'DTSTART;VALUE=DATE:{day:%Y%m%d}', f'DTEND;VALUE=DATE:{day + dt.timedelta(days=1):%Y%m%d}', 'TRANSP:TRANSPARENT']
        summ = f'ICT A-ET {title}'
    else:
        h, m = map(int, start.split(':'))
        s = dt.datetime.combine(day, dt.time(h, m))
        if end:
            eh, em = map(int, end.split(':')); e = dt.datetime.combine(day, dt.time(eh, em))
            summ = f'ICT A-ET {title}'
        else:  # deadline: blok van 30 minuten dat op het deadlinetijdstip eindigt
            e = s; s = s - dt.timedelta(minutes=30)
            summ = f'ICT A-ET {title} (deadline {start})'
        ev += [f'DTSTART;TZID={TZ}:{s:%Y%m%dT%H%M%S}', f'DTEND;TZID={TZ}:{e:%Y%m%dT%H%M%S}']
        if not end:
            ev += ['BEGIN:VALARM', 'ACTION:DISPLAY', f'DESCRIPTION:{esc(summ)}', 'TRIGGER:-PT24H', 'END:VALARM']
    ev[3:3] = [f'SUMMARY:{esc(summ)}', f'DESCRIPTION:{esc(desc)}']
    ev.append('END:VEVENT')
    lines += ev
lines.append('END:VCALENDAR')
os.makedirs(os.path.dirname(OUT), exist_ok=True)
with open(OUT, 'w', encoding='utf-8', newline='') as f:
    f.write('\r\n'.join(fold(l) for l in lines) + '\r\n')
print('ok', OUT, len(items), 'items')
