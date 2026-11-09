# MCP Risk Gazetteer — schema v0.1（占位发布，2026-11-07）

**一句话**：不是又一个评级表——每一条标签都带证据链（冻结基线参数路径 + 词表 rule 引用），每一条可追溯性声明都 pin 验证器指纹。设计目标：**可被论文和工程师默认引用**。

## 与现有评级的差异（学什么/不刚什么）

| 对象 | 它给什么 | 我们不刚 | 我们的增量 |
|---|---|---|---|
| CSA RiskRubric（36,527 servers，A-F） | 官方字母评级、多扫描器 | 不碰字母评级品类 | 证据链标注 + 纵向面板 + 运行时可验证声明 |
| PolicyLayer（2,031 servers/31,000 tools，六类） | verb 分类 | 不做托管网关 | server 级资金/凭证归因 + 引用源 |
| PointGuard | 生态扫描 | 不做扫描器 | 扫描结果之上的可引用标注层 |

## 字段要点（详见 risk-gazetteer-schema-v0.1.json）

1. `baseline`：强制锚定 2026-10-12 冻结快照双 SHA-256 + Zenodo DOI——标签永不脱离基线漂移。
2. `risk_classes`：直接采用 draft-correctover-gg-mcp-parameter-risk 五类 canonical 词表——图鉴标签就是词表的应用层，标准与数据互为引用。
3. `money_touching` / `credential_touching`：**无裸标签**——label=true 必须带非空 evidence（基线参数路径/词表规则），否则字段必须省略（fail-closed 语义延伸到标注层）。
4. `traceability`：是否可运行时复验 + 兼容收据格式（ccs-1.0 / boundaryattest-0.1 / l3-rollback-0.1 / none）+ 验证器 pin——这一块是别人都没有的：**把"谁可被独立验证"变成查询字段**。
5. `panel_week`：纵向面板锚，周更追加不覆盖——被引的是时间序列表，不是单期报告。

## 状态

- v0.1 = 字段定义权占位（schema + 本说明），CC0。
- 数据填充接 MCP Atlas 冻结基线重导出（Zenodo 侧），赶 CSA RiskRubric Q3 平台声量窗口前出首批标注。
- 中文场景标签（scene_tags_zh）为中文生态独有维度。

## White paper

The Financial MCP Risk Baseline v0.2 (Zenodo: [DOI 10.5281/zenodo.24028716](https://doi.org/10.5281/zenodo.24028716)) — headline numbers: 3,456 servers with a funds-movement surface (1,301 write-polarity), 2,663 servers with compound money+credential exposure. Method: `financial_exposure_screener.py` (CC0) recomputes every number from the frozen exports.

## Data layering

Aggregate statistics and method are public (this repo + the white paper). Server-level, evidence-bearing labels (baseline parameter paths, vocabulary rule refs, traceability pins) are the citation-grade layer — released to PoC participants and citation users on request under the schema.

## Related

- Baseline census: Zenodo DOI 10.5281/zenodo.23333514 (MCP Atlas Milestone A, ODC-BY, SHA-256 frozen 2026-10-12); static audit record: DOI 10.5281/zenodo.23333516 (ODC-BY). Citation erratum: the earlier 10.5281/zenodo.23333369 reference pointed to the Joint Interoperability Report — corrected in whitepaper v0.2.1 (DOI 10.5281/zenodo.24072293)
- Vocabulary: draft-correctover-gg-mcp-parameter-risk-01 (five canonical classes)
- Receipts: draft-correctover-ccs-10 + L3-R rollback-evidence extension (DSHCorrectover/ccs-conformance-vectors @ 9bf254c)
