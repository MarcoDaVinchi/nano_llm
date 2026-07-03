# Nano LLM Lab — startup design

Date: 2026-07-03
Status: Approved for startup planning
Project path: `/Users/mag/workspace/llm/nano_llm`

## 1. Purpose

`nano_llm` is an end-to-end learning laboratory for understanding how large language models work by manually building small, observable versions of their mechanisms.

The goal is not to create a practically useful local LLM. Current open-weight models are far more capable for real inference. The value of this project is to build, inspect, and experiment with small systems so the user can transfer that understanding to larger open-weight and proprietary models later.

## 2. Learning goals

The project should help the user understand:

- how raw text becomes tokens;
- how token streams become training examples;
- how next-token prediction works;
- what loss, logits, probabilities, perplexity, and sampling mean in practice;
- how embeddings, attention, causal masking, transformer blocks, and tiny GPT-style models fit together;
- how training loops, gradient descent, autograd, checkpoints, and evaluation interact;
- why large production LLMs behave differently from tiny scratch-built models;
- how to reason about real models using intuitions gained from smaller ones.

## 3. Non-goals

This project should not optimize for:

- building a production LLM serving product;
- competing with existing open-weight models;
- hiding concepts behind high-level libraries without explanation;
- maximizing benchmark scores;
- creating a polished app before the internals are understood.

Useful tooling is allowed, but only when it supports experimentation, observability, or learning.

## 4. User and environment context

The user:

- is experienced with Go and Java;
- has written basic Python scripts;
- has no PyTorch experience yet;
- is comfortable in both Russian and English;
- prefers Go for engineering/tooling because it compiles to self-contained executables;
- is pragmatic and open to other tools/languages where they make sense.

Compute target:

- Apple Silicon laptop with large unified memory;
- local training should use Apple Silicon where possible, likely via PyTorch MPS/Metal;
- CPU fallback should remain available for tiny experiments;
- cloud/GPU can be optional later, not required for project startup.

## 5. Project strategy

The project uses a two-track strategy:

### Track 1 — Build from scratch

This is the main track. It builds progressively from text processing to a tiny GPT-style model:

```text
corpus → tokenizer → dataset → baseline model → embeddings → attention → transformer → training → generation → evaluation
```

### Track 2 — Compare with real LLMs

This is a supporting track. It uses local open-weight models to compare behavior and build intuition:

```text
tiny scratch model behavior ↔ local open-weight model behavior
```

This track is not intended to produce a practical inference product. It exists to help answer questions like:

- how do sampling settings change outputs?
- how does tokenizer behavior differ?
- why does instruction tuning matter?
- why does scale/data/training quality dominate tiny-model behavior?
- what can be explained by architecture, and what comes from data and training?

## 6. Repository format

The project should be organized around runnable experiments plus concise documentation.

Experiments are the primary unit of learning. Docs provide explanations, deeper dives, and durable notes.

Proposed structure:

```text
nano_llm/
  README.md
  AGENTS.md
  CONTEXT.md
  MEMORY.md
  ROADMAP.md
  Makefile
  .gitignore

  docs/
    00-roadmap.md
    glossary.md
    experiments.md
    decisions/
    superpowers/
      specs/
        2026-07-03-nano-llm-lab-design.md

  experiments/
    README.md
    001-corpus-and-tokenizer/
    002-bigram-baseline/
    003-embeddings/
    004-self-attention/
    005-tiny-transformer/
    006-tiny-gpt-training/
    007-sampling-strategies/
    008-compare-local-llm/

  cmd/
    nano/

  internal/
    corpus/
    tokenizer/
    eval/

  python/

  data/
    raw/
    processed/

  models/
    checkpoints/
```

## 7. Step 0 — Agent-ready project initialization

Before implementing LLM experiments, the repository should be initialized as an agent-friendly long-running research project.

Step 0 should include:

1. initialize a git repository;
2. create basic project files;
3. create agent collaboration files;
4. define documentation and experiment conventions;
5. create a high-level roadmap;
6. record current project context and decisions.

Recommended Step 0 files:

