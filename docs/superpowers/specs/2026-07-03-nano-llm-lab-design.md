# Nano LLM Lab — startup design

Date: 2026-07-03
Status: Approved for startup planning
Project path: `/Users/mag/workspace/llm/nano_llm`

## 1. Purpose

`nano_llm` is an end-to-end practical learning laboratory for LLM technology.

Its purpose is to help the user learn how large language models work by building, running, inspecting, modifying, and explaining small observable versions of their mechanisms.

The goal is not to create a practically useful local LLM or to let an agent produce one on the user's behalf. Current open-weight models are far more capable for real inference.

The value is transferable understanding that can later be applied to larger open-weight and proprietary models.

## 2. Learning goals

The project should cover both LLM internals and the surrounding LLM development ecosystem.

The user should understand:

- how raw text becomes tokens;
- how token streams become training examples;
- how next-token prediction works;
- what loss, logits, probabilities, perplexity, and sampling mean in practice;
- how embeddings, attention, causal masking, transformer blocks, and tiny GPT-style models fit together;
- how training loops, gradient descent, autograd, checkpoints, and evaluation interact;
- how Python, PyTorch, data loading, project structure, checkpoints, Hugging Face-style model layouts, local inference runtimes, and evaluation harnesses fit into practical LLM work;
- why large production LLMs behave differently from tiny scratch-built models;
- how to reason about real models using intuitions gained from smaller ones.

## 3. Non-goals

This project should not optimize for:

- building a production LLM serving product;
- competing with existing open-weight models;
- hiding concepts behind high-level libraries without explanation;
- maximizing benchmark scores;
- creating a polished app before the internals are understood;
- reinventing mature tools as production replacements;
- letting an AI agent silently complete conceptual work without the user's active learning.

Useful tooling is allowed when it supports experimentation, observability, or learning.

## 4. Learning guardrails

These guardrails are meant to prevent agent over-enthusiasm and preserve practical learning. They are not homework enforcement for the user.

### 4.1 Learning checkpoints

A new LLM mechanism is not complete merely because code, docs, or tests exist. It is complete only after the user has passed a learning checkpoint for that mechanism.

For each conceptually new mechanism, the user should be able to:

1. state a hypothesis or expected behavior;
2. run, inspect, or reason through the experiment;
3. explain what the mechanism does and what was simplified;
4. describe how the result changed their understanding;
5. record remaining questions or confusion if the concept is not clear yet.

### 4.2 Canonical interaction pattern

The default interaction style is **hybrid learner-authored work**:

- the agent may provide scaffolding, file structure, command wiring, or a small skeleton;
- the user should implement or explain the key LLM mechanism;
- the agent reviews the key mechanism strictly and educationally.

For complex topics, use **guided pair learning**: the agent breaks the mechanism into very small steps, the user writes or explains each step, and the agent reviews immediately before moving on.

For important checkpoints or core mechanisms, use the stricter cycle:

1. identify the active Learning Unit and current step;
2. ask the user for a prediction or hypothesis;
3. have the user record `Before` in `LEARNING.md`;
4. ask the user to implement or explain the key mechanism;
5. have the user record `My Attempt`;
6. perform a Learning Review;
7. fix issues together;
8. inspect instrumentation and outputs;
9. have the user fill `After`;
10. update `STATUS.md`;
11. only then move to the next step.

The user may ask for direct explanation, agent-authored code, or help finishing a unit at any time. These are allowed.

The agent should label them as explanation or agent-authored support, not as evidence that a learning checkpoint has been passed.

When a requested agent action may bypass learning of a key mechanism, the agent should give a short warning that it may amount to completing part of the lesson for the learner.

Do not show this warning as a routine session-start ritual; use it only when there is a concrete bypass risk.

### 4.3 Concept vs boilerplate

The important boundary is concept versus boilerplate.

Agent-authored support usually does not need a warning for parser glue, Makefile targets, CLI wrappers, report templates, file layout, or other mechanical code that is not the key mechanism being studied.

A warning is appropriate when the user asks the agent to implement a conceptual core, such as tokenization logic, cross-entropy, attention, sampling, checkpoint interpretation, or the training loop.

