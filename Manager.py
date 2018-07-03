import datetime as dt 
from dataGather import dataGather
from graph import graph
from monteCarlo import monteCarlo
from scikitTester import scikitTester

#stockTicker = 'AAPL'
#stockTicker = 'RADA'
#stockTicker = 'DRYS'
stockTicker = 'NVDA'
#stockTicker = 'test' # invalid ticker

start = dt.datetime(2018, 1, 1) 
end = dt.datetime(2018, 7, 2)

# montecarlo displayed
datagather1 = dataGather(start,end,stockTicker)
dataFrame = datagather1.getData()

if dataFrame is None:
    # need something between if and else of python complains
    print("")
else:
    monteCarlo1 = monteCarlo(dataFrame, 1000)
    #graph1 = graph("day","prices","MonteCarlo "+stockTicker, monteCarlo1.runSim())
    #graph1.displayGraph()
    
    #dataFramedataFrame
    #print(datagather1.dataFrame['Date'])
    print(datagather1.dataFrame.index)

    #scikitLearn
    #scikitTester1 = scikitTester()
    #print(datagather1.getDates())
    #print(datagather1.dataFrame['Date'])
    #predicted_price = scikitTester1.predict_price(datagather1.getData().index, datagather1.getData(), 1) 
    
    #tensorFlow
