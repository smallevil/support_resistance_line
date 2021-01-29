# -*- coding: utf-8 -*-
# @Author: smallevil
# @Date:   2020-12-22 16:37:40
# @Last Modified by:   smallevil
# @Last Modified time: 2020-12-22 19:52:05
#
import numpy as np
import pandas as pd
from support_resistance_line import SupportResistanceLine

from TBStockData import TBStockData

if __name__ == '__main__':
    TBStock = TBStockData()
    histList = TBStock.getDays('000929', indexs=[])
    sr = pd.Series(histList[-251:]['close'].values)
    sr = sr.rolling(3).mean().dropna()

    srl = SupportResistanceLine(sr, kind='support')

    #srl.plot_top_lines()
    #srl.twin.plot_top_lines()

    aa = srl.plot_both(show=True)
    print(aa)
    #srl.plot_steps()