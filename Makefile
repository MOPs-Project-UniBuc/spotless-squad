
.PHONY: help
help:
	@# Magic line used to create self-documenting makefiles.
	@# See https://stackoverflow.com/a/35730928
	@awk '/^#/{c=substr($$0,3);next}c&&/^[[:alpha:]][[:alnum:]_-]+:/{print substr($$1,1,index($$1,":")),c}1{c=0}' Makefile | column -s: -t

# only pytest
.PHONY: pytest
pytest:
	pytest \
	-v \
	-n auto \
	--random-order \
	--html=pytest-report.html --self-contained-html \
	--exitfirst \
	spotlesssquad/tests/

# pytest + coverage
.PHONY: pycoverage
pycoverage:
	pytest \
	-v \
	-n auto \
	--random-order \
	--html=pytest-report.html --self-contained-html \
	--exitfirst \
	--no-cov-on-fail \
	--cov=spotlesssquad/ \
	--cov-branch \
	--cov-report=html:./coverage-html \
	--cov-report=json:./coverage.json \
	spotlesssquad/tests/

.PHONY: mypy
# TODO...
mypy:
	rm -rf .mypy_cache

	pre-commit run mypy --all

.PHONY: checks
# TODO...
checks:
	rm -rf .mypy_cache

	pre-commit run --all-files

	pytest --junitxml=junit.xml spotlesssquad/tests/

	./helmfiles-check.sh

.PHONY: ruff
ruff:
	pre-commit run ruff --all
	pre-commit run ruff-format --all
