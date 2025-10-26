
import pandas as pd
import numpy as np
import matplotlib as mp

class quantAirTools:
    #Returns a cleaned and joined csv datasets
    def QAcleanToCSV(dataset1,dataset2,outputfile):
 #Imports device data
        qa1Info = pd.read_csv(dataset1,delimiter=',',engine='python',on_bad_lines='skip')
        qa2Info = pd.read_csv(dataset2,delimiter=',',engine='python',on_bad_lines='skip')

#Adding corresponding data from each Modulair sensor
        qa1 = pd.read_csv(dataset1,delimiter=',',engine='python',skiprows=[0-2],header=3)
        qa2 = pd.read_csv(dataset2,delimiter=',',engine='python',skiprows=[0-2],header=3)

#Reducing dataframes to only include variables of interest
        qa1 = qa1[['timestamp_iso','opc_pm25','pm25_env','opc_pm10','pm10_env']]
        qa2 = qa2[['timestamp_iso','opc_pm25','pm25_env','opc_pm10','pm10_env']]

#Adding id columns for join
        qa1['id'] = range(1, len(qa1) + 1)
        qa2['id'] = range(1, len(qa2) + 1)

#joining data by new 'id' variable
        qaJoin = pd.merge(qa1,qa2,on='id',how='outer')

#Changing format of timestamp to datetime
        qaJoin.timestamp_iso_x = pd.to_datetime(qaJoin.timestamp_iso_x, yearfirst=True)
        qaJoin.timestamp_iso_y = pd.to_datetime(qaJoin.timestamp_iso_y, yearfirst=True)
        
        qaJoin.to_csv(outputfile)
        print(qaJoin)
        return(qaJoin)
        
   
   
    #Returns time series graphs of QuantAir PM Data
    def QAplot(cleanedData):
        
       
        QAplot() # type: ignore


    #Returns a summary of cleaned data
    def QASummary(cleanedData):


        QASummary() # type: ignore

quantAirTools.QAcleanToCSV(dataset1='TalbotColocateO1.csv',dataset2='TalbotColocateO2.csv',outputfile='TalbotColocateJoined')
