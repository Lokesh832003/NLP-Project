import math
import re
from nltk.corpus import stopwords

#input

file = open("text.txt", "r", encoding="utf8")

text=""

for i in file.read():
    if i=='\n':
        text=text+' '
    else:
        text = text + i
        
print('Original Text = ', text)
print('Original Text no. of words = ', len(text.split()))

sents=re.split('।',text)  # '।' is the equivalent of period in Nepali

len_sents = len(sents)

words=text.split()

#Frequency of all words    
freq_in_sent = {}
stopWords = set(stopwords.words("nepali"))

for i in sents: #iterate through each sentence
    freq_table = {}
    words=i.split()
    for j in words: #iterate through each word in ith sentence
        if j in stopWords:
            continue

        if j in freq_table:
            freq_table[j] += 1
        else:
            freq_table[j] = 1
    freq_in_sent[i[:10]] = freq_table #set first 10 chars of sentence as key of element of bigger dictionary
#print(freq_in_sent)

#Term Frequency in a sentence
termfreq = {}

for i, j in freq_in_sent.items():  #here i is the sentence and j is sub-dictionary
    tf_table = {}

    len_sent = len(j)
    for a, b in j.items(): #a is key of sub-dictionary and b is the values
        tf_table[a] = b / len_sent

    termfreq[i] = tf_table
#print(termfreq)

#Count no. of that word in a document
doc_word_count = {}
for i, j in freq_in_sent.items():
    for a, b in j.items():
        if a in doc_word_count:
            doc_word_count[a] += 1
        else:
            doc_word_count[a] = 1
#print(doc_word_count)

#Inverse document frequency matrix
idf_matrix = {}

for i, j in freq_in_sent.items():
    idf_table = {}

    for a in j.keys():
        idf_table[a] = math.log10(len_sents / float(doc_word_count[a]))

    idf_matrix[i] = idf_table
#print(idf_matrix)


#Term freq and IDF matrix together
tf_idf_matrix = {}
for (i1, j1), (i2, j2) in zip(termfreq.items(), idf_matrix.items()):
    tf_idf_table = {}

    for (a1, b1), (a2, b2) in zip(j1.items(), j2.items()):  
        tf_idf_table[a1] = float(b1 * b2)

    tf_idf_matrix[i1] = tf_idf_table
#print(tf_idf_matrix)


#Assigning a score to each sentence based on tf_idf matrix
sentence_scores = {}
for i, j in tf_idf_matrix.items():
    score_sent = 0
    len_sent = len(j)
    
    for a, b in j.items():
        score_sent += b
    if len_sent !=0:
        #print(score_sent, " ", len_sent)
        sentence_scores[i] = score_sent / len_sent
    else:
        sentence_scores[i]=0
#print(sentence_scores)
        
estimated_scores = sentence_scores

#Getting the max score of a sentence
max_score = 0
for i in estimated_scores:
    if estimated_scores[i]>max_score:
        max_score = estimated_scores[i]

#sumValues = 0
#for i in sentence_scores:
#    sumValues += sentence_scores[i]


# Taking 40% of the max score as threshold
threshold = max_score*0.4
#print("Threshold is - " ,threshold)


#Adding sentences to summary based on threshold    
summary = []
for i in sents:
    if i[:10] in sentence_scores and sentence_scores[i[:10]] >= (0.75*threshold):
        summary.append(i)
        
        
#Separating sentences using | 
summary = '।'.join(summary)

print('\nSummarized Text = ',summary)
print('Summarized Text no. of words= ', len(summary.split()))
