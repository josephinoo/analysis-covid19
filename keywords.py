import os
keywords = ['coronavirus', 'pandemia']
countries = ['Caracas,Venezuela', 'Lima,Peru', 'Colombia', ""]
for keyword in keywords:
    os.system(
        'twint --near Lima,Peru --search '+keyword+'  -o Lima_Peru_'+keyword+'.csv --csv --since 2020-01-01')
