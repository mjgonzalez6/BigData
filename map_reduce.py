from mrjob.job import MRJob
from mrjob.step import MRStep
import simplejson
import json
import matplotlib.pyplot as plt
import numpy as np
from mrjob.protocol import JSONValueProtocol
import re
import itertools
import csv


class EstrellasCategoria(MRJob):


    def mapper_business_categories(self, _, line):
        line = obj = json.loads(line)
        business_id = line['business_id']
        stars_count = line['stars']
        #user_id = line['user_id']
       # category = line['categories']
        yield business_id, stars_count

    def reducer_business(self, stars_number, business_list):

        yield stars_number, sum(business_list)


    def max_reducer(self, stat, values):
        TEMP = [values]
        yield [stat, max(values)]

    def steps(self):

        return [MRStep(mapper=self.mapper_business_categories,
                       reducer=self.reducer_business), MRStep(reducer=self.max_reducer)]


if __name__ == '__main__':
    EstrellasCategoria.run()
