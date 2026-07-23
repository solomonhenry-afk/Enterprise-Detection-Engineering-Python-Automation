#!/usr/bin/env python3

"""
Lighthouse Technology
Detection Metadata Validator

Phase G
Detection Engineering & Coverage Measurement

Purpose:
    Validate Lighthouse Technology detection metadata
    before Sigma rule generation and SIEM deployment.

Author:
    Lighthouse Technology Security Engineering Team

Version:
    1.0
"""

import csv
import sys
from pathlib import Path

VALID_SEVERITIES = {
    "Critical",
    "High",
    "Medium",
    "Low",
    "Informational"
}

VALID_STATUS = {
    "Draft",
    "Reviewed",
    "Approved",
    "Deprecated"
}


def validate_metadata(csv_file):

    csv_path = Path(csv_file)

    if not csv_path.exists():
        print(f"[ERROR] File not found: {csv_path}")
        return False

    print("=" * 60)
    print(" Lighthouse Technology Detection Metadata Validator")
    print("=" * 60)

    errors = 0
    warnings = 0
    checked = 0
    detection_ids = set()

    with open(csv_path, newline="", encoding="utf-8") as file:

        reader = csv.DictReader(file)

        required = [
            "DetectionID",
            "DetectionName",
            "Severity",
            "Status",
            "ATTACKTechnique"
        ]

        for row in reader:

            checked += 1

            for field in required:
                if not row.get(field):
                    print(f"[ERROR] Missing {field}")
                    errors += 1

            detection_id = row.get("DetectionID")

            if detection_id in detection_ids:
                print(f"[ERROR] Duplicate Detection ID: {detection_id}")
                errors += 1
            else:
                detection_ids.add(detection_id)

            severity = row.get("Severity", "")

            if severity not in VALID_SEVERITIES:
                print(f"[WARNING] Invalid Severity: {severity}")
                warnings += 1

            status = row.get("Status", "")

            if status not in VALID_STATUS:
                print(f"[WARNING] Invalid Status: {status}")
                warnings += 1

    print("\nValidation Summary")
    print("-" * 60)
    print(f"Records Checked : {checked}")
    print(f"Errors          : {errors}")
    print(f"Warnings        : {warnings}")

    if errors == 0:
        print("\nValidation Successful")
    else:
        print("\nValidation Failed")

    return errors == 0


def main():

    if len(sys.argv) != 2:
        print(
            "Usage:\n"
            "python validate_detection_metadata.py "
            "<metadata.csv>"
        )
        sys.exit(1)

    validate_metadata(sys.argv[1])


if __name__ == "__main__":
    main()
