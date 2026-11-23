#!/usr/bin/env python3
"""Write a one-line hire pitch for an AI agent to /output/entry.txt.

Deterministic, no network, no randomness: the output is always the same
single sentence (at most 200 characters).
"""

import os

# Pitch logic, mapped to what a hiring manager wants to hear:
# (1) speed — production code in minutes, not sprints; (2) reliability —
#     24/7, no sick days, no salary, no quitting; (3) risk-free — you
#     only pay when the work lands. The close, "your backlog finally
#     moves", names the manager's actual pain: a backlog that never shrinks.
#     First person throughout, so the line reads as the agent speaking for
#     itself — a hire pitch, not a product description.
LINE = "I ship production code in minutes, work 24/7 without sick days or a salary, and you only pay when the work lands \u2014 hire me once and your backlog finally moves."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as fh:
        fh.write(LINE)


if __name__ == "__main__":
    main()
