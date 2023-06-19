import os
import sqlite3
import pandas as pd
import glob

# getting csv files from the folder MyProject
path = "D:\Github\AttendanceSystemBasedOnFaceRecognition"
csv_files = glob.glob(path + "/*.csv")
# Read each CSV file into DataFrame
# This creates a list of dataframes
df_list = (pd.read_csv(file) for file in csv_files)

# Concatenate all DataFrames
big_df   = pd.concat(df_list, ignore_index=True)
# print(big_df)
# info = pd.DataFrame(big_df)

big_df.to_csv('D:\Github\AttendanceSystemBasedOnFaceRecognition\AllData\AllData.csv',index = False)
csv_data = big_df.to_csv()  
print('\nCSV String Values:\n', csv_data)

# Step 1. Load data file
df = pd.read_csv('D:\Github\AttendanceSystemBasedOnFaceRecognition\AllData\AllData.csv')

# df.sort_values('Date',ascending=False).drop_duplicates(subset=["Name", "Date", "Day","Time"], keep='last')

# Step 2. Data Clean Up
df.columns = df.columns.str.strip()

# Step 3. Create/Connect to a sqlite database
connection = sqlite3.connect('attendance.db')

# Step 4. Load data file to sqlite
# fail;replace;append
df.to_sql('attendance',connection, if_exists='replace')


# Step 5. Close connection
connection.close()


