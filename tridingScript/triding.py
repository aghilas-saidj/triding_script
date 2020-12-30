#!/usr/bin/env python3

from tradingview_ta import TA_Handler, Interval
import pandas as pd
from os import system
from time import sleep

n_stock = []
CLOSE = []
VWMA = []
VWMA_1_DAY = []
VWMA_7_DAYS = []
VWMA_30_DAYS = []
EMA5 = []
EMA10 = []
EMA20 = []
EMA30 = []
EMA100 = []
SMA5 = []
SMA10 = []
SMA20 = []
SMA30 = []
SMA100 = []

p = [' ']

#====================================FOR NASDAQ=========================================



socket_list_choosed = open('Symbol_List.txt' , "r" )
lines = socket_list_choosed.readlines()

print ("**please wait for data extraction from tradingview.com **")
print (" ")
sleep(2)
for SMBL in lines:

    try:



        handler = TA_Handler()
        handler.set_symbol_as(SMBL.strip())
        handler.set_exchange_as_crypto_or_stock("NASDAQ")
        handler.set_screener_as_stock("america")
        



        analysis = handler.get_analysis()


        y = analysis.indicators
        
        #print (y)

        n_stock.append(analysis.symbol)
        #print (analysis.symbol+" ======> OK ")
        CLOSE.append(str(y['close']))

        VWMA.append(str(y['VWMA']))

        EMA5.append(str(y['EMA5']))
        SMA5.append(str(y['SMA5']))


        EMA10.append(str(y['EMA10']))
        SMA10.append(str(y['SMA10']))

        EMA20.append(str(y['EMA20']))
        SMA20.append(str(y['SMA20']))

        EMA30.append(str(y['EMA30']))
        SMA30.append(str(y['SMA30']))

        EMA100.append(str(y['EMA100']))
        SMA100.append(str(y['SMA100']))










        handler.set_interval_as(Interval.INTERVAL_1_DAY)
        analysis = handler.get_analysis()
        y = analysis.indicators
        VWMA_1_DAY.append(str(y['VWMA']))

        handler.set_interval_as(Interval.INTERVAL_1_WEEK)
        analysis = handler.get_analysis()
        y = analysis.indicators
        VWMA_7_DAYS.append(str(y['VWMA']))


        handler.set_interval_as(Interval.INTERVAL_1_MONTH)
        analysis = handler.get_analysis()
        y = analysis.indicators
        VWMA_30_DAYS.append(str(y['VWMA']))



    except:
        pass


    try:
        system('clear')
    except:
        pass
    try:
        system('cls')
    except:
       pass

    try:
        socket1 = pd.DataFrame(
                 {
                 'symbol':p+n_stock,
                 'CLOSE':p+CLOSE ,
                 'VWMA':p+VWMA ,
                 'VWMA_1_DAY':p+VWMA_1_DAY,
                 'VWMA_7_DAYS':p+VWMA_7_DAYS,
                 'VWMA_30_DAYS':p+VWMA_30_DAYS,
                 'EMA5':p+EMA5,
                 'EMA10':p+EMA10,
                 'EMA20':p+EMA20,
                 'EMA100':p+EMA100,
                 'SMA5':p+SMA5,
                 'SMA10':p+SMA10,
                 'SMA20':p+SMA20,
                 'SMA100':p+SMA100

                 }) 
        print (socket1)


    except:
        pass


    

#==============================================









#=========================FOR NYSE=========================

