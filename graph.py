import pandas as pd 
pd.core.common.is_list_like = pd.api.types.is_list_like
import pandas_datareader.data as web 
import datetime as dt 
import numpy as np 
import matplotlib.pyplot as plt 
from matplotlib import style
style.use('ggplot') 

class graph:
    def __init__(self, xlabel, ylabel, graphName, dataFrameInput):
        self.xlabel = xlabel
        self.ylabel = ylabel
        self.graphName = graphName
        self.dataFrameInput = dataFrameInput
        fig = plt.figure()
        fig.suptitle(self.graphName)
        plt.plot(self.dataFrameInput)
        plt.xlabel(self.xlabel)
        plt.ylabel(self.ylabel)

    def displayGraph(self):
        plt.show()
    
    def addAnotherLineToPlot(self, line):
        plt.plot(line)

