#! /usr/bin/env python

import json
import os
import requests
import socket

HOSTNAME = socket.gethostname()
SYSTEM_LOAD = os.getloadavg()


def make_post(uri='http://localhost:5000/things', data=None):
    headers = {
        'Content-Type': 'application/json'
    }
    return requests.post(uri, data=data, headers=headers)


def main():
    for i in range(3):
        data = {
            'name': 'system_load',
            'device': HOSTNAME + str(i),
            'value': SYSTEM_LOAD
        }
        # print json.dumps(data, indent=4)
        response = make_post(data=json.dumps(data))
        print "Response Code: %s\n %s" % (response.status_code, response.text)


if __name__ == '__main__':
    main()
