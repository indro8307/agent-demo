# agent-demo

A tiny practice project for learning how to create and run **subagents in Claude Code**.

It contains a small Python module with a couple of deliberate bugs, plus two agents that find them:

| Agent | What it does | Tools |
|---|---|---|
| `reviewer` | Reviews code for bugs and missing edge cases. Read-only, never edits files. | Read, Grep, Glob |
| `test-writer` | Writes unit tests and runs them in Docker. | Read, Write, Bash, Glob |

## Project structure

```
agent-demo/
├── .claude/
│   └── agents/
│       ├── reviewer.md
│       └── test-writer.md
├── .dockerignore
├── Dockerfile
├── calc.py
├── requirements.txt
└── README.md
```

## Setup

```bash
git clone <your-repo-url>
cd agent-demo
```

Claude Code runs on the host. Tests run in Docker, so start Docker Desktop first.

```bash
docker build -t agent-demo .
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

## Run tests in Docker

The image installs pytest from `requirements.txt`. Your project is mounted at `/app`, so you do not need to rebuild after editing `calc.py` or the tests.

```bash
docker build -t agent-demo .
docker run --rm -v "${PWD}:/app" agent-demo
```

That writes `report.xml` in the project folder.

## Note

The bugs in `calc.py` are intentional: `average()` subtracts 1 from the result, and `divide()` doesn't handle division by zero.

## Learn more

- [Claude Code subagents documentation](https://code.claude.com/docs/en/sub-agents)
