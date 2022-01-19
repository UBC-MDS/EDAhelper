from EDAhelper.plot_histogram import plot_histogram
import pandas as pd
import pytest
import altair as alt

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

def test_plot_histogram():
    """Test plot_histogram on a dataframe."""
    # Case 1: Test default settings and return
    result = plot_histogram(df())
    assert isinstance(
        result, alt.vegalite.v4.api.RepeatChart
    ), "Altair Chart object should be returned."

    # Case 2: Test erroneous inputs
    with pytest.raises(Exception):
        plot_histogram([1, 2, 3])

    with pytest.raises(Exception):
        plot_histogram(df(), columns = "A")

    with pytest.raises(Exception):
        plot_histogram(df(), num_bins = "ten")
        