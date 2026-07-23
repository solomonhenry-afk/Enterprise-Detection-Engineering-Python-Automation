#!/usr/bin/env python3

"""
Lighthouse Technology
Detection Evidence Collector

Phase G – Detection Engineering & Coverage Measurement

Purpose:
    Collect detection metadata and generate a normalized
    detection evidence register.

Author:
    Lighthouse Technology Detection Engineering Team

Version:
    1.0
"""

import csv
import sys
from pathlib import Path
from datetime import datetime

INPUT_FILE = Path(
    "data/normalized/detection/LHT-DetectionMetadata.csv"
)

OUTPUT_FILE = Path(
    "data/normalized/detection/LHT-DetectionEvidence-Normalized.csv"
)


def load_metadata():

    if not INPUT_FILE.exists():
        print(f"[ERROR] Input file not found:\n{INPUT_FILE}")
        sys.exit(1)

    detections = []

    with open(INPUT_FILE, newline="", encoding="utf-8") as csvfile:

        reader = csv.DictReader(csvfile)

        for row in reader:

            detection_id = (row.get("Detection_ID") or "").strip()

            if not detection_id:
                continue

            detections.append(
                {
                    "Evidence_ID": f"EVD-{detection_id}",
                    "Detection_ID": detection_id,
                    "Detection_Name": (row.get("Detection_Name") or "").strip(),
                    "MITRE_ID": (row.get("MITRE_ID") or "").strip(),
                    "MITRE_Tactic": (row.get("MITRE_Tactic") or "").strip(),
                    "Severity": (row.get("Severity") or "").strip(),
                    "Validation_Status": "Validated",
                    "Evidence_Source": "Detection Metadata",
                    "Collection_Date": datetime.now().strftime("%Y-%m-%d"),
                }
            )

    return detections


def write_evidence(records):

    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)

    fields = [
        "Evidence_ID",
        "Detection_ID",
        "Detection_Name",
        "MITRE_ID",
        "MITRE_Tactic",
        "Severity",
        "Validation_Status",
        "Evidence_Source",
        "Collection_Date",
    ]

    with open(
        OUTPUT_FILE,
        "w",
        newline="",
        encoding="utf-8"
    ) as csvfile:

        writer = csv.DictWriter(csvfile, fieldnames=fields)

        writer.writeheader()

        writer.writerows(records)


def print_summary(records):

    print("=" * 65)
    print(" Lighthouse Technology Detection Evidence Collector")
    print("=" * 65)

    print()

    print(f"Evidence Records Collected : {len(records)}")

    print("\nGenerated:")

    print(f"  {OUTPUT_FILE}")

    print("\nCollection Complete.")


def main():

    records = load_metadata()

    if not records:
        print("[WARNING] No detection metadata found.")
        return

    write_evidence(records)

    print_summary(records)


if __name__ == "__main__":
    main()
