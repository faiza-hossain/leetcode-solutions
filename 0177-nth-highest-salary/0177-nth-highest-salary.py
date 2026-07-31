import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    sorted_salaries=employee['salary'].sort_values(ascending=False)
    unique_s_s=sorted_salaries.unique()
    if N<=0 or N>len(unique_s_s):
        return pd.DataFrame({f"getNthHighestSalary({N})":[None]})
    else:
        result=unique_s_s[N-1]
        return pd.DataFrame({f"getNthHighestSalary({N})":[result]})