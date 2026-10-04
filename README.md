# Automated ML Training Pipeline

Level: 11 — ML Engineering

Skills: Python, a training gate

A run passes when rows >= 10 and target is present. It does not write a model to a registry.

```bash
pip install -r requirements.txt
pytest -q
```

This is a local laptop proof. It does not call a hosted model and it does not apply production changes.
