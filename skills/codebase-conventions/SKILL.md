---
name: codebase-conventions
description: Reviews and improves naming, repository layout, comments, and documentation using project conventions. Use when names or file locations are misleading, comparable modules follow conflicting conventions, or comments and documentation have drifted from the code.
---

# Codebase Conventions

## Scope

When this skill is invoked, use the three areas below as the review criteria. A general request such as "review the whole codebase" means a conventions review of the current repository. Honor any target or narrower focus the user specifies.

Trace runtime behavior to verify a specific convention problem. Keep a finding when correcting a name, file placement, comment, or documentation would address the problem while preserving intended behavior. For example, flag help that describes a command as read-only when it is intended to write files. An implementation defect that violates a correctly stated contract belongs to a correctness review.

## Naming Conventions

- Use established domain terms for the same concept across files, directories, code, commands, and documentation. Follow the project's naming patterns for comparable items.
- Name files and directories for their contents or responsibility. Name functions for their operation and variables for their meaning. Include units or scope where ambiguity matters, as in `timeout_ms`.
- Trace a misleading script or command name to its entry point. Use consistent verbs and make consequential side effects clear in the name or help text. Distinguish read-only checks from fixes that write files, for example with separate `check` and `fix` commands. Check callers before changing a shared or public name.

## Repository Layout

- Place each file where a maintainer would look for its owner. Keep implementation, feature-specific tests, and supporting files near the feature or module they serve when the toolchain permits it.
- Keep single-owner code with its owner. Move it to a shared location once multiple modules use it and that location has a clear responsibility.
- Add a directory when it establishes a distinct responsibility or solves a concrete navigation problem. Before moving files, trace imports, build rules, test discovery, script references, and any public paths that depend on their locations.

## Comments and Documentation

- Express behavior through names, code, and configuration. Keep inline comments for intent, constraints, and exceptions that a reader cannot readily infer. Document public interfaces with the usage and guarantees callers need.
- Keep each maintained fact in one authoritative location and link to it from other places. Keep documentation focused on the reader's task, prerequisites, and relevant decisions. Verify stale paths, commands, and defaults against their actual definitions before updating or removing them.
- Update affected comments, examples, and documentation in the same change as the code, configuration, or commands they describe. If the implementation conflicts with a documented contract, establish the intended behavior before changing either.

## Workflow

### 1. Establish the review context

Identify the scope and the revision or working tree under review. Read the applicable project guidance and locate relevant modules, entry points, and documentation. Compare modules with similar responsibilities. Use established patterns where written rules are absent, and allow differences supported by distinct responsibilities or toolchain requirements.

### 2. Review each area

Use one agent to review the areas in order by default. When the user explicitly requests parallel review and subagents are available, run one independent read-only reviewer per area concurrently. Give each reviewer the same scope, project guidance, and reporting requirements.

For each area, note what was checked. For each finding, provide the file and line, the applicable convention or verifiable evidence, the concrete impact on navigation, understanding, or maintenance, and the smallest correction that addresses it.

### 3. Verify and report

Collect all review results, verify the evidence with focused checks, and merge findings that describe the same issue. Check each proposed correction against Scope before including the finding. Use one report section per applicable review area. In each section, state what was checked, list verified findings, and surface any unresolved convention or contract conflicts.

For review-only requests, deliver the report. When asked to make changes, present a plan for approval before broad edits across modules. Preserve intended behavior and public contracts unless the user requests a change. After editing, verify affected imports, entry points, command examples, and documentation links, then run the relevant project checks.
