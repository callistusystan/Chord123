import re
from .music_theory import KEYS, MODE, INCREMENT, hasChords, isMusical

class Transposer:
    def __init__(self, content='', origKey='A', targetKey='A'):
        self.content = content
        self.origKey = origKey
        self.targetKey = targetKey

    def chordToChord(self, chord, increment):
        j = KEYS.index(chord)
        return KEYS[(j+increment)%12]

    def transpose(self, chord, increment):
        chords = chord.split('/');

        firstChord = self.chordToChord(chords[0], increment)

        if len(chords) == 2:
            return "{}/{}".format(firstChord, self.chordToChord(chords[1], increment))
        return firstChord

    def parse(self):
        lines = self.content.split('\n')

        origKeyId = KEYS.index(self.origKey)
        targetKeyId = KEYS.index(self.targetKey)

        increment = (targetKeyId-origKeyId)%12

        output = ''
        for line in lines:
            newLine = ''
            newLine = re.sub(r"([A-G](?![A-Zac-z])[#b]?)", lambda chord: self.transpose(chord.group(0), increment), line)
            output += newLine + '\n'
        return output