Boilerplate can still become a learning opportunity.

If the same ecosystem task appears repeatedly, the agent may suggest a small Learning Unit or side quest.

Examples include Python idioms, parsers, CLI design, data loading, packaging, PyTorch project structure, local inference usage, and eval harness design.

### 4.4 Task modes

Agents should classify each task before acting:

1. **Mechanical Mode** — scaffolding, git, file layout, Makefile, plumbing, dependency wiring, and other work that introduces no new LLM mechanism. The agent may implement directly.
2. **Learning Mode** — new LLM concepts and mechanisms. The default is learner-authored implementation or explanation, with strict agent review. Agent-authored code is allowed on request, with a warning when it risks bypassing learning.
3. **Lesson Mode** — hard or confusing concepts, or explicit structured teaching sessions. Use `teach`-style artifacts when they add learning value.
4. **Debugging Mode** — non-trivial failure analysis inside a Learning Unit.

When in doubt between Mechanical Mode and Learning Mode, choose Learning Mode.

### 4.5 Anti-overreach

When a question or checkpoint is meant to build understanding, the agent should avoid silently taking over the learning work. Prefer:

- hints over answers;
- counterexamples over conclusions;
- small manual checks over full derivations;
- review questions over lectures;
- partial scaffolds over complete solutions.

The agent may give a direct explanation or write code when the user asks for it, after a genuine attempt, or when correctness requires immediate clarification.

### 4.6 No hidden magic

High-level libraries and APIs are allowed, but they must not hide the mechanism being learned.

When using tools such as `torch.nn`, `torch.nn.functional.cross_entropy`, tokenizer libraries, Hugging Face loaders, Ollama, `llama.cpp`, MLX, or similar abstractions, explicitly document or discuss:

- what the tool does for the project;
- which part of the mechanism the user has implemented or inspected manually;
- which part is temporarily accepted as a black box;
- why using the black box is acceptable now;
- whether and when the project should return to a manual or toy version.

Using a library is not evidence of understanding it. A mechanism counts as learned only when the user can explain the relevant abstraction boundary.

### 4.7 Learning Review

Before reviewing learner-authored code for a new LLM mechanism, the user should record a short `My Attempt` section in `LEARNING.md`:

```md
## My Attempt

- What I tried:
- Why I wrote it this way:
- What I am unsure about:
```

The review should evaluate both the implementation and the user's stated mental model. It should surface incorrect assumptions, missing abstractions, and places where code works accidentally.

Learning reviews should be adversarial in standards and educational in tone. The agent should:

- search for mistakes instead of confirming by default;
- test edge cases and failure modes;
- distinguish “the code runs” from “the mechanism is understood”;
- ask targeted questions when the mental model is ambiguous;
- propose minimal corrections before full rewrites;
- avoid rewriting the whole solution unless asked or necessary;
- state clearly when something is incorrect, misleading, or accidentally working.

### 4.8 Small enough to debug by hand

Each new mechanism should first be demonstrated on data small enough for the user to trace manually before scaling up or automating.

Examples:

- tokenizer: a 10–30 character string;
- bigram model: 3–5 tokens and a tiny count matrix;
- softmax/cross-entropy: 2–3 logits;
- attention: sequence length 3 and embedding dimension 2;
- training loop: one batch and either one or two parameters or a very small network;
- sampling: a vocabulary of about 5 tokens.

If the mechanism cannot be debugged by hand yet, the experiment is probably too large for the first learning pass.

### 4.9 Scale-up ladder

Each new mechanism should move through an explicit scale-up ladder before becoming a larger experiment:

1. **Hand-trace example** — manually trace the mechanism on tiny data.
2. **Minimal code** — write the smallest implementation that reproduces the hand-traced behavior.
3. **Instrumented experiment** — add logs, assertions, visualizations, or intermediate dumps.
4. **Library comparison** — compare with PyTorch, Hugging Face, tokenizer libraries, or other high-level tools when relevant.
5. **Scaled version** — only then increase data size, model size, sequence length, or automation.

Skipping rungs is allowed only when the user explicitly chooses to skip them and records why the shortcut is acceptable.

### 4.10 Instrumentation

