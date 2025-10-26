

import pandas as pd
import numpy as np
import matplotlib as mp
import matplotlib.pyplot as plt
import glob

class quantAirTools:

    dataLibrary = {}
    deviceLibrary = {}
    dataJoin = pd.DataFrame()
 
    #Returns a cleaned and joined csv datasets
    def QAcleanToCSV(outputfile,*datasets):
 
        
        dataList = []
        #Imports device data


        for dataset in datasets: 
            
            device = pd.read_csv(dataset,delimiter=',',engine='python',on_bad_lines='skip')
            data = pd.read_csv(dataset,delimiter=',',engine='python',skiprows=[0-2],header=3)
            data = data[['timestamp_iso','opc_pm25','pm25_env','opc_pm10','pm10_env']]

            data.timestamp_iso = pd.to_datetime(data.timestamp_iso,yearfirst=True)
            data['id'] = range(1, len(data) + 1)
            data = data.add_suffix(f'{dataset}')
            dataList.append(data)
            quantAirTools.dataLibrary[dataset] = data
        dataJoin = pd.concat(dataList, axis=1)
        print(dataJoin)
        dataJoin.to_csv(outputfile)
        return outputfile
        


class quantAirTools:

    def QAPlotter(inputFile,startTime,endTime,var):

        pd.read_csv(inputFile)
        startTime = pd.to_datetime(startTime)
        endTime = pd.to_datetime(endTime)
        dataList = []
        ydata = inputFile(regex=f'^{var}')
        dataList.append(ydata)
        plt.plot(x=(range(startTime,endTime)),y=ydata)
        plt.show()

quantAirTools.QAcleanToCSV('TestJoin.csv','TalbotColocateO1.csv','TalbotColocateO2.csv','TalbotColocateQA1.csv','TalbotColocateQA2.csv')
quantAirTools.QAPlotter('TestJoin.csv','2025-10-7 17:23:00','2025-10-7 18:23:00','pm_25')
