import pytest
import pandas as pd
import altair as alt
from EDAhelper.numeric_plots import numeric_plots


def df():
    df = pd.DataFrame({
        'A': [100, 142],
        'B': [94, 55],
        'C': [94, 68],
        'D': [3.86, 4.05],
        'E': [34, 92],
        'name': ['Jennifer', 'Rowan', 'Steven', 'Vera'] 
    })
    return df


def test_numeric_plots():

    actual = numeric_plots(df())

    # Check that the return value is a list of objects
    assert isinstance(
        actual, alt.vegalite.v4.api.RepeatChart), "The return value should be an Altair plot objects."

#    for i in range(0, len(actual)):
#        assert isinstance(
#            actual[i], alt.vegalite.v4.api.RepeatChart), "The return list should contain objects of Altair plots."

    n_numeric_cols = 5

    assert actual

def test_numeric_plots_error():
    """Check TypeError raised when any of the argument type is wrong."""

    list_object = ["Python", "is", "a", "language"]
    with pytest.raises(TypeError):
        numeric_plots(list_object)
