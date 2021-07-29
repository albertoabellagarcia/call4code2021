import csv
import datetime
import pandas as pd
import openpyxl
from scipy.stats.stats import pearsonr
from scipy.stats.stats import spearmanr
from scipy.stats.stats import kendalltau

from statistics import mean
from statistics import stdev

import math

def corr(plant, feature):
    sensor_dict = {} #AAA_COD


    reader = csv.DictReader(open(plant + "_" + feature + "_real time_2019-2020_DAILY_AVG.csv"))
    df = pd.read_excel(plant + ".xlsx")


    for row in reader:
        sensor_dict[row['Data/Ora']] = row['Valore']

    sensor_data = sensor_dict.keys()


    dates = df['DATE'].tolist()
    dates2 = []
    for d in dates:
        dates2.append(d.strftime("%Y-%m-%d"))
    dates = dates2

#    print(dates)

    values = df[feature].tolist()

    lab_dict = {dates[i]: values[i] for i in range(len(dates))}


    sensor = []
    lab = []

    keys_list = list(sensor_dict)



    for i in range(len(sensor_dict)):
        date = keys_list[i]
        if date in dates and sensor_dict[date] != "" and lab_dict[date] != "----" and lab_dict[date] != "" and not math.isnan(float(lab_dict[date])):
            sensor.append(sensor_dict[date])
            lab.append(lab_dict[date])

    sensor2 = []
    for num in sensor:
        sensor2.append(float(num))
    sensor = sensor2


    if feature == "COD":
        lab2 = []
        for i in range(len(sensor)):
            if lab[i] == 2.5 and sensor[i] > 15:
                lab2.append(15)
            elif lab[i] == 7.5 and sensor[i] <= 15:
                lab2.append(sensor[i])
            # elif lab[i] == 7.5 and sensor[i] <= 15 and sensor[i] > 5:
            #     lab2.append(7.5)
            else:
                lab2.append(lab[i])
        lab = lab2

    print(lab)
    print(sensor)
    print(len(sensor))
    print(len(lab))

    correlation, p_value = pearsonr(sensor, lab)
    #print("corr")
    print(mean(abs(x - y) for x, y in zip(sensor, lab)))
    print(stdev(lab))
    #print(correlation)
    # coef, p = spearmanr(sensor, lab)
    # print(coef)
    # coef, p = kendalltau(sensor, lab)
    # print(coef)

corr("GGG", "SST")