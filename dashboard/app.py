from flask import Flask, render_template
import json
import glob
from collections import Counter

app = Flask(__name__)

@app.route("/")

def dashboard():

    # Read ALL JSON reports
    json_files = glob.glob("output/*.ocsf.json")

    if not json_files:
        return "No reports found!"

    total_findings = 0
    failed_findings = 0

    aws_findings = 0
    azure_findings = 0

    severity_counter = Counter()
    service_counter = Counter()

    # Process all reports
    for report_file in json_files:

        with open(report_file, "r") as file:
            data = json.load(file)

        for finding in data:

            total_findings += 1

            status = finding.get("status_code", "")
            severity = finding.get("severity", "UNKNOWN")

            resources = finding.get("resources", [])

            service_name = "unknown"

            if resources:
                service_name = (
                    resources[0]
                    .get("group", {})
                    .get("name", "unknown")
                )

            # Detect cloud provider
            provider = (
                finding.get("cloud", {})
                .get("provider", "unknown")
            )

            if provider == "aws":
                aws_findings += 1

            elif provider == "azure":
                azure_findings += 1

            # Count FAIL findings
            if status == "FAIL":

                failed_findings += 1

                severity_counter[severity.upper()] += 1
                service_counter[service_name] += 1

    return render_template(
        "index.html",
        total_findings=total_findings,
        failed_findings=failed_findings,
        aws_findings=aws_findings,
        azure_findings=azure_findings,
        severity_counter=severity_counter,
        top_services=service_counter.most_common(10)
    )

if __name__ == "__main__":
    app.run(debug=True)
