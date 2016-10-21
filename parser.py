import json
import re
from pprint import pprint


def parse(filename):
    data = []

    with open(filename) as f:
        for line in f:

            datum = {}

            resultObj = re.search( r"result': u'(.+?)'}", line).group(1)
            urlObj = re.search( r"url': u'(.+?)', ", line).group(1)

            datum['url'] = urlObj
            datum['result'] = resultObj

            data += [datum]

    pprint(data)
    return data


def test():
    parse('sample.txt')
