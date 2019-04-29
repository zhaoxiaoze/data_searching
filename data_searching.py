from urllib.request import urlopen
import re
import string
import operator


words = ["the", "be", "and", "of", "a", "in", "to", "have", "it", "i", "that",
         "for", "you", "he", "with", "on", "do", "say", "this", "they", "is",
         "an", "at", "but", "we", "his", "from", "that", "not", "by", "she",
         "or", "as", "what", "go", "their", "can", "who", "get", "if", "would",
         "her", "all", "my", "make", "about", "know", "will", "as", "up", "one",
        "time", "has", "been", "there", "year", "so", "think", "when", "which",
        "them", "some", "me", "people", "take", "out", "into", "just", "see",
        "him", "your", "come", "could", "now", "than", "like", "other", "how",
        "then", "its", "our", "two", "more", "these", "want", "way", "look",
        "first", "also", "new", "because", "day", "more", "use", "no", "man",
        "find", "here", "thing", "give", "many", "well",]

def clean_input(input):

    input = re.sub('\n+' ,' ', input).lower()
    input = re.sub('\[[0-9]*\]', '', input)
    input = re.sub(' +',' ', input)
    input = bytes(input,'UTF-8')
    input = input.decode('ascii', 'ignore')

    cleanInput = []
    input = input.split(' ')

    for item in input:

        item = item.strip(string.punctuation)

        if len(item) > 1 or item.lower() == 'a' or item.lower() == 'i':

            cleanInput.append(item)

    return cleanInput


def getNgram(input,n):

    input = clean_input(input)

    output = {}

    num = len(input)


    for i in range(num - n + 1):

         ngramTemp = " ".join(input[i:i + n])

         check_word = ngramTemp.split(' ')

         if check_word[0] not in words and check_word[1] not in words :
        # ngramTemp = input[i] +' ' +  input[i + n]

             if ngramTemp not in output:

                 output[ngramTemp] = 0

             output[ngramTemp] +=1





    return output




'''
    for key in output.keys():
        
        content = key.split(' ')
        
        for word in words:
            
            if word != content[0]:
                
                if content not in clean_input:
                    clean_input[key] = 0
                clean_input[key] += 1
'''




content = str(urlopen("http://pythonscraping.com/files/inaugurationSpeech.txt").read(), 'UTF-8')

ngram = getNgram(content, 2)

sortedNgram = sorted(ngram.items(),key = operator.itemgetter(1), reverse = True)

print(sortedNgram)