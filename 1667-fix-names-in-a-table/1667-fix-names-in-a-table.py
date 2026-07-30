import pandas as pd

def fix_names(users: pd.DataFrame) -> pd.DataFrame:
    users['name']=users['name'].apply(lambda x:x.capitalize())
    users=users.sort_values('user_id')
    return users