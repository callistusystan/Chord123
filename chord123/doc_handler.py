import re
from docx import Document
from docx.shared import RGBColor, Pt
from .music_theory import isMusical, isSection, hasChords

class DocumentHandler:
    def __init__(self, path):
        with open(path, 'rb') as f:
            self.document = Document(f)

    def save(self, filename):
        self.document.save(filename)
