# PLP-Project

# 🩺 AI-Powered Health Compliance & Emergency Support System

## 🌍 SDG Alignment
**Sustainable Development Goal 3: Good Health and Well-Being**  
This project addresses:
- **Target 3.4**: Reduce mortality from non-communicable diseases through prevention and treatment.
- **Target 3.8**: Achieve universal health coverage, including timely access to essential healthcare services.

---

## 📘 Project Overview

The **AI-Powered Health Compliance & Emergency Support System** helps patients stay on track with their treatment regimens while monitoring real-time health metrics through wearable devices. It leverages machine learning to:
- Detect medication non-compliance and abnormal health patterns
- Offer personalized recommendations and reminders
- Trigger emergency alerts and doctor outreach when critical conditions are detected

---

## 🚀 Key Features

### ✅ Treatment Adherence Tracker
- Log and track medications or appointments
- Calculate and display a weekly compliance score
- Use behavioral patterns to predict future non-compliance

### 🧠 AI-Powered Anomaly Detection
- Analyze heart rate, blood oxygen, and activity level for signs of distress
- Use models like Isolation Forest and LSTM for anomaly prediction
- Label and display risk levels: `Normal`, `Warning`, `Critical`

### 🛎️ Smart Reminders & Personalized Tips
- Adaptive notification system based on compliance history
- AI-generated messages to keep patients motivated and engaged

### ☎️ Emergency Alert & Doctor Notification System
- Trigger automatic alerts when health anomalies or skipped doses reach critical levels
- Manual “Panic Button” to contact a linked doctor
- Send reports via:
  - SMS or Email (via Twilio or SendGrid)
  - In-app messaging
  - Location-sharing (optional)

### 📊 User & Doctor Dashboards
- Patients view trends, streaks, recommendations, and alerts
- Doctors can access shared summaries and receive real-time alerts

---

## 🧠 AI and Technology Stack

| Component | Tools |
|----------|-------|
| **Backend** | Python, Flask, REST API |
| **Frontend** | HTML/CSS/JS (or Flutter/React Native) |
| **ML Models** | Isolation Forest, Random Forest, LSTM |
| **Libraries** | scikit-learn, TensorFlow, Pandas |
| **Database** | SQLite / Firebase / PostgreSQL |
| **Messaging APIs** | Twilio (SMS), SendGrid (email) |
| **Hosting** | Azure / Google Cloud / AWS |
| **Notification** | Firebase Cloud Messaging |

---

## 🔁 Sample Workflow

```text
1. User logs medication → AI updates compliance streak
2. Wearable sends heart rate → AI flags as “abnormal”
3. Missed dose + abnormal vitals → AI flags status as CRITICAL
4. Alert generated:
   - Sends SMS/email to doctor
   - Shows emergency contact options to patient


🛠 Setup Instructions
Clone the repository

bash
Copy
Edit
git clone https://github.com/your-username/health-compliance-ai.git
cd health-compliance-ai
Install dependencies

bash
Copy
Edit
pip install -r requirements.txt
Run the Flask app

bash
Copy
Edit
python app.py
Simulate data

python
Copy
Edit
import pandas as pd
import numpy as np

data = {
    'timestamp': pd.date_range(start='2023-10-01', periods=100, freq='T'),
    'heart_rate': np.random.randint(60, 100, 100),
    'blood_oxygen': np.random.randint(90, 100, 100),
    'med_taken': np.random.choice([1, 0], 100, p=[0.85, 0.15])
}
df = pd.DataFrame(data)
📡 Emergency Alert Logic (Sample)
python
Copy
Edit
from twilio.rest import Client

if risk_level == "CRITICAL":
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="URGENT: Patient XYZ has a critical health alert. View details immediately.",
        from_='+1234567890',
        to='+2547XXXXXXXX'
    )
📊 Model Evaluation
python
Copy
Edit
from sklearn.metrics import classification_report
print(classification_report(y_test, y_pred))
🔐 Ethical and Privacy Considerations
Patient data is encrypted and shared only with consent

GDPR & HIPAA compliant practices

Recommendations are not medical diagnoses; users are advised to consult licensed healthcare professionals

🧩 Future Enhancements
Real-time wearable API integration (e.g., Samsung Health)

Multilingual support

Doctor/caregiver mobile view

Voice assistant integration for reminders

👨‍⚕️ Contributors
Tony Wabuko – AI Developer, Medical Student
Brian Sangura - AI developer, Medical Student



📬 Contact
For questions or demo access, contact:
📧 tonywabuko@gmail.com
📞 +254 799104517
