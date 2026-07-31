import pandas as pd

def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    return patients[patients['conditions'].str.split(' ').apply(lambda x:any(w.startswith('DIAB1')for w in x))]