import sysconfig

import yaml


def read(filename):
    with open(filename, encoding='UTF-8') as f:
        file = yaml.full_load(f)
    return file


if __name__=='__main__':
    t = read('reported_words.yaml')
    print(t)