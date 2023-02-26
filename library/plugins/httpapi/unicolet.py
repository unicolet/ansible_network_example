#!/usr/bin/python
from __future__ import absolute_import, division, print_function
from ansible_collections.ansible.netcommon.plugins.plugin_utils.httpapi_base import HttpApiBase
import json, logging
logging.basicConfig(filename='unicolet.log', filemode='a', level=logging.DEBUG)


__metaclass__ = type

DOCUMENTATION = """
author: unicolet
name: unicolet
short_description: fake unicolet platform support
description: just playing around with ansible network plugins
version_added: 1.0.0
"""

class HttpApi(HttpApiBase):
    def __init__(self, *args, **kwargs):
        logging.debug("loaded httpapi")
        super(HttpApi, self).__init__(*args, **kwargs)
        self._device_info = None
    
    def send_request(self, data, path, method='POST'):
        logging.debug("sending request")
        headers = {'Content-Type': 'application/json'}
        try:
            response, response_content = self.connection.send(path, data, method=method, headers=headers)
        except exc:
            return exc.code, exc.read()
        return handle_response(response_content)

    def update_auth(self, response, response_text):
        logging.debug("update auth")
        cookie = response.info().get('Set-Cookie')
        if cookie:
            return {'Cookie': cookie}
        return None

    def login(self, username, password):
        logging.debug("login")
        login_path = '/my/login/path'
        data = {'user': username, 'password': password}

        response = self.send_request(data, path=login_path)
        try:
            # This is still sent as an HTTP header, so we can set our connection's _auth
            # variable manually. If the token is returned to the device in another way,
            # you will have to keep track of it another way and make sure that it is sent
            # with the rest of the request from send_request()
            self.connection._auth = {'X-api-token': response['token']}
        except KeyError:
            raise AnsibleAuthenticationFailure(message="Failed to acquire login token.")

    def get_device_info(self):
        logging.debug("get_device_info")
        if self._device_info:
            return self._device_info
        device_info = {}
        device_info["network_os"] = "unicolet"
        self._device_info = device_info
        return self._device_info

def handle_response(response):
    logging.debug(response)
    return []
