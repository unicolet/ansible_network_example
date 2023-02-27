#!/usr/bin/python
from __future__ import absolute_import, division, print_function
import logging
from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.connection import Connection

__metaclass__ = type


DOCUMENTATION = """
module: unicolet_ping
short_description: Tests reachability
description:
- Tests reachability
version_added: 1.0.0
"""

logging.basicConfig(filename='/tmp/unicolet_ping.log', filemode='a', level=logging.DEBUG)

def verify_reachability(module):
    logging.debug("running verify_reachability")
    connection = Connection(module._socket_path)
    result = connection.get_device_info()
    logging.debug(result)
    return {"changed": False}
    # module.fail_json(
    #     msg="Not implemented yet."
    # )


def main():
    module = AnsibleModule(argument_spec=dict(), supports_check_mode=True)
    results = verify_reachability(module)
    module.exit_json(**results)


if __name__ == "__main__":
    main()
