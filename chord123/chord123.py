import re
from argparse import ArgumentParser
from .doc_handler import DocumentHandler
from .translator import Translator
from .transposer import Transposer

'''
Function that translates the input numbers file into the specified key.
'''
def translate(inputFile, key, outputFile):
    dh = DocumentHandler(inputFile)
    tr = Translator(dh.content, key)
    output = tr.parse()
    dh.save(output, outputFile)

'''
Function that transposes the input chord file into the specified key.
'''
def transpose(inputFile, origKey, newKey, outputFile):
    dh = DocumentHandler(inputFile)
    tr = Transposer(dh.content, origKey, newKey)
    output = tr.parse()
    dh.save(output, outputFile)

def getOutputName(inputFile, key):
    inputFile = re.sub(r"\s+\([A-G][#b]?\)", '', inputFile)
    dotPos = inputFile.index('.')
    name = inputFile[:dotPos]
    extension = inputFile[dotPos:]

    return "{} ({}){}".format(name, key, extension)

def main():
    parser = ArgumentParser()
    parser.add_argument('-t1', '--transpose', help='transpose from key to key', nargs=3)
    parser.add_argument('-t2', '--translate', help='translate from number system to chords', nargs=2)
    args = parser.parse_args()

    if args.transpose is not None:
        inputFile, key1, key2 = args.transpose
        transpose(inputFile, key1, key2, getOutputName(inputFile, key2))
    elif args.translate is not None:
        inputFile, key = args.translate
        translate(inputFile, key, getOutputName(inputFile, key))
    else:
        print("Invalid command: For help, enter chord123 --help")
