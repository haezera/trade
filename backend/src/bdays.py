import numpy as np


def calculateBusinessDays(startData, endDate):
    return np.busday_count(
        startData.strftime('%Y-%m-%d'), endDate.strftime('%Y-%m-%d'))
