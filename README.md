# nano_llm

`nano_llm` is a practical learning lab for LLM technology.

The project exists to build transferable understanding of language-model internals and the surrounding LLM development ecosystem. It is not trying to produce a useful production LLM, and it should not become an agent-authored project that the user merely observes.

## Audience

This repository is for an experienced Go/Java developer learning LLM internals, Python/PyTorch ecosystem practices, and local model tooling through small observable experiments.

## Current stage

Current milestone: **Milestone 0 — agent-ready repo scaffold**.

Milestone 0 creates durable repository artifacts before any tokenizer or model implementation starts:

- `AGENTS.md` for future agent operating rules;
- `ROADMAP.md` for course sequence and active Learning Unit;
- `CONTEXT.md` for canonical glossary terms;
- `MEMORY.md` for human-readable session notes;
- `templates/` for Learning Unit artifacts.

## Quick start

```bash
make help
make status
make verify
```

No LLM experiment code exists yet. The next learning step after Milestone 0 is planning Milestone 1: corpus → tokenizer → bigram baseline.

## Non-goals

- Production inference serving.
- Competing with open-weight models.
- Maximizing benchmark scores.
- Hiding mechanisms behind libraries without explanation.
- Letting an AI agent silently complete conceptual learning work.

## Canonical spec

The startup design is in:

- `docs/superpowers/specs/2026-07-03-nano-llm-lab-design.md`
