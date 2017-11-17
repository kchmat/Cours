#!/etc/bin/python
# -*- coding: utf-8 -*-
import os
from ansible.module_utils.basic import *

def main():
    module = AnsibleModule(
        argument_spec=dict(
            path=dict(required=True),
            cont=dict(required=True),
            emplacement=dict(required=False, default="/TMP/Mod1.txt"),
        ),
        supports_check_mode=True
    )

    # Retrieving parameters value
    path = module.params['path']
    cont = module.params['cont']
    emplacement = module.params['emplacement']

    # Check if paths are valid

    if not os.path.exists(path):
        os.system("mkdir {0}".format(path))
        os.system(" {0} >> /{1}/{2}".format(cont, path, emplacement))
        module.exit_json(changed=True, msg=path+"est cree")
    elif os.path.exists(path):
        os.system(" {0} le dossier existe >> /{1}/{2}".format(cont, path, emplacement))
    else:
        module.fail_json(msg=path+" exists")

if __name__ == '__main__':
    main()