- `README.md` — project overview and quick start;
- `AGENTS.md` — instructions for future AI agents working in this repo;
- `CONTEXT.md` — durable project context: goals, non-goals, architecture, current milestone;
- `MEMORY.md` — human-readable decision and session log;
- `ROADMAP.md` — staged project roadmap;
- `.gitignore` — ignores generated data, checkpoints, caches, virtual environments;
- `Makefile` — common commands, initially minimal;
- `docs/glossary.md` — durable vocabulary for LLM concepts;
- `docs/experiments.md` — experiment conventions;
- `experiments/README.md` — required structure for each experiment;
- placeholder directories for `cmd/`, `internal/`, `python/`, `data/`, and `models/`.

### AGENTS.md should state

- This is a learning laboratory, not a production-first codebase.
- Prefer explainability over cleverness.
- Keep experiments small and runnable.
- Every experiment should have a README explaining goal, commands, expected observations, and follow-up questions.
- Use Go for CLI/tooling/data preparation where practical.
- Use Python/NumPy/PyTorch for ML internals when they are the clearest learning path.
- Do not hide important mechanisms behind libraries without documenting what they do.
- Update `CONTEXT.md`, `MEMORY.md`, docs, or decision records when project direction changes.

## 8. Milestones

### Milestone 0 — Agent-ready repo scaffold

Outcome:

```text
empty directory → initialized, documented, agent-ready repository
```

Deliverables:

- git repository initialized;
- agent/context/memory files created;
- roadmap and experiment conventions created;
- first commit created.

### Milestone 1 — Corpus → tokenizer → bigram baseline

Outcome:

```text
text corpus → tokens → model statistics → next-token prediction → generated text → evaluation
```

Deliverables:

- small English corpus prepared;
- simple tokenizer implemented;
- train/validation split created;
- bigram or n-gram baseline implemented;
- generation command implemented;
- loss/perplexity or comparable eval introduced;
- documentation explaining next-token prediction.

Rationale: this gives the first complete language-modeling loop without needing PyTorch yet.

### Milestone 2 — Neural foundations

Outcome:

```text
manual/statistical baseline → learned representations
```

Deliverables:

- Python/NumPy or PyTorch tensor introduction;
- embeddings experiment;
- logits, softmax, and cross-entropy explained;
- minimal training loop;
- comparison with bigram baseline.

### Milestone 3 — Attention and transformer internals

Outcome:

```text
embeddings → causal self-attention → transformer block
```

Deliverables:

- single-head self-attention experiment;
- causal mask visualization/explanation;
- multi-head attention;
- positional embeddings;
- residual connections;
- layer norm;
- minimal transformer block.

### Milestone 4 — Tiny GPT training

Outcome:

```text
transformer blocks → tiny causal language model → generated text
```

Deliverables:

- tiny GPT-like model;
- training loop on Apple Silicon where possible;
- checkpoints;
- generation command;
- qualitative and quantitative eval;
- notes on overfitting and scale limits.

### Milestone 5 — Checkpoints and SafeTensors

Outcome:

```text
trained tiny model → named tensors → portable checkpoint artifacts → inspectable model weights
```

Deliverables:

- explain PyTorch `state_dict` as the first mental model for model weights;
- save and load tiny-model checkpoints using PyTorch-native checkpointing;
- introduce SafeTensors as a safe, fast tensor serialization format rather than a replacement for PyTorch;
- save the same tiny-model weights as `.safetensors`;
- inspect SafeTensors contents by listing tensor names, shapes, dtypes, and metadata;
- document why weights alone are not a complete model without architecture, config, and tokenizer;
- compare how Hugging Face-style model directories combine config, tokenizer files, and SafeTensors weight shards.

Rationale: modern LLM artifacts often use SafeTensors, but SafeTensors is easiest to understand after the user has a concrete `state_dict` and checkpoint mental model. PyTorch remains the learning tool for computation, autograd, and training; SafeTensors becomes the learning tool for weight storage, safety, and ecosystem compatibility.

### Milestone 6 — Sampling and evaluation

Outcome:

```text
trained tiny model → controlled generation → observed behavior
```

Deliverables:

- greedy decoding;
- temperature;
- top-k;
- top-p;
- repeat behavior observations;
- simple eval harness.

### Milestone 7 — Compare with local open-weight models

Outcome:

```text
tiny model intuitions → comparison with capable local models
```

Deliverables:

