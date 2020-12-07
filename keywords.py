import os 
keywords = ['coronavirus', 'pandemia', "covid 19", "cuarentena", "casos"]
countries = ['Honduras,Tegucigalpa',
             'Nicaragua,Managua', 'Panama,Panama', 'Paraguay,Asuncion', 'Uruguay,Montevideo']
for country in countries:
    date = country.split(",")[0]
    for keyword in keywords:

        os.system(
            'twint --near '+country + " " + "--search " + keyword + "  -o " + date + "_" + keyword+'.csv --csv --since 2020-01-01')
