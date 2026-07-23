#!/usr/bin/env python3

"""
Lighthouse Technology Detection Engineering

Sigma Rule Generator

Purpose:
    Generate standardized Sigma detection rules
    from detection engineering metadata.

Phase:
    Phase G - Detection Engineering &
    Coverage Measurement

Author:
    Lighthouse Technology Security Engineering Team

Version:
    1.0
"""

import argparse
import datetime
import uuid
import yaml
from pathlib import Path


RULE_TEMPLATE = {
    "title": "",
    "id": "",
    "status": "experimental",
    "description": "",
    "author": "Lighthouse Technology Detection Engineering Team",
    "date": "",
    "references": [],
    "tags": [],
    "logsource": {
        "product": "",
        "service": ""
    },
    "detection": {
        "selection": {},
        "condition": "selection"
    },
    "falsepositives": [],
    "level": "medium"
}


def generate_sigma_rule(metadata):

    rule = RULE_TEMPLATE.copy()

    rule["title"] = metadata["name"]

    rule["id"] = str(uuid.uuid4())

    rule["description"] = metadata["description"]

    rule["date"] = datetime.date.today().isoformat()

    rule["tags"] = metadata.get(
        "attack_mapping",
        []
    )

    rule["logsource"] = {
        "product": metadata.get(
            "product",
            "windows"
        ),
        "service": metadata.get(
            "service",
            "security"
        )
    }

    rule["detection"]["selection"] = metadata.get(
        "selection",
        {}
    )

    rule["falsepositives"] = metadata.get(
        "falsepositives",
        [
            "Legitimate administrative activity"
        ]
    )

    rule["level"] = metadata.get(
        "severity",
        "medium"
    )

    return rule


def save_rule(rule, output):

    output_path = Path(output)

    output_path.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    with open(
        output_path,
        "w",
        encoding="utf-8"
    ) as file:

        yaml.dump(
            rule,
            file,
            sort_keys=False
        )

    print(
        f"[+] Sigma rule generated: {output}"
    )


def main():

    parser = argparse.ArgumentParser(
        description=
        "Generate Lighthouse Technology Sigma Rule"
    )

    parser.add_argument(
        "--name",
        required=True,
        help="Detection rule name"
    )

    parser.add_argument(
        "--description",
        required=True,
        help="Detection description"
    )

    parser.add_argument(
        "--output",
        required=True,
        help="Sigma YAML output path"
    )

    args = parser.parse_args()


    metadata = {

        "name": args.name,

        "description": args.description,

        "attack_mapping": [
            "attack.execution",
            "attack.t1059"
        ],

        "product": "windows",

        "service": "security",

        "severity": "high",

        "selection": {

            "EventID": 4688

        }

    }


    rule = generate_sigma_rule(
        metadata
    )


    save_rule(
        rule,
        args.output
    )


if __name__ == "__main__":

    main()
