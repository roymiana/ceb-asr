'''
CMSC 198: Special Problem in Computer Science
Developing an Automatic Speech Recognition for the Cebuano Language
2018-11363 Miana, Jose Roy C.
'''

'''
< extract-transcription.py >
extracts all transcription from the final csv file and writes it in a text file
'''

import pandas as pd
import re
from string import punctuation

my_punctuation = punctuation.replace("'", "")

data_csv = pd.read_csv('../data/final.csv')

saved_column = data_csv['transcription'].to_list()

with open('../data/transcription.txt', 'w', encoding="utf-8") as file:

    for line in saved_column:

        cleaned = str(line).replace('"', '').replace('-', ' ')
        cleaned = cleaned.translate(str.maketrans('', '', my_punctuation))
        cleaned = re.sub(' +', ' ', cleaned)
        cleaned = cleaned.rstrip().lstrip()

        file.write(cleaned + ' ')

print('Finished Extracting Transcription in CSV')