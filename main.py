import csv 
import requests
import os

def get_courses(core):
    # 4400 is the value for Fall Quarter 2022.
    url = "https://www.scu.edu/apps/ws/courseavail/search/4400/ugrad"

    payload = f"newcore={core}&maxRes=10000"
    headers = {
        "authority": "www.scu.edu",
        "accept": "*/*",
        "x-requested-with": "XMLHttpRequest",
        "user-agent": os.getenv("USER_AGENT"),
        "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
        "sec-gpc": "1",
        "origin": "https://www.scu.edu",
        "sec-fetch-site": "same-origin",
        "sec-fetch-mode": "cors",
        "sec-fetch-dest": "empty",
        "accept-language": "en-US,en;q=0.9",
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    data = response.json()
    return data


if __name__ == "__main__": 
    courses = {}

    # Core Codes
    coreDict = {
             "I_PTHAMS": "American Studies (Pathway)",
             "I_PTHAE": "Applied Ethics (Pathway)",
             "I_PTHB": "Beauty (Pathway)",
             "I_PTHCHD": "Children, Family, & Society (Pathway)",
             "I_PTHCINST": "Cinema Studies (Pathway)",
             "I_PTHDEM": "Democracy (Pathway)",
             "I_PTHDT": "Design Thinking (Pathway)",
             "I_PTHFHP": "Feeding the World (Pathway)",
             "I_PTHGGE": "Gender, Globalization & Empire (Pathway)",
             "I_PTHGSB": "Gender, Sexuality & the Body (Pathway)",
             "I_PTHGB": "Global Health (Pathway)",
             "I_PTHHR": "Human Rights (Pathway)", 
             "I_PTHIS": "Islamic Studies (Pathway)",
             "I_PTHJA": "Justice and the Arts (Pathway)",
             "I_PTHLSJ": "Law & Social Justice (Pathway)",
             "I_PTHLPOSC": "Leading People, Org & Soc Chng (Pathway)",
             "I_PTHPS": "Paradigm Shifts (Pathway)",
             "I_PTHPR": "Politics & Religion (Pathway)",
             "I_PTHRPSI": "Race Place & Soc Inequalities (Pathway)",
             "I_PTHS": "Sustainability (Pathway)",
             "I_PTHDA": "The Digital Age (Pathway)",
             "I_PTHVST": "Values Science Technology (Pathway)",
             "I_PTHV": "Vocation (Pathway)",
             "I_AW": "Advanced Writing",
             "E_ARTS": "Arts",
             "E_CE": "Civic Engagement",
             "F_CTW1": "Critical Thinking and Writing 1",
             "F_CTW2": "Critical Thinking and Writing 2",
             "F_CI1": "Cultures and Ideas 1",
             "F_CI2": "Cultures and Ideas 2",
             "E_CI3": "Cultures and Ideas 3",
             "E_DV": "Diversity",
             "E_ETH": "Ethics",
             "I_EL": "Experiential Learning for Social Justice",
             "F_RTC1": "Religion Theology & Culture 1",
             "E_RTC2": "Religion Theology & Culture 2",
             "E_RTC3": "Religion Theology & Culture 3",
             "E_STS": "Science Technology & Society",
             "E_SOSC": "Social Science",
             "E_ARTSPAR": "Partial Credit Arts",
             "E_CEPAR": "Partial Credit Civic Engagement",
             "E_STSPAR": "Partial Credit Engineering, Math, CS"
    }

    for core in coreDict:
        print(f"Fetching {coreDict[core]} . . .")

        # Fetch course data and add it to dict
        data = get_courses(core)
        for info in data["results"]:
            if info["class_nbr"] in courses:
                newCore = f"{courses.get(info['class_nbr']).get('core')}, {coreDict[core]}"
                courses.get(info["class_nbr"]).update({"core": newCore})
            else:
                newCourse = {
                    "course": f"{info['subject']} {info['catalog_nbr']} ({info['class_nbr']})",
                    "name": info["class_descr"],
                    "core": coreDict[core]
                }
                courses.update({info["class_nbr"]: newCourse})


    rows = ["COURSE TAG", "COURSE NAME", "CORES SATISFIED"] 

    with open("scu_double_dips-fall_2022.csv", "w") as csv_file: 
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(rows) # write header

        for course in courses:

            # Checking if there are multiple cores for a course.
            if "," in courses.get(course).get("core"):   
    
                main_stuff =  [ courses.get(course).get("course"), courses.get(course).get("name"), courses.get(course).get("core") ]
                
                csv_writer.writerow([main_stuff[0], main_stuff[1], main_stuff[2]]) # write each item
