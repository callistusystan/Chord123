from argparse import ArgumentParser
from .doc_handler import DocumentHandler
from .translator import Translator

'''
Function that translates the inputFile into the specified key.


'''
def translate(inputFile, key, outputFile):
    dh = DocumentHandler(inputFile)
    tr = Translator(dh.content, key)
    output = tr.parse()
    dh.save(output, outputFile)

def getOutputName(inputFile, key):
    dotPos = inputFile.index('.')
    name = inputFile[:dotPos]
    extension = inputFile[dotPos:]

    return "{} ({}){}".format(name, key, extension)

def main():
    parser = ArgumentParser()
    parser.add_argument('-i', '--input', help='path of file to translate')
    parser.add_argument('-k', '--key', help='key to translate into')
    args = parser.parse_args()

    if args.input is None or args.key is None:
        print("Insufficient arguments")
        return

    translate(args.input, args.key, getOutputName(args.input, args.key))
