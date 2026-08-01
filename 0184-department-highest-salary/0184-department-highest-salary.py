import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    merged=employee.merge(department,left_on='departmentId',right_on='id',suffixes=('_employee','_department'))
    highest_salary=merged.groupby('departmentId').apply(lambda x:x[x['salary']==x['salary'].max()])
    highest_salary=highest_salary.reset_index(drop='True')
    df=highest_salary[['name_department','name_employee','salary']]
    df.columns=['Department','Employee','Salary']
    return df