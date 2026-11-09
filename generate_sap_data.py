import sqlite3
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Initialize Database
conn = sqlite3.connect('sap_operations.db')
cursor = conn.cursor()

# Set random seed for reproducibility
np.random.seed(42)
n_orders = 1000

# Generate Sales Order Header (VBAK) & Items (VBAP)
order_ids = [f"SO100{i}" for i in range(n_orders)]
start_date = datetime(2026, 1, 1)
order_dates = [start_date + timedelta(days=int(np.random.randint(0, 90))) for _ in range(n_orders)]
depots = ['Gurgaon_Depot_01', 'Mumbai_Depot_02', 'Bengaluru_Depot_03', 'Kolkata_Depot_04']
materials = ['HILTI-TE300', 'HILTI-GX3', 'HILTI-PD-E', 'HILTI-HIT-HY200', 'HILTI-PR30']

vbak_data = {
    'VBELN': order_ids,
    'ERDAT': [d.strftime('%Y-%m-%d') for d in order_dates],
    'WERKS': np.random.choice(depots, n_orders, p=[0.4, 0.25, 0.2, 0.15]),
    'MATNR': np.random.choice(materials, n_orders),
    'KSMENG': np.random.randint(1, 50, n_orders),
    'TARGET_SLA_DAYS': 2
}

df_vbak = pd.DataFrame(vbak_data)

# Generate Delivery Notes (LIKP/LIPS) with variable delays
delivery_lags = np.random.choice([1, 2, 3, 4, 5], n_orders, p=[0.5, 0.25, 0.15, 0.06, 0.04])
df_vbak['ACTUAL_DELIVERY_DATE'] = [
    (datetime.strptime(d, '%Y-%m-%d') + timedelta(days=int(lag))).strftime('%Y-%m-%d')
    for d, lag in zip(df_vbak['ERDAT'], delivery_lags)
]
df_vbak['DELIVERY_STATUS'] = np.where(delivery_lags <= df_vbak['TARGET_SLA_DAYS'], 'ON_TIME', 'SLA_BREACH')

# Save to SQLite tables mimicking SAP tables
df_vbak.to_sql('VBAK_LIPS_COMBINED', conn, if_exists='replace', index=False)
print("Successfully generated SAP transactional database: sap_operations.db")
conn.close()