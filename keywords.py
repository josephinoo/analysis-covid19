import os
keywords = ['coronavirus']
countries = ['Honduras,Tegucigalpa']
for country in countries:
    date = country.split(",")[0]
    for keyword in keywords:

        os.system(
            'twint --near '+country + " " + "--search " + keyword + "  -o " + date + "_" + keyword+'.json --json --since 2020-01-01')
