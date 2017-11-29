import re

KEYS = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#'];
MODE = ['', 'm', 'm', '', '', 'm', 'dim']
INCREMENT = [0, 2, 4, 5, 7, 9, 11];

def hasChords(line):
    return bool(re.search(r"[A-G](?![A-Zac-z])[#b]?[Mm]?", line))

def isMusical(line):
    return bool(re.search(r"[A-G](?![A-Zac-z])[#b]?[Mm]?", line)) or bool(re.search(r"\+[0-12]", line))
