# Limbus Company Season 8 (a1c10p1) E2E Test Infrastructure Specification

> **Document ID**: LLC-TEST-INFRA-S8-01  
> **Status**: APPROVED / ACTIVE  
> **Version**: 1.0.0  
> **Target System**: Limbus Company Season 8 (a1c10p1) Chinese Localization & Native Mod Deployment  
> **Author**: E2E Test Suite Architect (`teamwork_preview_test_writer`)  
> **Project Root**: `/home/buxinzi/Documents/巴士汉化-哈基米版/`  
> **Test Suite Directory**: `/home/buxinzi/Documents/巴士汉化-哈基米版/tests/e2e/`  

---

## 1. Executive Summary & Testing Philosophy

The Limbus Company Chinese Localization (LLC zh-CN) project delivers complete, high-fidelity translation, typography, and game engine integration for Season 8 (`a1c10p1`). Because the translation interacts directly with the Unity C# client runtime, TextMeshPro typography engine, and mod loader architecture, defects such as unclosed tags, missing formatting placeholders, or unmapped characters (e.g., full-width tilde `～`) cause direct game crashes, text box overflows, or square glyph rendering bugs (`□`).

To ensure zero fatal defects reach production, this test infrastructure enforces an **opaque-box end-to-end (E2E) testing methodology**:
1. **Opaque-Box Verification**: Tests inspect observable project outputs (workspace localization JSON files, Steam deployment directory, font binary integrity, linter execution results) without relying on internal script implementation details.
2. **Authoritative Baseline Comparison**: Tests compare Chinese localization assets directly against official Korean game client baseline files (`Localize/kr/`).
3. **Four-Tier Hierarchy**: Progressive coverage structure spanning Feature Coverage (Tier 1), Boundary & Corner Cases (Tier 2), Cross-Feature Interactions (Tier 3), and Real-World End-to-End Scenarios (Tier 4).
4. **Zero Workspace Side Effects**: The test suite is strictly read-only with respect to `workspace/LLC_zh-CN/` and Steam installation paths, maintaining total test isolation.

---

## 2. Feature Inventory & Tier Mapping

The test infrastructure covers all 17 features defined in `PROJECT.md`, mapping each feature to specific verification tiers and test cases.

| Feature ID | Feature Name | Target Scope | Milestone | Primary Verification Tier | Min Tests | Test Identifiers |
|---|---|---|---|---|---|---|
| **F01** | Linter Engine Hardening | `tools/linter.py` (8-rule validation engine) | M1 | Tier 1 (Coverage), Tier 2 (Boundary) | 5 | `test_f01_*` |
| **F02** | E2E Test Suite Creation | `TEST_INFRA.md`, `tests/e2e/`, `TEST_READY.md` | E2E | Tier 1 (Coverage) | 5 | `test_f02_*` |
| **F03** | Combat Skills Translation | `Skills_Enemy-a1c10p1.json`, `Skills_Abnormality-a1c10p1.json` | M2 | Tier 1, Tier 2, Tier 3 | 5 | `test_f03_*` |
| **F04** | Combat Passives Translation | `Passives_Enemy-a1c10p1.json`, `Passives_Abnormality-a1c10p1.json` | M2 | Tier 1, Tier 3 | 5 | `test_f04_*` |
| **F05** | Battle Keywords & Buffs | `BattleKeywords-a1c10p1.json`, `Bufs-a1c10p1.json` | M2 | Tier 1, Tier 2, Tier 3 | 5 | `test_f05_*` |
| **F06** | Enemy & Boss Mechanics | `Enemies-a1c10p1.json`, `PanicInfo-a1c10p1.json`, `BattleSpeechBubbleDlg-a1c10p1.json` | M2 | Tier 1, Tier 4 | 5 | `test_f06_*` |
| **F07** | Season 8 UI Windows | `MainUIText-a1c10p1.json`, `BattlePass-a1c10.json`, `BattleResultHint-a1c10p1.json`, 5 extra UI files | M2 | Tier 1, Tier 2 | 5 | `test_f07_*` |
| **F08** | Announcers & Stage Nodes | `Announcer-a1c10p1.json`, `StageNode-a1c10p1.json`, `Items-a1c10p1.json`, Announcers 53-55 | M2 | Tier 1, Tier 4 | 5 | `test_f08_*` |
| **F09** | Missing Story Files Creation | Ingestion & translation of `StoryData/S1004B.json` & `StoryData/S1062B.json` | M3 | Tier 1, Tier 4 | 5 | `test_f09_*` |
| **F10** | StoryData Deep Translation | Complete translation of all 20 existing Chapter 10 story files (`S1000B` ~ `S1061B`, `S9991B`) | M3 | Tier 1, Tier 3, Tier 4 | 5 | `test_f10_*` |
| **F11** | RPGSystem Ingestion & Translation | Creation & translation of 45 `RPGSystem/` files (1,397 exploration entries) | M3 | Tier 1, Tier 2, Tier 4 | 5 | `test_f11_*` |
| **F12** | Personality Voices Translation | Identity voices: Hong Lu (10616), Ishmael (10816), Ryoshu (10416) | M3 | Tier 1, Tier 3 | 5 | `test_f12_*` |
| **F13** | Full Workspace Linter Sweep | 100% sweep of workspace: 0 syntax errors, 0 full-width `～`, 1:1 placeholders | M4 | Tier 1, Tier 2 | 5 | `test_f13_*` |
| **F14** | Steam Native Mod Deployment | Sync to `LimbusCompany_Data/Lang/LLC_zh-CN/` and config setup | M4 | Tier 1, Tier 3, Tier 4 | 5 | `test_f14_*` |
| **F15** | Sarasa Gothic Font Mounting | Binary verification of `ChineseFont.ttf` (23.8MB, SHA-256 integrity) | M4 | Tier 1, Tier 3, Tier 4 | 5 | `test_f15_*` |
| **F16** | 100% E2E Acceptance Pass | Global acceptance gate across all Season 8 requirements | Final | Tier 1, Tier 4 | 5 | `test_f16_*` |
| **F17** | Adversarial Coverage Hardening | White-box stress tests, corrupt input resilience, large scale payload checks | Final | Tier 1, Tier 2 | 5 | `test_f17_*` |

