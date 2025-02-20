import pandas as pd


df = pd.read_excel(r"C:\Users\mayan\OneDrive\Desktop\casestudy\raw_tweets_queens_death.xlsx", engine="openpyxl")


df.to_csv(r"C:\Users\mayan\OneDrive\Desktop\casestudy\output_file.csv", index=False) 

print("Excel file successfully converted to CSV!")
