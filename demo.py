# -*- coding: utf-8 -*-
__author__ = "Johnnatan Messias"
__copyright__ = "Max Planck Institute for Software Systems - MPI-SWS"
__email__ = "johnme@mpi-sws.org"
__website__ = "http://johnnatan.me"
__status__ = "Done"

import json
import gzip
from political_leaning_api import Political_Leaning


demo = Political_Leaning(token="Your_Token_Here")


def main():
    inFile = gzip.open('input_test.gz')
    for line in inFile:
        data = json.loads(line)
        print('username=%s' % data['user']['screen_name'])
        print('\tresponse=%s' % demo.get_political_leaning(friends_ids=data['friend_ids']))
    inFile.close()

if __name__ == "__main__":
    main()