---

## 3. Test Suite Architecture

```
/home/buxinzi/Documents/巴士汉化-哈基米版/
├── TEST_INFRA.md                          <- This infrastructure specification
├── TEST_READY.md                          <- Test readiness publication & summary
└── tests/
    └── e2e/
        ├── __init__.py                    <- Package initialization
        ├── common.py                      <- Test utilities, path anchors & validators
        ├── test_tier1_feature_coverage.py <- Tier 1: 17 Features (>=5 tests each, 85+ tests)
        ├── test_tier2_boundary_corner.py  <- Tier 2: Boundary & Corner Cases (15+ tests)
        ├── test_tier3_cross_feature.py    <- Tier 3: Pairwise Cross-Feature Interactions (10+ tests)
        ├── test_tier4_real_world.py       <- Tier 4: Real-World Game Application Scenarios (5+ tests)
        └── run_tests.py                   <- Master CLI test runner & structured reporter
```

### 3.1 Tier Classification & Intent

#### Tier 1: Feature Coverage (Opaque Verification)
- **Objective**: Verify existence, non-emptiness, valid UTF-8 JSON structure, schema conformity, and baseline integration for all 17 features.
- **Rule**: Minimum 5 tests per feature (total >= 85 tests).
- **Scope**:
  - File existence in `workspace/LLC_zh-CN/`.
  - JSON parseability and UTF-8 encoding without BOM/corrupt bytes.
  - Data structure adherence (`dataList`, `levelList`, `coinlist`, `texts`, `steps`).
  - Target parity against Korean reference assets.
  - Deployment assets and font metadata.

#### Tier 2: Boundary & Corner Cases
- **Objective**: Stress-test schema edges and textual boundary conditions.
- **Scope**:
  - Empty text descriptions (`""`) and whitespace-only strings.
  - Extremely long narrative blocks and skill descriptions (>4,000 characters).
  - Deeply nested coin hierarchies (multiple levels and coins).
  - Multiple placeholders (`{0} {1} {2} {Slot}`) with varying ordering.
  - Mixed and nested Unity TextMeshPro tags (`<color=...>`, `<b>`, `<i>`, `<size>`, `<mark>`).
  - Strict absence of full-width tildes (`～` -> `~`).
  - Key identifier variations (`"id"` as integer vs `"key"` as string).

#### Tier 3: Cross-Feature Interactions (Pairwise Matrix)
- **Objective**: Test semantic and technical synergy between interconnected modules.
- **Pairs Evaluated**:
  1. **Combat Skill + Battle Keyword**: Skills referencing keywords ensure proper `[关键词] ` trailing space.
  2. **Passive Skill + Buff Mechanism**: Buff description verb usage aligns with passive trigger semantics (`获得` vs `施加` vs `增加`).
  3. **Combat Skill + Font Glyph Set**: All characters in translated skill descriptions exist within Sarasa Gothic SC character bounds.
  4. **Story Dialogue + Sinner Voice Characterization**: Sinner lines adhere to persona constraints (e.g., Faust third person, Ryoshu middle dots `·`, Dante `<嘀嗒>`).
  5. **RPG System Dialogue + Rich Text Markup**: Exploration dialogues containing color tags render cleanly without broken speaker tokens.
  6. **Steam Deployment + Config + Font**: `config.json` specifies `"lang": "LLC_zh-CN"` and relative font path points to valid font asset.
  7. **Boss Raid UI + Enemy Data + Speech Bubbles**: Terminology consistency across Boss Raid 4, Enemy definitions, and battle speech bubbles (e.g., 雷横, 赤神, 见证决斗).

