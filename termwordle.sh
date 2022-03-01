#!/bin/bash
pip install pandas  2> /dev/null
pip install colorama 2> /dev/null
wget -O valid_words.csv https://raw.githubusercontent.com/dhruva3223/termwordle/master/valid_words.csv
wget -O wordle_game.py https://raw.githubusercontent.com/dhruva3223/termwordle/master/wordle_game.py
wget -O wordle_words.csv https://raw.githubusercontent.com/dhruva3223/termwordle/master/wordle_words.csv
echo "\nSuccessfully installed!"
cd
echo "alias playwordle='python3 ./wordle_game.py'" >> .bashrc