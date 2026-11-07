# The Financial MCP Risk Baseline (v0.2)

**Guigui Wang — Correctover (AI Reliability)**
**2026-11-07 · v0.2 (with data appendix)**

---

## 1. Executive summary

Model Context Protocol (MCP) servers are entering regulated industries through the front door: agents in banking, insurance, and healthcare increasingly invoke tools that move money, touch credentials, and write to systems of record. Regulators are already responding — the Hong Kong SFC announced at Fintech Week 2026 that it will issue guidance for high-autonomy AI applications alongside a cybersecurity framework for licensed firms; Apple's FY2026 10-K lists AI-agent over-permission as a risk factor; US authorities have issued the first FASCSA supply-chain exclusion order against an AI model vendor (DHS, DeepSeek, 2026).

What is missing is a **baseline**: a frozen, citable, evidence-bearing inventory of which public MCP tools touch money, which touch credentials, and which are independently verifiable at runtime. This document defines that baseline and its method.

## 2. The baseline (frozen, SHA-256 anchored)

Our census of public MCP infrastructure — **MCP Atlas Milestone A** — was frozen on 2026-10-12 and published on Zenodo (DOI 10.5281/zenodo.23333369; audit record 10.5281/zenodo.23333516):

- **42,163 servers** indexed; **229,827 tool-parameter schemas** audited (229,539 live + 288 historical);
- dual SHA-256 pinned exports (`servers` `3071866184…`, `server_tools` `2350dc773d…`), zero malformed rows, reproducible by third parties;
- per-tool risk vocabulary aligned with the IETF individual draft `draft-correctover-gg-mcp-parameter-risk-01` (five canonical classes: credential / filesystem / command / money / url).

The baseline is deliberately static: it does not age, and every label in the gazetteer built on it carries an evidence chain back to pinned parameter paths.

## 3. The gazetteer method (no naked labels)

Three properties distinguish this from letter-grade scanner reports (CSA RiskRubric A-F; PolicyLayer verb classes):

1. **Evidence-bearing labels.** `money_touching: true` is only valid with a non-empty evidence list (frozen-baseline parameter paths + vocabulary rule refs). A label that cannot show its evidence must be omitted — fail-closed applies to annotation, not just to runtime.
2. **Traceability as a query field.** Each entry states whether the server's decisions are independently verifiable at runtime, under which receipt format (`ccs-1.0`, `boundaryattest-0.1`, `l3-rollback-0.1`), with a pinned verifier fingerprint. To our knowledge no existing grading scheme exposes this.
3. **Longitudinal panel.** Weekly anchors append, never overwrite — researchers cite a time series, not a screenshot.

Schema: `correctover-risk-gazetteer/0.1` (CC0, github.com/DSHCorrectover — deliverables `mcp-risk-gazetteer`).

## 4. The verifiability layer (from verdicts to reversals)

Evidence does not stop at static labels. The same trust root supports:

- **Signed decision receipts** (Ed25519 over RFC 8785 canonical bytes, hash-chained, offline-verifiable — no vendor backend required), aligned with the IETF `draft-correctover-ccs-10` evidence model;
- **L3-R rollback-evidence receipts** (`ccs.rollback-evidence/0.1`, pinned 2026-11-07): a linked receipt attesting that a settled action was reversed, with a fail-closed rule — an executed-rollback claim without a transaction reference is unverifiable and rejected by the checker. For financial deployments this is the difference between "we compensated" and "here is a verifiable reversal record bound to the original decision."

The paired-fixture work with an independent implementer (BoundaryAttest × CCS, merged 2026-11-07) demonstrates the cross-format audit trail on one shared decision event; the current corpus has additionally passed byte-level independent re-verification by an external reviewer.

## 4.5 Data appendix v0.2 — financial exposure in the frozen census

Two independent signals over the same 229,539-tool population (method note: bucket = name/description signal from the audit report; param = parameter-level schema signal, recomputed row-by-row for this appendix — both directions agree at scale):

| Signal | Tools | Distinct servers | Write-polarity tools |
|---|---|---|---|
| Payment / funds-movement surface (bucket) | 6,498 (2.83%) | **3,456** | 1,301 |
| `money_amount` parameter class (param) | 15,224 | **4,335** | — |
| Credential / secret handling surface (bucket) | 15,295 (6.66%) | **3,947** | 2,086 |
| `credential_value` parameter class (param) | 14,752 | **4,988** | — |
| **Compound exposure: servers with both money- and credential-touching tools** | — | **2,663** | — |

Reading: financial exposure in the public MCP ecosystem is not hypothetical — 3,456 servers ship a funds-movement surface, 1,301 of them with write polarity (tools that can move money, not just read balances), and 2,663 servers combine money and credential handling in one trust boundary. Every number above recomputes from the frozen, SHA-256-anchored exports; the recomputation script ships with the appendix (CC0).

**Data layering.** This appendix publishes the method and the aggregate statistics. Server-level, evidence-bearing labels (baseline parameter paths, vocabulary rule refs, traceability pins) are the citation-grade layer and are released to PoC participants and citation users on request under the gazetteer schema — they are the working layer of engagements, not a bulk download.

Source: MCP Atlas audit 2026-10-13 (Zenodo record 23333516), `data-out/surface_stats.json` + `data-out/live_tools_labels.csv`, recomputed 2026-11-07.

## 5. What we ask of early adopters

Financial/insurtech teams running MCP tool calls against production-adjacent systems: a free, time-boxed PoC — we map your tool inventory against the baseline, label money/credential exposure with evidence chains, and produce a signed, re-verifiable assessment you can show your auditor. In exchange: a case study and your corrections. (Contact: wangguigui@correctover.com)

## 6. Honest limits

- The baseline is a **static compliance audit**: it maps what tools *can* do, not what a specific deployment *did* — runtime claims require runtime receipts.
- IETF documents cited are individual drafts, not RFCs; we cite them as method anchors, not standards.
- Labels are only as good as their evidence chain; entries with thin evidence are marked and excluded from citation-grade subsets.

## 7. Citation

```
Wang, G. (2026). The Financial MCP Risk Baseline v0.1 — a frozen, evidence-bearing
census method for tool-level financial and credential exposure.
Zenodo. DOI 10.5281/zenodo.23333369 (baseline). correctover-risk-gazetteer/0.1.
```

---
**v0.2 — published with data appendix. The frozen baseline and all recomputations are independently verifiable.*
