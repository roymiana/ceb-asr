'''
CMSC 198: Special Problem in Computer Science
Developing an Automatic Speech Recognition for the Cebuano Language
2018-11363 Miana, Jose Roy C.
'''

'''
< check-logs.py >
checks if log is present in the audio files
'''

import os, csv

log_path = '../logs'
audio_path = '../audio'

csv_file = 'log_present.csv'

header = ['log', 'files']
audio_list = []
data = []

audio_directory = os.listdir(audio_path)

for audio in audio_directory:

    audio_list.append(audio)
    
print('Audio List Finished')

log_directory = os.listdir(log_path)

for log in log_directory:

    with open(log_path + '/'+ log, 'r', encoding="utf-8") as log_file:

        lines = log_file.readlines()[13:]

        for line in lines:

            line = line.strip()
            parsed_line = line.split()
            audio_file_name = parsed_line[0]
            
            if audio_file_name in audio_list:
                data.append([audio_file_name, 'present'])
            else:
                data.append([audio_file_name, 'delete'])

print('Log List Finished')

with open(csv_file, 'w', encoding='UTF8', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(header)
    writer.writerows(data)

print('Finished')