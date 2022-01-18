import pandas as pd
import altair as alt
from EDAhelper.EDAhelper import numeric_plots


@pytest.fixture
def numeric_cols():
    movies = pd.read_json("lab2-movies.json")
    numeric_cols = movies.select_dtypes(include=['float64', 'int64']
                                        ).drop('id', axis=1)
    return numeric_cols


def test_numeric_plots():
    actual = numeric_plots(numeric_cols())

    # Check that the return value is a list of objects
    assert isinstance(actual, list),
    "The return value should be a list of Altair plot objects."

    for i in range(0, len(actual)):
        assert isinstance(actual[i], alt.vegalite.v4.api.RepeatChart),
        "The return list should contain objects of Altair plots."


def test_numeric_plots_error():
    """Check TypeError raised when any of the argument type is wrong."""
    list_object = ["Python", "is", "a", "language"]
    with pytest.raises(TypeError):
        numeric_plot(list_object)

    with pytest.raises(TypeError):
        numeric_plot(numeric_cols(), list_object)
