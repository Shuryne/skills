---
name: codebase-conventions
description: Reviews and improves naming, repository layout, comments, and documentation using project conventions. Use when names or file locations are misleading, comparable modules follow conflicting conventions, or comments and documentation have drifted from the code.
---

# Codebase Conventions

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

1. Read the applicable project guidance and compare modules with similar responsibilities. Use established patterns where written rules are absent. Allow differences supported by distinct responsibilities or toolchain requirements. Surface unresolved conflicts in the project's conventions.
2. For each finding, identify the location, the applicable convention or evidence, the concrete navigation or maintenance problem, and the proposed change. Present a plan for approval before editing when the request involves broad cleanup across modules.
3. Preserve intended behavior and public contracts unless the user requests a change. Verify affected imports, entry points, command examples, and documentation links, then run the relevant project checks.
