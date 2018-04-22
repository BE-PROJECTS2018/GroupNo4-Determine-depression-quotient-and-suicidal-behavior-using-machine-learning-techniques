import pandas as pd
import numpy
arr = numpy.array([])
series = pd.read_csv(r'C:\Users\.....\.csv', header=1)
arr = numpy.array(series)
sd=numpy.std(arr, axis=0)
mean=numpy.mean(arr, axis=0)
dq=sd+mean
dq
