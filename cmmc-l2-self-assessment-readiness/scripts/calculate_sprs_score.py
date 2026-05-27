#!/usr/bin/env python3
"""
SPRS Score Calculator for NIST SP 800-171 Self-Assessment

Calculates the Supplier Performance Risk System (SPRS) score based on the
DoD Assessment Methodology. Reads the control assessment workbook CSV and
computes the final score out of 110.

Usage:
    python3 calculate_sprs_score.py <control-assessment-workbook.csv>

Output:
    - Final SPRS score
    - Breakdown by control family
    - List of gaps with point deductions
"""

import csv
import sys
from collections import defaultdict
from typing import Dict, List, Tuple


def validate_point_deduction(value: str) -> int:
    """Validate and convert point deduction value."""
    if not value or value.strip() == "":
        return 0

    try:
        deduction = int(value.strip())
        if deduction not in [0, 1, 3, 5]:
            print(f"Warning: Invalid point deduction value '{deduction}'. Must be 0, 1, 3, or 5.")
            return 0
        return deduction
    except ValueError:
        print(f"Warning: Non-numeric point deduction value '{value}'. Treating as 0.")
        return 0


def parse_control_id(control_id: str) -> str:
    """Extract family from control ID (e.g., '3.1.1' -> '3.1')."""
    parts = control_id.strip().split('.')
    if len(parts) >= 2:
        return f"{parts[0]}.{parts[1]}"
    return control_id


def calculate_sprs_score(csv_file_path: str) -> Tuple[int, Dict, List]:
    """
    Calculate SPRS score from control assessment workbook.

    Returns:
        - Final SPRS score (0-110)
        - Dictionary of family-level results
        - List of gaps with details
    """

    # Track control-level status (one status per control, not per objective)
    control_status = {}  # control_id -> (status, max_deduction)
    control_details = {}  # control_id -> (title, objectives)

    total_deductions = 0
    gaps = []

    try:
        with open(csv_file_path, 'r', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)

            for row in reader:
                control_id = row.get('Control ID', '').strip()
                control_title = row.get('Control Title', '').strip()
                objective_id = row.get('Assessment Objective ID', '').strip()
                status = row.get('Status', '').strip()
                gap_description = row.get('Gap Description', '').strip()
                point_deduction_str = row.get('Point Deduction', '').strip()

                if not control_id:
                    continue

                # Initialize control details if not seen before
                if control_id not in control_details:
                    control_details[control_id] = {
                        'title': control_title,
                        'objectives': [],
                        'gap_description': ''
                    }

                control_details[control_id]['objectives'].append(objective_id)

                # Track status and point deduction at control level
                # A control is "Not Met" if any objective is "Not Met"
                # Point deduction is assigned once per control, not per objective
                if status in ['Met', 'Not Met', 'Not Applicable']:
                    point_deduction = validate_point_deduction(point_deduction_str)

                    if control_id not in control_status:
                        control_status[control_id] = {
                            'status': status,
                            'deduction': point_deduction,
                            'gap_description': gap_description
                        }
                    else:
                        # If we see "Not Met" for any objective, control is "Not Met"
                        if status == 'Not Met':
                            control_status[control_id]['status'] = 'Not Met'
                            # Use the maximum deduction specified for this control
                            if point_deduction > control_status[control_id]['deduction']:
                                control_status[control_id]['deduction'] = point_deduction
                        if gap_description:
                            control_status[control_id]['gap_description'] = gap_description

    except FileNotFoundError:
        print(f"Error: File '{csv_file_path}' not found.")
        sys.exit(1)
    except Exception as e:
        print(f"Error reading CSV file: {e}")
        sys.exit(1)

    # Calculate total deductions and build gaps list
    for control_id, status_info in control_status.items():
        if status_info['status'] == 'Not Met':
            deduction = status_info['deduction']
            total_deductions += deduction

            gaps.append({
                'control_id': control_id,
                'control_title': control_details[control_id]['title'],
                'deduction': deduction,
                'gap_description': status_info['gap_description']
            })

    # Calculate final score
    final_score = 110 - total_deductions

    # Calculate family-level breakdown
    family_results = defaultdict(lambda: {'total': 0, 'met': 0, 'not_met': 0, 'na': 0, 'deductions': 0})

    for control_id, status_info in control_status.items():
        family_id = parse_control_id(control_id)
        family_results[family_id]['total'] += 1

        if status_info['status'] == 'Met':
            family_results[family_id]['met'] += 1
        elif status_info['status'] == 'Not Met':
            family_results[family_id]['not_met'] += 1
            family_results[family_id]['deductions'] += status_info['deduction']
        elif status_info['status'] == 'Not Applicable':
            family_results[family_id]['na'] += 1

    return final_score, dict(family_results), gaps


