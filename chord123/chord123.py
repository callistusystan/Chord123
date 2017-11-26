from argparse import ArgumentParser
from .doc_handler import DocumentHandler
from .translator import Translator

def translate(inputFile, key, outputFile):
    dh = DocumentHandler(inputFile)
    tr = Translator(dh.content, key)
    output = tr.parse()
    dh.save(output, outputFile)

def main():
    parser = ArgumentParser()
    parser.add_argument('-i', '--input', help='path of file to translate')
    parser.add_argument('-k', '--key', help='key to translate into')
    args = parser.parse_args()

    if args.input is None or args.key is None:
        print("Insufficient arguments")
        return

    dotPos = args.input.index('.')
    name = args.input[:dotPos]
    extension = args.input[dotPos:]

    translate(args.input, args.key, "{} ({}){}".format(name, args.key, extension))
