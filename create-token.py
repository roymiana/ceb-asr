'''
CMSC 198: Special Problem in Computer Science
Developing an Automatic Speech Recognition for the Cebuano Language
2018-11363 Miana, Jose Roy C.
'''

'''
< create-token.py >
creates a token dictionary
'''
unique_char = ''

with open('transcription.txt', 'r', encoding="utf-8") as transcription_file:

    transcription = transcription_file.read()

    unique_char = ''.join(set(transcription))
    unique_char = ''.join(sorted(unique_char))

with open('all-characters.txt', 'w', encoding="utf-8") as char_file:

    for char in unique_char:

        char_file.write(char)
        char_file.write('\n')

with open('tokens.txt', 'w', encoding="utf-8") as token_file:

    token_file.write('|\n')

    for char in unique_char:

        if char.isalpha() or char.isalnum():
            token_file.write(char + '\n')
        else:
            if char == '\'':
                token_file.write(char + '\n')

print('Finished Creating Token File')