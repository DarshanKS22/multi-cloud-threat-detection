#!/bin/bash

echo "======================================================"
echo " REAL-TIME MULTI-CLOUD THREAT DETECTION SYSTEM"
echo "======================================================"

echo ""
echo "[1] Starting AWS Security Scan..."
echo ""

# AWS Scan
prowler aws --region ap-south-1

echo ""
echo "[2] Starting Azure Security Scan..."
echo ""

# Azure Scan
prowler azure --az-cli-auth

echo ""
echo "[3] Running Threat Analyzer..."
echo ""

# Threat Analysis
python3 scripts/parser.py

echo ""
echo "[4] Running Alert Engine..."
echo ""

# Alert Engine
python3 scripts/alert.py

echo ""
echo "[5] Scan Completed Successfully!"
echo ""

echo "Reports Generated In:"
echo "output/"

echo ""
echo "======================================================"
echo " MULTI-CLOUD SECURITY WORKFLOW FINISHED"
echo "======================================================"
