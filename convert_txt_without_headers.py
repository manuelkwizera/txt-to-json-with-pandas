import pandas as pd
import json
from io import StringIO

data = """DATE,05/26/24 14:04:54,CO,100.00,SO2,20.00,NO2,15.00,O3,16.00,CO2,0.00,T,0.00,RH,0.00,PM1.0,1.40,PM2.5,1.80,PM10,1.80,WD,0.00,WS,0.00,BATT,4.01,CHRG,0.00,RUN,0.00,SD,1,RAW,0,0,0,0,0,0,0,0,STAT,6b,0,f0,LAT,0.00000,LON,0.00000,CRC,923758416Z
DATE,05/26/24 14:11:12,CO,8200.56,SO2,980.23,NO2,46.65,O3,307.42,CO2,558.00,T,30.60,RH,43.60,PM1.0,8.80,PM2.5,12.93,PM10,14.24,WD,0.00,WS,0.00,BATT,4.01,CHRG,955.32,RUN,136.93,SD,1,RAW,-2627,3867,25,1241,-37,-66,26,-219,STAT,6b,0,f0,LAT,0.00000,LON,0.00000,CRC,2955245545Z
DATE,05/26/24 14:11:22,CO,23662.32,SO2,1399.20,NO2,145.25,O3,422.97,CO2,551.25,T,30.60,RH,43.53,PM1.0,11.19,PM2.5,16.30,PM10,17.77,WD,0.00,WS,0.00,BATT,4.01,CHRG,955.32,RUN,140.16,SD,1,RAW,-4320,6296,50,1950,-63,-117,45,-380,STAT,6b,0,f0,LAT,0.00000,LON,0.00000,CRC,3713408366Z
DATE,05/26/24 14:11:32,CO,24373.58,SO2,1384.21,NO2,162.64,O3,449.16,CO2,556.81,T,30.60,RH,43.51,PM1.0,13.05,PM2.5,18.76,PM10,20.65,WD,0.00,WS,0.00,BATT,4.01,CHRG,955.32,RUN,136.93,SD,1,RAW,-4467,6428,49,1928,-67,-131,47,-413,STAT,6b,0,f0,LAT,0.00000,LON,0.00000,CRC,317343393Z"""

# Convert the string data into a file-like object
data_io = StringIO(data)

# Read the data into a DataFrame
df = pd.read_csv(data_io, header=None)

# Reshape the DataFrame to have 'DATE' as the key and all other columns as values
df_dicts = []
for index, row in df.iterrows():
    # Ensure all keys are strings and convert to lowercase
    entry = {str(key).lower(): value for key, value in zip(row[0::2], row[1::2])}
    df_dicts.append(entry)

# Convert the list of dictionaries to JSON
json_output = json.dumps(df_dicts, indent=4)


# Write the dictionary to a JSON file
json_file_path = 'data-two.json'
with open(json_file_path, 'w') as json_file:
    json.dump(df_dicts, json_file, indent=4)


#print(json_output)
