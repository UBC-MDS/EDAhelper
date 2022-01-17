def plot_histogram(data, columns):
    """
    Creates histograms for numerical features within a dataframe using Altair.

    Parameters
    ----------
    data : pd.DataFrame
        A pandas dataframe
    columns : list, optional
        A list of numerical features for which to create histograms, or by 
        default will plot all numerical features in dataframe.

    Returns
    ------
    plot : altair.Chart object
        An Altair plot for each specified continuous feature

    Examples
    --------
    >>> df = pd.DataFrame(np.array([[1, 2, 3], [4, 5, 6], ["A", "B", "C"]]),
                        columns=['a', 'b', 'c'])
    >>> plot_histogram(df, columns = ['a', 'b'])
    """