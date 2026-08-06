import pandas as pd

def categorize_products(activities: pd.DataFrame) -> pd.DataFrame:
    df=activities.groupby('sell_date').agg({'product':lambda x:','.join(sorted(list(set(x))))}).reset_index()
    df.columns=['sell_date', 'products']
    df['num_sold'] = activities.groupby('sell_date')['product'].nunique().values
    df=df[['sell_date', 'num_sold', 'products']]
    df =df.sort_values('sell_date')
    return df
