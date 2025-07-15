import pandas as pd
import joblib

model = joblib.load('models/isolation_forest.pkl')

def check_compliance_and_risk(df):
    required_columns = ['heart_rate', 'blood_oxygen', 'med_taken']
    if not all(col in df.columns for col in required_columns):
        raise ValueError(f"Missing one or more required columns: {required_columns}")

    X = df[['heart_rate', 'blood_oxygen']]
    df['anomaly'] = model.predict(X)
    df['anomaly'] = df['anomaly'].apply(
        lambda x: 'Anomaly' if x == -1 else 'Normal'
    )
    
    missed = df['med_taken'].value_counts().get(0, 0)
    risk = 'CRITICAL' if missed > 3 or 'Anomaly' in df['anomaly'].values else 'STABLE'
    
    return {
        'risk': risk,
        'missed_doses': missed,
        'records': df.to_dict(orient='records')
    }
    
def check_compliance_and_risk(df):
    required_columns = ['heart_rate', 'blood_oxygen', 'med_taken']
    missing = [col for col in required_columns if col not in df.columns]
    if missing:
        return f"Missing columns: {missing}"  # changed from raise error
    ...

