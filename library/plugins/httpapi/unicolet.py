#!/usr/bin/python
from __future__ import absolute_import, division, print_function
import logging
from ansible_collections.ansible.netcommon.plugins.plugin_utils.httpapi_base import HttpApiBase
import json

__metaclass__ = type

DOCUMENTATION = """
author: unicolet
name: unicolet
short_description: fake unicolet platform support
description: just playing around with ansible network plugins
version_added: 1.0.0
"""

logging.basicConfig(filename='/tmp/unicolet.log', filemode='a', level=logging.DEBUG)

class HttpApi(HttpApiBase):
    def __init__(self, *args, **kwargs):
        logging.debug("loaded httpapi")
        super(HttpApi, self).__init__(*args, **kwargs)
        self._device_info = None

    def send_request(self, data, **message_kwargs):
        """Prepares and sends request(s) to device."""
        pass

    def get_device_info(self):
        logging.error("get_device_info")
        if self._device_info:
            return self._device_info
        device_info = {}
        device_info["network_os"] = "unicolet"
        self._device_info = device_info
        return self._device_info
