# Kinetic Typography Subtitle Linter for Arabic Social Ads

> Check selected subtitle timing, line length, and wrapping rules for Arabic and English SRT/VTT files. Results are lint suggestions, not a guarantee of readability on every device.

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Format: CLI_SCRIPT](https://img.shields.io/badge/Format-CLI--SCRIPT-green.svg)](#)
[![Tier: 2](https://img.shields.io/badge/Tier-2-orange.svg)](#)
[![Region: MENA](https://img.shields.io/badge/Region-Egypt%20%7C%20GCC%20%7C%20Saudi-purple.svg)](#)
[![Tests: Passing](https://img.shields.io/badge/Tests-Passing-brightgreen.svg)](#)
[![Owner: mahmoudabdelnaby1](https://img.shields.io/badge/Owner-mahmoudabdelnaby1-blue.svg)](https://github.com/mahmoudabdelnaby1)

---

## 📌 Problem Statement & Target Persona

### Target Persona
**PRO** operating in high-growth e-commerce, digital publishing, and direct-response marketing across Saudi Arabia, UAE, and Egypt.

### Core Problem
Develop a pure Python subtitle validation tool for Arabic and English social video (`subtitle_linter.py`): 1) Parses SRT and VTT files, 2) Flags subtitles exceeding recommended reading speed (>160 WPM), 3) Checks maximum characters per line (flagging >38 chars on mobile), 4) Detects reversed punctuation marks in Arabic bidirectional text, 5) Outputs an automated correction report.

---

## 🛠️ Repository Architecture & Deliverables

This repository provides self-contained, documented implementations and specifications:

- `docs/arabic-subtitle-best-practices.md`
- `examples/bad_subtitles.srt`
- `examples/fixed_subtitles.srt`
- `guidelines/mobile-subtitle-standards.md`
- `LICENSE`
- `README.md`
- `src/subtitle_linter.py`
- `tests/test_linter.py`
- `tests/test_subtitles.py`


---

## 🚀 Quick Start & How to Run Locally

### Run Test Suite Locally
```bash
# Ensure no bytecode generation
export PYTHONDONTWRITEBYTECODE=1  # Linux / macOS
$env:PYTHONDONTWRITEBYTECODE="1"  # Windows PowerShell

# Run Python unittest discovery
python -m unittest discover -s tests
```

### Run CLI Script
```bash
python src/subtitle_linter.py --help
```

---

## 📊 Sample Input & Output Fixtures

> **Data Disclosure:** Any included sample data is illustrative and may be synthetic; it is not a measured customer result or market benchmark unless a source and collection method are stated alongside it. These files run offline with standard libraries and require no paid third-party API credentials.

```json
{
  "domain": "content",
  "repository": "kinetic-typography-subtitle-linter",
  "status": "READY_FOR_LOCAL_REVIEW",
  "license": "MIT"
}
```

---

## ⚠️ Known Technical & Domain Constraints

- **Arabic Glyph Shaping & BiDi Integrity:** Ensures subtitle renderers do not detach Arabic letters or reverse character sequences when applying kinetic motion effects.
- **Words-Per-Screen Limits:** Caps subtitle chunks at 3 to 5 words to maintain readability during fast-paced social video narration.
- **Contrast & Shadow Enclosure:** Mandates text drop shadows or contrasting backdrop bars to prevent white text from disappearing on bright video backgrounds.

---

## 📚 Primary Documentation & Verifiable References

- [W3C Web Video Text Tracks (WebVTT) Format](https://www.w3.org/TR/webvtt1/) - Standard specification for timed text and caption display.
- [BBC Subtitle Guidelines for Arabic and RTL Text](https://bbc.github.io/subtitle-guidelines/) - Broadcasting standards for line breaks, timing, and RTL typography.
- [Unicode Standard - Arabic Script Shaping (UAX #9)](https://www.unicode.org/reports/tr9/) - Rules for bidirectional text display and font shaping.

---


## 👤 Maintainer & License

- **Author & Maintainer:** [Mahmoud Abdelnaby](https://github.com/mahmoudabdelnaby1) (`@mahmoudabdelnaby1`)
- **License:** [MIT License](LICENSE) - Open-source, auditable, and freely adaptable for internal enterprise or commercial use.