- local-model comparison harness;
- same prompts/evals run against tiny and real models;
- notes on tokenizer, instruction tuning, context length, scale, data, and sampling differences.

## 9. Language and tooling decisions

### Go

Use Go for:

- CLI entrypoints;
- corpus preparation;
- tokenizer experiments where useful;
- evaluation harnesses;
- experiment orchestration;
- simple local APIs if needed later.

### Python / NumPy / PyTorch

Use Python for:

- tensor experiments;
- neural network internals;
- PyTorch autograd;
- transformer training;
- Apple Silicon MPS experiments.

### SafeTensors and checkpoint formats

Use SafeTensors for:

- understanding how modern LLM weights are stored;
- safe tensor serialization without Python pickle semantics;
- inspecting tensor names, shapes, dtypes, and metadata;
- comparing tiny local checkpoints with Hugging Face-style model artifacts;
- learning the boundary between weights, architecture code, config, and tokenizer files.

SafeTensors should not replace PyTorch in the learning path. In this project:

```text
PyTorch = computation, autograd, training, model structure
SafeTensors = checkpoint/weight storage, inspection, interchange
```

Introduce SafeTensors after PyTorch `state_dict`, not before it.

### Local model tooling

Potential tools for the comparison track:

- `llama.cpp`;
- MLX ecosystem;
- Ollama;
- other local inference runtimes as needed.

These are optional and should be introduced only when they serve a concrete comparison experiment.

## 10. Documentation conventions

Each experiment should include:

- purpose;
- concept being studied;
- commands to run;
- expected output or observations;
- questions to answer after running;
- links to related docs;
- notes on what is intentionally simplified.

Docs should be concise, but allow deep dives when a concept deserves it.

Suggested docs:

```text
docs/00-roadmap.md
docs/01-tokenization.md
docs/02-bigram.md
docs/03-embeddings.md
docs/04-attention.md
docs/05-transformer.md
docs/06-training.md
docs/07-sampling.md
docs/08-evaluation.md
docs/glossary.md
```

## 11. Suggested skills for future agents

These are harness-level skills known to the user. They should be treated as optional recommendations, not automatic requirements.

### `teach`

Use when the session goal is to teach a specific LLM concept using this repository as the learning workspace.

Good uses:

- create a focused lesson on tokenization, logits, cross-entropy, attention, causal masks, sampling, or training loops;
- create `lessons/*.html`, `reference/*.html`, `learning-records/*.md`, `MISSION.md`, or `RESOURCES.md` when the user explicitly wants a teaching session;
- add retrieval practice or short quizzes for long-term retention;
- turn a confusing experiment into a structured lesson.

Do not use for normal implementation tasks, repo scaffolding, bug fixes, or quick documentation edits.

### `handoff`

Use when ending a session that another agent should continue. The handoff should summarize current state, link to existing specs/plans/docs instead of duplicating them, and include suggested skills for the next session.

### `tdd`

Use later when implementing testable Go or Python components where a red-green-refactor loop would clarify behavior.

### `diagnose`

Use when experiments, training runs, or CLI commands fail in unclear ways and need systematic debugging.

### `review`

Use when there are meaningful changes to review against project standards or a spec.

### `setup-matt-pocock-skills`

Consider only if the project later needs a fuller agent/documentation/issue-tracker convention setup. For Step 0, manual lightweight files are enough unless the user asks otherwise.

## 12. First implementation recommendation

Start with Milestone 0 only.

Do not begin tokenizer/model work until the repository has:

- `AGENTS.md`;
- `CONTEXT.md`;
- `MEMORY.md`;
- `ROADMAP.md`;
- experiment conventions;
- git initialized;
- initial commit.

After Milestone 0, create a detailed implementation plan for Milestone 1:

```text
corpus → tokenizer → bigram baseline → generation → eval
```

## 13. Open questions for later

These do not block startup:

- Which exact English starter corpus should be used?
- Should the first tokenizer be character-level, byte-level, word-level, or BPE?
- Should the first neural experiment use NumPy before PyTorch, or go directly to PyTorch with careful explanation?
- Which local open-weight runtime should be used first for comparison?
- Should teaching artifacts from `teach` live inside the main repo or be separated from core engineering docs?
