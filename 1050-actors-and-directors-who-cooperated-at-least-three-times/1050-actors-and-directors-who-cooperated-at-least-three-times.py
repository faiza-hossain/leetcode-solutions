import pandas as pd

def actors_and_directors(actor_director: pd.DataFrame) -> pd.DataFrame:
    pairs = actor_director.groupby(['actor_id', 'director_id']).size()
    result = pairs[pairs >= 3].reset_index().drop(columns=0)
    return result