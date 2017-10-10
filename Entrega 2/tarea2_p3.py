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

import sys, os, re


class MRJoin(MRJob):
    SORT_VALUES = True

    def mapper(self, _, line):
        line = obj = json.loads(line)
        try:
            business = line['business_id'].encode("utf-8")
            user = line['user_id'].encode("utf-8")
        except:
            pass

        yield user, [business]

    def reducer(self, key, values):
        value = [x for x in values]
        if len(values > 1):
            user = values[0]
            for value in values[1:]:
                yield key, [user, value]
            else:
                pass

def steps(self):
        return [MRStep(mapper=self.mapper, reducer=self.reducer)]




if __name__ == '__main__':
  MRJoin.run()
