#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Master E2E Test Runner for Limbus Company Season 8 (a1c10p1).
Executes test suites across Tiers 1-4, records structured metrics,
and exits with code 0 on complete pass or 1 on failure.
"""

import argparse
import io
import json
import os
from pathlib import Path
import sys
import time
import unittest
from typing import Dict, List, Any

# Ensure project root is in sys.path
PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from tests.e2e.test_tier1_feature_coverage import TestTier1FeatureCoverage
from tests.e2e.test_tier2_boundary_corner import TestTier2BoundaryCorner
from tests.e2e.test_tier3_cross_feature import TestTier3CrossFeature
from tests.e2e.test_tier4_real_world import TestTier4RealWorld

TIER_MAP = {
    1: ("Tier 1 (Feature Coverage)", TestTier1FeatureCoverage),
    2: ("Tier 2 (Boundary & Corner)", TestTier2BoundaryCorner),
    3: ("Tier 3 (Cross-Feature Matrix)", TestTier3CrossFeature),
    4: ("Tier 4 (Resource Scenarios)", TestTier4RealWorld),
}


def run_tier(tier_num: int, tier_name: str, test_case_cls: type, verbose: bool = False) -> Dict[str, Any]:
    """Run a single test tier and return structured metrics."""
    suite = unittest.TestLoader().loadTestsFromTestCase(test_case_cls)
    stream = io.StringIO()
    runner = unittest.TextTestRunner(stream=stream, verbosity=2 if verbose else 1)
    
    start_time = time.time()
    result = runner.run(suite)
    duration = time.time() - start_time
    
    failures = []
    for test, err in result.failures:
        failures.append({"test": test.id(), "error": err.strip()})
    errors = []
    for test, err in result.errors:
        errors.append({"test": test.id(), "error": err.strip()})
        
    return {
        "tier": tier_num,
        "name": tier_name,
        "total": result.testsRun,
        "passed": result.testsRun - len(result.failures) - len(result.errors),
        "failed": len(result.failures),
        "errors": len(result.errors),
        "duration": round(duration, 3),
        "failure_details": failures,
        "error_details": errors,
    }


def main():
    parser = argparse.ArgumentParser(description="Limbus Company Season 8 E2E Test Suite Runner")
    parser.add_argument("--tier", type=int, choices=[1, 2, 3, 4], help="Run a specific test tier only (1, 2, 3, or 4)")
    parser.add_argument("--json", action="store_true", help="Output machine-readable JSON results")
    parser.add_argument("-v", "--verbose", action="store_true", help="Verbose test failure output")
    args = parser.parse_args()

    selected_tiers = [args.tier] if args.tier else [1, 2, 3, 4]

    tier_results = []
    total_run = 0
    total_passed = 0
    total_failed = 0
    total_errors = 0
    total_time = 0.0

    for t_num in selected_tiers:
        t_name, t_cls = TIER_MAP[t_num]
        metrics = run_tier(t_num, t_name, t_cls, verbose=args.verbose)
        tier_results.append(metrics)
        total_run += metrics["total"]
        total_passed += metrics["passed"]
        total_failed += metrics["failed"]
        total_errors += metrics["errors"]
        total_time += metrics["duration"]

    pass_rate = (total_passed / total_run * 100) if total_run > 0 else 0.0

    if args.json:
        output_payload = {
            "summary": {
                "total": total_run,
                "passed": total_passed,
                "failed": total_failed,
                "errors": total_errors,
                "pass_rate_percent": round(pass_rate, 2),
                "duration_seconds": round(total_time, 3),
                "all_passed": (total_failed == 0 and total_errors == 0),
            },
            "tiers": tier_results,
        }
        print(json.dumps(output_payload, indent=2, ensure_ascii=False))
    else:
        print("=" * 82)
        print("           LIMBUS COMPANY SEASON 8 (a1c10p1) E2E TEST SUITE REPORT")
        print("=" * 82)
        for t in tier_results:
            print(f"  {t['name']:<34}: {t['total']:3d} tests | PASS: {t['passed']:3d} | FAIL: {t['failed']:3d} | ERR: {t['errors']:2d} ({t['duration']:.2f}s)")
        print("-" * 82)
        print(f"  TOTAL SUMMARY:                     {total_run:3d} tests | PASS: {total_passed:3d} | FAIL: {total_failed:3d} | ERR: {total_errors:2d} ({total_time:.2f}s)")
        print(f"  PASS RATE: {pass_rate:.2f}%")
        print("=" * 82)

        if total_failed > 0 or total_errors > 0:
            print("\n" + "!" * 30 + " DETAILED FAILURES " + "!" * 30)
            for t in tier_results:
                if t["failed"] > 0 or t["errors"] > 0:
                    print(f"\n[{t['name']}]")
                    for f in t["failure_details"]:
                        test_short_name = f["test"].split(".")[-1]
                        err_line = f["error"].splitlines()[-1] if f["error"] else "Unknown assertion failure"
                        print(f"  [FAIL] {test_short_name}: {err_line}")
                    for e in t["error_details"]:
                        test_short_name = e["test"].split(".")[-1]
                        err_line = e["error"].splitlines()[-1] if e["error"] else "Unknown runtime error"
                        print(f"  [ERR]  {test_short_name}: {err_line}")
            print("\n" + "=" * 82)

    # Exit code: 0 on complete pass, 1 if any failure/error
    sys.exit(0 if (total_failed == 0 and total_errors == 0) else 1)


if __name__ == "__main__":
    main()
