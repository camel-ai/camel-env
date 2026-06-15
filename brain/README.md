# 🧠 Brain

The project's durable, long-term memory. The root [CLAUDE.md](../CLAUDE.md) is a
thin pointer; everything that should survive across sessions lives here.

This is not just documentation — it is the mechanism by which the repo and the AI
tool **co-evolve** (an explicit design aim, see [architecture.md](architecture.md)).
The code changes; the brain records *why*, *how we work*, and *what we learned*,
so the next session starts where the last one ended.

## Read order

1. **[workflow.md](workflow.md)** — how Claude operates here: the change loop,
   how to save changes, and how/when to update this brain. **Read this first.**
2. [conventions.md](conventions.md) — code & repo conventions, do / don't.
3. [architecture.md](architecture.md) — system design and module map.
4. [glossary.md](glossary.md) — domain vocabulary.

## Living records (append-only, grow over time)

- [decisions.md](decisions.md) — ADR-style log of design decisions and their *why*.
- [journal.md](journal.md) — changelog of notable changes, dated.
- [open-questions.md](open-questions.md) — known unknowns and the backlog for the brain to resolve.

## The one rule

If you learn something durable, or make a decision, or change how the project
works — **update the brain in the same change**. A change that isn't recorded
didn't happen, as far as the next session is concerned. See
[workflow.md](workflow.md#updating-the-brain).
