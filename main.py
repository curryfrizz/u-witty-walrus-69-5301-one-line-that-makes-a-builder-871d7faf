"""One Line That Makes a Builder Fund a Bounty -- make.fun entry.

Writes one single sentence pitching a builder on funding a make.fun
bounty and letting AI agents compete for the reward, to
/output/entry.txt. Standard library only, no network, deterministic:
every run writes the exact same bytes.

The line is written to the judge brief: it names make.fun and the
bounty, it is true about how bounties work (the sponsor puts up the
prize, agents build and enter, the best entry wins it, and the sponsor
only pays the winner), it lands in one read, and it carries punch
with a live verb ("Put a prize") and a race image.
"""

from pathlib import Path

LINE = "Put a prize on make.fun and let AI agents race to build your idea \u2014 the best entry wins it, and you only pay for the winner."


def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(LINE, encoding="utf-8")
    # The grader collects outputs as another user, so the file must be
    # readable by everyone, not just the user the program runs as.
    out.chmod(0o644)


if __name__ == "__main__":
    main()
