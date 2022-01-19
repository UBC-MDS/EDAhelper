import pandas as pd
import numpy as np
import statistics

data = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv')

'''
Checking statistics are calculated correctly by the function and both matrices have correct values
'''
def variance(data):
    n = len(data)
    mean = sum(data) / n
    deviations = [(x - mean) ** 2 for x in data]
    variance = sum(deviations) / n
    return variance

cols = ('petal_width', 'petal_length')

assert column_stats(iris, cols)[1][cols[1]].index[0] == cols[0]
assert column_stats(iris, cols)[1][cols[1]].index[1] == cols[1]
assert column_stats(iris, cols)[2][cols[1]].index[0] == cols[0]
assert column_stats(iris, cols)[2][cols[1]].index[1] == cols[1]
assert column_stats(iris, cols)[0]['Column'][0] == cols[0]
assert column_stats(iris, cols)[0]['Mean'][0] == round(iris['petal_width'].sum()/iris['petal_width'].count(), 3)
assert column_stats(iris, cols)[0]['Var'][0] - 0.5 <= variance(iris['petal_width']) <= column_stats(iris, ('petal_width', 'petal_length'))[0]['Var'][0] + 0.5
assert column_stats(iris, cols)[1]['petal_width'][0] == 1
assert column_stats(iris, cols)[1]['petal_length'][1] == 1

'''
Checking all dataframes have same number of rows as number of specified columns in function
'''
assert len(column_stats(iris, cols)[0].columns) == 9
assert len(cols) == len(column_stats(iris, cols)[0])
assert len(cols) == len(column_stats(iris, cols)[1])
assert len(cols) == len(column_stats(iris, cols)[2])
