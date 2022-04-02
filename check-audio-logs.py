'''
CMSC 198: Special Problem in Computer Science
Developing an Automatic Speech Recognition for the Cebuano Language
2018-11363 Miana, Jose Roy C.
'''

'''
< check-audio-logs.py >
checks if audio files and logs match
'''

import os, csv

log_path = '../logs'
audio_path = '../audio'

csv_file = 'list.csv'

header = [  'log', 'files', 'statement' ]
log_list = []
data = []

log_directory = os.listdir(log_path)

for log in log_directory:

    with open(log_path + '/'+ log, 'r', encoding="utf-8") as log_file:

        lines = log_file.readlines()[13:]

        for line in lines:
            
            line = line.strip()
            parsed_line = line.split()
            audio_file_name = parsed_line[0]
            log_list.append(audio_file_name)

log_list.sort()
print('Log List Finished')

audio_directory = os.listdir(audio_path)

for (audio, log) in zip(audio_directory, log_list):
    
    data.append([audio, log, audio==log])

print('Audio List Finished')

with open(csv_file, 'w', encoding='UTF8', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(header)
    writer.writerows(data)

print('Finished')