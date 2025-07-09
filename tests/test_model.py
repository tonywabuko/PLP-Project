# test_model.py - placeholder content
from app.models import check_compliance_and_risk
import pandas as pd

def test_check_risk():
    data = pd.DataFrame({
        'heart_rate': [70, 72, 150, 80],
        'blood_oxygen': [95, 97, 85, 98],
        'med_taken': [1, 0, 0, 0]
    })
    result = check_compliance_and_risk(data)
    assert 'risk' in result
    assert result['missed_doses'] == 3

