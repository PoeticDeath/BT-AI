import warnings
warnings.filterwarnings('ignore')
from keras.preprocessing.text import text_to_word_sequence as ttws
import BTGen
def acceptGen(inpt):
    new_words = ''
    skips = 0
    N = False
    notwords = ['']
    try:
        while True:
            word = BTGen.generate_seq(BTGen.model, BTGen.tokenizer, BTGen.seq_length, inpt, 1)
            if N:
                inpt = ' '.join(inpt.split(' ')[:1])
            else:
                inpt = ' '.join(inpt.split(' ')[1:])
            if word in notwords:
                inpt = inpt + ' ' + str(skips)
                skips += 1
                continue
            print(new_words, word)
            if input('Y or Enter: ').upper() == 'Y':
                skips = 0
                notwords = ['']
                N = False
                new_words += word + ' '
                inpt += ' ' + word
            else:
                notwords += [word]
                N = True
                inpt = inpt + ' ' + str(skips)
                skips += 1
    except KeyboardInterrupt:
        return new_words
inpt = ' '.join(ttws(open('BTNew.txt', 'rb').read().decode()))
print(acceptGen(inpt))
