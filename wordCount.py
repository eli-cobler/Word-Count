input_file = "yourtextfile.txt"


def text_blocks(text_file):
    AllWords = []
    for line in open(text_file):
        row = line.split(' ')
        AllWords += list(row)

    word_limit = 1000
    i = 1
    with open(text_file, 'w') as file:
        for word in AllWords:
            if("." in word and i>=word_limit):
                file.write(word.strip('\n')+"\n\n\n\n")
                i = 0
            else:
                file.write(word.strip('\n')+" ")

            i += 1

if __name__ == '__main__':
    text_blocks(input_file)
