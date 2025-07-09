# models.py - placeholder content
import pandas as pd
import joblib

model = joblib.load('models/isolation_forest.pkl')


def check_compliance_and_risk(df):
    X = df[['heart_rate', 'blood_oxygen']]
    df['anomaly'] = model.predict(X)
    df['anomaly'] = df['anomaly'].apply(
        lambda x: 'Anomaly' if x == -1 else 'Normal')
    missed = df['med_taken'].value_counts().get(0, 0)
    risk = 'CRITICAL' if missed > 3 or 'Anomaly' in df['anomaly'].values else 'STABLE'
    return {'risk': risk, 'missed_doses': missed}
