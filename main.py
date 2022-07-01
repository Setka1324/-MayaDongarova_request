import requests
import pandas as pd
import openpyxl

stations = ['aberporth','armagh','ballypatrick','bradford','braemar', 'camborne', 'cambridge', 'cardiff', 'chivenor', 'cwmystwyth', 'dunstaffnage', 'durham', 'eastbourne', 'eskdalemuir', 'heathrow', 'hurn','lerwick','leuchars','lowestoft','manston','nairn','newtonrigg','oxford','paisley','ringway','rossonwye','shawbury','sheffield','southampton','stornoway','suttonbonington','tiree','valley','waddington','whitby','wickairport','yeovilton']

for name in stations:
    
    r = requests.get('https://www.metoffice.gov.uk/pub/data/weather/uk/climate/stationdata/' + str(name) + 'data.txt')

    text = r.text

    text = text.split('\r\n')
    year_1 = []
    year_2 = []
    year_3 = []
    year_4 = []
    year_5 = []
    year_6 = []
    year_7 = []
    year_8 = []
    year_9 = []
    year_10= []
    year_11= []
    year_12= []


    parameter_1 = []
    parameter_2 = []
    parameter_3 = []
    parameter_4 = []
    parameter_5 = []
    parameter_6 = []
    parameter_7 = []
    parameter_8 = []
    parameter_9 = []
    parameter_10= []
    parameter_11= []
    parameter_12= []


    data_year_1 = { 'year' : year_1, 'parameter' : parameter_1}
    data_year_2 = { 'year' : year_2, 'parameter' : parameter_2}
    data_year_3 = { 'year' : year_3, 'parameter' : parameter_3}
    data_year_4 = { 'year' : year_4, 'parameter' : parameter_4}
    data_year_5 = { 'year' : year_5, 'parameter' : parameter_5}
    data_year_6 = { 'year' : year_6, 'parameter' : parameter_6}
    data_year_7 = { 'year' : year_7, 'parameter' : parameter_7}
    data_year_8 = { 'year' : year_8, 'parameter' : parameter_8}
    data_year_9 = { 'year' : year_9, 'parameter' : parameter_9}
    data_year_10 ={ 'year' : year_10, 'parameter' : parameter_10}
    data_year_11 ={ 'year' : year_11, 'parameter' : parameter_11}
    data_year_12 ={ 'year' : year_12, 'parameter' : parameter_12}

    data_month = {
        '1' : data_year_1,
        '2' : data_year_2,
        '3' : data_year_3,
        '4' : data_year_4,
        '5' : data_year_5,
        '6' : data_year_6,
        '7' : data_year_7,
        '8' : data_year_8,
        '9' : data_year_9,
        '10' : data_year_10,
        '11' : data_year_11,
        '12' : data_year_12
    }
    
    check = False

    for i in range(len(text)):

        data = text[i].split(' ')
        filtered = list(filter(('').__ne__, data))
        
        
        
        if check == True:
            
            if len(filtered) > 2:

                if filtered[3] != '---':
                    try:
                        data_month[str(filtered[1])]['parameter'].append(float(filtered[3]))
                    except:
                        data_month[str(filtered[1])]['parameter'].append(float(filtered[3][:len(filtered[3])-1]))
                else:
                    data_month[str(filtered[1])]['parameter'].append(0)
                data_month[str(filtered[1])]['year'].append(int(filtered[0]))

        for i in range(len(filtered)):   
            if filtered[i] == 'degC':
                check = True

    with pd.ExcelWriter(str(name)+'.xlsx') as writer:
        for i in range(1,13):
            df = pd.DataFrame(data = data_month[str(i)])
            df.to_excel(writer, sheet_name= str(name) + str(i))
   
