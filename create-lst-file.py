'''
CMSC 198: Special Problem in Computer Science
Developing an Automatic Speech Recognition for the Cebuano Language
2018-11363 Miana, Jose Roy C.
'''

'''
< create-lst-file.py >
creates a list file in specific format for the audio and their transcription data
'''

from alive_progress import alive_bar
from time import sleep
import os, math, csv, re
import soundfile as sf

log_path = '../logs'
audio_path = '../audio'

csv_files = [  'final.csv', 'ceb.csv'   ]

header = [  'sample.id', 'input_handle', 
            'input_size', 'transcription'   ]
log_list = []
data = []

def list_to_string(s):
    return ' '.join(map(str, s))

log_directory = os.listdir(log_path)
total_log_files = len(log_directory)

with alive_bar(total_log_files, title='Processing Log Files') as bar:

    for log in log_directory:

        with open(log_path + '/'+ log, 'r', encoding="utf-8") as log_file:

            lines = log_file.readlines()[13:]

            for line in lines:

                line = line.strip()
                parsed_line = line.split()

                audio_file_name = parsed_line[0]
                if parsed_line[2] == 'Digit"':
                    del parsed_line[:3]
                else:
                    del parsed_line[:2]

                transcription = list_to_string(parsed_line).replace('"', '')
                transcription = transcription.replace('. ---', '')
                transcription = transcription.replace('&', 'and')
                transcription = re.sub("[\(\[].*?[\)\]]", "", transcription)

                log_list.append([audio_file_name, transcription])

        sleep(0.03)
        bar()

log_list.sort(key=lambda log_list:log_list[0])
print('Log List Finished')

audio_directory = os.listdir(audio_path)
total_audio_files = len(audio_directory)

with alive_bar(total_audio_files, title='Processing Audio Files') as bar:

    i = 0

    for audio in audio_directory:

        audio_file = sf.SoundFile(audio_path + '/' + audio)

        audio_length = (audio_file.frames / audio_file.samplerate) * 1000
        audio_length = math.ceil(audio_length*100) / 100

        data.append([audio[:-4], '/'+audio, audio_length, log_list[i][1]])
        i += 1

        bar()

print('Audio List Finished')

with open(csv_files[0], 'w', encoding='UTF8', newline='') as file:

    writer = csv.writer(file)
    writer.writerow(header)
    writer.writerows(data)

with open(csv_files[1], 'w', encoding='UTF8', newline='') as file:

    writer = csv.writer(file, delimiter=' ')
    writer.writerow(header)
    writer.writerows(data)

print('Finished')