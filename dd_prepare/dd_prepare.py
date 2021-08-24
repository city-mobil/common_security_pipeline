import defectdojo_apiv2
import os
import json
from datetime import date
from pprint import pformat, pprint
import requests

print('[x] dd_prepare.py has started')
dd_base_url = os.environ.get('DD_BASE_URL',"https://defectdojo.example.com") #FIX IT
dd_auth_key = os.environ.get('DD_AUTH_KEY', "INSERT_HERE_DD_RANDOM_TOKEN")  #FIX IT
project_name = os.environ.get('CI_PROJECT_PATH_SLUG', 'debug_project1')
project_url = os.environ.get('CI_PROJECT_URL', 'common_security/debug_1')
pipeline_id = os.environ.get('CI_PIPELINE_ID', 'debug_engagment2')
username = os.environ.get('GITLAB_USER_LOGIN', 'SameName')
os

def handle_dd_responce(resp, context='', exit_on_error=False):
    if resp.response_code not in (200, 201) or resp.success != True or isinstance(resp.data, str):
        if context:
            context = f', context: {context}'
        print(f'[!] Error. Message: {resp.message}. Status_code: {resp.response_code}, data: {pformat(resp.data)}, {context}')
        if exit_on_error:
            exit(1)
        if isinstance(resp.data, dict) or isinstance(resp.data, list):
            return resp.data
        try:
            return json.loads(resp.data)
        except:
            return {'error': str(resp.data)}
    #return jsop data if all good
    return resp.data

dd = defectdojo_apiv2.DefectDojoAPIv2(dd_base_url, dd_auth_key, username, api_version="v2",  verify_ssl=False, timeout=360)

#check if product already exist
result = dd.list_products(name=project_name)
result = handle_dd_responce(result, project_name)
if result.get('count') == 1:
    print(f'[x] Product {project_name} already exist')
    #get product_id
    product_id = result.get('results')[0].get('id')
else:
    #create product if not exist
    result = dd.create_product(project_name, project_url, 1)
    result = handle_dd_responce(result, project_name)
    print(f'[x] Create product {project_name}')
    # get product_id
    product_id = result.get('id')


#name, product_id, lead_id, status, target_start, target_end,
resp = dd.create_engagement(pipeline_id, product_id, date.today().strftime('%Y-%m-%d'), date.today().strftime('%Y-%m-%d'))
result = handle_dd_responce(resp, exit_on_error=True)
engagment_name = result.get("name", 'ci_reporter: unkown_error')
engagment_id = result.get('id')
print(f'[x] Create engagment. Id: {str(engagment_id)}, Name: {result.get("name")}')
print(f'[x] Check product at {dd_base_url}/product/{str(product_id)}')
print(f'[x] Check engagment at {dd_base_url}/engagement/{str(engagment_id)}')#






#save data
with open('security_variables.env', 'a+') as f:
    f.write(f'\nDD_PRODUCT_ID={product_id}\nDD_ENGAGEMENT_ID={engagment_id}')
    f.write(f'\nDD_BASE_URL={dd_base_url}\nDD_AUTH_KEY={dd_auth_key}')
    f.write(f'\nCI_PROJECT_PATH_SLUG={project_name}\nCI_PROJECT_URL={pipeline_id}')
    f.write(f'\nCI_PIPELINE_ID={pipeline_id}\nGITLAB_USER_LOGIN={username}')
    f.write(f'\nDD_ENGAGMENT_NAME={engagment_name}\nDD_PROJECT_ENV=Default')



#CI_PROJECT_PATH
