#!/usr/bin/env python3

"""
Lighthouse Technology
MITRE ATT&CK Coverage Mapper

Phase G – Detection Engineering & Coverage Measurement

Purpose:
    Parse Lighthouse Technology detection metadata and
    automatically generate ATT&CK coverage statistics and
    an executive coverage report.

Author:
    Lighthouse Technology Detection Engineering Team

Version:
    1.0
"""

import csv
import sys
from pathlib import Path
from collections import defaultdict

# ----------------------------------------------------------------------
# Configuration
# ----------------------------------------------------------------------

INPUT_FILE = Path("data/normalized/detection/LHT-DetectionMetadata.csv")

OUTPUT_REPORT = Path(
    "reports/detection/ATTACK-Coverage-Automated-Report.md"
)

# ----------------------------------------------------------------------
# Load Detection Metadata
# ----------------------------------------------------------------------


def load_detection_metadata():

    if not INPUT_FILE.exists():

        print(f"[ERROR] Metadata file not found:\n{INPUT_FILE}")
        sys.exit(1)

    attack_mapping = defaultdict(list)

    with open(INPUT_FILE, newline="", encoding="utf-8") as csvfile:

        reader = csv.DictReader(csvfile)

        for row in reader:

            detection_id = (row.get("Detection_ID") or "").strip()
            detection_name = (row.get("Detection_Name") or "").strip()

            mitre_id = (row.get("MITRE_ID") or "").strip()
            mitre_tactic = (row.get("MITRE_Tactic") or "").strip()

            if not detection_id:
                continue

            if not mitre_id:
                continue

            attack_mapping[mitre_id].append(
                {
                    "DetectionID": detection_id,
                    "DetectionName": detection_name,
                    "Tactic": mitre_tactic,
                }
            )

    return attack_mapping


# ----------------------------------------------------------------------
# Generate Markdown Report
# ----------------------------------------------------------------------


def generate_report(mapping):

    OUTPUT_REPORT.parent.mkdir(parents=True, exist_ok=True)

    total_rules = sum(len(v) for v in mapping.values())

    with open(OUTPUT_REPORT, "w", encoding="utf-8") as report:

        report.write("# ATT&CK Coverage Assessment Report\n\n")

        report.write("## Executive Summary\n\n")

        report.write(
            f"Total Detection Rules: **{total_rules}**\n\n"
        )

        report.write(
            f"Unique ATT&CK Techniques: **{len(mapping)}**\n\n"
        )

        report.write("---\n\n")

        report.write("## ATT&CK Technique Coverage\n\n")

        report.write("| MITRE ID | Tactic | Detection Rules |\n")
        report.write("|-----------|--------|----------------:|\n")

        for mitre in sorted(mapping):

            tactic = mapping[mitre][0]["Tactic"]

            report.write(
                f"| {mitre} | {tactic} | {len(mapping[mitre])} |\n"
            )

        report.write("\n---\n\n")

        report.write("## Detection Mapping\n\n")

        for mitre in sorted(mapping):

            report.write(f"### {mitre}\n\n")

            for detection in mapping[mitre]:

                report.write(
                    f"- **{detection['DetectionID']}** — "
                    f"{detection['DetectionName']}\n"
                )

            report.write("\n")

        report.write("---\n")
        report.write(
            "\nGenerated automatically by "
            "Lighthouse Technology "
            "ATT&CK Coverage Mapper.\n"
        )


# ----------------------------------------------------------------------
# Console Summary
# ----------------------------------------------------------------------


def print_summary(mapping):

    print("=" * 65)
    print(" Lighthouse Technology ATT&CK Coverage Mapper")
    print("=" * 65)

    total_rules = sum(len(v) for v in mapping.values())

    print()

    print(f"Detection Rules      : {total_rules}")
    print(f"ATT&CK Techniques    : {len(mapping)}")

    print("\nTechnique Coverage")
    print("-" * 65)

    for mitre in sorted(mapping):

        tactic = mapping[mitre][0]["Tactic"]

        print(
            f"{mitre:<12}"
            f"{tactic:<25}"
            f"{len(mapping[mitre]):>5}"
        )

    print("\nReport Generated")

    print(f"  {OUTPUT_REPORT}")

    print("\nCoverage Mapping Complete.")


# ----------------------------------------------------------------------
# Main
# ----------------------------------------------------------------------


def main():

    mapping = load_detection_metadata()

    if not mapping:

        print("[WARNING] No ATT&CK mappings found.")
        return

    generate_report(mapping)

    print_summary(mapping)


if __name__ == "__main__":
    main()
