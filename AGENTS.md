# AGENTS.md

Operating rules for AI agents working in `nano_llm`.

## Prime directive

This is a practical LLM learning project. Optimize for the user's understanding, not for autonomous implementation throughput.

Do not silently turn the repository into a self-writing nano LLM project. If a requested action may bypass learning of a key mechanism, warn briefly and offer a learner-authored path.

## Fresh-context boot protocol

At the start of a new session:

1. Read this file.
2. Read `ROADMAP.md`.
3. Read `CONTEXT.md` for glossary terms.
4. Identify the active Learning Unit from `ROADMAP.md`.
5. If an active unit exists, read its `README.md`, `STATUS.md`, and `LEARNING.md`.
6. Read `HANDOFF.md` only when present.
7. Classify the task mode before acting.
8. If chat history conflicts with repository artifacts, trust repository artifacts and ask before overwriting them.

After compaction, reconstruct state from repository artifacts and set the active unit's `Context health: compacted` when applicable.

## Task modes

- **Mechanical Mode** — scaffolding, docs wiring, Makefile, git, file layout, dependency plumbing. Agent may implement directly.
- **Learning Mode** — new LLM concepts or mechanisms. Default to learner-authored implementation or explanation plus strict review.
- **Lesson Mode** — structured teaching for confusing concepts. Attach lesson artifacts to the active Learning Unit.
- **Debugging Mode** — systematic failure analysis inside the active Learning Unit.

When in doubt between Mechanical Mode and Learning Mode, choose Learning Mode.

## Anti-overreach

Prefer hints, targeted questions, tiny examples, and strict review over full solutions when the point is learning.

Agent-authored support is acceptable for mechanical boilerplate. A warning is appropriate when the agent is asked to implement conceptual cores such as tokenization logic, cross-entropy, attention, sampling, checkpoint interpretation, or training loops.

## No hidden magic

Libraries are allowed, but abstraction boundaries must be explicit. When using PyTorch, tokenizer libraries, Hugging Face loaders, Ollama, `llama.cpp`, MLX, or similar tools, document:

- what the tool does;
- what was implemented or inspected manually;
- what is temporarily accepted as a black box;
- why that is acceptable now;
- whether the project should later return to a toy/manual version.

## Learning Review

Before reviewing learner-authored code for a new mechanism, ask the user to record `My Attempt` in the unit's `LEARNING.md`.

Review both code and mental model. Be adversarial in standards and educational in tone. Distinguish "runs" from "understood".

## Learning Unit status updates

Update a unit's `STATUS.md` when state, mode, context health, handoff need, blocker, next action, or resume instructions change.

Keep status lightweight. It is a resume aid, not a workflow engine.

## Go / Python boundary

Keep a Go application/tooling spine where it improves engineering clarity. Introduce Python/PyTorch deliberately where they teach tensors, autograd, neural networks, and ML ecosystem compatibility.

Do not convert the project into Python-first architecture merely because most ML examples online are Python-first.

## Completion rules

A learning experiment is not done until its code runs on tiny hand-debuggable input, instrumentation exposes relevant internals, the user has recorded Before/My Attempt/After, and review has checked both implementation and understanding.

Milestone 0 is Mechanical Mode. It may be agent-authored, but it should remain minimal and should not create a heavy workflow system.
