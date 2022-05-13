def get_courses(core):
    #4400 is the value for Fall Quarter 2022.
    url = "https://www.scu.edu/apps/ws/courseavail/search/4400/ugrad"

    payload = "newcore=" + core + "&maxRes=10000"
    headers = {
        'authority': 'www.scu.edu',
        'accept': '*/*',
        'x-requested-with': 'XMLHttpRequest',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'sec-gpc': '1',
        'origin': 'https://www.scu.edu',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'accept-language': 'en-US,en;q=0.9',
            }

    response = requests.request("POST", url, headers=headers, data=payload)
    data = response.json()
    return data


if __name__ == '__main__':
    import requests

    courses = {}

    #Core Codes
    coreDict = {"I_AW": "Advanced Writing",
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
             "E_SOSC": "Social Science"
    }

    for core in coreDict:
        print("Fetching " + coreDict[core] + " . . .")

        #Fetch course data and add it to dict
        data = get_courses(core)
        for info in data["results"]:
            if info['class_nbr'] in courses:
                newCore = courses.get(info['class_nbr']).get("core") + ", " + coreDict[core]
                courses.get(info['class_nbr']).update({"core": newCore})
            else:
                newCourse = {
                    "course": info['subject'] + " " + info['catalog_nbr'],
                    "name": info['class_descr'],
                    "core": coreDict[core]
                }
                courses.update({info['class_nbr']: newCourse})

    print("\nDouble Dip Courses:\n")
    for course in courses:
        #Checking if there are multiple cores for a course.
        if "," in courses.get(course).get("core"):
            row = [courses.get(course).get("course"),courses.get(course).get("name"),courses.get(course).get("core")]
            #Formatting Output
            print("{: <10} \t {: <30} \t {: <40}".format(*row))

