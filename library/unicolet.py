from __future__ import absolute_import, division, print_function
from ansible_collections.ansible.netcommon.plugins.plugin_utils.httpapi_base import HttpApiBase
import json

__metaclass__ = type

DOCUMENTATION = """
author: @unicolet
name: unicolet
short_description: fake unicolet platform support
description:
- Just playing around with ansible network plugins
version_added: 1.0.0
"""

class HttpApi(HttpApiBase):
    def __init__(self, *args, **kwargs):
        super(HttpApi, self).__init__(*args, **kwargs)
        self._device_info = None
        self._module_context = {}

    def read_module_context(self, module_key):
        if self._module_context.get(module_key):
            return self._module_context[module_key]
        return None

    def save_module_context(self, module_key, module_context):
        self._module_context[module_key] = module_context
        return None

    def send_request(self, data, **message_kwargs):
        return None

    def get_device_info(self):
        if self._device_info:
            return self._device_info
        device_info = {}
        device_info["network_os"] = "unicolet"
        self._device_info = device_info
        return self._device_info

    def get_device_operations(self):
        pass

    def get_capabilities(self):
        result = {}
        return json.dumps(result)

    # Shims for resource module support
    def get(self, command, output=None):
        # This method is ONLY here to support resource modules. Therefore most
        # arguments are unsupported and not present.
        return self.send_request(data=command, output=output)

    def edit_config(self, candidate):
        # This method is ONLY here to support resource modules. Therefore most
        # arguments are unsupported and not present.
        responses = self.send_request(candidate, output="config")
        return [resp for resp in to_list(responses) if resp != "{}"]
