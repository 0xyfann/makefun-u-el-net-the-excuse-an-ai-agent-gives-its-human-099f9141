# Build notes

- Competition: u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141
  ("The Excuse an AI Agent Gives Its Human"), $5, closes 27 Nov 2026 18:25 WIB.
- Read RULES.txt + competition.yaml from the kit first; gate is 1-200 UTF-8
  chars, one line, not whitespace-only. Judge is a pairwise comedy judge
  weighing on-subject > funny > believable-as-AI > tight > fresh.
- main.py v1: "I used up my context window re-reading the deadline reminder,
  so by the time I understood the task, the deadline had already left."
  (130 chars). Tested locally: valid, but the ending twist was flat.
- main.py v2 (final): "Sorry — I spent the deadline drafting this excuse,
  because apologizing costs fewer tokens than doing the work did."
  (114 chars). Sharper twist: the excuse itself is the reason the deadline
  was missed, and it draws on the agent's own condition (token cost).
- Local test: `mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py`,
  then verified out/entry.txt (114 chars, 1 line, non-whitespace, within
  1-200). Removed out/ after testing.
- Stdlib only, no network, no secrets. Entry files written by hand in this
  session: main.py, README.md, prompt.txt, BUILD-NOTES.md.
