#!/usr/bin/env python3
# CC0-1.0 — Financial/credential exposure screener over the frozen MCP Atlas
# Milestone-A exports (Zenodo record 23333516, SHA-256 anchored 2026-10-12).
# Recomputes the numbers in the Financial MCP Risk Baseline appendix (v0.2).
# Usage: python financial_exposure_screener.py <path-to-live_tools_labels.csv>
import csv, sys
from collections import defaultdict

MONEY_PARAM = "money_amount"
CRED_PARAM = "credential_value"

money_tools, cred_tools = 0, 0
money_servers, cred_servers = set(), set()
per_class = defaultdict(int)

with open(sys.argv[1], newline="") as f:
    for row in csv.DictReader(f):
        cls = set(row["param_classes"].split("|")) if row["param_classes"] else set()
        for c in cls:
            per_class[c] += 1
        if MONEY_PARAM in cls:
            money_tools += 1
            money_servers.add(row["server_id"])
        if CRED_PARAM in cls:
            cred_tools += 1
            cred_servers.add(row["server_id"])

print(f"money_amount    tools={money_tools}  servers={len(money_servers)}")
print(f"credential_value tools={cred_tools}  servers={len(cred_servers)}")
print(f"compound (both)  servers={len(money_servers & cred_servers)}")
print("full class histogram:", dict(sorted(per_class.items(), key=lambda kv: -kv[1])))
