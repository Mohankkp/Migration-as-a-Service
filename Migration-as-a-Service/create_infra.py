import os
import datetime
import yaml

# Path to directories
PATH_ANSIBLE = "/root/Migration-as-a-Service/src/southbound/ansible/"
PATH_PARSER = "/root/Migration-as-a-Service/parser_scripts/"

tenant='t5.yml'
dir_name = tenant.split(".")
yaml_file = "/root/Migration-as-a-Service/src/northbound/config_files/infrastructure/t5.yml"

with open(yaml_file, 'r') as file:
    yaml_content = yaml.safe_load(file)

# Check files for infrastructure build
os.system("python3 " + str(PATH_PARSER) + "parse_tenant.py " + str(tenant))
print("Tenant build infra")

# Make infra Cloud 1
os.system("ansible-playbook " + str(PATH_ANSIBLE) + "create_infra_C1.yml -i " + str(PATH_ANSIBLE) + "inventory --extra-vars 'tenant_name=" + str(dir_name[0]) + "' -vvv") 
print("Cloud 1 infra created")

# routes in cloud 1
#os.system("ansible-playbook " + str(PATH_ANSIBLE) + "routes_C1.yml -i " + str(PATH_ANSIBLE) + "inventory --extra-vars 'tenant_name=" + str(dir_name[0]) + "' -v")
#print("Add routes Cloud 1")

# Make VM templates on cloud 1
os.system("ansible-playbook " + str(PATH_ANSIBLE) + "create_vm_C1_templates.yml -i " + str(PATH_ANSIBLE) + "inventory --extra-vars 'tenant_name=" + str(dir_name[0]) + "' -v")
print("Make VM template C1")

# Make VMs in cloud 1
os.system("ansible-playbook " + str(PATH_ANSIBLE) + "create_vm_C1.yml -i " + str(PATH_ANSIBLE) + "inventory --extra-vars 'tenant_name=" + str(dir_name[0]) + "' -v") 
print("Make VMs C1")
