#!/etc/bin/python
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

from ansible.module_utils.basic import *


#################################################main() is the entrypoint into your module.
def main():
  
#AnsibleModule comes from from ansible.module_utils.basic import *. It has to be imported with the *

    module = AnsibleModule(argument_spec={})
    response = {"hello": "world"}
    module.exit_json(changed=False, meta=response)
#AnsibleModule helps us handle incoming parameters and exiting the program (module.exit_json())


if __name__ == '__main__':  
    main()

    
# on utilise le module ansible par :
- module_name: parameters
