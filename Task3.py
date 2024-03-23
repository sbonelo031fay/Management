#You are provided with insurance dataset on blackboard. Please logon on blackboard and download the
#dataset

import pandas as pd
import matplotlib.pyplot as plt
#Read dataset frm csv file
dataframe = pd.read_csv("C:/Users/Sibonelo Faye/Downloads/motor_insure.csv/motor_data11-14lats.csv")

#Inspect its column by displaying the first 10 records.
print(dataframe.head(10))

#Display records for make and usage for sets_num that are more than 40.
'''fields = dataframe[dataframe["sets_num"]>40]

records = fields[["make", "usage"]]
print(records)'''

#§ Plot a basic graph showing effective_yr on y axes and carrying capacity on x-axes
plt.plot(dataframe["EFFECTIVE_YEAR"], dataframe["CARRYING_CAPACITY"])
plt.xlabel("Effective Year")
plt.plot("Carrying Capacity")
plt.title("Effective Year vs Carrying Capacity")
plt.show()