This project aims to summarize any given Telugu text of any size by making use of TF_IDF matrix i.e. Term Frequency and Inverse Document Frequency matrix. The project was originally referenced from a Nepali Summarizer(https://github.com/himalayan-sanjeev/Nepali_Text_Summarization_Extractive#readme) which uses the same methodology to summarize Nepali text

The procedure is as follows-
1. The text file containing the Telugu text is taken as input. All of the \n or newline characters are converted to spaces for easier text processing
2. The text is divided into sentences using | as a delimiter, and into words using space as a delimiter
3. The frequency of all the words in a sentence is taken. This is achieved by creating a new dictionary, iterating through the sentences and using the first 10 characters of the sentence as the key for that specific sentence. Then the frequency for each word in that sentence is calculated by iterating through all the words in the sentence (stopwords are omitted). This is repeated for all sentences
4. Term frequency of every word in a sentence is calculated by dividing the frequency of a word by the sentence's length. Term frequency is the measure of how often a word is repeated in a given sentence/document
5. Inverse Document Frequency of all words in a sentence is calculated by logging the length of the sentence with the count of words in that sentence/document. IDF is a measure of how rare or common a word is in that sentence/document (math.log10(len_sents / float(doc_word_count[a])))
6. TF_IDF matrix is created. This is done by multiplying the Term frequency and Inverse Document Frequency of the same word in a sentence. This matrix is what decides how important or relevant a sentence is for the given document
7. A score is assigned to each sentence. This is achieved by taking a sentence and adding all of the TF_IDF values in that sentence and then dividing that sum with the length of the sentence (sentence_scores[i] = score_sent / len_sent)
8. The maximum score is calculated by duplicating the sentence scores dictionary and then finding the maximum value in that list
9. The threshold is calculated by taking 40% of the maximum score
10. The sentences are summarized. This is done by iterating through all of the sentences and appending the sentences with a score higher that the threshold into the summary
11. The summary is joined using | to depict the end of a sentence

Note:
The length of both original text and the summarized text is given for comparison. The Threshold is modifiable 
