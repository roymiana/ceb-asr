'''
CMSC 198: Special Problem in Computer Science
Developing an Automatic Speech Recognition for the Cebuano Language
2018-11363 Miana, Jose Roy C.
'''

'''
< create-lexicon.py >
creates a lexicon text file
'''

unique_words = []

with open('transcription.txt', 'r', encoding="utf-8") as transcription_file:
    transcription = transcription_file.read()
    unique_words = set(transcription.split(' '))

with open('lexicon.txt', 'w', encoding="utf-8") as lexicon_file:

    for word in unique_words:

        for char in word:

            if char.isalpha() or char.isalnum():
                lexicon_file.write(char)
            else:
                if char == '-' or char == '\'':
                    lexicon_file.write(char)

        lexicon_file.write(' ')

        for char in word:

            if char.isalpha() or char.isalnum():
                lexicon_file.write(char + ' ')
            else:
                if char == '-':
                    lexicon_file.write('| ')
                if char == '\'':
                    lexicon_file.write('\' ')

        lexicon_file.write('|\n')


print('Finished Extracting CSV')