For learning experiments, it is not enough for code to run, print loss, or generate text. The experiment should expose relevant internals, such as:

- raw text, tokens, token IDs, and decoded text;
- tensor shapes and dimensionality changes;
- logits, probabilities, and selected next tokens;
- attention scores, attention weights, and masks;
- gradients, parameter deltas, or optimizer updates;
- intermediate losses and evaluation values;
- sampling candidates and filtered distributions;
- checkpoint tensor names, shapes, dtypes, and metadata.

Instrumentation should be small and readable, not a logging framework. Its job is to make hidden state visible enough for reasoning.

### 4.11 Definition of done

A learning experiment is done only when:

1. `README.md` explains purpose, command, expected observations, and simplifications.
2. Code runs on tiny hand-debuggable input.
3. Instrumentation exposes the relevant internals.
4. The user has written `Before` and `My Attempt` in `LEARNING.md`.
5. The agent has completed a Learning Review of code and reasoning.
6. The user has filled `After` in `LEARNING.md`.
7. Any high-level libraries used have No Hidden Magic notes.
8. The next scale-up step is explicit or intentionally deferred.

A milestone is complete only when its implementation deliverables exist, its learning checkpoints have been passed, each included learning experiment satisfies this Definition of Done, and skipped learning steps are recorded with reasons.

## 5. User and environment context

The user:

- is experienced with Go and Java;
- has written basic Python scripts;
- has Python gaps because Python is not the user's main stack;
- has no PyTorch experience yet;
- is comfortable in both Russian and English;
- prefers Go for engineering/tooling because it compiles to self-contained executables;
- is pragmatic and open to other tools/languages where they make sense.

Compute target:

- Apple Silicon laptop with large unified memory;
- local training should use Apple Silicon where possible, likely via PyTorch MPS/Metal;
- CPU fallback should remain available for tiny experiments;
- cloud/GPU can be optional later, not required for startup.

## 6. Project strategy

The project uses a two-track strategy.

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

This track is not intended to produce a practical inference product. It helps answer questions like:

- how do sampling settings change outputs?
- how does tokenizer behavior differ?
- why does instruction tuning matter?
- why does scale/data/training quality dominate tiny-model behavior?
- what can be explained by architecture, and what comes from data and training?

## 7. Repository format

The project should be organized around Learning Units plus concise documentation. A Learning Unit is a resumable lesson/experiment, usually under `experiments/00X-*`.

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
    glossary.md
    experiments.md
    decisions/
    superpowers/
      specs/
        2026-07-03-nano-llm-lab-design.md

  templates/
    LEARNING.md
    STATUS.md
    HANDOFF.md

  experiments/
    README.md
    001-corpus-and-tokenizer/
      README.md
      STATUS.md
      LEARNING.md
      HANDOFF.md        # optional, when fresh-context resume needs extra detail
    002-bigram-baseline/
    002a-python-pytorch-survival-kit/  # optional/supporting
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

## 8. Learning Units and fresh-context resumability

A Learning Unit may take one short session or stretch across many iterations. It may branch into implementation, `teach`-style lesson work, debugging, review, or deep conceptual discussion, then return to the main course path.

A Learning Unit should be restartable from a fresh agent context without relying on prior chat history. The canonical resume path is:

1. read `AGENTS.md` for global operating rules;
2. read `ROADMAP.md` for course sequence and current position;
3. read the Learning Unit's `README.md` for scope and commands;
4. read the Learning Unit's `STATUS.md` for current state, active step, blockers, and next action;
5. read the Learning Unit's `LEARNING.md` for predictions, attempts, review history, understanding, and confusion;
6. read `HANDOFF.md` only when present for extra resume context.

### 8.1 Learning Unit files

Each Learning Unit should contain:

- `README.md` — scope, concept, commands, expected observations, simplifications, and links;
- `STATUS.md` — current state, active step, blockers, next action, and mode transitions;
- `LEARNING.md` — predictions, attempts, review notes, understanding, confusion, and revisit items;
- code/data/scripts for the minimal experiment;
- optional `HANDOFF.md` — only when extra context is needed after a complex multi-session path.

The startup spec is not meant to become a separate spec for every Learning Unit. Individual units should use lightweight README/STATUS/LEARNING artifacts by default.

