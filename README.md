# EDAhelper

Tools to make EDA easier!

## About

This package is aimed at making the EDA process more effective. Basically, we found there were tons of repetitive work when getting a glimpse of the data set. To stop wasting time in repeating procedures, our team came up with the idea to develop a toolkit that includes the following functions:

  1. Clean the data and replace missing values by using the method preferred.
  2. Provide the description of the data such as the distribution of each column of the data.
  3. Give the correlation plot between different columns and omit the pairs that are not significantly correlated.
  4. Combine the plots and make them suitable for the report.

## Contributors

- Rowan Sivanandam
- Steven Leung
- Vera Cui
- Jennifer Hoang

## Feature specifications

  1. `preprocess(path, method='most_frequent', fill_value = None)` : <br>
  The function is to preprocess data in txt or csv by dealing with missing values. There are 5 imputation methods provided (None, 'most_frequent', 'mean', 'median', 'constant'). Finally, it will return the processed data as pandas.DataFrame.
  
## Related projects

Surely, EDA is not a new topic to data scientists. There are quite a few packages doing similar work on PyPI. However, most of them only include limited functions like just providing descriptive statistics. Our proposal is more of a one-in-all toolkit for EDA. Below is a list of sister-projects.

- [auto-eda](https://pypi.org/project/auto-eda/) : It is an automatic script that generating information in the dataset.
- [easy-eda](https://pypi.org/project/easy-eda/) : Exploratory Data Analysis.
- [quick-eda](https://pypi.org/project/quick-eda/) : Important dataframe statistics with a single command.
- [eda-report](https://pypi.org/project/eda-report/) : A simple program to automate exploratory data analysis and reporting.

## Installation

```bash
$ pip install EDAhelper
```

## Usage

Example usage:
```python
from EDAhelper import EDAhelper
EDAhelper.preprocess('file_path')
```

## Contributing

Interested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.

## License

`EDAhelper` was created by Rowan Sivanandam, Steven Leung, Vera Cui, Jennifer Hoang. It is licensed under the terms of the MIT license.

## Credits

`EDAhelper` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).
