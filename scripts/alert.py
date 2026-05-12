import json
import glob

print("=" * 50)
print("REAL-TIME ALERT ENGINE")
print("=" * 50)

# Find latest JSON report
json_files = glob.glob("output/*.ocsf.json")

if not json_files:
    print("No JSON report found!")
    exit()

latest_file = max(json_files)

# Load report
with open(latest_file, "r") as file:
    data = json.load(file)

high_alerts = 0

# Process findings
for finding in data:

    status = finding.get("status_code", "")
    severity = finding.get("severity", "").upper()

    # Only HIGH severity failed findings
    if status == "FAIL" and severity == "HIGH":

        high_alerts += 1

        title = (
            finding.get("finding_info", {})
            .get("title", "Unknown Threat")
        )

        resources = finding.get("resources", [])

        service = "unknown"

        if resources:
            service = (
                resources[0]
                .get("group", {})
                .get("name", "unknown")
            )

        print("\n" + "=" * 50)
        print("HIGH SEVERITY ALERT DETECTED")
        print("=" * 50)

        print(f"Service   : {service}")
        print(f"Severity  : {severity}")
        print(f"Issue     : {title}")

print("\n" + "=" * 50)

if high_alerts == 0:
    print("No HIGH severity alerts found.")
else:
    print(f"Total HIGH Alerts Detected: {high_alerts}")

print("=" * 50)
