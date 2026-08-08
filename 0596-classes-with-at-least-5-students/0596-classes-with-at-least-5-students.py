import pandas as pd

def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
        return courses.groupby('class').filter(lambda x: len(x) >= 5)['class'].drop_duplicates().to_frame()
