import pytest
import pandas as pd
import altair as alt
from EDAhelper.numeric_plots import numeric_plots


def df():
    df = pd.DataFrame({
        'A': [100, 142, 30, 40],
        'B': [94, 55, 100, 120],
        'C': [94, 68, 20, 17],
        'D': [3.86, 4.05, 5.6, 1.0],
        'E': [34, 92, 100, 200],
        'name': ['Jennifer', 'Rowan', 'Steven', 'Vera']
    })
    return df


def test_numeric_plots_return_obj():
    """Check that the return value is a list of objects."""
    actual_obj = numeric_plots(df())

    assert isinstance(
        actual_obj, alt.vegalite.v4.api.RepeatChart), "The return value should be an Altair plot object."

def test_numeric_plots_unit_1():
    """Unit test case 1"""
    actual_obj = numeric_plots(df())

    # Unit test case 1: 
    expected_1 = 5
    actual_1 = len(actual_obj.spec._kwds['data'].columns)
    assert expected_1 == actual_1, "The number of columns in the dataframe are incorrect."

def test_numeric_plots_unit_2():
    """Unit test case 2"""
    actual_obj = numeric_plots(df())

    # Unit test case 2
    expected_2 = df().select_dtypes(include=['float64', 'int64']).columns
    actual_2 = actual_obj._kwds['repeat'].row
    assert set(expected_2) == set(actual_2), "The rows in the repeated plots are incorrect."

def test_numeric_plots_unit_3():
    """Unit test case 3"""
    actual_obj = numeric_plots(df())

    # Unit test case 3
    expected_3 = df().select_dtypes(include=['float64', 'int64']).columns
    actual_3 = actual_obj._kwds['repeat'].column
    assert set(expected_3) == set(actual_3), "The columns in the repeated plots are incorrect."

def test_numeric_plots_error():
    """Check TypeError raised when any of the argument type is wrong."""

    list_object = ["Python", "is", "a", "language"]
    with pytest.raises(TypeError):
        numeric_plots(list_object)
