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

data_csv = pd.read_csv('final.csv')

saved_column = data_csv['transcription'].to_list()

with open('transcription.txt', 'w', encoding="utf-8") as file:

    for line in saved_column:

        cleaned = str(line).replace('"', '')
        cleaned = re.sub(' +', ' ', cleaned)
        cleaned = cleaned.rstrip().lstrip()

        file.write(cleaned + ' ')

print('Finished Extracting Transcription in CSV')