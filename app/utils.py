# utils.py - placeholder content
def calculate_compliance(df):
    total = len(df)
    taken = df['med_taken'].sum()
    return round((taken / total) * 100, 2)
