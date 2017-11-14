#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Author: AEE
#
# Check for available space on a given path.
#

# Documentation
DOCUMENTATION = '''
---
version_added: "0.1"
module: folder_available
short_description: folder_available
description:
  - This module check if there's the TMP floder  available
options:
  path:
    description:
      path to check

notes:
requirements: []
author: AEE
'''

EXAMPLES = '''
- name: "folder available /TMP"
  folder_available: path=/TMP
'''

def main():
    # module declaration
    module = AnsibleModule(
        argument_spec=dict(
            path=dict(required=True),
        ),
        supports_check_mode=True
    )

    # Retrieving parameters value
    path = module.params['path']


    # Check if paths are valid

    if not os.path.exists(path):
        os.system("mkdir {0}".format(path))
        module.exit_json(changed=True, msg=path+"est cree")

    else:
        module.fail_json(msg=path+" exists")


# import module snippets
from ansible.module_utils.basic import *
if __name__ == '__main__':
    main()

