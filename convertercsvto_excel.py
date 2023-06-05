import pandas as pd
uwu = pd.read_csv(f"expenses.csv") #Read the dataframe
uwu.to_excel(f'expenses.xlsx', index=False) #Save the dataframe