# Workflow — how Claude works in this repo

This is the operating contract. It describes the behavior expected when making
changes and, crucially, how those changes are **saved** and how the brain
**co-evolves** with the code.

## The change loop

Every non-trivial task follows: **Orient → Change → Verify → Record.**

### 1. Orient (before touching code)
- Read the brain files relevant to the task — at minimum
  [conventions.md](conventions.md) and the relevant part of
  [architecture.md](architecture.md).
- Read the actual code/config you're about to change. Don't assume; the brain
  records intent, the code is ground truth. If they disagree, that's a finding —
  note it (see [open-questions.md](open-questions.md)).

### 2. Change
- Keep changes small and focused; one logical change at a time.
- Match the conventions in [conventions.md](conventions.md) and the style of
  surrounding code.
- Respect the module boundaries in [architecture.md](architecture.md) — put code
  where it belongs (e.g. a reward function goes in `verifiers/`, not `utils/`).

### 3. Verify
- Run the relevant tests / linters before considering the change done. If none
  exist yet for the area, say so plainly rather than implying it was tested.
- Report outcomes faithfully: failing tests are reported with their output;
  skipped steps are stated as skipped.

### 4. Record (this is what makes the brain work)
- Update the brain **in the same change** — see [Updating the brain](#updating-the-brain).
- Then save the change — see [Saving changes](#saving-changes).

## Saving changes

- **Never commit on `main` directly.** Branch first. `main` is the default/PR base.
- **Only commit or push when the user asks.** Making edits ≠ committing them.
- Git identity in this repo: `Michaelsqj`. Use the `gh` CLI for any GitHub work.
- **Commit message format:**
  - Imperative subject, ≤ ~72 chars: `verifiers: add exact-match reward fn`.
  - Body explains *why*, not just *what*, when the reason isn't obvious.
  - End commit messages with the required trailer:
    ```
    Co-Authored-By: Claude Opus 4.8 (1M context) <noreply@anthropic.com>
    ```
- **One concern per commit.** Don't bundle unrelated changes.
- If a change alters design or conventions, the brain update belongs **in the
  same commit** as the code — they must not drift apart.

## Updating the brain

The brain is only useful if it stays current. Update it as part of the work, not
as an afterthought.

| When this happens... | Update this file |
|----------------------|------------------|
| You make or revise a design decision | [decisions.md](decisions.md) (append a dated entry) |
| You complete a notable change | [journal.md](journal.md) (append a dated one-liner) |
| You establish or change a coding/repo rule | [conventions.md](conventions.md) |
| You change the system's structure or module roles | [architecture.md](architecture.md) |
| You introduce or redefine a domain term | [glossary.md](glossary.md) |
| You hit an unknown, a gotcha, or a TODO worth keeping | [open-questions.md](open-questions.md) |

Guidelines:
- **Append-only files** ([decisions.md](decisions.md), [journal.md](journal.md)):
  add new entries at the top of the entries section, dated `YYYY-MM-DD`. Don't
  rewrite history; if a decision is reversed, add a new entry that supersedes it.
- **Living docs** ([conventions.md](conventions.md),
  [architecture.md](architecture.md), [glossary.md](glossary.md)): edit in place
  to keep them accurate. They describe the *current* truth.
- Keep entries short and concrete. Prefer a precise sentence over a paragraph.
- Resolve an open question by moving its conclusion into the appropriate living
  doc and deleting it from [open-questions.md](open-questions.md).
- If the brain says something the code contradicts, fix the brain — stale memory
  is worse than no memory.

## Anti-patterns
- ❌ Making a design decision and not recording it.
- ❌ Committing on `main`, or committing without being asked.
- ❌ Letting the brain and code drift apart across separate commits.
- ❌ Adding boilerplate to the brain. Every line should earn its place.
