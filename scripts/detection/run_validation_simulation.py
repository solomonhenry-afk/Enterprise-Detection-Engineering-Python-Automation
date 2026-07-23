#!/usr/bin/env python3

"""
Lighthouse Technology
Detection Validation Simulation

Phase G – Detection Engineering & Coverage Measurement

Purpose:
    Simulate enterprise detection validation and generate
    normalized validation results for reporting.

Author:
    Lighthouse Technology Detection Engineering Team

Version:
    1.0
"""

import csv
from pathlib import Path
from datetime import datetime

INPUT_FILE = Path(
    "data/normalized/detection/LHT-DetectionMetadata.csv"
)

OUTPUT_FILE = Path(
    "data/normalized/detection/LHT-DetectionValidationResults.csv"
)


def load_detections():

    detections = []

    if not INPUT_FILE.exists():
        print(f"[ERROR] Missing file: {INPUT_FILE}")
        return detections

    with open(INPUT_FILE, newline="", encoding="utf-8") as csvfile:

        reader = csv.DictReader(csvfile)

        for row in reader:

            detection_id = (row.get("Detection_ID") or "").strip()

            if not detection_id:
                continue

            detections.append(row)

    return detections


def simulate_validation(detections):

    results = []

    for index, row in enumerate(detections, start=1):

        status = "PASS"

        if index % 5 == 0:
            status = "TUNING_REQUIRED"

        results.append({

            "Simulation_ID":
                f"SIM-{index:03}",

            "Detection_ID":
                row.get("Detection_ID"),

            "Detection_Name":
                row.get("Detection_Name"),

            "MITRE_ID":
                row.get("MITRE_ID"),

            "MITRE_Tactic":
                row.get("MITRE_Tactic"),

            "Simulation_Result":
                status,

            "Detection_Fired":
                "Yes" if status == "PASS" else "Partial",

            "Validation_Date":
                datetime.now().strftime("%Y-%m-%d"),

            "Validated_By":
                "Detection Engineering Team"
        })

    return results


def save_results(results):

    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)

    fields = [

        "Simulation_ID",
        "Detection_ID",
        "Detection_Name",
        "MITRE_ID",
        "MITRE_Tactic",
        "Simulation_Result",
        "Detection_Fired",
        "Validation_Date",
        "Validated_By"

    ]

    with open(
        OUTPUT_FILE,
        "w",
        newline="",
        encoding="utf-8"
    ) as csvfile:

        writer = csv.DictWriter(
            csvfile,
            fieldnames=fields
        )

        writer.writeheader()

        writer.writerows(results)


def print_summary(results):

    passed = sum(
        1 for r in results
        if r["Simulation_Result"] == "PASS"
    )

    tuning = sum(
        1 for r in results
        if r["Simulation_Result"] == "TUNING_REQUIRED"
    )

    print("=" * 65)
    print(" Lighthouse Technology Validation Simulator")
    print("=" * 65)

    print()

    print(f"Total Simulations : {len(results)}")
    print(f"Passed            : {passed}")
    print(f"Tuning Required   : {tuning}")

    print("\nResults Saved:")

    print(f"  {OUTPUT_FILE}")

    print("\nSimulation Complete.")


def main():

    detections = load_detections()

    if not detections:

        print("[WARNING] No detections available.")
        return

    results = simulate_validation(detections)

    save_results(results)

    print_summary(results)


if __name__ == "__main__":
    main()
