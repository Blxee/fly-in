
install:
	@poetry install

run:
	@poetry run flyin

debug:
	@poetry run python3 -m pdb src/fly_in/cli.py

clean:
	@rm -rf  __pycache__ .mypy_cache

lint:
	@flake8 .
	@mypy . --warn-return-any --warn-unused-ignores --ignore-missing-imports --disallow-untyped-defs --check-untyped-defs

lint-strict:
	@flake8 .
	@mypy . --strict
