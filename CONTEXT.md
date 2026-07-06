# Nano LLM Lab

Nano LLM Lab is a learning laboratory for building small, observable language-modeling mechanisms in order to understand larger LLMs.

## Language

**Learning Checkpoint**:
A required pause where the user demonstrates understanding of a newly introduced LLM mechanism before the project treats that mechanism as complete.
_Avoid_: completion checkbox, implementation milestone, agent review

**Learner-Authored Implementation**:
The preferred default for new LLM mechanisms: the user writes or explains the key mechanism, while the agent reviews it strictly and helps correct misunderstandings. This is a guardrail against agent overreach, not a ban on pragmatic agent-authored support code.
_Avoid_: passive review, unnoticed agent-completed lesson

**Mechanical Mode**:
A task mode for scaffolding, file layout, plumbing, git, Makefile, and similar work that introduces no new LLM mechanism.
_Avoid_: learning task, concept implementation

**Learning Mode**:
The default task mode for new LLM concepts: the user predicts behavior, writes the first small implementation, and learns through strict agent review and joint correction.
_Avoid_: passive implementation, agent-completed mechanism

**Lesson Mode**:
An optional task mode for confusing or explicitly requested teaching sessions that may produce structured lessons, references, quizzes, resources, or learning records.
_Avoid_: normal implementation, mechanical scaffolding

**No Hidden Magic**:
A project rule that high-level tools may be used only when their abstraction boundary is explicit: what they do, what was learned manually, what remains a black box, and why that is acceptable.
_Avoid_: black-box success, library-driven understanding

**Learning Journal**:
A per-experiment `LEARNING.md` file where the user records predictions, surprises, explanations, remaining confusion, and revisit items.
_Avoid_: agent memory, implementation log, README

**Anti-Overreach Rule**:
A project rule that agents should avoid silently taking over learning work; agents should prefer hints, counterexamples, small checks, and review questions unless the user explicitly asks for direct help.
_Avoid_: unnoticed agent-completed lesson, answer dump

**Attempt Record**:
The `My Attempt` section in an experiment's `LEARNING.md` where the user records what they tried, why, and what they are unsure about before agent review.
_Avoid_: code-only review, post-hoc explanation

**Learning Review**:
A strict but educational review of learner-authored code and reasoning that checks correctness, edge cases, hidden misunderstandings, and whether the mechanism is actually understood.
_Avoid_: approval review, code-only review, rewrite service

**Small Enough to Debug by Hand**:
A rule that each new mechanism starts with data, tensors, or code small enough for the user to manually trace before scaling up or automating.
_Avoid_: first-pass automation, too-large toy example

**Scale-Up Ladder**:
The progression for learning a mechanism: hand-trace example, minimal learner-authored code, instrumented experiment, library comparison, then scaled version.
_Avoid_: jump to full implementation, premature scaling

**Instrumentation**:
Small, readable outputs that expose the internal state of an experiment, such as tokens, shapes, logits, probabilities, attention weights, gradients, losses, sampling candidates, or checkpoint tensors.
_Avoid_: opaque success output, logging framework

**Learning Experiment Done**:
A completion standard for experiments requiring README purpose/commands, hand-debuggable input, instrumentation, user `LEARNING.md` entries, Learning Review, No Hidden Magic notes when relevant, and an explicit next scale-up step or deferral.
_Avoid_: runnable only, code complete

**Milestone Complete**:
A milestone state reached only when deliverables exist, user learning checkpoints are passed, included experiments meet Learning Experiment Done, and any skipped learning steps are explicitly recorded.
_Avoid_: code complete, tests pass only, runnable milestone

**Learning Unit**:
A resumable lesson/experiment in the repository, usually an `experiments/00X-*` directory, that can span multiple sessions and contains README, STATUS, LEARNING, code/data, and optional HANDOFF artifacts.
_Avoid_: teach lesson, one-shot task, chat-only lesson

**Unit Status**:
The `STATUS.md` file inside a Learning Unit that records state, mode, current step, next action, blockers, progress, mode transitions, and fresh-context resume instructions.
_Avoid_: chat state, hidden progress, stale todo list