#### Tier 4: Real-World End-to-End Scenarios
- **Objective**: Simulate full in-game gameplay paths and lifecycle flows.
- **Scenarios Evaluated**:
  1. **Sisyphus Department Store Floor Walkthrough**: Complete exploration path across Floors 1, 2, 3, 4, B1, and B2 verifying narrative chaining, quests, NPCs, and items.
  2. **Boss Raid Combat Execution**: End-to-end boss encounter flow (Leiheng / Red God) verifying stage intro, skills, passive triggers, panic states, and combat speech bubbles.
  3. **Full Story Chapter 10 Playthrough**: Sequential chapter reading from `S1000B` through `S1062B` ensuring unbroken narrative flow and character consistency.
  4. **Steam Deployment & Game Launch Sanity**: Full client mod mounting validation mimicking game boot sequence.

---

## 4. Linguistic & Technical Inviolables (Zero-Tolerance Rules)

The test suites enforce the following zero-tolerance rules derived from `ORIGINAL_REQUEST.md` and `standards_and_linter_spec.md`:

| Rule ID | Inviolable | Requirement | Severity |
|---|---|---|---|
| **INV-01** | Full-width Tilde Ban | Exactly 0 instances of `～` (U+FF5E); must be replaced by ASCII `~` (U+007E). | FATAL |
| **INV-02** | Keyword Trailing Space | Keywords in combat/buff descriptions must be followed by a single ASCII space `0x20` (e.g. `[震颤 ] ` or `流血 `). | ERROR |
| **INV-03** | Verb Triad Conformity | Buff count -> `获得`; Debuff count -> `施加`; Potency intensity -> `增加`; Decay -> `减少`/`消耗`. | ERROR |
| **INV-04** | 1:1 Placeholder Parity | Placeholders `{0}`, `{1}`, `{Slot}` must match 1:1 between Korean source and Chinese target. | FATAL |
| **INV-05** | TMP Tag Balance | All Unity TextMeshPro tags (`<b>`, `<i>`, `<color>`, `<size>`, `<mark>`) must be strictly balanced (LIFO). | FATAL |
| **INV-06** | Font Asset Integrity | `ChineseFont.ttf` must match exact size (23,870,096 bytes) and SHA-256 hash `a56a06f1af...`. | FATAL |
| **INV-07** | Punctuation Standards | Story dialogues must use six-dot ellipses `……` and Chinese double quotes `“”`. | WARN |

---

## 5. Master Test Runner Specification

The test runner `tests/e2e/run_tests.py` orchestrates execution across all four tiers:

### 5.1 CLI Interface
```bash
# Run complete test suite (all 4 tiers)
python3 tests/e2e/run_tests.py

# Run specific tier
python3 tests/e2e/run_tests.py --tier 1
python3 tests/e2e/run_tests.py --tier 2
python3 tests/e2e/run_tests.py --tier 3
python3 tests/e2e/run_tests.py --tier 4

# Output machine-readable JSON metrics
python3 tests/e2e/run_tests.py --json

# Verbose test reporting
python3 tests/e2e/run_tests.py -v
```

### 5.2 Structured Reporting Output Format
The runner outputs a structured execution report:
```
================================================================================
          LIMBUS COMPANY SEASON 8 (a1c10p1) E2E TEST SUITE REPORT
================================================================================
  Tier 1 (Feature Coverage):        85 tests | PASS:  45 | FAIL:  40 | ERR: 0
  Tier 2 (Boundary & Corner):       16 tests | PASS:  12 | FAIL:   4 | ERR: 0
  Tier 3 (Cross-Feature Matrix):    10 tests | PASS:   5 | FAIL:   5 | ERR: 0
  Tier 4 (Real-World Scenarios):     5 tests | PASS:   2 | FAIL:   3 | ERR: 0
--------------------------------------------------------------------------------
  TOTAL SUMMARY:                   116 tests | PASS:  64 | FAIL:  52 | ERR: 0
  PASS RATE: 55.17%
================================================================================
```

### 5.3 Exit Code Contract
- **Exit Code `0`**: All executed tests passed (100% pass rate).
- **Exit Code `1`**: One or more tests failed or encountered errors.

During initial baseline execution (prior to worker translation milestones), the suite will naturally report failures for missing files and untranslated content, providing the exact benchmark against which progress is measured.

---

## 6. Maintenance & Extensibility Guidelines

1. **Adding Tests**: New tests should be co-located in the corresponding tier module under `tests/e2e/`.
2. **Deterministic Outputs**: Test assertions must rely on deterministic properties (file existence, byte sizes, schema keys, text patterns) and never depend on volatile timestamps or system locales.
3. **No Facades**: Facade tests that trivially assert `True` are strictly forbidden. All assertions must evaluate actual data structures.
4. **Pytest Support**: All test cases inherit from `unittest.TestCase` and can be invoked either via `python3 tests/e2e/run_tests.py` or `pytest tests/e2e/`.
