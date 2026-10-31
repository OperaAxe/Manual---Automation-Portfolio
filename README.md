## Quality improvements and next steps

This repo already has a clear QA story, but it can be improved in a few ways to feel more mature and easier to maintain.

### What I improved
- Centralized the browser fixture in `tests/conftest.py` so the test suite has a single source of truth for setup.
- Added a `smoke` marker so quick checks can be separated from broader automation coverage.
- Added lightweight quality tooling in `requirements.txt` for linting and coverage reporting.
- Kept the test layout simple and readable while making it easier to scale.

### Recommended workflow

Run the full suite:

```bash
pytest -v
```

Run only smoke checks:

```bash
pytest -m smoke -v
```

Check linting:

```bash
ruff check .
```

Check coverage:

```bash
pytest --cov=tests
```

### Why this matters
A QA portfolio looks stronger when it shows not just test cases, but also a repeatable quality workflow. Having smoke tests, shared fixtures, and lint/coverage basics makes the project feel more like a real automation suite rather than a one-off script collection.

### Next ideas
- Add a `tests/test_storefront_smoke.py` file for a dedicated smoke layer.
- Introduce a small page object model if the suite grows.
- Add more negative-path and edge-case tests to show deeper QA thinking.
- Add CI badges and workflow runs to make the project feel more polished.