Create a heavier spec only when the unit involves a genuinely complex design choice or multi-part plan.

### 8.2 `STATUS.md` shape

`STATUS.md` is the main anti-context-rot file for a Learning Unit. It should stay short; 10–30 lines is usually enough.

```md
# Status

State: planned | in_progress | blocked | review | done
Mode: Mechanical | Learning | Lesson | Debugging
Context health: fresh | stable | long | compacted | stale
Handoff needed: yes | no
Current step:
Next action:
Blockers:

## Progress

- [ ] ...

## Mode transitions

- YYYY-MM-DD: Learning → Debugging because ...

## Resume instructions

When a fresh agent starts here:

1. Read `AGENTS.md`.
2. Read `ROADMAP.md`.
3. Read this Learning Unit's `README.md`, `STATUS.md`, and `LEARNING.md`.
4. Continue from: ...
5. Do not: ...
```

Update `STATUS.md` when state, mode, context health, handoff need, blocker, next action, or resume instructions change.

### 8.3 Lightweight status discipline

Status and mode tracking exists only to preserve learning continuity across fresh contexts. It must not become a workflow engine, issue tracker, or bureaucratic state machine.

Record only meaningful transitions, such as entering Debugging, entering Lesson Mode, becoming blocked, splitting work into a new Learning Unit, deferring a branch, or returning to Learning Mode. Do not record micro-transitions.

If status details grow too large, move details into `LEARNING.md`, `HANDOFF.md`, or `debug/FINDINGS.md`.

Side branches should end in one of four lightweight outcomes: return to Learning, blocked, split into a new Learning Unit, or explicitly deferred.

### 8.4 Attached Lesson Mode

A Learning Unit is not the same as a `teach` lesson HTML. `teach` artifacts may be created inside or near a Learning Unit when useful, but the Learning Unit remains the operational repo artifact.

If a unit enters Lesson Mode, update `STATUS.md` with `Mode: Lesson` and link lesson artifacts from `STATUS.md` or `LEARNING.md`.

Preferred layout:

```text
experiments/001-corpus-and-tokenizer/
  README.md
  STATUS.md
  LEARNING.md
  teach/
    lessons/
    reference/
    learning-records/
```

If `teach` artifacts are stored elsewhere, the Learning Unit must still link to them clearly.

### 8.5 Attached Debugging Mode

Debugging Mode should stay attached to the active Learning Unit. If an experiment breaks, update `STATUS.md` with `Mode: Debugging`, describe the blocker, and make the next reproduction step explicit.

When the investigation becomes non-trivial, keep debugging artifacts under the unit:

```text
experiments/001-corpus-and-tokenizer/
  debug/
    REPRO.md
    HYPOTHESES.md
    FINDINGS.md
```

Debugging is part of practical LLM learning. Shape mismatches, NaN losses, exploding gradients, tokenizer bugs, data leakage, and confusing sampling behavior should be captured as learning material.

### 8.6 Side Quest Promotion

If a Lesson, Debugging, or deep-dive branch grows beyond one or two iterations, or becomes independently valuable, decide whether to return, defer, or split it into its own Learning Unit.

When a side quest is deferred or split:

1. add or update an entry in `ROADMAP.md`;
2. record dependency and priority: now, later, or optional;
3. explain briefly why it was deferred or split;
4. link it from the current unit's `STATUS.md` or `LEARNING.md`;
5. return the current unit to the main path unless the user chooses to pursue the side quest now.

### 8.7 Roadmap index

`ROADMAP.md` is the course-level Learning Unit index and the source for the current unit.

```md
# Roadmap

Current Learning Unit: experiments/001-corpus-and-tokenizer

## Learning Units

| Unit | Status | Mode | Concept | Depends on |
|---|---|---|---|---|
| 001 | planned | Learning | Corpus/tokenizer | none |
| 002 | planned | Learning | Bigram baseline | 001 |
| 002a | optional | Learning | Python/PyTorch survival kit | when Python/PyTorch friction blocks progress |
```

A fresh agent should use `ROADMAP.md` to identify the current Learning Unit, then use that unit's `STATUS.md` for detailed state.

### 8.8 Fresh-context and compaction recovery

Future `AGENTS.md` should include this mandatory boot protocol:

1. read `AGENTS.md`;
2. read `ROADMAP.md`;
3. identify the current Learning Unit from `ROADMAP.md` and unit statuses;
4. read that unit's `README.md`, `STATUS.md`, and `LEARNING.md`;
5. read `HANDOFF.md` when present;
6. classify the task mode;
7. continue from `Next action`, unless the user redirects;
8. if chat history conflicts with repository artifacts, trust repository artifacts and ask before overwriting them.

After compaction, reconstruct state from repository artifacts before continuing and set `Context health: compacted` in the active unit's `STATUS.md`.

If the current unit has drifted through multiple branches, debugging sessions, or teach sessions, set `Handoff needed: yes` and create or update `HANDOFF.md`.

Use the `handoff` skill when ending a complex session, before a likely context reset, or when another agent should continue. Handoffs should link to `AGENTS.md`, `ROADMAP.md`, and active Learning Unit artifacts rather than duplicating them.

## 9. Step 0 — Agent-ready project initialization

Before implementing LLM experiments, initialize the repository as an agent-friendly long-running research project.

Milestone 0 is Mechanical Mode. The agent may implement it directly because it introduces no LLM mechanism. Its purpose is to install the learning workflow guardrails before LLM mechanism work starts.

Milestone 0 should create minimal templates and guardrails, not exhaustive course content or a heavy workflow system. Keep files short and operational; expand them only when a Learning Unit needs more detail.

Step 0 should keep project files sharply separated by purpose:

- `CONTEXT.md` — glossary for canonical project language only;
- `README.md` — project purpose, audience, non-goals, and quick start;
- `ROADMAP.md` — milestones, current stage, learning sequence, and Learning Unit index;
- `AGENTS.md` — operating rules for future AI agents;
- `MEMORY.md` — human-readable session notes and decision history;
- ADRs — hard-to-reverse decisions with real trade-offs, when needed.

Recommended Step 0 files:

- `README.md`;
- `AGENTS.md`;
- `CONTEXT.md`;
- `MEMORY.md`;
- `ROADMAP.md`;
- `.gitignore`;
- `Makefile`;
- `docs/glossary.md`;
- `docs/experiments.md`;
- `experiments/README.md`;
- `templates/LEARNING.md`;
- `templates/STATUS.md`;
- `templates/HANDOFF.md`;
- placeholder directories for `cmd/`, `internal/`, `python/`, `data/`, and `models/`.

`AGENTS.md` should capture task modes, learner-authored implementation, anti-overreach, no-hidden-magic, scale-up ladder, instrumentation, fresh-context recovery, Go/Python boundary, and completion rules.

## 10. Milestones

### Milestone 0 — Agent-ready repo scaffold

Outcome:

```text
empty directory → initialized, documented, agent-ready repository
```

Deliverables:

- git repository initialized;
- agent/context/memory files created;
- roadmap and experiment conventions created;
- minimal templates created for `LEARNING.md`, `STATUS.md`, and `HANDOFF.md`;
- `AGENTS.md` captures the operating guardrails;
- first commit created.

Learning checkpoints:

- user can explain why this repository is a practical LLM learning lab, not an agent-completed product;
- user can describe which durable files hold glossary, roadmap, agent rules, memory, and decisions;
- user can identify the next learning mechanism before implementation begins.

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

Learning checkpoints:

- user can explain how raw text becomes discrete tokens and why token choice changes the problem;
- user can predict what a bigram or n-gram model can and cannot learn before seeing generated text;
- user can explain next-token prediction, train/validation split, loss, and perplexity using this tiny baseline;
- user records at least one confusion, surprise, or follow-up question before moving to neural models.

Rationale: this gives the first complete language-modeling loop without needing PyTorch yet.

### Milestone 2 — Neural foundations

Outcome:

```text
manual/statistical baseline → learned representations
```

Recommended supporting Learning Unit:

- `002a-python-pytorch-survival-kit` — optional and used when Python/PyTorch mechanics start blocking LLM understanding. It can cover venv/dependencies, running modules, tensors, shapes, stack traces, Apple Silicon PyTorch setup, `argparse`, and basic Python project layout. Familiar topics can be checked off externally without a full lesson.

