.PHONY: test-scenarios

test-scenarios:
	@bash tests/scenarios/run-scenarios.sh

.PHONY: test
test:
	python3 -m unittest discover -s tests/unit -v
