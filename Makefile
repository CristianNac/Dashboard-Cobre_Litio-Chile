# === Config ===

PY ?= poetry run python
MODULE ?= dashboard_mineria
ENTRY ?= app
PYTHONPATH ?= src

.PHONY: run clean

run:
	PYTHONPATH=$(PYTHONPATH) $(PY) -m $(MODULE).$(ENTRY)

clean:
	@echo "Limpiando __pycache__ y archivos temporales..."
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type d -name ".pytest_cache" -exec rm -rf {} +
	find . -type d -name ".ruff_cache" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete




