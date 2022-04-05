# -*- coding: utf-8 -*-
"""
Created Wed Oct 18 2017
Updated Mon Oct 01 2018

Maps queries across multiple servers and reduces the result into a single
query output.

updated to python 3

@author: Eric Orenstein
@author: pldr
"""

from django.conf import settings

import numpy as np
from lxml import html
import urllib.request
from http import cookiejar
import json
from reducers import label_reducer, image_list_reducer
import sys

def do_login(opener,server_url):

    login_url = server_url+settings.CSRF_URL
    login_form = opener.open(login_url).read()

    csrf_token = html.fromstring(login_form).xpath(
            '//input[@name="csrfmiddlewaretoken"]/@value'
            )[0]

    # Values dictionary for login
    values = {
            'username': settings.MAP_USER_NAME,
            'password': settings.MAP_USER_PASSWORD
            }

    params = json.dumps(values)

    log_req = urllib.request.Request(server_url+settings.USER_LOGIN_URL,
        params.encode(), headers={'X-CSRFToken': str(csrf_token),
                       'X-Requested-With': 'XMLHttpRequest',
                       'User-agent': 'Mozilla/5.0',
                       'Content-type': 'application/json'
                       }
        )

    log_resp = opener.open(log_req)

    return csrf_token

def reduce_result(server_data,reducer=None):

    if reducer is None:
        output = []
        for data in server_data:
            output.extend(data)
        return output
    else:
    
        if reducer == 'label_reducer':
            return label_reducer(server_data)
        if reducer == 'image_list_reducer':
            return image_list_reducer(server_data)
        
        return server_data


def send_to_server(server_url,api_path,login_required=False,jdoc=None):
    """
    Connects to server and submits the jdoc, returns result

    :param server_url: the url for the server
    :param api_path: the path to the api call
    :param login_required: when True, a login attempt will be made
    :param jdoc: json document containing LabelSet to be moved to planktivore

    :return lab_resp: response from planktivore as string
    """


    print(server_url + '/' + api_path)

    # log into the server
    cj = cookiejar.CookieJar()
    opener = urllib.request.build_opener(
        urllib.request.HTTPCookieProcessor(cj),
        urllib.request.HTTPHandler(debuglevel=0)
    )

    if login_required:

        csrf_token = do_login(server_url)

    # send label request
    if jdoc:
        api_req = urllib.request.Request(server_url+'/' + api_path,
                jdoc.encode(),
                headers = {'X-CSRFToken': str(csrf_token),
                    'X-Requested-With': 'XMLHttpRequest',
                    'User-agent': 'Mozilla/5.0',
                    'Content-type': 'application/json'}
                )
        api_resp = opener.open(api_req)
    else:
        api_resp = opener.open(server_url+'/' + api_path)


    #print lab_resp.read()

    return api_resp.read()

def map_request(server_list,api_path):

    results = {}

    results['server_url'] = []
    results['data'] = []

    for server in server_list:
        try:
            reply = send_to_server(server,api_path)

            results['server_url'].append(server)
            results['data'].append(json.loads(reply.decode('utf-8')))

        except:
            pass

    return results


if __name__ == '__main__':

    def test_image_list():

        settings.configure(
            MAP_USER_NAME='spcbridge',
            MAP_USER_PASSWORD='c4lanu4',
            CSRF_URL='/admin/?next=/data/admin',
            USER_LOGIN_URL='/rois/login_user')


        print(settings)

        server_list = ['http://spc.ucsd.edu/data','http://planktivore.ucsd.edu/data']

        api_path = 'rois/images/SPCP2/1538380800000/1538467199000/0/24/50/67/1356/0.05/1/clipped/ordered/skip/Any/anytype/Any/Any/?page=2'

        results = map_request(server_list,api_path)

        #image_list = reduce_result(results,image_list_reducer)

        #print(image_list)

    if len(sys.argv) > 1:

        print(sys.argv[1])

        exec(sys.argv[1]+'()')
