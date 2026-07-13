# Workflow dependency and migration-surface audit

Date: 2026-07-13  
Wayfinder ticket: [Audit workflow dependencies and migration surfaces](https://github.com/MarcoDaVinchi/nano_llm/issues/2)

## Question

Which active instructions, documents, templates, links, terms, historical artifacts, and installed Matt skills must be preserved, migrated, retired, or left untouched to reach the [Migrate nano_llm to a Matt-native learning workflow](https://github.com/MarcoDaVinchi/nano_llm/issues/1) destination?

## Method and baseline

This audit used the current working tree, git history, the root operating documents, all repository Markdown files, `docs/agents/`, the installed skill definitions under `/Users/mag/.agents/skills/`, the GitHub map and its native child/dependency metadata, and `gh auth status`.

The working-tree baseline matters:

- `main` and `origin/main` both point to `80d7821` (`chore: add agent-ready learning scaffold`).
- `AGENTS.md`, `ROADMAP.md`, and `MEMORY.md` already contain local uncommitted changes.
- `docs/agents/` is already present locally but untracked.
- Those local changes predate this audit and must be preserved rather than overwritten by migration execution.
- Unit 001 is `planned` but its directory does not exist, so there is currently no active Learning Unit and no unit-local `STATUS.md`, `LEARNING.md`, or `HANDOFF.md` to update.

This is a workflow audit, not migration execution. It does not move historical files, rewrite routing, alter templates, or activate Learning Unit 001.

## Findings

1. **There is no active Superpowers installation to remove.** `/Users/mag/.codex/superpowers` and `/Users/mag/.agents/skills/superpowers` are absent, and no Superpowers-named plugin cache entry was found. The remaining migration is repository policy, naming, and routing.
2. **The only active direct link to the tool-named design is in `README.md`.** The two files under `docs/superpowers/` are still tracked and readable, but one is a superseded startup design and the other is a completed plan with an obsolete imperative to invoke Superpowers skills.
3. **The learning workflow is already deeper than any one installed skill.** `AGENTS.md`, `ROADMAP.md`, `CONTEXT.md`, per-unit artifacts, and templates jointly define learner authorship, checkpoints, fresh-context recovery, attached Lesson/Debugging modes, and completion. Generic Matt skills should route work around this system, not replace it.
4. **The Matt suite covers the generic engineering flow well.** It has tools for grilling, domain modeling, wayfinding, research, prototypes, specs, tickets, triage, implementation, TDD, debugging, review, teaching, and handoff.
5. **Two nano_llm mechanisms are intentionally project-specific:** Learning Unit progression and Learning Review of both code and mental model. Generic `implement`/`review` flows do not establish learner understanding and therefore cannot become completion authority.
6. **Installed skills need adapters, not blind invocation.** Several assume `docs/adr/`, temporary handoff files, a standalone teaching workspace, or an autonomous implement/review/commit flow. nano_llm instead uses `docs/decisions/`, unit-local artifacts, attached teaching/debugging, and learner-authored conceptual cores.
7. **Global skill behavior is not pinned by the repository.** `/Users/mag/.agents/skills/` lives outside the repo and contains overlapping aliases/versions such as `review`/`code-review` and `diagnose`/`diagnosing-bugs`. Durable invariants must remain in repository artifacts.
8. **No new ticket is exposed by the audit.** The remaining gaps are already owned by the map's routing, documentation taxonomy, lifecycle, Project integration, acceptance, execution, and validation tickets. Whether a small project-specific orchestration skill is useful remains fog until routing and lifecycle are defined.

## Repository inventory

### Preserve as active sources of truth

| Surface | Current role | Required treatment |
| --- | --- | --- |
| `AGENTS.md` | Prime directive, boot protocol, task modes, anti-overreach, No Hidden Magic, Learning Review, status discipline, Go/Python boundary, completion rules | Preserve all pedagogical rules. Extend only the `Agent skills` area with explicit Matt routing after [Define Matt skill routing for nano_llm modes](https://github.com/MarcoDaVinchi/nano_llm/issues/3) resolves. |
| `ROADMAP.md` | Course-level current position and Learning Unit index | Preserve as learning-state authority. Never replace it with issues or Project Status. Incorporate the existing local Milestone 1 changes. |
| `CONTEXT.md` | Canonical project glossary | Preserve as the single domain glossary. Matt domain-modeling work must update it rather than create competing vocabulary. |
| `MEMORY.md` | Human-readable durable notes that complement git and unit artifacts | Preserve. Its startup-spec commit reference is historical provenance, not an active workflow dependency. Incorporate the existing local Milestone 0 acceptance note. |
| `docs/experiments.md` | Lightweight Learning Unit conventions | Preserve; align wording only after the lifecycle ticket decides the exact creation/progression process. |
| `templates/LEARNING.md` | Before/My Attempt/During/After journal | Preserve learner-authored sections. Structural changes, if any, belong to [Define the Learning Unit lifecycle under the Matt workflow](https://github.com/MarcoDaVinchi/nano_llm/issues/5). |
| `templates/STATUS.md` | Resume state, mode, context health, blockers, and next action | Preserve lightweight status discipline. Do not turn it into a tracker or board mirror. |
| `templates/HANDOFF.md` | Optional extra recovery context | Preserve as the project-specific handoff shape; generic handoff skills must point back to canonical artifacts rather than duplicate them. |
| `docs/agents/domain.md` | Single-context domain-doc consumer rules | Preserve the local untracked setup output. Reconcile its `docs/decisions/` convention with installed skills that hardcode or search `docs/adr/`; do not allow a second decision store to appear. |
| `docs/agents/issue-tracker.md` | GitHub Issues and Wayfinder operations | Preserve the local untracked setup output. Extend it later with the Project owner/number and interaction rules decided by [Define GitHub Project board integration and agent interaction semantics](https://github.com/MarcoDaVinchi/nano_llm/issues/10). |
| `docs/agents/triage-labels.md` | Five canonical triage-role mappings | Preserve the local untracked setup output. These labels govern engineering intake, not learner progress. |
| `docs/decisions/` | Home for meaningful hard-to-reverse decisions | Preserve. It is empty today; do not create ADRs merely to restate ordinary workflow instructions. |

### Migrate or refresh

| Surface | Evidence | Required treatment |
| --- | --- | --- |
| `README.md` current stage | Still says Milestone 0 is current, while the working `ROADMAP.md` says Milestone 1 planning | Refresh from `ROADMAP.md`; keep `ROADMAP.md` authoritative rather than duplicating detailed state. |
| `README.md` “Canonical spec” link | Directly names `docs/superpowers/specs/...` as canonical | Remove canonical authority. Link active operating artifacts and, if useful, link the renamed historical design explicitly as history. |
| `experiments/README.md` | Describes Unit 001 as planned and says to use templates, but does not yet express the final lifecycle | Refresh when Unit 001 is scaffolded/activated; do not pre-implement tokenizer behavior. |
| `AGENTS.md` `Agent skills` block | Configures tracker, labels, and domain docs but does not route work by nano_llm mode or work shape | Add exact routing only after the dedicated HITL decision. Preserve explicit user invocation and project policy precedence. |
| `docs/agents/issue-tracker.md` | Covers issues, claims, close, sub-issues, and dependencies but not GitHub Project behavior | Add Project semantics only after the dedicated board ticket. Issues/dependencies/assignee remain authoritative. |
| `make verify` / `scripts/verify_markdown.py` | Currently validates Markdown tabs and balanced fences across the repo | Keep the lightweight check. Whether migration needs a separate focused check belongs to [Define migration acceptance criteria and verification](https://github.com/MarcoDaVinchi/nano_llm/issues/6). |

### Retire from active authority, preserve as neutral history

| Surface | Why it is not active | Required treatment |
| --- | --- | --- |
| `docs/superpowers/specs/2026-07-03-nano-llm-lab-design.md` | Its durable content has been promoted into `AGENTS.md`, `ROADMAP.md`, `CONTEXT.md`, templates, and supporting docs; its path and repository-layout examples retain tool-specific naming | Move to a neutral historical design path chosen by [Define neutral documentation taxonomy and history policy](https://github.com/MarcoDaVinchi/nano_llm/issues/4). Mark it historical, superseded, and non-canonical. Preserve provenance and useful rationale. |
| `docs/superpowers/plans/2026-07-06-milestone-0-agent-ready-scaffold.md` | Milestone 0 is complete, yet every checkbox is open and the header requires `superpowers:subagent-driven-development` or `superpowers:executing-plans` | Move to neutral plan history, mark completed/non-executable, and remove or visibly neutralize the obsolete execution directive. Do not treat unchecked boxes as live work. |
| The terms “canonical startup spec” and “Superpowers execution skill” | They imply active authority or runtime availability that no longer exists | Retain only where needed to explain history; do not use them in current instructions or resume paths. |

### Leave untouched unless another ticket explicitly needs them

- `Makefile`, `scripts/verify_markdown.py`, `.gitignore`, and placeholder code/data/model directories have no active Superpowers dependency.
- `docs/glossary.md` correctly points to `CONTEXT.md`; it does not duplicate the glossary.
- `cmd/`, `internal/`, `python/`, `data/`, and `models/` are future implementation surfaces, not workflow-migration targets.
- Git history and the startup-design commit references remain provenance; do not rewrite history.
- Personal/global skill installations unrelated to the project are outside this repository migration.

## Canonical terms that must survive migration

The migration must preserve the meanings in `CONTEXT.md`, especially these groups:

- **Learner agency:** Learning Checkpoint, Learner-Authored Implementation, Anti-Overreach Rule, Attempt Record, Explanation Is Not Completion, Agent-Authored Support.
- **Learning state:** Learning Unit, Learning Journal, Unit Status, Context Health, Handoff Needed, Learning Unit Index, Lightweight Status Discipline.
- **Modes and attachment:** Mechanical Mode, Learning Mode, Lesson Mode, Debugging Mode, Attached Lesson Mode, Attached Debugging Mode, Side Quest Promotion.
- **Understanding and observability:** No Hidden Magic, Learning Review, Small Enough to Debug by Hand, Scale-Up Ladder, Instrumentation, Learning Experiment Done, Milestone Complete.
- **Engineering boundary:** Concept vs Boilerplate, LLM Development Ecosystem, Go/Python Boundary, Go-First Spine, Naive Reimplementation, Reimplementation for Learning.

Matt workflow terms such as issue, ticket, spec, triage role, map, and implementation flow must not redefine those learning terms. In particular:

- a closed engineering issue is not a passed Learning Checkpoint;
- `review`/`code-review` is not automatically a nano_llm Learning Review;
- Project Status is not Unit Status;
- a `teach` workspace is not a Learning Unit unless its artifacts are attached to the active unit;
- a generated spec or ticket set is not routine lesson content.

## Installed skill inventory

The migration should change repository routing, not install, uninstall, fork, or edit global skills.

### Core Matt flow: preserve installed, route deliberately

| Skill or family | What it covers | Audit classification |
| --- | --- | --- |
| `ask-matt` | Router over the generic Matt flow | Preserve installed. Optional fallback when explicit project routing does not answer the work shape; it must not override `AGENTS.md`. |
| `grilling`, `grill-with-docs`, `grill-me` | One-question-at-a-time HITL design exploration; repo-aware wrapper adds domain docs | Preserve installed. Repository decisions normally need the repo-aware path; exact wrapper/primitive wording belongs to the routing ticket. |
| `domain-modeling`, `ubiquitous-language` | Sharpen terminology and record domain language/decisions | Preserve installed. `domain-modeling` fits active `CONTEXT.md`; avoid introducing a competing `UBIQUITOUS_LANGUAGE.md` without an explicit decision. |
| `wayfinder` | Multi-session fog-clearing map over tracker tickets | Preserve installed and keep the GitHub conventions already configured. It plans/decides by default; this map explicitly permits execution. |
| `research` | Primary-source investigation recorded as a Markdown asset | Preserve installed. Fits AFK investigation tickets such as this audit. |
| `prototype` | Throwaway concrete artifact for a HITL design question | Preserve installed. Prototype code is evidence for a decision, not destination code or learner completion. |
| `to-spec` | Synthesize requirements already discussed into a tracker spec without another interview | Preserve installed. Use only for learning-system or engineering work, not every Learning Unit. |
| `to-tickets` | Split a spec/plan into dependency-aware tracer-bullet tickets | Preserve installed. Do not turn routine learning progression into an issue graph. |
| `triage`, `qa` | Process incoming reports and create/shape engineering issues | Preserve installed. Their configured labels are engineering roles, not unit states. |
| `implement`, `tdd` | Execute specified engineering work test-first | Preserve installed. `implement` assumes a TDD/review/commit flow; project anti-overreach and learner-authored rules take precedence for conceptual LLM mechanisms. |
| `diagnose`, `diagnosing-bugs` | Systematic bug diagnosis and regression testing | Preserve installed. Route non-trivial unit failures into Attached Debugging Mode; choose the canonical name in the routing ticket. |
| `review`, `code-review` | Standards/spec review of a diff from a fixed point | Preserve installed. Useful for engineering review, but insufficient by itself for Learning Review; choose the canonical name in the routing ticket. |
| `teach` | Stateful, multi-session concept teaching rooted at the current directory | Preserve installed as optional Attached Lesson Mode, never the default advancement path. Running it at repository root would create a parallel course workspace; it must be rooted in or linked from the active unit. |
| `handoff`, `claude-handoff` | Temporary Markdown context bridge versus direct fresh-agent handoff | Preserve installed. Generic `handoff` writes outside the durable unit by default; the repository's optional unit `HANDOFF.md`, `STATUS.md` update, and boot protocol remain authoritative. Exact choice belongs to routing. |
| `codebase-design`, `design-an-interface`, `improve-codebase-architecture` | Deep-module vocabulary, alternative interfaces, and architecture surveys | Preserve installed as optional engineering tools. They do not replace learning architecture or domain language. |

### One-time or situational Matt skills: leave installed, do not add default routing now

- `setup-matt-pocock-skills` has already produced the local `AGENTS.md`/`docs/agents/` setup. Re-run only when deliberately changing tracker, label vocabulary, or domain-doc layout.
- `request-refactor-plan` is relevant only for an explicit refactor-planning request.
- `scaffold-exercises` assumes a different TypeScript course layout and linter; it is not the Learning Unit scaffolder for nano_llm.
- `zoom-out`, writing skills, `write-a-skill`, and other narrowly triggered skills may remain available globally but need no project-default route.
- Browser, Azure/Foundry, Obsidian, Vercel, article editing, TypeScript migration/setup, and similar unrelated installed skills are outside the migration scope.

The installed aliases are not guaranteed to be identical: `implement` explicitly invokes `code-review`, while `review` is a separate installed definition; `diagnose` and `diagnosing-bugs` also differ. The routing decision must name the intended canonical entry points rather than treating aliases as interchangeable.

## Workflow coverage matrix

| Work shape | Current nano_llm authority | Matt coverage | Fit and remaining boundary | Owning follow-up |
| --- | --- | --- | --- | --- |
| Recover fresh context | `AGENTS.md` boot protocol; `ROADMAP.md`; active unit `README.md`/`STATUS.md`/`LEARNING.md`; optional `HANDOFF.md` | `handoff` can bridge sessions | Partial. The repository artifacts, not a temporary generic handoff, decide current learning state. There is no active unit yet. | [Define the Learning Unit lifecycle under the Matt workflow](https://github.com/MarcoDaVinchi/nano_llm/issues/5) and later validation |
| Classify Mechanical/Learning/Lesson/Debugging work | `AGENTS.md` and `CONTEXT.md` | `ask-matt` routes generic work shapes | Partial. Project mode and anti-overreach take precedence. | [Define Matt skill routing for nano_llm modes](https://github.com/MarcoDaVinchi/nano_llm/issues/3) |
| Resolve a repo-backed design decision | `CONTEXT.md`, relevant decisions, user as decision-maker | `grill-with-docs` + `grilling` + `domain-modeling` | Strong fit when HITL; facts should be read from the repo rather than asked. | Routing ticket |
| Navigate a huge foggy effort | GitHub issue tracker conventions | `wayfinder` | Strong fit; map, child issues, native dependencies, assignee claims, and close semantics are already working. | Current map; Project visualization ticket for board behavior |
| Research an external/local fact | Repository Markdown asset | `research` | Strong fit. Background research must use primary sources and link the asset. | Routing ticket |
| Test a design through a throwaway artifact | Decision discussion | `prototype` | Strong fit, but it is HITL and the artifact is not production or learner-completion evidence. | Routing ticket |
| Synthesize discussed requirements | Issues for bounded engineering/system changes | `to-spec` | Strong fit only after requirements are already discussed; not an interview and not routine unit content. | Routing ticket |
| Decompose a multi-session build | Engineering issue graph | `to-tickets` | Strong fit for implementation work; inappropriate for ordinary learning progress. | Routing ticket |
| Process incoming bugs/requests | GitHub Issues + triage labels | `triage`, `qa` | Strong fit for external engineering intake; generated Wayfinder/to-tickets work should not be re-triaged. | Routing ticket and Project visualization ticket |
| Implement mechanical/support work | Code/spec/ticket plus project rules | `implement` + `tdd` + `code-review` | Strong for engineering work. Partial for conceptual LLM work because the learner must author/understand the key mechanism. | Routing ticket |
| Diagnose a failing experiment | Active unit `STATUS.md` and optional `debug/` artifacts | `diagnose` / `diagnosing-bugs` | Strong method, partial state integration: the generic loop does not update unit artifacts; enter Attached Debugging Mode and return or split explicitly. | Routing and lifecycle tickets |
| Teach a confusing concept | Active unit and Attached Lesson Mode | `teach` | Partial. Useful only when attached to the unit; explanation alone is not completion. | Routing and lifecycle tickets |
| Review engineering changes | Project standards/spec | `review` / `code-review` | Strong for diff review. | Routing ticket |
| Review learner understanding | `LEARNING.md` My Attempt + code + mental-model questions + instrumentation | No exact generic equivalent | Intentional project-specific mechanism. Generic code review may contribute but cannot certify understanding. | Lifecycle ticket; no new skill ticket yet |
| Create/activate/progress a Learning Unit | `ROADMAP.md`, templates, per-unit artifacts | No exact generic equivalent | Intentional project-specific lifecycle, not an issue workflow. | Lifecycle ticket, then Unit 001 scaffold/validation |
| Visualize engineering work on a board | Issues, native dependencies, assignee claims | No dedicated Matt skill; GitHub CLI/Project behavior | Project may visualize but must not become authority for learning state or claims. Current token has `repo` but lacks `project` scope. | [Define GitHub Project board integration and agent interaction semantics](https://github.com/MarcoDaVinchi/nano_llm/issues/10) |
| Verify the migration | `make verify`, repository inspection, fresh-context exercise | Generic implementation/review tools only | Acceptance must define checks for stale links, history labels, routing, tracker config, and recovery behavior. | [Define migration acceptance criteria and verification](https://github.com/MarcoDaVinchi/nano_llm/issues/6) |

## Non-obvious migration risks

1. **Decision-store split:** the repository config says `docs/decisions/`, while several installed skills expect `docs/adr/`. Routing or execution must adapt the skills to the configured path instead of silently creating a second store or skipping decisions.
2. **Autonomous implementation drift:** unqualified `implement` may test, review, commit, and close specified work. For a conceptual LLM core that would bypass learner authorship even if the resulting code is correct.
3. **Detached state:** generic `handoff`, `teach`, and diagnosis flows do not automatically update the active unit's durable state. They must be wrapped by the unit lifecycle.
4. **Dual state machines:** issue labels/frontier/closure coordinate engineering work; `ROADMAP.md` and unit status/journal record learning continuity and completion. Neither state may imply the other.
5. **Unpinned global behavior:** future global skill updates can change workflow assumptions without a repository diff. Keep the invariants and adapters in `AGENTS.md` and `docs/agents/`, and verify behavior in a fresh context.
6. **Stale authority:** `README.md` still reports Milestone 0 while `ROADMAP.md` reports Milestone 1 planning. The old design also proposes an older unit split. Current state must always come from `ROADMAP.md`.
7. **Tracker automation detail:** `docs/agents/issue-tracker.md` records the semantic operations but not every GitHub API identifier/fallback detail. Acceptance should test actual sub-issue/dependency/frontier operations rather than assuming the prose is executable automation.

## Migration ownership and boundaries

The audit leaves each change in exactly one existing map ticket:

- [Define Matt skill routing for nano_llm modes](https://github.com/MarcoDaVinchi/nano_llm/issues/3) owns canonical skill names, selection boundaries, explicit invocation, fallbacks, and project-policy precedence.
- [Define neutral documentation taxonomy and history policy](https://github.com/MarcoDaVinchi/nano_llm/issues/4) owns final neutral paths and history markers.
- [Define the Learning Unit lifecycle under the Matt workflow](https://github.com/MarcoDaVinchi/nano_llm/issues/5) owns unit creation, activation, progression, status updates, and any template changes.
- [Define GitHub Project board integration and agent interaction semantics](https://github.com/MarcoDaVinchi/nano_llm/issues/10) owns Project identity, import/auto-add, Status automation, assignee semantics, agent behavior, OAuth scope, and documentation.
- [Define migration acceptance criteria and verification](https://github.com/MarcoDaVinchi/nano_llm/issues/6) owns executable checks and fresh-context acceptance.
- [Execute the repository workflow migration](https://github.com/MarcoDaVinchi/nano_llm/issues/7) applies the decided moves and edits while preserving the pre-existing local working-tree changes.
- [Scaffold and activate Learning Unit 001](https://github.com/MarcoDaVinchi/nano_llm/issues/8) and [Validate fresh-context recovery and learner progression](https://github.com/MarcoDaVinchi/nano_llm/issues/9) prove the migrated lifecycle without implementing tokenizer logic.

## Conclusion

The route is a documentation-and-routing migration, not a plugin migration. Preserve the nano_llm learning system as the governing layer, route generic engineering work through the installed Matt skills, retire tool-named historical artifacts from active authority without deleting provenance, and keep issues/Projects separate from learner state.

The installed suite has sufficient generic coverage to continue the map. The only uncovered behaviors are deliberately nano_llm-specific and already have lifecycle/routing tickets, so this audit does not justify a new ticket or a project-specific skill yet.