Deliverables:

- Python/NumPy or PyTorch tensor introduction;
- embeddings experiment;
- logits, softmax, and cross-entropy explained;
- minimal training loop;
- comparison with bigram baseline.

Learning checkpoints:

- user can explain what a tensor represents in the experiment and how it differs from ordinary Go/Java data structures;
- user can describe embeddings as learned vectors and contrast them with direct token statistics;
- user can connect logits, softmax probabilities, cross-entropy loss, and gradient-based updates;
- user can explain what improved, worsened, or stayed unclear compared with the bigram baseline.

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

Learning checkpoints:

- user can explain queries, keys, values, attention weights, and why causal masking prevents looking ahead;
- user can predict how changing a toy sequence changes attention behavior;
- user can distinguish the essential transformer mechanism from simplifying implementation details;
- user can explain why positional information, residual connections, and layer norm are introduced.

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

Learning checkpoints:

- user can trace one batch from tokens through model output, loss, backward pass, and parameter update;
- user can explain what makes this model GPT-like and what is intentionally tiny or unrealistic;
- user can interpret training and validation behavior, including overfitting and underfitting signs;
- user can explain why generated text remains weak even when the training loop works.

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

Learning checkpoints:

- user can explain the difference between model architecture, configuration, tokenizer, and weight tensors;
- user can inspect a checkpoint and identify tensor names, shapes, dtypes, and what part of the model they correspond to;
- user can explain why SafeTensors is a serialization format, not a training framework or PyTorch replacement;
- user can reason about what is missing when only a weights file is available.

Rationale: modern LLM artifacts often use SafeTensors, but SafeTensors is easiest to understand after a concrete `state_dict` and checkpoint mental model.

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

Learning checkpoints:

- user can predict how greedy decoding, temperature, top-k, and top-p should change outputs before running them;
- user can explain the trade-off between determinism, diversity, coherence, and repetition;
- user can distinguish model quality from decoding strategy effects;
- user records which sampling intuitions transfer to real LLMs and which remain uncertain.

### Milestone 7 — Compare with local open-weight models

Outcome:

```text
tiny model intuitions → comparison with capable local models
```

Deliverables:

- local-model comparison harness;
- same prompts/evals run against tiny and real models;
- notes on tokenizer, instruction tuning, context length, scale, data, and sampling differences.

Learning checkpoints:

- user can separate behavior caused by tokenizer, scale, data, instruction tuning, context length, and sampling settings;
- user can explain why tiny-model intuitions are useful but incomplete for production-scale LLMs;
- user can design a small comparison prompt or eval and predict what each model class will likely do;
- user records at least one practical lesson for using or evaluating real LLMs.

## 11. Language and tooling decisions

### 11.1 Go / Python boundary

Python is the standard language of much of the ML ecosystem, largely for historical and ecosystem reasons. It is not automatically the most suitable or efficient language for every part of this project.

The project should keep a Go application/tooling spine where that improves engineering clarity, and introduce Python libraries where they are the clearest path to tensors, autograd, neural networks, and ecosystem compatibility.

Use Go for:

- CLI entrypoints;
- corpus preparation;
- tokenizer experiments where useful;
- evaluation harnesses;
- experiment orchestration;
- simple local APIs if needed later;
- application-level integration with Python libraries or artifacts at later stages.

Use Python for:

- learning the practical Python ecosystem around LLM work, because it is not the user's primary stack;
- tensor experiments;
- neural network internals;
- PyTorch autograd;
- transformer training;
- Apple Silicon MPS experiments;
- compatibility with ML ecosystem artifacts and libraries.

Future `AGENTS.md` should say: do not convert the Go-first application/tooling spine into a Python-first architecture merely because most ML examples online are Python-first.

If the language boundary itself becomes educationally relevant, record it in `LEARNING.md` or promote it as a side quest.

### 11.2 Reimplementation for learning

Naive or native reimplementation of established tools and algorithms is allowed when it serves learning and deeper understanding.

