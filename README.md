# EDAhelper
[![Documentation Status](https://readthedocs.org/projects/edahelper/badge/?version=latest)](https://edahelper.readthedocs.io/en/latest/?badge=latest)
[![codecov](https://codecov.io/gh/UBC-MDS/EDAhelper/branch/master/graph/badge.svg?token=2aRO8HaPHn)](https://codecov.io/gh/UBC-MDS/EDAhelper)
![github workflow](https://github.com/UBC-MDS/EDAhelper/actions/workflows/ci-cd.yml/badge.svg)

Tools to make EDA easier!

## About

This package is aimed at making the EDA process more effective. Basically, we found there were tons of repetitive work when getting a glimpse of the data set. To stop wasting time in repeating procedures, our team came up with the idea to develop a toolkit that includes the following functions:

  1. Clean the data and replace missing values by using the method preferred.
  2. Provide the description of the data such as the distribution of each column of the data.
  3. Give the correlation plot between different numeric columns automatically.
  4. Combine the plots and make them suitable for the report.

## Contributors

- Rowan Sivanandam
- Steven Leung
- Vera Cui
- Jennifer Hoang

## Feature specifications

  1. `preprocess(path, method=None, fill_value=None, read_func=pd.read_csv, **kwarg)` : <br>
  The function is to preprocess data in txt or csv by dealing with missing values. There are 5 imputation methods provided (None, 'most_frequent', 'mean', 'median', 'constant'). Finally, it will return the processed data as pandas.DataFrame.
  2. `column_stats(data, column1, column2 = None, column3 = None, column4 = None)` : <br>
  The function is to obtain summary statistics of column(s) including count, mean, median, mode, Q1, Q3, variance, standard deviation, correlation. Finally, it will return summary table detailing all statistics and correlations between chosen columns.
  3. `plot_histogram(data, columns=["all"], num_bins=30)`: : <br>
  The function is to create histograms for numerical features within a dataframe using Altair. Finally, it will return an Altair plot for each specified continuous feature.
  4. `numeric_plots(df)` : <br>
  The function takes a dataframes and plot the possible pairs of the numeric columns using Altair, creating a matrix of correlation plots.

  
## Related projects

Surely, EDA is not a new topic to data scientists. There are quite a few packages doing similar work on PyPI. However, most of them only include limited functions like just providing descriptive statistics. Our proposal is more of a one-in-all toolkit for EDA. Below is a list of sister-projects.

- [auto-eda](https://pypi.org/project/auto-eda/) : It is an automatic script that generating information in the dataset.
- [easy-eda](https://pypi.org/project/easy-eda/) : Exploratory Data Analysis.
- [quick-eda](https://pypi.org/project/quick-eda/) : Important dataframe statistics with a single command.
- [eda-report](https://pypi.org/project/eda-report/) : A simple program to automate exploratory data analysis and reporting.

## Installation

You can also use Git to clone the repository from GitHub to install the latest development version:
```bash
$ git clone https://github.com/UBC-MDS/EDAhelper.git
$ cd dist
$ pip install EDAhelper-3.0.0-py3-none-any.whl
```
or install from `PyPI`:
```bash
$ pip install edahelper
```

## Usage

Example usage:
```python
from EDAhelper.preprocess import preprocess
EDAhelper.preprocess('file_path')

from EDAhelper.column_stats import column_stats
EDAhelper.column_stats(df, columns = ('Date', 'PctPopulation', 'CrimeRatePerPop'))

from EDAhelper.plot_histogram import plot_histogram
EDAhelper.plot_histogram(df, columns = ['A', 'B'])

from EDAhelper.numeric_plots import numeric_plots
EDAhelper.numeric_plots(df) 
```

## Contributing

Interested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.

## License

`EDAhelper` was created by Rowan Sivanandam, Steven Leung, Vera Cui, Jennifer Hoang. It is licensed under the terms of the MIT license.

## Credits

`EDAhelper` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).