**Context Health**:
A `STATUS.md` field describing whether the current working context is fresh, stable, long, compacted, or stale for the active Learning Unit.
_Avoid_: implicit chat freshness

**Handoff Needed**:
A `STATUS.md` field indicating whether the active Learning Unit needs a `HANDOFF.md` update before another agent or fresh context can safely continue.
_Avoid_: assumed continuity

**Learning Unit Index**:
The course-level table in `ROADMAP.md` that lists Learning Units, their status, mode, concept, dependencies, and the current active unit.
_Avoid_: hidden course state, chat roadmap

**Attached Lesson Mode**:
A Lesson Mode rule that structured `teach` artifacts must be linked to or stored under the active Learning Unit rather than becoming a parallel course system.
_Avoid_: detached teach session, parallel lesson tree

**Attached Debugging Mode**:
A Debugging Mode rule that non-trivial debugging work stays attached to the active Learning Unit through `STATUS.md` and optional `debug/` artifacts such as REPRO, HYPOTHESES, and FINDINGS.
_Avoid_: detached debugging chat, disposable failure analysis

**Lightweight Status Discipline**:
A rule that `STATUS.md` exists only for fresh-context recovery and learning continuity, recording meaningful transitions without becoming a workflow engine or bureaucracy.
_Avoid_: workflow engine, issue tracker, micro-transition log

**Side Quest Promotion**:
A lightweight rule for turning a growing Lesson, Debugging, or deep-dive branch into a deferred or current Learning Unit in `ROADMAP.md`, with dependency, priority, reason, and links from the current unit.
_Avoid_: lost tangent, course derailment

**Canonical Interaction Pattern**:
The default user-agent workflow for Learning Mode: hybrid learner-authored work by default, guided pair learning for complex topics, and a stricter prediction/attempt/review/after cycle for important checkpoints.
_Avoid_: agent-led implementation, passive user review

**Explanation Is Not Completion**:
A rule that direct agent explanations are allowed on request but do not replace learner attempts, Learning Review, Learning Journal entries, or checkpoints.
_Avoid_: explained therefore done

**Agent-Authored Support**:
Code, explanation, or finishing work written by the agent at the user's request; allowed when useful, but should be labelled with a warning when it may bypass learner understanding of the key mechanism.
_Avoid_: silent lesson completion, hidden agent overreach

**Concept vs Boilerplate**:
The boundary used for anti-overreach warnings: conceptual LLM mechanisms need learner attention, while mechanical support code can usually be agent-authored unless repeated ecosystem work becomes a learning opportunity.
_Avoid_: warning on every helper task, ignoring ecosystem learning

**LLM Development Ecosystem**:
The practical tooling and conventions around LLM work, including Python, PyTorch, data loading, project structure, checkpoint formats, Hugging Face-style model layouts, local inference runtimes, and evaluation harnesses.
_Avoid_: model internals only, production platform

**External Check-Off**:
A lightweight way to mark a recommended topic as already familiar enough without running a full Learning Unit, while still recording that it was considered.
_Avoid_: forced lesson, assumed knowledge

**Go/Python Boundary**:
The project boundary where Go provides the application/tooling spine and Python/PyTorch is introduced where it best teaches tensors, autograd, neural networks, and ML ecosystem compatibility.
_Avoid_: Python by default, Go-only constraint

**Go-First Spine**:
The project's preference to keep application, CLI, orchestration, and tooling structure in Go where it improves clarity, instead of becoming Python-first only because ML examples commonly use Python.
_Avoid_: Python-first drift, Go-only constraint

**Naive Reimplementation**:
A deliberately small, observable reimplementation of an established tool or algorithm used for learning and deeper understanding, not for production superiority.
_Avoid_: production replacement, clever rewrite

**Reimplementation for Learning**:
A small, observable rebuild of a mature mechanism to understand it; distinct from trying to replace mature tools as production infrastructure.
_Avoid_: production reinvention, library replacement

