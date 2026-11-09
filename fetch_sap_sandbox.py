import requests
import pandas as pd
import sqlite3

# SAP Business Accelerator Hub Sandbox API Endpoint for Sales Orders
url = "https://sandbox.api.sap.com/s4hanacloud/sap/opu/odata/sap/API_SALES_ORDER_SRV/A_SalesOrder"

headers = {
    "APIKey": "YOUR_SAP_SANDBOX_API_KEY",  # Get your free key from api.sap.com
    "Accept": "application/json"
}

try:
    response = requests.get(url, headers=headers, params={"$top": 50})
    if response.status_code == 200:
        data = response.json().get('d', {}).get('results', [])
        if data:
            df_sap = pd.DataFrame(data)

            # Store live API payload into our local SQLite database
            conn = sqlite3.connect('sap_operations.db')
            df_sap.to_sql('SAP_SANDBOX_SALES_ORDERS', conn, if_exists='replace', index=False)
            print("Successfully fetched live SAP sandbox records and saved to database!")
            conn.close()
        else:
            print("Connected to SAP Sandbox, but no records were returned.")
    else:
        print(f"Failed to connect. Status Code: {response.status_code}. Check your API key.")
except Exception as e:
    print(f"API Connection Error: {e}")