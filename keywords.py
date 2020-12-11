import os
keywords = ['coronavirus', 'covid19', 'cuarentena', 'covid', 'contagios']
countries = ['Venezuela,Caracas', 'Colombia,Bogota']
for country in countries:
    date = country.split(",")[0]
    for keyword in keywords:

        os.system(
            'twint --near '+country + " " + "--search " + keyword + "  -o " + date + "_" + keyword+'.json --json --since 2020-01-01')
