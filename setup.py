from setuptools import setup

setup(name='numchord',
      version='0.1',
      description='A command line script to translate a .docx of number-system chords to a specified key',
      author='Callistus Tan',
      author_email='callistusystan@example.com',
      license='MIT',
      entry_points = {
        "console_scripts": ['numchord = numchord.numchord:main']
        },
      packages=['numchord'],
      zip_safe=False)
