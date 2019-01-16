import pandas as pd
import re
from nltk.corpus import stopwords


fullCorpus = pd.read_csv('new.tsv', sep='|', header=None)
fullCorpus.columns = ['label', 'body_text']
fullCorpus.head()

def convert_to_lowercase(text):
    input_str =text
    input_str = input_str.lower()
    return input_str
fullCorpus['body_text_lower'] = fullCorpus['body_text'].apply(lambda x: convert_to_lowercase(x))


# print seperate file for lowercase output
print('----------------------------Print in the punctuation.txt-----------------------------------------')
file = open('lowercase.txt', 'w')
lowercased = fullCorpus['body_text_lower']
for index, val in lowercased.iteritems():
    line = str(index)+'\t'+str(val)
    file.write(line+'\n')
file.close()



def remove_numbers(text):
    result = re.sub(r'\d+', '', text)
    return result
fullCorpus['body_text_no_numbers'] = fullCorpus['body_text_lower'].apply(lambda x: remove_numbers(x))
print('finished')

# print seperate file for without number output
print('----------------------------Print in the no_number.txt-----------------------------------------')
file = open('no_numbers.txt', 'w')
no_numbers = fullCorpus['body_text_no_numbers']
for index, val in no_numbers.iteritems():
    line = str(index)+'\t'+str(val)
    file.write(line+'\n')
file.close()

stopwords = stopwords.words('english')+["based", "regarding"]
print(stopwords)

if __name__ == '__main__':
    remove_numbers('12abcd405')