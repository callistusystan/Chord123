from docx import Document
from docx.shared import RGBColor, Pt
from .translator import Translator

class DocumentHandler:
    def __init__(self, path):
        with open(path, 'rb') as f:
            self.document = Document(f)
            self.content = self.getText(self.document)

    def getText(self, document):
        content = []
        for paragraph in document.paragraphs:
            content.append(paragraph.text)
        return '\n'.join(content)

    def save(self, content, filename):
        t = Translator()

        document = Document()
        endOfLine1 = content.index('\n')

        # get heading and body
        body = content.split('\n')
        heading = []
        while body[0] == '' or not t.isMusical(body[0]):
            if body[0] != '':
                heading.append(body[0])
            body.pop(0)

        # start writing
        document.add_heading(heading, 0)
        p = document.add_paragraph()
        for line in body:
            if line == '':
                p = document.add_paragraph()
            else:
                run = p.add_run(line+'\n')
                run.font.size = Pt(14)
                if t.hasChords(line):
                    run.bold = True
                    run.font.color.rgb = RGBColor(0, 0, 0xFF)

        document.save(filename)
