all:
	@echo "Using python, nothing to compile. Proceed with next"

run%: task%.py
	@python3 $<