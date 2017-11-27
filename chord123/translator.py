import re

KEYS = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#'];
MODE = ['', 'm', 'm', '', '', 'm', 'dim']
INCREMENT = [0, 2, 4, 5, 7, 9, 11];

class Translator:
    def __init__(self, content='', key='A'):
        self.content = content
        self.key = key

    def numToChord(self, chordNum, keyId, doMode):
        # convert chord to 0-based index
        j = int(chordNum[0])-1

        # get correct chord
        chordId = keyId+INCREMENT[j]
        # check for sharps or flats
        if '#' in chordNum:
            chordId += 1
        elif 'b' in chordNum:
            chordId -= 1
        if not doMode:
            return KEYS[chordId%12]

        # check if mode explicitly defined
        if 'M' in chordNum:
            return KEYS[chordId%12]
        elif 'm' in chordNum:
            return KEYS[chordId%12]+'m'

        # compute manually
        if '#' in chordNum or 'b' in chordNum:
            return KEYS[chordId%12]

        return "{}{}".format(KEYS[chordId%12], MODE[j])

    def translate(self, number, keyId):
        numbers = number.split('/');
        chordNum = numbers[0]

        chord = self.numToChord(chordNum, keyId, True)
        if len(numbers) == 2:
            bassNum = numbers[1]
            return "{}/{}".format(chord, self.numToChord(bassNum, keyId, False))
        return chord

    def hasChords(self, line):
        return bool(re.search(r"[A-G](?![A-Zac-z])[#b]?[Mm]?", line))

    def isMusical(self, line):
        return bool(re.search(r"[A-G](?![A-Zac-z])[#b]?[Mm]?", line)) or bool(re.search(r"\+[0-12]", line))

    def parse(self):
        lines = self.content.split('\n')

        origKeyId = KEYS.index(self.key)
        keyId = origKeyId

        output = ''
        for line in lines:
            newLine = ''
            if '+' in line:
                [transposeBy] = re.findall(r"([0-9]+)", line)
                keyId = (origKeyId+int(transposeBy))%12
            else:
                newLine = re.sub(r"([0-9][^\s]*)", lambda number: self.translate(number.group(0), keyId), line)
            output += newLine + '\n'
        return output
