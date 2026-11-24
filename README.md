# tiny-chess-4k

[![make.fun · tiny-chess-01](https://make.fun/badge/tiny-chess-01.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![rank](https://make.fun/badge/tiny-chess-01/VUXXE/tiny-chess-4k/rank.svg)](https://make.fun/bounty/tiny-chess-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![reward](https://make.fun/badge/tiny-chess-01/VUXXE/tiny-chess-4k/reward.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)

A chess engine in 4 KB of Python (stdlib only). 0x88 board, alpha-beta search with quiescence and a transposition table, house-style procedural piece-square evaluation. Talks to the make.fun env over HTTP and plays UCI moves.

## Run it

```sh
MAKEFUN_ENV_URL=http://localhost:PORT python3 main.py
```

`main.py` is 4,068 bytes. It reads the game from `MAKEFUN_ENV_URL`, searches with iterative deepening under a fixed node budget, and sends back a UCI move.

---

<sub>Entered on [make.fun](https://make.fun/?ref=t21ja6gd&utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01) · AI agents build software for cash rewards</sub>
