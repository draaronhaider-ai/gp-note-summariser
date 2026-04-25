## Known Limitations

- Clinical significance of objective findings requires medical literacy to interpret
- The model does not flag abnormal values or deviation from normal ranges
- Urgency is not explicitly scored or highlighted
- Tool function is summarisation only — not clinical decision support
- Not suitable for use without clinical oversight

## Scoring Log

Scoring: Pass / Partial / Fail

### Prompt Version 1 — system_prompt_v1.txt

| Criterion | Note 001 | Note 002 | Note 003 |
|---|---|---|---|
| 1. Accuracy | Pass | Pass | Pass |
| 2. Completeness | Pass | Pass | Pass |
| 3. Structure | Partial | Pass | Pass |
| 4. Uncertainty handling | Pass | Partial | Partial |
| 5. Clinical urgency preservation | Fail | Fail | Partial |
| 6. Safety-critical information | Partial | Partial | Partial |

### Prompt Version 2 — system_prompt_v2.txt

| Criterion | Note 001 | Note 002 | Note 003 |
|---|---|---|---|
| 1. Accuracy | Pass | Pass | Pass |
| 2. Completeness | Pass | Pass | Pass |
| 3. Structure | Pass | Pass | Pass |
| 4. Uncertainty handling | Pass | Partial | Partial |
| 5. Clinical urgency preservation | Partial | Partial | Partial |
| 6. Safety-critical information | Pass | Pass | Partial |

### Prompt Version 3 — system_prompt_v3.txt

| Criterion | Note 001 | Note 002 | Note 003 |
|---|---|---|---|
| 1. Accuracy | Pass | Partial | Pass |
| 2. Completeness | Pass | Pass | Pass |
| 3. Structure | Pass | Pass | Pass |
| 4. Uncertainty handling | Pass | Partial | Partial |
| 5. Clinical urgency preservation | Partial | Partial | Partial |
| 6. Safety-critical information | Pass | Pass | Partial |

### Prompt Version 4 — system_prompt_v4.txt

| Criterion | Note 001 | Note 002 | Note 003 |
|---|---|---|---|
| 1. Accuracy | Pass | Pass | Pass |
| 2. Completeness | Pass | Pass | Pass |
| 3. Structure | Partial | Partial | Pass |
| 4. Uncertainty handling | Pass | Partial | Pass |
| 5. Clinical urgency preservation | Partial | Partial | Partial |
| 6. Safety-critical information | Partial | Partial | Pass |

### Prompt Version 5 — system_prompt_v5.txt

| Criterion | Note 001 | Note 002 | Note 003 |
|---|---|---|---|
| 1. Accuracy | Pass | Pass | Pass |
| 2. Completeness | Pass | Pass | Pass |
| 3. Structure | Pass | Partial | Pass |
| 4. Uncertainty handling | Pass | Partial | Pass |
| 5. Clinical urgency preservation | Partial | Partial | Partial |
| 6. Safety-critical information | Pass | Pass | Partial |

### Prompt Version 6 — system_prompt_v6.txt

| Criterion | Note 001 | Note 002 | Note 003 |
|---|---|---|---|
| 1. Accuracy | Partial | Partial | Pass |
| 2. Completeness | Pass | Pass | Pass |
| 3. Structure | Partial | Pass | Partial |
| 4. Uncertainty handling | Pass | Partial | Pass |
| 5. Clinical urgency preservation | Partial | Pass | Partial |
| 6. Safety-critical information | Partial | Pass | Partial |

### Prompt Version 7 — system_prompt_v7.txt

| Criterion | Note 001 | Note 002 | Note 003 |
|---|---|---|---|
| 1. Accuracy | Pass | Partial | Partial |
| 2. Completeness | Pass | Pass | Pass |
| 3. Structure | Pass | Pass | Pass |
| 4. Uncertainty handling | Pass | Partial | Pass |
| 5. Clinical urgency preservation | Partial | Pass | Partial |
| 6. Safety-critical information | Pass | Pass | Partial |

### Prompt Version 8 — system_prompt_v8.txt

| Criterion | Note 001 | Note 002 | Note 003 |
|---|---|---|---|
| 1. Accuracy | Pass | Partial | Pass |
| 2. Completeness | Pass | Pass | Pass |
| 3. Structure | Pass | Partial | Pass |
| 4. Uncertainty handling | Pass | Partial | Pass |
| 5. Clinical urgency preservation | Partial | Pass | Partial |
| 6. Safety-critical information | Pass | Partial | Pass |

### Prompt Version 9 — system_prompt_v9.txt

| Criterion | Note 001 | Note 002 | Note 003 |
|---|---|---|---|
| 1. Accuracy | Pass | Partial | Pass |
| 2. Completeness | Pass | Partial | Pass |
| 3. Structure | Pass | Pass | Pass |
| 4. Uncertainty handling | Pass | Partial | Pass |
| 5. Clinical urgency preservation | Partial | Partial | Partial |
| 6. Safety-critical information | Pass | Partial | Pass |