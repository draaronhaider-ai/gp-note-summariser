# GP Note Summariser

A clinical documentation tool that takes GP consultation notes and converts them into summaries based on the SOAP framework (Subjective, Objective, Assessment, Plan) using Anthropic's Claude API.

**Live demo:** [huggingface.co/spaces/draaronhaider-ai/gp-note-summariser](https://huggingface.co/spaces/draaronhaider-ai/gp-note-summariser)

---

## Overview

GP consultation notes are arguably written in an environment where there is significant pressure to complete admin work, on top of clinical tasks, within time-limited sessions. Such a heavy admin burden may produce clinical notes that are inconsistent, excessively abbreviated and potentially variable in quality. This tool was created to process consultation notes and return them in a standardised format (SOAP framework), increasing readability overall. The tool was designed to automatically flag any abnormal values, and safety-critical information and any red flags that would need immediate attention.

The project was built by a medical graduate at the intersection of clinical medicine and applied AI, with the goal of demonstrating how large language models can be applied thoughtfully to primary care documentation — and where their limitations lie.

## Features

- Structured SOAP output with consistent formatting
- Automatic flagging of abnormal vital signs against standard adult reference ranges
- Automatic flagging of abnormal blood test results across the core GP panel (FBC, U&Es, LFTs, TFTs, metabolic, cardiac, haematinics)
- Clinical scoring tool thresholds (PHQ-9, GAD-7, MMSE, MoCA, AUDIT, CHA₂DS₂-VASc, NYHA, MRC dyspnoea, NRS pain)
- Safety-critical item identification (suicidal ideation, anticoagulants, unknown allergies, safeguarding concerns, DNACPR, capacity concerns, pregnancy)
- RED FLAGS section for acute presentations meeting haemodynamic instability or safeguarding thresholds
- Abbreviation expansion (SOB → shortness of breath, etc.)

## Prompt Engineering

The tool went through 9 documented iterations, where each iteration was tested using three synthetic GP notes:

- **Note 001** — a clean, structured cardiac presentation (58M, exertional dyspnoea, possible early cardiac failure)
- **Note 002** — a complex, ambiguous acute presentation in an elderly patient with dementia (~80F, subacute deterioration, diagnostic uncertainty)
- **Note 003** — a sensitive mental health presentation with passive suicidal ideation (34F, moderate-severe depression)

Each version was then scored against a simple rubric which assessed the tool's capabilities in six criterion:

| Criterion | Description |
|---|---|
| Accuracy | No hallucinated content beyond what is in the original note |
| Completeness | All clinically relevant information captured |
| Structure | Correct SOAP categorisation |
| Uncertainty handling | Unconfirmed information appropriately flagged |
| Clinical urgency preservation | Urgency signal preserved from original note |
| Safety-critical information | High-risk items visible and correctly formatted |

Key prompt design decisions included limiting the flagging of information to the Subjective and Objective sections only (except safeguarding concerns), strictly prohibiting interpretive labels, enforcing single-location medication and allergy documentation, and explicitly defining a RED FLAGS section triggered by documented observations rather than model inference.

---

## Known Limitations

- **This tool is a summarisation aid only.** It is not a clinical decision support system and should not be used as a substitute for clinical judgement.
- Flagging of abnormal values is based on population-level thresholds and does not account for patient-specific baselines (e.g. a known hypertensive patient with BP 148/92 will be flagged despite this being their managed baseline).
- The model does not interpret constellations of findings — abnormal values are flagged individually, not as a clinical gestalt.
- Output consistency varies across runs due to the probabilistic nature of LLMs. The same note may produce slightly different outputs on different runs.
- The tool is optimised for UK primary care (GP) settings and standard adult reference ranges. It is not validated for secondary care, paediatric, or specialist contexts.
- Blood test flagging applies only to the core GP panel. Unusual or specialist investigations will not be flagged against reference ranges.
- Despite efforts to prevent any interpretive analysis, the tool still seems to struggle with this task at times - reflecting the broad but critical issue of information hallucination observed in LLMs.

---

## Regulatory Note

This tool does not qualify as a Software as a Medical Device (SaMD) under MHRA guidance as it does not make clinical decisions or provide diagnostic outputs — it summarises and structures information already documented by a clinician. It is intended as a demonstration tool only and has not been validated for clinical use.

---

## Project Structure

```
gp-note-summariser/
├── app.py                          # Gradio interface
├── requirements.txt
├── data/
│   └── sample_notes/               # Synthetic test notes (001, 002, 003)
├── prompts/
│   └── system_prompt_v1–v9.txt     # All prompt versions
├── src/
│   └── summariser.py               # Core summarisation script
├── evaluation/
│   └── eval_rubric.md              # Scoring rubric and version logs
```

---

## Technical Stack

- **LLM:** Anthropic Claude (claude-opus-4-5)
- **Interface:** Gradio
- **Deployment:** Hugging Face Spaces
- **Language:** Python 3.14

--

## About

Built by a medical graduate exploring the application of large language models in UK primary care, and, more broadly, different ways in which clinicians can apply AI solutions to their own practice. This project is part of a portfolio demonstrating work at the intersection of clinical medicine, prompt engineering, and healthcare AI. 

Try the live demo here: [huggingface.co/spaces/draaronhaider-ai/gp-note-summariser](https://huggingface.co/spaces/draaronhaider-ai/gp-note-summariser)

For professional enquiries: [github.com/draaronhaider-ai](https://github.com/draaronhaider-ai)
