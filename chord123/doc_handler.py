from docx import Document
from docx.shared import RGBColor, Pt
from .music_theory import isMusical, isSection, hasChords

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
        document = Document()
        endOfLine1 = content.index('\n')

        # get heading and body
        body = content.split('\n')
        heading = []
        while len(body) > 0 and (body[0] == '' or (isMusical(body[0]) or isSection(body[0])) == False):
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
                if hasChords(line):
                    run.bold = True
                    run.font.color.rgb = RGBColor(0, 0, 0xFF)

        document.save(filename)
