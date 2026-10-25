# agent-demo

A tiny practice project for learning how to create and run **subagents in Claude Code**.

It contains a small Python module with a couple of deliberate bugs, plus two agents that find them:

| Agent | What it does | Tools |
|---|---|---|
| `reviewer` | Reviews code for bugs and missing edge cases. Read-only, never edits files. | Read, Grep, Glob |
| `test-writer` | Installs pytest if needed, writes unit tests, runs them, and reports results. | Read, Write, Bash, Glob |

## Project structure

```
agent-demo/
├── .claude/
│   └── agents/
│       ├── reviewer.md
│       └── test-writer.md
├── calc.py
├── requirements.txt
└── README.md
```

## Setup

```bash
git clone <your-repo-url>
cd agent-demo
Requires Python 3. The test-writer agent installs pytest automatically if it’s missing.
```

## Usage

Start Claude Code from the project folder:

```bash
claude
```

Then try:

```
Use the reviewer agent to check calc.py
```

```
Use the test-writer agent to write tests for calc.py
```

Or run both at once:

```
In parallel: have the reviewer agent review calc.py, and have the test-writer agent write and run tests for it. Then summarize what both found.
```

## Note

The bugs in `calc.py` are intentional: `average()` subtracts 1 from the result, and `divide()` doesn't handle division by zero.

## Learn more

- [Claude Code subagents documentation](https://code.claude.com/docs/en/sub-agents)
