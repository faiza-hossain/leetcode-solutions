import pandas as pd

def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    result = activity.sort_values('event_date').groupby('player_id').head(1).reset_index(drop=True)
    result = result.rename(columns={'event_date': 'first_login'})
    return result[['player_id', 'first_login']]