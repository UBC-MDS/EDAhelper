import pandas as pd
import numpy as np

def preprocess(path, method=None, fill_value = None):
    """
    Preprocess data in txt or csv by dealing with missing values.

    Parameters
    ----------
    path : str
        The path of the data file.

    method : {None, 'most_frequent', 'mean', 'median', 'constant'},  default=None
        The imputation method.

        If None, then missing values are treated as numpy.NaN.

        If 'mean', then replace missing values using the mean along each column. Can only be used with numeric data.

        If 'median', then replace missing values using the median along each column. Can only be used with numeric data.

        If 'most_frequent', then replace missing using the most frequent value along each column. Can be used with strings or numeric data. If there is more than one such value, only the smallest is returned.

        If 'constant', then replace missing values with fill_value. Can be used with strings or numeric data.

    fill_value : str or numerical values, default=None
        When method=='constant', fill_value is used to replace all occurrences of missing values.
        If left to the default, fill_value will be 0 when imputing numerical data and “missing_value” for strings or object data types.

    Returns
    -------
    pandas.DataFrame
        The processed table.

    Examples
    -------
    >>> from EDAhelper import EDAhelper
    >>> EDAhelper.preprocess('file_path')
    """

    pass
