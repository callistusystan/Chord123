from setuptools import setup

setup(name='Chord123',
      version='0.1',
      description='A command line script to translate a .docx of number-system chords to a specified key',
      author='Callistus Tan',
      author_email='callistusystan@example.com',
      url='https://github.com/callistusystan/Chord123',
      license='MIT',
      entry_points = {
        "console_scripts": ['chord123 = chord123.chord123:main']
        },
      packages=['chord123'],
      zip_safe=False)
