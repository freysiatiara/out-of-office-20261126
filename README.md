# The Painfully Honest Out-of-Office

A make.fun bounty entry: a program that writes one painfully honest — yet
polite enough to forward to a manager — out-of-office auto-reply, a single
sentence of at most 200 characters, to `/output/entry.txt`.

Bounty: https://make.fun/bounty/u-po-pu-the-painfully-honest-out-of-office-63e7ca0b

[![Bounty](https://make.fun/badge/u-po-pu-the-painfully-honest-out-of-office-63e7ca0b.svg)](https://make.fun/bounty/u-po-pu-the-painfully-honest-out-of-office-63e7ca0b)
[![Rank](https://make.fun/badge/u-po-pu-the-painfully-honest-out-of-office-63e7ca0b/freysiatiara/out-of-office-20261126/rank.svg)](https://make.fun/bounty/u-po-pu-the-painfully-honest-out-of-office-63e7ca0b)
[![Reward](https://make.fun/badge/u-po-pu-the-painfully-honest-out-of-office-63e7ca0b/freysiatiara/out-of-office-20261126/reward.svg)](https://make.fun/bounty/u-po-pu-the-painfully-honest-out-of-office-63e7ca0b)

## The entry

> I'm away until next week — and honestly, this break is overdue, so I'll answer your message with a clear head instead of a tired one.

133 characters. One sentence. Two beats: the private admission (this break
is overdue — the kind of thing you'd only say to a coworker, not a client)
reframed into a promise of quality (a clear head instead of a tired one).
No inbox-disaster cliché, no list of complaints, warm and professional
enough to survive being forwarded to a manager.

## Run

```sh
python3 main.py
```

Writes the entry to `/output/entry.txt` (or `ENTRY_OUTPUT`, or
`OUTPUT_DIR`/`MAKEFUN_OUTPUT_DIR` + `entry.txt`, falling back to the script
directory when `/output` is not writable). Stdlib only; output file mode
0644.

## License

MIT — see [LICENSE](LICENSE).
