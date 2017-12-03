import re
from .music_theory import KEYS_SHARP, MODE, INCREMENT, hasChords, isMusical

class Translator:
    def __init__(self, document=None, key='A'):
        self.document = document
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
            return KEYS_SHARP[chordId%12]

        # check if mode explicitly defined
        if 'M' in chordNum:
            return KEYS_SHARP[chordId%12]
        elif 'm' in chordNum:
            return KEYS_SHARP[chordId%12]+'m'

        # compute manually
        if '#' in chordNum or 'b' in chordNum:
            return KEYS_SHARP[chordId%12]

        return "{}{}".format(KEYS_SHARP[chordId%12], MODE[j])

    def translate(self, number, keyId):
        numbers = number.split('/');
        chordNum = numbers[0]

        chord = self.numToChord(chordNum, keyId, True)
        if len(numbers) == 2:
            bassNum = numbers[1]
            if bassNum == '':
                return "{}/".format(chord)
            else:
                return "{}/{}".format(chord, self.numToChord(bassNum, keyId, False))
        return chord

    def parse(self):
        origKeyId = KEYS_SHARP.index(self.key)
        keyId = origKeyId

        for p in self.document.paragraphs:
            inline = p.runs
            for i in range(len(inline)):
                if '+' in inline[i].text:
                    [transposeBy] = re.findall(r"([0-9]+)", inline[i].text)
                    keyId = (origKeyId+int(transposeBy))%12
                else:
                    inline[i].text = re.sub(r"([0-9](?!x)[^\s]*)", lambda number: self.translate(number.group(0), keyId), inline[i].text)
