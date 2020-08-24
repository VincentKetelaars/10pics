.PHONY:

lint:
	poetry run black ten_pics -l 120
	poetry run isort ten_pics

lint-check:
	poetry run pydocstyle
	poetry run black ten_pics -l 120 --check
	poetry run isort ten_pics --check-only
	poetry run flake8 ten_pics
	poetry run mypy ten_pics
	poetry run pylint ten_pics
