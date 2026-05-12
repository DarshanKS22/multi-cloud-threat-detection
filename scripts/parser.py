import json
import glob
from collections import Counter

print("=" * 60)
print("REAL-TIME MULTI-CLOUD THREAT ANALYZER")
print("=" * 60)

# Find latest report
json_files = glob.glob("output/*.ocsf.json")

if not json_files:
    print("No JSON report found!")
    exit()

latest_file = max(json_files)

print(f"\nReading Report: {latest_file}")

# Load JSON
with open(latest_file, "r") as file:
    data = json.load(file)

total_findings = 0
failed_findings = 0

severity_counter = Counter()
service_counter = Counter()

# Process findings
for finding in data:

    total_findings += 1

    # Correct fields from OCSF structure
    status = finding.get("status_code", "")
    severity = finding.get("severity", "UNKNOWN")

    # Extract service name
    resources = finding.get("resources", [])

    service_name = "unknown"

    if resources:
        service_name = (
            resources[0]
            .get("group", {})
            .get("name", "unknown")
        )

    # Count FAIL findings
    if status == "FAIL":

        failed_findings += 1

        severity_counter[severity.upper()] += 1
        service_counter[service_name] += 1

print("\nTHREAT SUMMARY")
print("=" * 60)

print(f"Total Findings      : {total_findings}")
print(f"Failed Findings     : {failed_findings}")

print("\nSeverity Breakdown")
print("-" * 60)

for severity, count in severity_counter.items():
    print(f"{severity:<15}: {count}")

print("\nTop Affected Services")
print("-" * 60)

for service, count in service_counter.most_common(10):
    print(f"{service:<25}: {count}")

print("\nAnalysis Complete!")
print("=" * 60)
