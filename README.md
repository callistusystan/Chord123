# Chord123 #

Chord123 is a command line tool built with Python, that translates chords from the number system to chords in specific keys. Currently, it only works for .docx file types.

This program was built to quicken the chord writing process in the church I visit.

The name Chord123, is a word play on chords and numbers, with the message that this app makes translation easy as 1 2 3! :smile:

## Screenshots ##
<div>
  <img src="/screenshots/screenshot1.png" width="640px">
</div>

## Installation ##

Requirements:

1. Python3 with PIP

Steps:

1. Clone this project and extract it on your computer
2. Open a terminal and change to the project directory
3. Enter one of the following commands:

	```
	> pip install .

    	OR

	> python3 -m pip install .
	```

## Usage ##

Steps:

1. Open a terminal and change to the directory with the .docx file you wish to translate
2. Enter the following commands:

	```
		> chord123 [--transpose] <file.docx> <original_key> <transpose_key>
		NOTE: key should be in { A, A#, B, C, C#, D, D#, E, F, F#, G, G# }
	```
