# # detection/model.py
import pandas as pd
import random
from datetime import datetime, timedelta
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier

# Generate and preprocess dataset
def financial_transactions(num_records):
    data = []
    for _ in range(num_records):
        account_no = f"ACC{random.randint(10000000, 99999999)}"
        ifsc_code = f"IFSC{random.randint(100000, 999999)}"
        amount = round(random.uniform(10, 10000), 2)
        transaction_date = datetime.now() - timedelta(days=random.randint(0, 30))
        transaction_type = random.choice(['credit', 'debit'])
        is_fraud = random.choices([0, 1], weights=[0.50, 0.50])[0]
        
        data.append({
            'Transaction ID': f"T{random.randint(100000, 999999)}",
            'Account Number': account_no,
            'IFSC Code': ifsc_code,
            'Amount': amount,
            'Transaction Date': transaction_date,
            'Transaction Type': transaction_type,
            'Fraud Label': is_fraud
        })
    
    return pd.DataFrame(data)

# Training the model
def train_model():
    num_records = 1000
    dataset = financial_transactions(num_records)
    dataset['Transaction Date'] = pd.to_datetime(dataset['Transaction Date']).view('int64') / 10**9
    label_encoder = LabelEncoder()
    dataset['Transaction Type'] = label_encoder.fit_transform(dataset['Transaction Type'])
    X = dataset.drop(['Transaction ID', 'Account Number', 'IFSC Code', 'Fraud Label'], axis=1)
    y = dataset['Fraud Label']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    model = RandomForestClassifier(random_state=42)
    model.fit(X_train, y_train)
    return model, label_encoder

model, label_encoder = train_model()

