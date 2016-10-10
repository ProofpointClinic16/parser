import json
from pprint import pprint


def parse(filename):
    data = []

    with open(filename) as f:
        for line in f:
            line = line.replace("u'","\"")
            line = line.replace("u\"", "\"")
            line = line.replace("':", "\":")
            line = line.replace("',", "\",")
            line = line.replace("']", "\"]")
            line = line.replace("'}", "\"}")
            line = line.replace(" date", " \"date")
            line = line.replace("),", ")\",")
            line = line.replace(")',", ")\",")
            line = line.replace("None", "\"None\"")
            line = line.replace("Object", "\"Object")

            data += [json.loads(line)]

    pprint(data)


def test():
    parse('sample.txt')
