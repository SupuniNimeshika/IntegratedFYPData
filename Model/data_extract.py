import random

def get_data():
    angryfile = open('data/angry.txt','r')
    angry = angryfile.readlines()
    sadfile = open('data/sad.txt','r')
    sad = sadfile.readlines()
    happyfile = open('data/happy.txt','r')
    happy = happyfile.readlines()
    calmfile = open('data/calm.txt','r')
    calm = calmfile.readlines()


    data = []
    for line in angry:
        str=line.translate({ord('\n'): None})
        str= 'angry|'+str
        data.append(str)

    for line in sad:
        str=line.translate({ord('\n'): None})
        str= 'sad|'+str
        data.append(str)

    for line in calm:
        str=line.translate({ord('\n'): None})
        str= 'calm|'+str
        data.append(str)

    for line in happy:
        str=line.translate({ord('\n'): None})
        str= 'happy|'+str
        data.append(str)

    # random.shuffle(data)


# print seperate file for final shuffle output
    print('----------------------------Print in the final.txt-----------------------------------------')
    file = open('data/final.tsv', 'w')
    final_post=random.shuffle(data)
    for data_post in data:
       print(data_post)
       file.write(data_post+'\n')
    file.close()

# if __name__ == '__main__':
#     get_data()

