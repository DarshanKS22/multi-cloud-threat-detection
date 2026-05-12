# REAL-TIME THREAT DETECTION IN MULTI-CLOUD ENVIRONMENT USING PROWLER

# 1. INTRODUCTION

This project is a Real-Time Multi-Cloud Threat Detection System developed using Prowler, Python, Flask, Bash scripting, AWS, Azure, and GitHub Actions.

The main goal of this project is to automatically scan cloud environments, detect security vulnerabilities and misconfigurations, analyze threats, generate alerts, and visualize security findings through a dashboard.

The project supports:
- AWS Cloud
- Azure Cloud

This project demonstrates concepts of:
- Cloud Security
- DevSecOps
- Threat Detection
- Compliance Auditing
- Automation
- CI/CD Security Integration

---

# 2. WHAT IS PROWLER?

Prowler is an open-source cloud security scanning tool.

It is mainly used for:
- AWS security auditing
- Azure security auditing
- Compliance validation
- Vulnerability detection
- Misconfiguration detection

Prowler checks cloud environments against security best practices and compliance standards.

Examples:
- IAM Security
- CloudTrail logging
- MFA configuration
- Public storage access
- Encryption settings
- Monitoring configuration

---

# 3. WHY WE USED PROWLER

We used Prowler because:

- It supports both AWS and Azure.
- It automatically performs hundreds of security checks.
- It generates reports in HTML, JSON, and CSV format.
- It supports CIS benchmarks and compliance standards.
- It is widely used in cloud security and DevSecOps.
- It helps automate cloud threat detection.

---

# 4. PROJECT OBJECTIVE

The objectives of this project are:

- Detect cloud security threats automatically
- Monitor AWS and Azure environments
- Analyze vulnerabilities and compliance issues
- Generate real-time alerts
- Visualize findings in a dashboard
- Automate the workflow using scripts and CI/CD

---

# 5. TECHNOLOGIES USED

| Technology | Purpose |
|------------|---------|
| Python | Threat analysis and automation |
| Flask | Dashboard backend |
| HTML + Bootstrap | Dashboard frontend |
| Bash Script | Automation workflow |
| Prowler | Cloud security scanning |
| AWS CLI | AWS authentication |
| Azure CLI | Azure authentication |
| GitHub Actions | CI/CD automation |
| JSON | Security report parsing |

---

# 6. CLOUD PLATFORMS USED

## AWS Services Used

- IAM
- CloudTrail
- CloudWatch
- Config
- S3
- EC2
- Lambda

## Azure Services Used

- Defender
- Entra ID
- Storage Accounts
- Monitoring
- Security Center

---

# 7. PROJECT WORKFLOW

```text
AWS + Azure
      ↓
Prowler Security Scan
      ↓
JSON Security Reports
      ↓
Python Threat Analyzer
      ↓
Alert Engine
      ↓
Flask Dashboard
      ↓
GitHub Actions CI/CD