The project may intentionally rebuild small versions of tokenizers, tensor operations, losses, samplers, checkpoint inspectors, or evaluation tools even when mature libraries exist.

These reimplementations should be small, observable, and honest about what they simplify.

Distinguish **reimplementation for learning** from **reinvention for production**. Reimplementing a tiny tokenizer to understand tokenization is good.

Attempting to replace Hugging Face Tokenizers, PyTorch, SafeTensors, or mature inference runtimes as production-grade infrastructure is a non-goal.

### 11.3 SafeTensors and checkpoint formats

Use SafeTensors for:

- understanding how modern LLM weights are stored;
- safe tensor serialization without Python pickle semantics;
- inspecting tensor names, shapes, dtypes, and metadata;
- comparing tiny local checkpoints with Hugging Face-style model artifacts;
- learning the boundary between weights, architecture code, config, and tokenizer files.

SafeTensors should not replace PyTorch in the learning path:

```text
PyTorch = computation, autograd, training, model structure
SafeTensors = checkpoint/weight storage, inspection, interchange
```

Introduce SafeTensors after PyTorch `state_dict`, not before it.

### 11.4 Local model tooling

Potential tools for the comparison track:

- `llama.cpp`;
- MLX ecosystem;
- Ollama;
- other local inference runtimes as needed.

These are optional and should be introduced only when they serve a concrete comparison experiment.

## 12. Documentation conventions

Each Learning Unit should include:

- `README.md` with purpose, concept, commands, expected output or observations, links, and simplifications;
- `STATUS.md` with state, active step, blockers, next action, and mode transitions;
- `LEARNING.md` as the user's learning journal;
- small runnable code or notebooks/scripts where appropriate;
- optional `HANDOFF.md` when fresh-context resume needs extra detail.

`LEARNING.md` should use this shape:

```md
# Learning Journal

## Before

- What I expect:
- What I think this mechanism does:
- What I predict will happen when I run it:

## My Attempt

- What I tried:
- Why I wrote it this way:
- What I am unsure about:

## During

- What surprised me:
- What broke or confused me:
- What I changed:

## After

- What I can explain now:
- What is still unclear:
- What to revisit:
```

Docs should be concise, but allow deep dives when a concept deserves it.

Suggested docs:

```text
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

## 13. Suggested skills for future agents

These are harness-level skills known to the user. Treat them as optional recommendations, not automatic requirements.

### `teach`

Use as optional Lesson Mode, not as the default way to advance the project.

Good uses:

- create a focused lesson on tokenization, logits, softmax, cross-entropy, autograd/backprop, attention, causal masks, sampling, checkpoint anatomy, or training loops;
- create `MISSION.md`, `lessons/*.html`, `reference/*.html`, `learning-records/*.md`, `RESOURCES.md`, or `NOTES.md` when explicitly useful;
- add retrieval practice, short quizzes, or printable reference sheets;
- turn a confusing experiment into a structured lesson and learning record.

Do not use for mechanical repo work, scaffolding, CLI plumbing, Makefile changes, git operations, normal bug fixes, or quick documentation edits. Normal milestones do not have to create `lessons/*.html`.

### `handoff`

Use when ending a complex session, before a likely context reset, or when another agent should continue. The handoff should link to existing specs/plans/docs instead of duplicating them.

### `tdd`

Use later when implementing testable Go or Python components where a red-green-refactor loop would clarify behavior.

### `diagnose`

Use when experiments, training runs, or CLI commands fail in unclear ways and need systematic debugging.

### `review`

Use when there are meaningful changes to review against project standards or a spec.

### `setup-matt-pocock-skills`

Consider only if the project later needs a fuller agent/documentation/issue-tracker convention setup. For Step 0, manual lightweight files are enough unless the user asks otherwise.

## 14. First implementation recommendation

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

## 15. Open questions for later

These do not block startup:

- Which exact English starter corpus should be used?
- Should the first tokenizer be character-level, byte-level, word-level, or BPE?
- Should the first neural experiment use NumPy before PyTorch, or go directly to PyTorch with careful explanation?
- Which local open-weight runtime should be used first for comparison?
- Which Python/PyTorch survival-kit topics should be checked off externally versus explored as Learning Units?