for SMBL in lines:
    try:



        handler = TA_Handler()
        handler.set_symbol_as(SMBL.strip())
        handler.set_exchange_as_crypto_or_stock("NYSE")
        handler.set_screener_as_stock("america")
        



        analysis = handler.get_analysis()


        y = analysis.indicators
        n_stock.append(analysis.symbol)
        print (analysis.symbol+" ======> OK")
        CLOSE.append(str(y['close']))

        VWMA.append(str(y['VWMA']))

        EMA5.append(str(y['EMA5']))
        SMA5.append(str(y['SMA5']))


        EMA10.append(str(y['EMA10']))
        SMA10.append(str(y['SMA10']))

        EMA20.append(str(y['EMA20']))
        SMA20.append(str(y['SMA20']))

        EMA30.append(str(y['EMA30']))
        SMA30.append(str(y['SMA30']))

        EMA100.append(str(y['EMA100']))
        SMA100.append(str(y['SMA100']))


        handler.set_interval_as(Interval.INTERVAL_1_DAY)
        analysis = handler.get_analysis()
        y = analysis.indicators
        VWMA_1_DAY.append(str(y['VWMA']))

        handler.set_interval_as(Interval.INTERVAL_1_WEEK)
        analysis = handler.get_analysis()
        y = analysis.indicators
        VWMA_7_DAYS.append(str(y['VWMA']))


        handler.set_interval_as(Interval.INTERVAL_1_MONTH)
        analysis = handler.get_analysis()
        y = analysis.indicators
        VWMA_30_DAYS.append(str(y['VWMA']))


    except:
        pass


    try:
        system('clear')
    except:
        pass
    try:
        system('cls')
    except:
        pass

    try:
        socket1 = pd.DataFrame(
                 {
                 'symbol':p+n_stock,
                 'CLOSE':p+CLOSE ,
                 'VWMA':p+VWMA ,
                 'VWMA_1_DAY':p+VWMA_1_DAY,
                 'VWMA_7_DAYS':p+VWMA_7_DAYS,
                 'VWMA_30_DAYS':p+VWMA_30_DAYS,
                 'EMA5':p+EMA5,
                 'EMA10':p+EMA10,
                 'EMA20':p+EMA20,
                 'EMA100':p+EMA100,
                 'SMA5':p+SMA5,
                 'SMA10':p+SMA10,
                 'SMA20':p+SMA20,
                 'SMA100':p+SMA100

                 }) 
        print (socket1)


    except:
        pass


#=====================================================

socket_list_choosed.close()


n_stock = str(n_stock)
CLOSE = str(CLOSE)
VWMA = str(VWMA)
VWMA_1_DAY = str(VWMA_1_DAY)
VWMA_7_DAYS = str(VWMA_7_DAYS)
VWMA_30_DAYS = str(VWMA_30_DAYS)
EMA5 = str(EMA5)
EMA10 = str(EMA10)
EMA20 = str(EMA20)
EMA30 = str(EMA30)
EMA100 = str(EMA100)
SMA5 = str(SMA5)
SMA10 = str(SMA10)
SMA20 = str(SMA20)
SMA30 = str(SMA30)
SMA100 = str(SMA100)



socket = pd.DataFrame(
     {
     'SYMBOL':' '+n_stock,
     'CLOSE':' '+CLOSE ,
     'VWMA':' '+VWMA ,
     'VWMA_1_DAY':' '+VWMA_1_DAY,
     'VWMA_7_DAYS':' '+VWMA_7_DAYS,
     'VWMA_30_DAYS':' '+VWMA_30_DAYS,
     'EMA5':' '+EMA5,
     'EMA10':' '+EMA10,
     'EMA20':' '+EMA20,
     'EMA100':' '+EMA100,
     'SMA5':' '+SMA5,
     'SMA10':' '+SMA10,
     'SMA20':' '+SMA20,
     'SMA100':' '+SMA100

     }, index = [0]) 

#df = df.transpose()

    #print (socket)

socket.to_csv('stock.csv')

print ('NOTE: **the data is saved in the file stock.csv** ')

print ("**if you want to process new actions  add their symbol in the file Symbol_List.txt ")
print ('**And dont rename it***')
print ("**And and keep it in the same directory as the script file triding.py ***")
print ("**if you encounter any bug please contact me**")
print ("**Thanks**")
print("**Aghilas Saidj**")
