#!/usr/bin/env python
"""Naive Bayes Classifier

Usage:
    main.py    TRAIN TEST VOCAB [--ipython | -h]

Arguments:
    train        the training data prefix
    test         the testing data prefix
    vocab        the vocabulary file

Options:
    -h, --help     Show this screen.
    --ipython      using ipython notebook and we want to print figures; not save them
"""
from docopt import docopt

"""
main.py is the main entry point for the classifier.
"""
import csv

# graph tool
try:
    import numpy as nx
except ImportError:
    raise ImportError("This program requires Numpy and Matplotlib")


__author__ = "Aaron Gonzales"
__copyright__ = "GPL"
__license__ = "GPL"
__maintainer__ = "Aaron Gonzales"
__email__ = "agonzales@cs.unm.edu"


def read_file(filename, delim=' '):
    """ Reads a file and fills a list with that data.
        Args:
            filename (str) : path to the file you want to open
            delim (str): a delimiter for the file
    """
    data_list = []
    with open(filename, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=delim)
        for line in reader:
            data_list.append(line)
    return data_list


def main(_args):
    """ Drives the program."""
    if _args["--ipython"]:
        print("Ipython session selected; no saving of figures will happen")
    print("--------Training File: {computer}".format(computer=_args["TRAIN"]))
    print("--------Testing File: {computer}".format(computer=_args["TEST"]))

    train_data = read_file(_args['TRAIN'] + '.data')
    vocab_file = _args['VOCAB']



if __name__ == "__main__":
    main(docopt(__doc__))

