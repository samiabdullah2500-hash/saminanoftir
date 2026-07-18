# saminanoftir

**Find peaks** — A lightweight, deterministic Python toolkit for finding and analyzing peaks in FTIR, Raman, and other spectroscopy data.

Part of the NanoSami ecosystem for offline nanomaterials research.

## Features
- Robust peak detection with configurable parameters
- Export to CSV/JSON with provenance
- CLI and importable module
- Zero external dependencies beyond numpy/scipy (optional)

## Usage
```bash
python -m saminanoftir peaks data.csv --method ftir
```

## Installation
```bash
pip install -e .
```

See NanoSami project for integration.