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


def test_numeric_plots():
    actual = numeric_plots(df())

    # Check that the return value is a list of objects
    assert isinstance(
        actual, alt.vegalite.v4.api.RepeatChart), "The return value should be an Altair plot object."


def test_numeric_plots_error():
    """Check TypeError raised when any of the argument type is wrong."""

    list_object = ["Python", "is", "a", "language"]
    with pytest.raises(TypeError):
        numeric_plots(list_object)
