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

class UsersCount(MRJob):
    def mapper_userid(self, _, line):
        line = obj = json.loads(line)
        try:
            user = line['user_id']
            business = line['business_id']
        except:
            pass

        yield user, business

#Reducers de los usuarios que han hecho reviews del mismo negocio
    def reducer(self, user_id, business_id):
        business_list = [b for b in business_id]
        n_business = len(business_list)
        for business_id in business_list:
            yield business_id, tuple([user_id, n_business])

    def reducer2(self,business, extendend_userid):
        for combination in itertools.combinations(extendend_userid,2):
            sorted = sorted(combination)
            yield sorted, 1

    def reducer3(self,key, values):
        yield 'MAX', sum(values)*1.0/(key[0][1] + key[1][1] - sum(values))

    def reducer4(self, key, values):
        yield[key, max(values)]


    def steps(self):
        return [MRStep(mapper=self.mapper_userid, reducer=self.reducer),
                MRStep(reducer = self.reducer2),
                MRStep(reducer = self.reducer3),
                MRStep(reducer = self.reducer4)]


if __name__ == '__main__':
    UsersCount.run()