# -*- coding: utf-8 -*-
"""
Created on Fri Sep 15 15:35:56 2017

@author: Gabriel
"""
def lyrics_to_frequencies(lyrics):
    '''
    lyrics: a string
    Returns: a dictionary containing what times a letter appear in the word
    '''
    myDict = {}
    for word in lyrics:
        if word in myDict:
            myDict[word] += 1
        else:
            myDict[word] = 1
    return myDict

result = lyrics_to_frequencies(input('What is the word? '))

def most_common_words(freqs):
    values = freqs.values()
    best = max(values)
    words = []
    for k in freqs:
        if freqs[k] == best:
            words.append(k)
    return (words, best)

def words_often(freqs, minTimes):
    result = []
    done = False
    while not done:
        temp = most_common_words(freqs)
        if temp[1] >= minTimes:
            result.append(temp)
            for w in temp[0]:
                del(freqs[w])
        else:
            done = True
    return result

print(result)
print(words_often(result, 3))