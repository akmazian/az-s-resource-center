import requests
import json

def get_headers():
    return {
        'Authorization': 'Bearer 117C171D-B15F-4438-8F67-E3D9015EBDDF',
        'Accept': 'application/json'
        }

def get_departments(college: str) -> None:
    # assert college in ['be']

    url = 'https://ws.admin.washington.edu/student/v5/department.json'
 
    querystring = {
        'college_abbreviation': college,
        'sort_by': 'on'
    }

    headers = get_headers()

    response = requests.request("GET", url, headers=headers, params=querystring)
    response_dict = json.loads(response.text)
    response_json = json.dumps(response_dict, indent=4)

    f = open(f"{college.capitalize()} Departments", "x")
    f.write(response_json)

get_departments('inform')