def print_results(final_score: int, family_results: Dict, gaps: List):
    """Print formatted SPRS score results."""

    family_names = {
        '3.1': 'Access Control',
        '3.2': 'Awareness and Training',
        '3.3': 'Audit and Accountability',
        '3.4': 'Configuration Management',
        '3.5': 'Identification and Authentication',
        '3.6': 'Incident Response',
        '3.7': 'Maintenance',
        '3.8': 'Media Protection',
        '3.9': 'Personnel Security',
        '3.10': 'Physical Protection',
        '3.11': 'Risk Assessment',
        '3.12': 'Security Assessment',
        '3.13': 'System and Communications Protection',
        '3.14': 'System and Information Integrity'
    }

    print("=" * 80)
    print("NIST SP 800-171 SPRS SCORE CALCULATION")
    print("=" * 80)
    print()
    print(f"FINAL SPRS SCORE: {final_score} out of 110")
    print()
    print("=" * 80)
    print("RESULTS BY CONTROL FAMILY")
    print("=" * 80)
    print()

    # Sort families by ID
    sorted_families = sorted(family_results.items(), key=lambda x: x[0])

    for family_id, results in sorted_families:
        family_name = family_names.get(family_id, 'Unknown Family')
        print(f"{family_id} {family_name}")
        print(f"  Total Requirements: {results['total']}")
        print(f"  Met: {results['met']}")
        print(f"  Not Met: {results['not_met']}")
        print(f"  Not Applicable: {results['na']}")
        print(f"  Point Deductions: {results['deductions']}")
        print()

    if gaps:
        print("=" * 80)
        print(f"IDENTIFIED GAPS ({len(gaps)} controls)")
        print("=" * 80)
        print()

        # Sort gaps by deduction (highest first), then by control ID
        sorted_gaps = sorted(gaps, key=lambda x: (-x['deduction'], x['control_id']))

        for gap in sorted_gaps:
            print(f"Control: {gap['control_id']} - {gap['control_title']}")
            print(f"Point Deduction: {gap['deduction']}")
            if gap['gap_description']:
                print(f"Gap Description: {gap['gap_description']}")
            print()
    else:
        print("=" * 80)
        print("No gaps identified. All requirements are Met or Not Applicable.")
        print("=" * 80)
        print()

    print("=" * 80)
    print("ASSESSMENT SUMMARY")
    print("=" * 80)
    total_controls = sum(r['total'] for r in family_results.values())
    total_met = sum(r['met'] for r in family_results.values())
    total_not_met = sum(r['not_met'] for r in family_results.values())
    total_na = sum(r['na'] for r in family_results.values())

    print(f"Total Controls Assessed: {total_controls}")
    print(f"Controls Met: {total_met} ({total_met/total_controls*100:.1f}%)")
    print(f"Controls Not Met: {total_not_met} ({total_not_met/total_controls*100:.1f}%)")
    print(f"Controls Not Applicable: {total_na} ({total_na/total_controls*100:.1f}%)")
    print()
    print(f"Total Point Deductions: {110 - final_score}")
    print(f"FINAL SPRS SCORE: {final_score} out of 110")
    print("=" * 80)


def main():
    """Main entry point."""
    if len(sys.argv) != 2:
        print("Usage: python3 calculate_sprs_score.py <control-assessment-workbook.csv>")
        sys.exit(1)

    csv_file_path = sys.argv[1]
    final_score, family_results, gaps = calculate_sprs_score(csv_file_path)
    print_results(final_score, family_results, gaps)


if __name__ == '__main__':
    main()
