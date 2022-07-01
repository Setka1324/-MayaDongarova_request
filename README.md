# Description

Student asked me to transfer all the UK **temperature recordings** published on [Metoffice](metoffice.gov.uk) into Excel format.   
She needed the **min temperature** each year for each month separately *(later on max also)*  
It was also required to create a **unique file** for each weather station.  

# Source information

Website stores all the data as .txt files

`Sample`: 

```
yyyy  mm   tmax    tmin      af    rain     sun
           degC    degC    days      mm   hours
1941   1    ---     23.4    ---     74.7     ---
1941   2    ---     14.2    ---     69.1     ---
```

`URL format`:

https://www.metoffice.gov.uk/pub/data/weather/uk/climate/stationdata/ + station_mame + data.txt

`API`:

***NO API*** 

# Possible issues

- Not fixed time periods for different stations
- Text format violation (additional symbols/their absence)

# Solution

## Libraries

[***Requests***](https://requests.readthedocs.io/en/latest/) - for ***Downloading***  
[***Pandas***](https://pandas.pydata.org/docs/) - for ***Excel*** creation

## Brief

1. Download as txt
2. Convert data into list, where each element is a row
3. Convert each element into another list, where each element is a parameter
4. Conver the needed parameters into Excel

## Step-by step

1. Create lists (stations, month, year) manually
2. Download the .txt file via URL_format + station_name
3. Transfer .txt into a list, using "/n" as a separator

At this stage we will have a list, where each element is a row of an information  

Sample:  

```
[
"1941   2    ---     14.2    ---     69.1     ---", 
"1941   1    ---     23.4    ---     74.7     ---"
]
```

4. Transfer each *String* (element of the row) into a list, using " " as a separator
5. Get rid of all *None* values corresponding to extra **spaces** between words

Now we have a list of lists, containing all the types of data separately (max_temp, min_temp, etc...)

Sample:

```
[
['1941', '2', '---', '14.2', '---', '69.1', '---'], 
['1941', '3', '---', '23.4', '---', '74.7', '---']
]
```

We definitely know which indexes in the inner list are responsible for which types of data ( 0 - year, 1 - month, 2 - max_temp, etc...)

6. Sort all the data in the mannually created lists using month as a key_parameter
7. Unite them into dictionary ( year: year_list, parameter: parameter_list ) <sub>Adding several parameters, will create more columns in the Excel, I was asked not to do so</sub>
8. Create an Excel file with the current station name and write in all the data using *Pandas* DataFrame


***CODE IN MAIN.PY WAS DESIGNED FOR THE MIN_TEMP***
