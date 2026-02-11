# codexproject

A minimal Python starter project that includes:

- A reusable `Project` domain class for managing tasks.
- A small command-line interface (`codexproject`) for quick interactions.
- A pytest suite to validate core behavior.

## Quick start

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .[dev]
pytest
```

## CLI examples

```bash
codexproject demo
codexproject demo --add "Write project plan"
codexproject demo --complete 0
```
