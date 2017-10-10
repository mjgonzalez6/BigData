from mrjob.job import MRJob
from mrjob.step import MRStep
from mrjob.protocol import JSONValueProtocol
import re
import itertools
import csv
from pprint import pprint
import json
from collections import Counter
import re, string, timeit
import string


class reduceData(MRJob):


    def mapper_reviews(self, _, line):
        line = obj = json.loads(line)

        try:
            act_text = line['text'].encode("utf-8")
        except:
            pass
        #Remover signos de puntuacion
        clean_text = act_text.translate(None, string.punctuation)
        #Split simple por espacios
        i_words = clean_text.split(" ")
        for word in i_words:
            yield word.encode("utf-8"), line['text']

    #Palabras usadas una sola vez por texto
    def reducer_individual_word(self, i_words, text):
        for word in i_words:
            #Hago un set para buscar las palabras únicas
            word_set = set(word)
            count = len(word_set)
            i = 0
            if count == 1:
                yield word_set[i]
                i+=1
            #Agrego las palabras repetidas al set

    def reducer_text(self, word_set, line):
        yield [line['text'],word_set ]


    def steps(self):
        return [MRStep(mapper=self.mapper_reviews), MRStep(reducer=self.mapper_reviews()), MRStep(reducer=self.reducer_text())]

if __name__ == '__main__':
    reduceData.run()

