import math
import re
from nltk.corpus import stopwords

#input

file = open("text_tel.txt", "r", encoding="utf8")

text=""

for i in file.read():
    if i=='\n':
        text=text+' '
    else:
        text = text + i

print('Original Text = ', text)
print('Original Text no. of words = ', len(text.split()))

punctuation = ['.','?','!']

sents=re.split('.', text) 
#try '?' '. ' '.. ' '... ' as well

len_sents = len(sents)

words=text.split(" ")

print(words)
print(sents)

#Frequency of all words    
freq_matrix = {}
stopWords = list(stopwords.words("telugu"))
stopWords.extend(["చేత","వలన","గూర్చి","కొరకు"])

for i in sents:
    freq_table = {}
    words=i.split(" ")
    for j in words:
        if j in stopWords:
            continue

        if j in freq_table:
            freq_table[j] += 1
        else:
            freq_table[j] = 1

    freq_matrix[i[:10]] = freq_table

print(freq_matrix)

#Term Frequency 
tf_matrix = {}

for i, j in freq_matrix.items():
    tf_table = {}

    count_words_in_sentence = len(j)
    for a, b in j.items():
        tf_table[a] = b / count_words_in_sentence

    tf_matrix[i] = tf_table


count_doc_per_words = {}

for i, j in freq_matrix.items():
    for a, b in j.items():
        if a in count_doc_per_words:
            count_doc_per_words[a] += 1
        else:
            count_doc_per_words[a] = 1


idf_matrix = {}


for i, j in freq_matrix.items():
    idf_table = {}

    for a in j.keys():
        idf_table[a] = math.log10(len_sents / float(count_doc_per_words[a]))

    idf_matrix[i] = idf_table


tf_idf_matrix = {}

for (i1, j1), (i2, j2) in zip(tf_matrix.items(), idf_matrix.items()):
    tf_idf_table = {}

    for (a1, b1), (a2, b2) in zip(j1.items(), j2.items()):  
        tf_idf_table[a1] = float(b1 * b2)

    tf_idf_matrix[i1] = tf_idf_table


sentence_scores = {}

for i, j in tf_idf_matrix.items():
    total_score_per_sentence = 0

    count_words_in_sentence = len(j)
    for a, b in j.items():
        total_score_per_sentence += b
    if count_words_in_sentence !=0:
        sentence_scores[i] = total_score_per_sentence / count_words_in_sentence
    else:
        sentence_scores[i]=0
#print(sentence_scores)

estimated_scores = sentence_scores

max_score = 0
for i in estimated_scores:
    if estimated_scores[i]>max_score:
        max_score = estimated_scores[i]

#sumValues = 0
#for i in sentence_scores:
#    sumValues += sentence_scores[i]


# Taking half of the max score as threshold
threshold = max_score*0.4
#print("Threshold is - " ,threshold)
    
summary = []

for i in sents:
    if i[:10] in sentence_scores and sentence_scores[i[:10]] >= (0.75*threshold):
        summary.append(i)
summary = '.'.join(summary)

print('\nSummarized Text = ',summary)
print('Summarized Text no. of words= ', len(summary.split()))


