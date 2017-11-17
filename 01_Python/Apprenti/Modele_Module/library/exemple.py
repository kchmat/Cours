#!/etc/bin/python
from ansible.module_utils.basic import *
def main():
   module = AnsibleModule(
        argument_spec=dict(
            path=dict(required=True),
        ),
        supports_check_mode=True
    )
     Retrieving parameters value
    path = module.params['path']

    # Check if paths are valid

    if not os.path.exists(path):
        os.system("mkdir {0}".format(path))
        module.exit_json(changed=True, msg=path+"est cree")

    else:
        module.fail_json(msg=path+" exists")


if __name__ == '__main__':
    main()
