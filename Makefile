.PHONY: help status verify

help:
	@echo "nano_llm commands:"
	@echo "  make status  - show git status and current roadmap header"
	@echo "  make verify  - run lightweight repository checks"

status:
	@git status --short
	@echo
	@sed -n '1,40p' ROADMAP.md

verify:
	@python3 scripts/verify_markdown.py
