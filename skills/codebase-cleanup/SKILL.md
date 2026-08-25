---
name: codebase-cleanup
description: Audit and improve a project's code and documentation for redundancy, inconsistency, convention drift, and stale or conflicting information. Use for broad cleanup or maintainability work that requires a plan before editing; do not use for a narrowly scoped feature or bug fix.
---

# Codebase Cleanup

Audit the project as a coherent whole, propose a complete cleanup plan, and wait for explicit approval before modifying files. Keep behavioral changes visible so the user controls whether they enter the work.

## 1. Establish context

Before judging the code, understand the system it belongs to:

- Read repository instructions, contribution guides, architecture notes, ADRs, and other project-level conventions.
- Map the directory structure, entry points, configuration, core modules, tests, and user-facing documentation. Sample representative modules rather than inferring the whole project from one file.
- Inspect the Git status and diffs. Treat existing staged, unstaged, and untracked files as user work to preserve, not as cleanup material by default.
- Discover the repository's real validation commands from scripts, CI configuration, task runners, and documentation. Record the relevant build, test, type-check, lint, and formatting commands for the plan.

Do not modify files during this phase or the audit.

## 2. Audit

Review code, tests, comments, configuration, and documentation together. Classify findings under four headings:

- **Redundancy**: duplicated logic or explanations, dead code, obsolete compatibility paths, unused dependencies, and abstractions that only relay calls without reducing complexity.
- **Consistency**: equivalent operations using incompatible naming, structure, configuration access, error handling, logging, response shapes, or testing patterns.
- **Conventions**: code that conflicts with documented rules, tool configuration, or the dominant local pattern when no written rule exists.
- **Alignment**: comments, tests, examples, API documentation, setup instructions, or diagrams that describe behavior different from the implementation.

Use evidence, not aesthetics. A finding needs a concrete location and a practical consequence. Similar code is not automatically duplication: confirm that the copies represent the same concept and should evolve together. Confirm that apparently dead code has no runtime, configuration, generated, reflective, or external consumer before proposing deletion.

Prefer authority in this order: explicit project decisions, executable configuration and tests, dominant local patterns, then broadly applicable engineering practice. If two sources disagree, report the conflict instead of silently choosing one.

## 3. Present the plan

Present the complete audit before editing. Keep findings compact and use this shape:

| Field | Content |
| --- | --- |
| Location | Files, symbols, documentation sections, or configuration keys involved |
| Evidence | The specific duplication, mismatch, broken reference, or conflicting pattern |
| Impact | Why it affects maintainability, correctness, operability, or comprehension |
| Proposed change | The smallest coherent correction |
| Behavior risk | `None expected`, `Possible`, or `Intentional`, with an explanation when not none |
| Verification | Tests, checks, searches, or manual observations that demonstrate the result |

Label each finding as `cleanup`, `bug fix`, `documentation correction`, or `behavior change`. Prioritize by impact and confidence, then organize execution into dependency-aware batches that can be reviewed and verified independently.

For large projects, include every meaningful finding but keep speculative or low-confidence items separate from recommended work. Do not inflate the plan with formatting preferences already enforced by tooling.

After presenting the audit and batches, stop. Do not edit until the user explicitly approves all or selected items.

## 4. Execute approved batches

Implement only the approved findings. Keep code, tests, comments, examples, configuration, and documentation synchronized when they describe the same behavior.

Complete one approved batch at a time. Avoid opportunistic refactors outside the plan. If implementation reveals that an item is materially larger, riskier, or behavior-changing compared with the approved proposal, stop that item and return the decision to the user.

## 5. Verify and report

Run the targeted checks for each batch, then the broader repository checks justified by the change. Reinspect the final diff for accidental scope expansion, stale references, weakened tests, and modifications to unrelated user work.

Report:

- completed findings and affected areas;
- validation commands and results;
- approved items that were skipped or changed from the plan;
- remaining risks, follow-up candidates, and checks that could not be run.

Do not commit or push unless the user separately requests those actions.
