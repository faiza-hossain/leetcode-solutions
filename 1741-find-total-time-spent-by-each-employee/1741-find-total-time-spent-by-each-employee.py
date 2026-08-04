import pandas as pd

def total_time(employees: pd.DataFrame) -> pd.DataFrame:
    result = employees.groupby(['event_day', 'emp_id']).agg({'out_time': 'sum', 'in_time': 'sum'})
    result['total_time'] = result['out_time'] - result['in_time']
    result = result.reset_index()
    result = result.rename(columns={'event_day': 'day'})
    result = result[['day', 'emp_id', 'total_time']]
    result = result.sort_values(['day', 'emp_id'])
    return result