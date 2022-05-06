import pandas as pd

def load_data():
    df = pd.read_spss('D:\File Gw\Programming\Python\Project Akhir ProA\Colab\ResearchProjectData.sav')
    return df
df = load_data()
