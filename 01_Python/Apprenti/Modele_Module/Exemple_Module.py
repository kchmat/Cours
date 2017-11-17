#!/etc/bin/python
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
