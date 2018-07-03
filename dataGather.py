#http://pandas-datareader.readthedocs.io/en/latest/readers/morningstar.html#pandas_datareader.mstar.daily.MorningstarDailyReader.close
import pandas as pd 
pd.core.common.is_list_like = pd.api.types.is_list_like
import pandas_datareader.data as web 
import datetime as dt 

class dataGather:
    def __init__(self, startDate, endDate, stockTicker):
        self.stockTicker = stockTicker
        self.startDate = startDate
        self.endDate = endDate
        self.dates =[]
    
    def getData(self):
        try:
            # check for invalid ticker
            self.dataFrame = web.DataReader(self.stockTicker, 'morningstar', self.startDate, self.endDate, retry_count=0)['Close']#.reset_index()
        except ValueError:
            print(self.stockTicker+" is Invalid")
            return None
        return self.dataFrame

    def getDates(self):
        for x in range(len(self.dataFrame)):
            newdate = str(self.dataFrame.index[x])
            newdate = newdate[0:10]
            self.dates.append(newdate)
        return self.dates