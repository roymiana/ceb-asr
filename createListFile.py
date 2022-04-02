from alive_progress import alive_bar
from time import sleep
import os, math, csv, re
import soundfile as sf

header = ['sample.id', 'input_handle', 'input_size', 'transcription']
logs = []
data = []

def listToString(s):
    return ' '.join(map(str, s))

arr = os.listdir('../logs')
total = len(arr)
with alive_bar(total, title='Processing Log Files') as bar:
    for log in arr:
        with open('../logs/'+log, 'r', encoding="utf-8") as f:
            lines = f.readlines()[13:]
            for line in lines:
                line = line.strip()
                x = line.split()
                file = x[0]
                if x[2] == 'Digit"':
                    del x[:3]
                else:
                    del x[:2]
                transcription = listToString(x).replace('"', '')
                transcription = transcription.replace('. ---', '')
                transcription = transcription.replace('&', 'and')
                transcription = re.sub("[\(\[].*?[\)\]]", "", transcription)
                logs.append([file, transcription])
        sleep(0.03)
        bar()

logs.sort(key=lambda logs:logs[0])
print('Log List Finished')

arr = os.listdir('../audio')
total = len(arr)
i = 0
with alive_bar(total, title='Processing Audio Files') as bar:
    for audio in arr:
        # print('../audio/' + audio)
        f = sf.SoundFile('../audio/' + audio)
        ms = (f.frames / f.samplerate)*1000
        ms = math.ceil(ms*100)/100
        # print('seconds = ' + str(ms))
        data.append([audio[:-4], '/'+audio, ms, logs[i][1]])
        i += 1
        bar()

print('Audio List Finished')

with open('final.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)

    # write the header
    writer.writerow(header)

    # write multiple rows
    writer.writerows(data)

with open('my.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f, delimiter=' ')
    writer.writerow(header)
    writer.writerows(data)

print('Finished')