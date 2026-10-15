from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
import numpy as np

app = Flask(__name__)

# --- ROUTE 1: LANDING PAGE ---
@app.route('/')
def landing():
    return render_template('landing.html')

# --- PAGE 2: PORTAL TRANSITION (Entering the Upside Down) ---
@app.route('/portal')
def portal():
    return render_template('portal.html')

# --- ROUTE 2: INPUT PAGE ---
@app.route('/input', methods=['GET', 'POST'])
def input_page():
    if request.method == 'POST':
        # This part runs when they click "ANALYZE" on the input page
        try:
            # We assume the user uploads 3 files. 
            # In a real hackathon, wrap these in try/except blocks in case a file is missing.
            
            # 1. READ PERFORMANCE DATA
            f_perf = request.files['file_performance']
            df_perf = pd.read_excel(f_perf)
            fill_rate = df_perf['Historical Fill Rate'].mean()
            lead_time = df_perf['Avg Lead Time'].mean()

            # 2. READ BUFFER DATA
            f_buff = request.files['file_buffer']
            df_buff = pd.read_excel(f_buff)
            buffer_days = df_buff['Inventory Buffer'].mean()
            recovery_time = df_buff['Recovery Time'].mean()

            # 3. READ NETWORK DATA
            f_net = request.files['file_network']
            df_net = pd.read_excel(f_net)
            supplier_count = df_net['Supplier Count'].mean()
            concentration = df_net['Supplier Concentration Ratio'].mean()

            # 4. CALCULATE RISK (The Logic)
            risk_score = 0
            
            # Logic: High Fill Rate + Low Buffer + Low Supplier Count = DISASTER
            if fill_rate > 98: risk_score += 30
            if buffer_days > 60: risk_score += 10 # Hoarding inventory is also bad (sluggish)
            if supplier_count < 2: risk_score += 30
            if concentration > 0.8: risk_score += 20
            if recovery_time < 1: risk_score += 10

            risk_score = min(risk_score, 100)
            
            # Determine Status
            status = "DANGER" if risk_score > 75 else "SAFE"

            # Pass all data to the dashboard
            return render_template('dashboard.html', 
                                   score=int(risk_score), 
                                   status=status,
                                   fill_rate=round(fill_rate, 1),
                                   lead_time=round(lead_time, 1),
                                   buffer_days=round(buffer_days, 1),
                                   recovery_time=round(recovery_time, 1),
                                   supplier_count=int(supplier_count),
                                   concentration=round(concentration, 2))

        except Exception as e:
            return f"Error processing files: {e}. Please ensure specific columns exist."

    return render_template('input.html')

if __name__ == '__main__':
    app.run(debug=True)