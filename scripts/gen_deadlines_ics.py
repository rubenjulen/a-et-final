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
    # contact- en feedbackmomenten
    (D(12, 14), None, None, 'Blok 0 opent: voorbereiden', 'Kennispakket 0, practicum 1, intake en beginquiz. Lees eerst de studiewijzer.'),
    (D(1, 7), None, None, 'College 1 (op locatie)', 'Wat staat er op het spel? Werkt, mag, verantwoord; vier lenzen; K1.'),
    (D(1, 11), None, None, 'Feedforward op K1', 'Schriftelijk per groep.'),
    (D(1, 14), None, None, 'College 2 met gastspreker (op locatie)', 'Gastcollege en Lagerhuisdebat; bias, uitlegbaarheid, privacy en verantwoording; K2 en K3.'),
    (D(1, 25), None, None, 'Feedforward concept K2-K4; laatste dag casus wisselen', 'Daarna blijft de casus vast.'),
    (D(2, 18), None, None, 'Feedback en cijfer Assessment 1', 'Schriftelijk; de actiepunten verwerk je in de verwerkingslijst.'),
    (D(2, 25), None, None, 'College 3: feedback en Design Review (op locatie)', 'Elke groep presenteert de maatregelen in hoogstens 8 dia\'s.'),
    # deadlines
    (D(1, 6), DEADLINE, None, 'Blok 0 afronden', 'Intake, beginquiz, practicum 1 met evidence card 1, beschrijving van de eigen oplossing (groep).'),
    (D(1, 10), DEADLINE, None, 'K1 scope en teamafspraken', 'Groep, bij ICT A-ET K1.'),
    (D(1, 12), DEADLINE, None, 'Vragen gastspreker en debatstellingen', 'Groep, bij ICT A-ET Voorbereiding college 2.'),
    (D(1, 24), DEADLINE, None, 'Concept K2, K3 en K4 (optioneel)', 'Groep, bij ICT A-ET Concept K2-K4; feedforward op maandag 25 januari.'),
    (D(2, 3), '18:00', None, 'Uiterste moment uitstel aanvragen Assessment 1', 'Uitstel alleen met een reden.'),
    (D(2, 3), DEADLINE, None, 'Kennischeck 1', 'Individueel; telt niet mee.'),
    (D(2, 4), DEADLINE, None, 'Assessment 1 inleveren (30%)', 'Tussenrapport H1-H5 (groep), dilemma-canvas (individueel), AI-verklaring en peerbeoordeling.'),
    (D(2, 23), DEADLINE, None, 'Concept maatregelen en Design Review-dia\'s', 'Groep, maximaal 8 dia\'s, bij ICT A-ET Design Review.'),
    (D(2, 24), DEADLINE, None, 'Kennischeck 2', 'Individueel; telt niet mee.'),
    (D(3, 7), DEADLINE, None, 'Concept eindrapport naar de peergroep', 'Groep; met maatregelen, monitoring en beslismemo.'),
    (D(3, 9), DEADLINE, None, 'Peerfeedback terug', 'Eén pagina met de vaste vragen (ICT A-ET Peerfeedback).'),
    (D(3, 10), '18:00', None, 'Uiterste moment uitstel aanvragen Assessment 2', 'Uitstel alleen met een reden.'),
    (D(3, 10), DEADLINE, None, 'Kennischeck 3 en module-evaluatie', 'Individueel; telt niet mee.'),
    (D(3, 11), DEADLINE, None, 'Assessment 2 inleveren (70%)', 'Eindrapport met beslismemo (groep), reflectie (individueel), AI-verklaring en peerbeoordeling.'),
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
