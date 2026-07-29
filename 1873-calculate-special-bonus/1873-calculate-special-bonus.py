import pandas as pd

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    employees['bonus']=0
    condition=(employees['employee_id']%2!=0) & (~ employees['name'].str.lower().str.startswith('m'))
    employees.loc[condition,'bonus']=employees['salary']
    return employees[['employee_id','bonus']].sort_values('employee_id')