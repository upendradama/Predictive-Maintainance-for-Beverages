import pandas as pd
import matplotlib.pyplot as plt
from influxdb import InfluxDBClient

client = InfluxDBClient(host='localhost', port=8086)

client.get_list_database()
client.switch_database('beverage')


result = client.query("""select * from pet_sensor_readings where "Day" = '21' and "Hour" = '6' """)
result
result.raw
e = next(iter(result))

df = pd.DataFrame(e)
df_1 = df.drop(["Co2", "Month", "Year", "product", "Uday"], axis=1)
#client.query('select * from "pet_sensor_readings" where "time" = Now()-1d')
df_1.columns
neworder = ['time','Preform','Blower', 'Plasmax','Filler', 'Date_coder','Labeller', 'PSP', 'Palletizer', 'Day', "Week","Hour",]
df_1 = df_1.reindex(columns=neworder)

df_1['time'].head()

# x=df_1["time"].iloc[0:5013, ]
# y=df_1["Preform"].iloc[0:5013,]
# y1=df_1["Blower"].iloc[0:5013,]
# y2=df_1["Plasmax"].iloc[0:5013,]
# y3=df_1["Filler"].iloc[0:5013,]

# plt.plot(x, y, marker = 'o', color='Black')
# plt.plot(x, y1, marker = '', color='Blue')
# plt.plot(x, y2, marker = '', color='Red')
# plt.plot(x, y3, marker = '', color='Purple')
# plt.show()

# df_1["Preform"].value_counts()

# #points = result.get_points()
# is_16 = df_1['Day']=='16'
# day_16 = df_1[is_16]
# is_6 = day_16['Hour']=='6'
# day_166 = day_16[is_6]

# cond1 = df_1['Day'] =='16'
# cond2 = df_1['Hour'] =='6'
# allcond = cond1 & cond2
# df_1 = df_1[allcond]

# df_1['Preform'].value_counts()
# df_1['Blower'].value_counts()

# #ss_day16 = client.query('select "time","Preform","Blower", "Plasmax","Filler", "Date_coder","Labeller", "PSP", "Palletizer" from "pet_sensor_readings" where "Day"= '16' ' )
# #day_16 = next(iter(ss_day16))             

# ss_day16.raw

# df_1.head

# #df.to_csv("L:\pet_sensor_reading1.csv")

# #a = 1364797   
# #b = 1048574
# #print(a-b)

# #df_subset = df.iloc[1048575:1364797, :]

# df_1.to_csv("L:\pet_day16.csv")



        
      
     
    
         
 
           
            
