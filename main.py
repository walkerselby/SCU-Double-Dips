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
        'referer': 'https://www.scu.edu/apps/courseavail/?p=schedule',
        'accept-language': 'en-US,en;q=0.9',
        'cookie': 'SignOnDefault=; loginPopover=read; SESSION_LANGUAGE=eng; III_EXPT_FILE=aa17264; III_SESSION_ID=4419cd24129ce1947a0444bdbdd24794; III_ENCORE_PATRON=scu.edu; amplitude_id_9f6c0bb8b82021496164c672a7dc98d6_edmscu.edu=eyJkZXZpY2VJZCI6IjliMjcwOWIzLTE3NDctNDMxZi04MjE1LTdhODk5NTVkNGJiYVIiLCJ1c2VySWQiOm51bGwsIm9wdE91dCI6ZmFsc2UsInNlc3Npb25JZCI6MTY0MzgzNjE2NTcwMywibGFzdEV2ZW50VGltZSI6MTY0MzgzNjk3NTQ2MiwiZXZlbnRJZCI6MCwiaWRlbnRpZnlJZCI6NDksInNlcXVlbmNlTnVtYmVyIjo0OX0=; ezproxy=Dr0fSBm893R2RAo; ezproxyl=Dr0fSBm893R2RAo; ezproxyn=Dr0fSBm893R2RAo; AMCVS_4D6368F454EC41940A4C98A6%40AdobeOrg=1; AMCV_4D6368F454EC41940A4C98A6%40AdobeOrg=-2121179033%7CMCIDTS%7C19033%7CMCMID%7C24484561547074975815274812047936128197%7CMCAID%7CNONE%7CMCOPTOUT-1644435226s%7CNONE%7CvVersion%7C5.3.0; PS_TokenSite=https://ecampus.scu.edu/psp/csprd92/?csprdw5-80-PORTAL-PSJSESSIONID; SimpleSAMLAuthToken=_8c9eabb496aa7d81337bf4503c23b811c6625a5773; PS_DEVICEFEATURES=maf:0 width:1792 height:1120 clientWidth:988 clientHeight:1161 pixelratio:1.7999999523162842 touch:0 geolocation:1 websockets:1 webworkers:1 datepicker:1 dtpicker:1 timepicker:1 dnd:1 sessionstorage:1 localstorage:1 history:1 canvas:1 svg:1 postmessage:1 hc:0; csprdw5-80-PORTAL-PSJSESSIONID=GPz2TVxr6vxk870VwYZlmVagcarlhjEr!43749935; ExpirePage=https://ecampus.scu.edu/psp/csprd92/; PS_LOGINLIST=https://ecampus.scu.edu/csprd92; PS_TOKEN=pQAAAAQDAgEBAAAAvAIAAAAAAAAsAAAABABTaGRyAk4Abwg4AC4AMQAwABQrfs+Pv0dH7SxPux8i3iL1yFzqJWUAAAAFAFNkYXRhWXicJYw7CoAwEAUnKlYWXiRiPkasRexsglh6BC/o4XzEXXbmwS77AE1dGSO/FaX6C0fSTHii3G4c7HSZlZNbzETPqLXHFludhULHoJTEPy+lg57N8AFe8wsY; PS_LASTSITE=https://ecampus.scu.edu/psp/csprd92/; ps_theme=node:SA portal:EMPLOYEE theme_id:DEFAULT_THEME_FLUID css:DEFAULT_THEME_FLUID accessibility:N formfactor:3 piamode:2; psback=%22%22url%22%3A%22https%3A%2F%2Fecampus.scu.edu%2Fpsc%2Fcsprd92%2FEMPLOYEE%2FSA%2Fc%2FNUI_FRAMEWORK.PT_AGSTARTPAGE_NUI.GBL%3FCONTEXTIDPARAMS%3DTEMPLATE_ID%253aPTPPNAVCOL%26scname%3DSCU_SCU_CLASS_ENROLLMENT_CLASS%26PanelCollapsible%3DY%26PTPPB_GROUPLET_ID%3DSCU_ENROLLMENT_CLASSIC%26CRefName%3DSCU_ENROLLMENT_CLASSIC%22%20%22label%22%3A%22Enrollment%20Dates%22%20%22origin%22%3A%22PIA%22%20%22layout%22%3A%220%22%20%22refurl%22%3A%22https%3A%2F%2Fecampus.scu.edu%2Fpsc%2Fcsprd92%2FEMPLOYEE%2FSA%22%22; PS_TOKENEXPIRE=14_Feb_2022_03:36:36_GMT; SimpleSAML=276e2b1ec67c597445ce2c8616d93488'
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

    for course in courses:
        #Checking if there are multiple cores for a course.
        if "," in courses.get(course).get("core"):
            row = [courses.get(course).get("course"),courses.get(course).get("name"),courses.get(course).get("core")]
            #Formatting Output
            print("{: <10} \t {: <30} \t {: <40}".format(*row))

