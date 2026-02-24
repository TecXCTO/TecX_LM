  import re

def analyze_b300_logs(log_file):
    print(f"🔍 Analyzing B300 Training Logs: {log_file}...")
    
    anomalies = []
    with open(log_file, 'r') as f:
        for line in f:
            # 1. Check for Thermal Throttling (B300 pulls 1400W)
            if "Thermal Violation" in line or "Clock Throttle" in line:
                anomalies.append(f"⚠️ THERMAL ALERT: GPU is overheating. Check Liquid Cooling CDU.")

            # 2. Check for NVLink 6 Failures
            if "NVLink Error" in line or "Fabric Manager Timeout" in line:
                anomalies.append(f"🚨 NETWORK ALERT: NVLink 6 disconnect detected. Loss of sync.")

            # 3. Check for Nan/Inf (Math Divergence)
            if "Loss: nan" in line or "Grad: inf" in line:
                anomalies.append(f"📉 MATH ALERT: Gradient explosion. Reduce Learning Rate.")

    if not anomalies:
        print("✅ Logs are healthy. Blackwell Cluster stable.")
    else:
        for a in anomalies: print(a)

# Example Usage
# analyze_b300_logs("resonance_training_run_01.log")
