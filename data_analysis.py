#the dataset: This dataset is originally from the National Institute of Diabetes and Digestive and Kidney Diseases. The objective of the dataset is to diagnostically predict whether or not a patient has diabetes, based on certain diagnostic measurements included in the dataset.

import pandas as pd
path = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/diabetes.csv"
df = pd.read_csv(path)

#check the top n rows of the dataframe:
df.head(5)

#view the dimension of the dataframe: 
df.shape

#view basic statistical details:
df.describe()

#information about a DataFrame:
df.info()

#Identify missing values:
for column in missing_data.columns.values.tolist():
    print(column)
    print (missing_data[column].value_counts())
    print("")   

#check data format:
df.dtypes

#Visualization:
import matplotlib.pyplot as plt
import seaborn as sns

labels= 'Diabetic','Not Diabetic'
plt.pie(df['Outcome'].value_counts(),labels=labels,autopct='%0.02f%%')
plt.legend()
plt.show()
