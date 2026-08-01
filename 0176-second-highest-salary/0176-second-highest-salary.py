import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    sorted_salaries = employee['salary'].sort_values(ascending=False)
    unique_salaries = sorted_salaries.unique()

    if len(unique_salaries) < 2:
        return pd.DataFrame({'SecondHighestSalary': [None]})
    else:
        result = pd.Series(unique_salaries).iloc[1]
        return pd.DataFrame({'SecondHighestSalary': [result]})