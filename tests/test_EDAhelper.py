import numpy as np
from EDAhelper.EDAhelper import preprocess
import pandas as pd
import pytest


def expected_results(case):
    if case == 2:
        expected_dict = {'col_1': [1.25, 1.0, 1.0, 3.0, 0.0],
                         'col_2': [1.0, 2.0, 8.0/3, 5.0, 8.0/3],
                         'col_3': ['a', 'b', 'c', 'd', np.NaN]}
        expected_df = pd.DataFrame(data=expected_dict)
        return expected_df
    elif case == 3:
        expected_dict = {'col_1': [1.0, 1.0, 1.0, 3.0, 0.0],
                         'col_2': [1.0, 2.0, 2.0, 5.0, 2.0],
                         'col_3': ['a', 'b', 'c', 'd', np.NaN]}
        expected_df = pd.DataFrame(data=expected_dict)
        return expected_df
    elif case == 4:
        expected_dict = {'col_1': [1.0, 1.0, 1.0, 3.0, 0.0],
                         'col_2': [1.0, 2.0, 1.0, 5.0, 1.0],
                         'col_3': ['a', 'b', 'c', 'd', np.NaN]}
        expected_df = pd.DataFrame(data=expected_dict)
        return expected_df
    elif case == 5:
        expected_dict = {'col_1': [0, 1.0, 1.0, 3.0, 0.0],
                         'col_2': [1.0, 2.0, 0, 5.0, 0],
                         'col_3': ['a', 'b', 'c', 'd', np.NaN]}
        expected_df = pd.DataFrame(data=expected_dict)
        return expected_df
    elif case == 6:
        expected_dict = {'col_1': [9999, 1.0, 1.0, 3.0, 0.0],
                         'col_2': [1.0, 2.0, 9999, 5.0, 9999],
                         'col_3': ['a', 'b', 'c', 'd', np.NaN]}
        expected_df = pd.DataFrame(data=expected_dict)
        return expected_df

    return None


def test_preprocess():
    # Case 1: To test default settings and return
    file_path = 'https://raw.githubusercontent.com/pandas-dev/pandas/main/doc/data/titanic.csv'
    actual_df = preprocess(file_path)
    expected_df = pd.read_csv(file_path)
    test_result = actual_df.compare(expected_df)
    assert test_result.empty, 'Test data read incorrectly!'
    assert isinstance(actual_df, pd.DataFrame), 'Return wrong data type!'

    # Case 2: To test method = 'mean'
    file_path = './tests/data_preprocess.csv'
    # file_path = 'data_preprocess.csv'
    actual_df = preprocess(file_path, method='mean', index_col=0)
    test_result = actual_df.compare(expected_results(2))
    assert test_result.empty, 'method=`mean` applied incorrectly!'

    # Case 3: To test method = 'median'
    actual_df = preprocess(file_path, method='median', index_col=0)
    test_result = actual_df.compare(expected_results(3))
    assert test_result.empty, 'method=`median` applied incorrectly!'

    # Case 4: To test method = 'most_frequent'
    actual_df = preprocess(file_path, method='most_frequent', index_col=0)
    test_result = actual_df.compare(expected_results(4))
    assert test_result.empty, 'method=`most_frequent` applied incorrectly!'

    # Case 5: To test method = 'constant' and fill_value = None
    actual_df = preprocess(file_path, method='constant', index_col=0)
    test_result = actual_df.compare(expected_results(5))
    assert test_result.empty, 'method=`constant` applied incorrectly!'

    # Case 6: To test method = 'constant' and fill_value = 9999
    actual_df = preprocess(file_path, method='constant', fill_value=9999, index_col=0)
    test_result = actual_df.compare(expected_results(6))
    assert test_result.empty, 'method=`constant`, fill_value=9999 applied incorrectly!'

    # Case 7: To test inputs
    with pytest.raises(Exception):
        preprocess(5)

    with pytest.raises(Exception):
        preprocess(file_path, method='None')

    with pytest.raises(Exception):
        preprocess(file_path, method='constant', fill_value='0.0')

    with pytest.raises(Exception):
        preprocess(file_path, index_col_1=1)

