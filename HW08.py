import requests


def highestPopulation(regionalBloc):
    response_population = requests.get('https://restcountries.com/v2/regionalbloc/{}'.format(regionalBloc))
    data_population = response_population.json()
    highest = 0
    highest_country = ''
    for element in data_population:
        country = element['name']
        population = element['population']
        if population > highest:
            highest = population
            highest_country = country

    return highest_country


def commonTimeZones(code1, code2):
    timeZoneResponse = requests.get('https://restcountries.com/v2/alpha?codes={},{}'.format(code1, code2))
    timeZoneData = timeZoneResponse.json()
    timezones = {}
    commonZones = []
    countries = [code1, code2]
    index = 0
    for element in timeZoneData:
        timezones[countries[index]] = element['timezones']
        index += 1
    for zone in timezones[code1]:
        if zone in timezones[code2] and (zone not in commonZones):
            commonZones.append(zone)

    if len(commonZones) == 0:
        return 'No Common Time Zones'
    else:
        return commonZones


def registerDomains(companyName, countryList):
    domains = []
    for country in countryList:
        try:
            countryInfo = requests.get('https://restcountries.com/v3.1/name/{}'.format(country))
            countryData = countryInfo.json()
            countryDomain = countryData[0]['tld'][0]
            companyDomain = companyName.lower() + str(countryDomain)
            domains.append(companyDomain)
        except:
            continue

    return domains


def findCountry(capitalList):
    dict = {}
    for capital in capitalList:
        capitalInfo = requests.get('https://restcountries.com/v3.1/capital/{}'.format(capital))
        capitalData = capitalInfo.json()
        dict[capital] = capitalData[0]['name']['common']

    return dict


def commonLanguages(regionalBloc):
    regionInfo = requests.get('https://restcountries.com/v2/regionalbloc/{}'.format(regionalBloc))
    regionData = regionInfo.json()
    languages = []
    dict = {}
    commonLangs = []
    highest = 0
    for country in regionData:
        for lang in country['languages']:
            languages.append(lang['name'])

    for lang in languages:
        if lang not in dict:
            dict[lang] = 1
        if lang in dict:
            dict[lang] += 1

    for lang in dict:
        if dict[lang] > highest:
            highest = dict[lang]

    for lang in dict:
        if dict[lang] == highest:
            commonLangs.append(lang)

    if len(commonLangs) == 1:
        return commonLangs[0]
    else:
        return sorted(commonLangs)
