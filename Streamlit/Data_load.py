import pandas as pd

def load_data():
    df = pd.read_spss('ResearchProjectData.sav')
    return df
df = load_data()
