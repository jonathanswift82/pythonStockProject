#------------------------------------------------------------------------------------# 
#https://www.youtube.com/watch?v=_T0l015ecK4
import pandas as pd 
pd.core.common.is_list_like = pd.api.types.is_list_like
import numpy as np 
import pandas_datareader.data as web

class monteCarlo:
    def __init__(self, priceData, numberOfSimulations): 
        self.priceData = priceData
        self.numberOfSimulations = numberOfSimulations
 
    def runSim(self):
        returns = self.priceData.pct_change()
        lastPrice = self.priceData[-1] 
        numberOfDataPoints = len(self.priceData)
        simulation = pd.DataFrame()
        for x in range(self.numberOfSimulations): 
            count = 0
            dailyVol = returns.std()
            priceSeries = []
            price = lastPrice * (1 + np.random.normal(0, dailyVol))
            priceSeries.append(price)
            for y in range(numberOfDataPoints - 1):
                price = priceSeries[count] * (1 + np.random.normal(0, dailyVol))
                priceSeries.append(price)
                count += 1
            simulation[x] = priceSeries
        return simulation

