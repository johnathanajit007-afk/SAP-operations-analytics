import sqlite3
import pandas as pd

# Connect to the SAP database generated in Step 1
conn = sqlite3.connect('sap_operations.db')

# SQL Query executing aggregated SLA tracking & OTIF performance calculation
sql_query = """
SELECT 
    WERKS AS Depot_Location,
    MATNR AS Material_Code,
    COUNT(VBELN) AS Total_Orders,
    SUM(CASE WHEN DELIVERY_STATUS = 'ON_TIME' THEN 1 ELSE 0 END) AS On_Time_Deliveries,
    SUM(CASE WHEN DELIVERY_STATUS = 'SLA_BREACH' THEN 1 ELSE 0 END) AS SLA_Breaches,
    ROUND(CAST(SUM(CASE WHEN DELIVERY_STATUS = 'ON_TIME' THEN 1 ELSE 0 END) AS FLOAT) / COUNT(VBELN) * 100, 2) AS OTIF_Performance_Pct,
    SUM(KSMENG) AS Total_Units_Shipped
FROM VBAK_LIPS_COMBINED
GROUP BY WERKS, MATNR
ORDER BY OTIF_Performance_Pct ASC;
"""

# Execute query and pull into Pandas DataFrame
df_summary = pd.read_sql_query(sql_query, conn)

# Export processed audit summary for reporting
df_summary.to_csv('sap_sla_kpi_summary.csv', index=False)
print("SQL Analysis Complete: Output exported to sap_sla_kpi_summary.csv")

conn.close()