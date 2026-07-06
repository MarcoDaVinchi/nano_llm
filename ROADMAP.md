# ROADMAP.md

Course roadmap and Learning Unit index for `nano_llm`.

## Current position

Current milestone: **Milestone 0 — Agent-ready repo scaffold**

Status: `review`

Meaning: scaffold artifacts are being created or reviewed. Do not start tokenizer/model work until this milestone is accepted.

## Milestones

| Milestone | Status | Main concept | Notes |
| --- | --- | --- | --- |
| 0. Agent-ready repo scaffold | review | durable learning workflow | Mechanical Mode; agent-authored scaffold is acceptable. |
| 1. Corpus → tokenizer → bigram baseline | planned | first full LM loop | Next step after Milestone 0. |
| 2. Neural foundations | planned | tensors, embeddings, loss, training | May include Python/PyTorch survival kit. |
| 3. Attention and transformer internals | planned | causal self-attention | Start tiny and hand-debuggable. |
| 4. Tiny GPT training | planned | transformer LM training | Include checkpoints and generation. |
| 5. Checkpoints and SafeTensors | planned | model artifact anatomy | Introduce after PyTorch `state_dict`. |
| 6. Sampling and evaluation | planned | decoding behavior | Compare strategies and evals. |
| 7. Compare with local open-weight models | planned | transfer to real models | Use local runtime only when useful. |

## Learning Units

| Unit | Status | Mode | Concept | Depends on | Path |
| --- | --- | --- | --- | --- | --- |
| 001 | planned | Learning | Corpus, tokenizer, bigram baseline | Milestone 0 | `experiments/001-corpus-and-tokenizer/` |
| 002 | planned | Learning | Bigram baseline or neural foundations split | Unit 001 | TBD |
| 002a | optional | Lesson | Python/PyTorch survival kit | When needed | `experiments/002a-python-pytorch-survival-kit/` |

## Side quest policy

If a debugging, teach, or ecosystem topic grows beyond 1–2 iterations, decide whether to:

1. return to the current unit;
2. defer it and add a roadmap note;
3. split it into a separate Learning Unit.

Record dependency, priority, and reason when promoting a side quest.
