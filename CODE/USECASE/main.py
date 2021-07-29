# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import pandas as pd
import csv
import os

directory_in_str = "Fiware4Water Challenge - Milan Data/Estrazioni 30 ottobre"
directory = os.fsencode(directory_in_str)

for file in os.listdir(directory):
    filename = os.fsdecode(file)
    df = pd.read_csv("Fiware4Water Challenge - Milan Data/Estrazioni 30 ottobre/" + filename, delimiter=";")
    df['Data/Ora'] = df['Data/Ora'].astype(str)  # convert entire "Data/Ora" Column to string
    df['Data/Ora'] = pd.to_datetime(df['Data/Ora'], dayfirst=True)  # convert entire "Data/Ora" Column to datetime format this time
    df.index = df['Data/Ora']  # replace index with entire "Data/Ora" Column to work with groupby function
    df3 = df.groupby(pd.Grouper(freq='D')).mean()  # take daily average of multiple values

    df3 = df3.loc[:, ~df3.columns.str.contains('^Unnamed')]

    df3.to_csv(filename[:-4] + "_DAILY_AVG" + ".csv")



