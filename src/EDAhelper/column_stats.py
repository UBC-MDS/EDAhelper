import pandas as pd

def column_stats(data, columns = None):
    """
  Obtain summary statistics of column(s) including count, mean, median, mode, Q1, Q3, 
  variance, standard deviation, correlation.... (add more if required) in table format.

  Parameters
  -------------

  data: array_like
           The data set from which columns will be selected

  columns: string vector
            Columns for which to obtain summary stats and correlation (if > 1 column arguments used)

  Returns
  -------------
  array
          Summary table detailing all statistics and correlations between chosen columns

  Examples
  -------------
  >>> column_stats(df, columns = c('Date', PctPopulation', 'CrimeRatePerPop'))
  >>>
  """
    
      statsdict = {'Column': [], 'Count': [], 'Mean': [], 'Median': [], 'Mode': [], 'Q1': [], 'Q3': [], 'Var': [], 'Stdev': []}
    for column in columns:
        statsdict['Column'].append(column)
        statsdict['Count'].append(round(float(data[column].describe().loc['count']), 3))
        statsdict['Mean'].append(round(float(data[column].describe().loc['mean']), 3))
        statsdict['Median'].append(round(float(data[column].describe().loc['50%']), 3))
        statsdict['Mode'].append(round(float(data[column].mode()), 3))
        statsdict['Q1'].append(round(float(data[column].describe().loc['25%']), 3))
        statsdict['Q3'].append(round(float(data[column].describe().loc['75%']), 3))
        statsdict['Var'].append(round(data[column].var(), 3))
        statsdict['Stdev'].append(round(data[column].std(), 3))
    return pd.DataFrame.from_dict(statsdict)

    cols = []
    for column in columns:
        cols.append(column)
        
    covmatrix = pd.DataFrame(data, columns = cols)
    return covmatrix.cov()

    corrmatrix = pd.DataFrame(data, columns = cols)   
    return corrmatrix.corr()
