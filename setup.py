from setuptools import setup

setup(name='Chord123',
      version='0.12',
      description='A command line script to translate a .docx of number-system chords to a specified key',
      author='Callistus Tan',
      author_email='callistusystan@example.com',
      packages=['chord123'],
      keywords=['music', 'translate', 'chords', 'numbers'],
      url='https://github.com/callistusystan/Chord123',
      download_url='https://github.com/callistusystan/Chord123/archive/0.12.tar.gz',
      license='MIT',
      entry_points = {
        "console_scripts": ['chord123 = chord123.chord123:main']
      },
      install_requires=[
        'python-docx',
      ],
      zip_safe=False)
