import re
from .music_theory import KEYS_SHARP, KEYS_FLAT, MODE, INCREMENT, hasChords, isMusical

class Transposer:
    def __init__(self, document=None, origKey='A', targetKey='A'):
        self.document = document
        self.origKey = origKey
        self.targetKey = targetKey

    def chordToChord(self, chord, increment):
        if chord in KEYS_SHARP:
            j = KEYS_SHARP.index(chord)
            return KEYS_SHARP[(j+increment)%12]
        j = KEYS_FLAT.index(chord)
        return KEYS_FLAT[(j+increment)%12]

    def transpose(self, chord, increment):
        chords = chord.split('/');

        firstChord = self.chordToChord(chords[0], increment)

        if len(chords) == 2:
            return "{}/{}".format(firstChord, self.chordToChord(chords[1], increment))
        return firstChord

    def parse(self):
        origKeyId = KEYS_SHARP.index(self.origKey)
        targetKeyId = KEYS_SHARP.index(self.targetKey)

        increment = (targetKeyId-origKeyId)%12

        for p in self.document.paragraphs:
            if "I Am" in p.text:
                continue
            inline = p.runs
            for j in range(len(inline)):
                inline[j].text = re.sub(r"(?<![A-Za-z])([A-G](?![A-Zac-ln-z])[#b]?)", lambda chord: self.transpose(chord.group(0), increment), inline[j].text)
