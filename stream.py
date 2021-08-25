import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pandas import ExcelFile
import streamlit as st
df = pd.read_excel("D:\stream\data v2.xlsx") 
print(df)
#getting to know more about the dataset
def knowledge(data):
  # showing the shape of the dataset
  print("The shape is **********************")
  print(df.shape) 
  print("The information is **********************")
  # showing the info of the dataset
  print(df.info())
  print(" The size is**********************")
  print(df.size)
knowledge(df) 
#representation of our data county-wise

z=df.groupby(['County'])['_id'].count().sort_values(ascending=False)
z
df.drop(["start","end", "time ", "minutes", "Insert_Geotag_Location", "_Insert_Geotag_Location_latitude", 
           "_Insert_Geotag_Location_longitude", "_Insert_Geotag_Location_altitude","_Insert_Geotag_Location_precision",
           "Name_of_Enumerator","__version__","meta/instanceID","_id","_uuid","_submission_time","_index","_parent_table_name",
           "_parent_index","_tags","_notes"], axis=1, inplace = True)
# df.columns = df.columns.str.replace(' ', '_')
df.head()
# Accuracy 
knowledge(df)
df.columns = df.columns.str.replace('_', ' ')
df.columns = ['County', 'Age', 'Gender', 'Monthly Income',
       'Highest Level of Education Attained', 'Occupation',
       'Location', 'Did you vote in 2017',
       'Will you vote in the Refere', 'If No Why',
       'How will you vote in the Referendum',
       'If elections are today who would you vote for',
       'If you dont vote for that one who is your second choice', 'Do you support BBI',
       'Do you know what BBI wants to change',
       'Do you support the Hustler Nation',
       'Do you think the handshake brought us peace',
       'Who influences youin your community',
       'Do you trust your political leaders',
       'Do you trust your religious leaders',
       'Do you trust your elders', 'Where do you get your News from',
       'Have you understood BBI completely', 'Will you vote in 2022']
df["Occupation"].str.replace(r'\W',"")
df["Age"]= df["Age"].str.replace('_','-')
df.tail()
df["Monthly Income"]= df["Monthly Income"].str.replace('_',',')
df.tail()
df["Monthly Income"]= df["Monthly Income"].str.replace(',,,','-')
df["Monthly Income"]= df["Monthly Income"].str.replace(',,','-')
df.tail()
df["Monthly Income (Kshs)"]= df["Monthly Income"].str.replace('kshs,','')

df["Monthly Income"]= df["Monthly Income (Kshs)"]
df.head()
df_new = "D:\stream\df_new.csv"
df_new =pd.read_csv("D:\stream\df_new.csv")
df_new.head()
knowledge(df_new)
#checking for columns with null entries
df_new.isnull().any()
#number of null entries
df_new.isnull().sum().sum()
#checking our data for duplicates
df_new.duplicated().sum()
#outliers
knowledge(df_new)
df_new.columns
df_new['Have you understood BBI completely'].unique()
y=df_new['Have you understood BBI completely'].value_counts()
y
def completelyBBI(Dknow):
  if Dknow == 'yes'or 'no' or 'maybe' or 'i_don_t_care' :
    know = df_new["Have you understood BBI completely"] == Dknow
    return know.sum()
df_new["Have you understood BBI completely"].unique()
completelyBBI('yes') 
completelyBBI('maybe')
completelyBBI('no')
completelyBBI('i_don_t_care')
st.write("""My first App""")
if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(df_new)
st.line_chart(z)
data1=['yes','maybe','no','i_don_t_care']
#data1=df_new["Have you understood BBI completely"].unique()
y=[completelyBBI('yes'), completelyBBI('maybe'), completelyBBI('no'), completelyBBI('i_don_t_care')]
#fig = plt.figure(figsize =(8, 6))
colors = sns.color_palette('pastel')[0:4]
st.bar_chart(y)
