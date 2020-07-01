# -*- coding: utf-8 -*-
__author__ = "Johnnatan Messias"
__copyright__ = "Max Planck Institute for Software Systems - MPI-SWS"
__email__ = "johnme@mpi-sws.org"
__website__ = "http://johnnatan.me"
__status__ = "Done"

import requests
import traceback

nerros_permited = 3


class Political_Leaning:
    def __init__(self, token):
        self.api = "https://twitter-app.mpi-sws.org/search-political-bias-of-users/api/political_leaning.php"
        self.params = {'token': token}

    def get_political_leaning(self, friends_ids=[]):
        ans = {}
        nerr = 0
        data = ','.join([str(id_) for id_ in friends_ids])
        try:
            while nerr < nerros_permited:
                rq = requests.post(self.api, data=data,
                                   params=self.params, timeout=30)
                if rq.status_code != 200:
                    nerr += 1
                else:
                    ans = rq.json()
                    break
                rq.connection.close()
        except Exception as e:
            print("API ERROR\t" + str(e))
            print(traceback.print_exc())
        return ans
