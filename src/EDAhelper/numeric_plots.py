import pandas as pd
import altair as alt


def numeric_plots(df, ncols=5):
    """
    Takes a dataframe and plot the possible pairs of the numeric columns using Altair, 
    creating a matrix of correlation plots. The function conveniently breaks up the 
    features in the dataframe into blocks of `ncols` so that they can be fit into the 
    width of a page.

    Parameters:
        df: pandas.dataframe): 
            a pandas dataframe
        ncols: int
            number of columns.  default = 5

    Returns:
        splom: list
        a list of Altair chart objects for the plots
    """

    # Data validation
    if not isinstance(df, pd.DataFrame):
        raise TypeError("'df' should be of type 'pandas.DataFrame'.")

    if not isinstance(ncols, int):
        raise TypeError("'ncols' should be of type 'int'.")

    n_pages = int(df.shape[1] / ncols)
    if (df.shape[1] % ncols > 0):
        n_pages += 1

    splom = [None] * n_pages

    splom[0] = alt.Chart(df).mark_point(opacity=0.3, size=10).encode(
        alt.X(
            alt.repeat('row'),
            type='quantitative',
            scale=alt.Scale(zero=False)
        ),
        alt.Y(
            alt.repeat('column'),
            type='quantitative',
            scale=alt.Scale(zero=False)
        )
    ).properties(
        width=120,
        height=120
    ).repeat(
        column=list(df.columns),
        row=list(df.columns)
    ).configure_axis(
        labelFontSize=8,
        titleFontSize=8
    )

    return splom


print(numeric_plots.__doc__)
