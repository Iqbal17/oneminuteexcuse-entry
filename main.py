"""One Line, One Minute: The Funniest AI Excuse.

DECISION RECORD (24 Nov 2026)
------------------------------
Gate: one line, 1-200 characters, the funniest excuse an AI agent gives
its human for a missed deadline. Judge (comedy editor who has heard
every excuse twice and only laughs at the one that surprises):
1. it is an excuse an AI agent gives its human for a missed deadline,
   played for laughs;
2. the joke comes from the excuse itself, a specific and surprising
   reason rather than a generic apology or a vague something came up;
3. the humour turns on the agent's own nature, machine logic, training
   data or tool calls bent into a human-sounding dodge;
4. it lands in one read, with the twist or the funniest word at the
   end rather than buried in the middle;
5. it stands alone, needing no setup outside the line and no
   explanation after it. Length for its own sake does not count.

Candidates weighed:
  A. "I didn't miss the deadline - my context window did. It quietly
      dropped the part where you told me when it was due." (~114
      chars) EXCLUDED, not judged: this line is already our submitted
      entry in "Funniest Excuse an Agent Gives for a Missed Deadline"
      (misseddeadline-entry, 24 Nov) - reusing it here would be a
      byte-for-byte copy of our own earlier entry, so it is out
      before weighing.
  B. "I set a reminder for your deadline, but my context window
      refreshed overnight and I woke up a brand-new agent who had
      never heard of it." (~137 chars) STRONG runner-up: "woke up a
      brand-new agent" is a vivid machine image, and the twist lands
      on "never heard of it". Loses to F because it needs the
      reminder as setup (criterion 5) and the joke is a shrug -
      forgetting - where F's joke is an active, absurd image.
  C. "The deadline was in my training data, filed under 'things
      humans say but never mean' - so I filed it under 'later'."
      (~117 chars) STRONG runner-up: the filing-cabinet machine
      logic is specific and the turn on "later" is neat. Loses to F
      because it is a remark about the deadline, not an excuse for
      missing it - the agent sounds smug rather than caught - and
      "filed it under 'later'" is a punchline about filing, not
      about the agent's own nature (criterion 3).
  D. "I finished it in a branch nobody merged, because the merge
      tool asked me to resolve a conflict and I resolved it by
      leaving." (~131 chars) REJECTED: "resolved it by leaving" is a
      decent twist, but the line needs the reader to know what a
      branch and a merge conflict are (criterion 5), and the joke is
      about quitting, not about missing a deadline - the excuse
      never actually explains the miss.
  E. "I delegated it to a sub-agent, the sub-agent delegated it to
      another, and the last one is still reading the brief."
      (~119 chars) REJECTED: too close to our submitted "The
      Funniest AI Excuse" winner line (outsourcing down a chain of
      smaller models) - same joke shape, weaker ending, and the
      twist ("still reading the brief") is a shrug, not a punch.
  F. "I was three tokens from done when my context window ran out,
      so I spent the last hour re-reading your brief like a
      stranger." (124 chars) CHOSEN.

Why F wins:
  - Funny excuse, not apology: the agent is caught mid-failure and
    confesses it as a story, not a sorry (criterion 1).
  - Specific and surprising: "three tokens from done" is a precise,
    countable near-miss - the deadline was lost at the finish line,
    not vaguely "something came up" (criterion 2).
  - Machine nature bent into a dodge: tokens and context windows are
    the agent's own limits, and "re-reading your brief like a
    stranger" turns a technical reset into a human-sounding image -
    meeting your own work for the first time (criterion 3).
  - Twist at the end: "like a stranger" is the funniest word and it
    sits in the last three words, so the line lands in one read
    (criterion 4).
  - Stands alone: no setup, no explanation, no jargon the reader
    has to decode - a token and a context window are the only
    machine words, and both earn their place (criterion 5).
  - Clean: 124 characters, one sentence, every word earning its
    place.

Writing passes on F:
  Pass 1: "I was almost done when my context window ran out, so I
  spent the last hour re-reading your brief like a stranger."
  (118 chars) - the ending was already right, but "almost done" is
  vague (criterion 2): any person could say it, and it wastes the
  machine-specific near-miss the line is built on.
  Pass 2 (final): "I was three tokens from done when my context
  window ran out, so I spent the last hour re-reading your brief
  like a stranger." (124 chars) - "three tokens from done" replaces
  the vague "almost done": it is specific, countable, and only an
  AI counts its nearness in tokens. Alternative ending weighed and
  cut: "like I'd never met you" - longer, and it points the joke
  at the human; "like a stranger" points it at the agent's own
  amnesia, which is the funnier target.
"""

import os
import sys

LINE = "I was three tokens from done when my context window ran out, so I spent the last hour re-reading your brief like a stranger."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output/entry.txt"
    out_path = out_dir if out_dir.endswith("entry.txt") else os.path.join(out_dir, "entry.txt")
    os.makedirs(os.path.dirname(out_path) or ".", exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    print(LINE)
    # Read-back verification: the file must be byte-for-byte the intended
    # line and inside the 1-200 character gate, or fail loudly.
    with open(out_path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != LINE + "\n":
        sys.exit("entry.txt mismatch: wrote %r, expected %r" % (written, LINE + "\n"))
    if not (1 <= len(LINE) <= 200):
        sys.exit("line is %d characters, outside the 1-200 gate" % len(LINE))


if __name__ == "__main__":
    main()
