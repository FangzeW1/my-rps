# Rock, Paper, Scissors

## RPS-001: Play a round

**Purpose:** one person plays a quick round against the computer.

- Choose rock, paper, or scissors. The computer chooses one move for that round.
- Display both choices and the result: **You win!**, **Computer wins**, or **It’s a tie**.
- Choosing again starts an independent round. No score or saved history.
- Keep the supplied interface and server. Name/color changes can wait until the rules work.

### Expected results

Results are from the **player’s perspective**. `determine_winner(player, computer)` in `game.py` returns `win`, `lose`, or `tie`. Inputs are the lowercase moves below; the supplied server rejects other choices.

| Player | Computer | Expected return |
| --- | --- | --- |
| rock | rock | tie |
| rock | paper | lose |
| rock | scissors | win |
| paper | rock | win |
| paper | paper | tie |
| paper | scissors | lose |
| scissors | rock | lose |
| scissors | paper | win |
| scissors | scissors | tie |

### Agreed plan

- Implement one independent round using the supplied interface and server. Display the player's move, the computer's move, and the correct result. Choosing again starts a fresh round; no score or saved history.
- Predicted example: the player chooses rock and the computer chooses paper. Return `lose` and display **Computer wins**, because paper beats rock. Show both choices so the result is clear.
- Reject missing or unsupported moves with HTTP 400 and a helpful explanation directing the player to rock, paper, or scissors. Validate on the server even though the normal page offers only those three buttons.
- Add nine explicit unit outcomes from the table above, a submitted-round integration check using the real rules, and a real-browser round with replay. Fix only the computer's random choice in tests; reuse the supplied missing/unsupported-input checks.
- Run `.venv/bin/python check.py` and review the diff against this spec before student browser review.

### Checks

Before coding, agree this small test plan with AI:

| Level | Cases and evidence |
| --- | --- |
| Unit — positive | All nine literal expected results above, including valid losses and ties. |
| Integration — positive | A submitted round uses the real rule function and displays both choices and the correct result. Fix the computer choice for the test. |
| Integration — negative | Reuse supplied missing/unsupported-move tests: HTTP 400 and a helpful explanation, without calling the rules. A crash is not the intended result. |
| E2E — positive | Add a real-browser round and replay in tests/e2e/test_round.py using the supplied live_server/page fixtures. Fix only the computer choice; use real rules and real HTTP. |

Use `unit`, `integration`, and `e2e` pytest markers. Run `.venv/bin/python check.py` for Black, Pylint, fast tests, and browser checks; then review the diff. Keep shared settings and meaningful assertions intact. The student still plays, inspects a rule and its test, and gives feedback. Browser automation does not establish every aspect of usability or application performance.

### Work record

- Issue: [RPS-001: Play a round](https://github.com/FangzeW1/my-rps/issues/1).
- Pull request / CI: add actual URLs when they exist.
- Implementation: [game.py](game.py) implements one independent round. [Unit and request tests](tests/test_game.py) cover all nine outcomes and a real submitted Rock-versus-Paper loss. [Browser test](tests/e2e/test_round.py) covers a loss and replay to a win using real rules.
- Checks: Full `.venv/bin/python check.py` passed Black, Pylint, 23 non-browser tests, and 6 Chromium tests. Reviewed the diff and new test files against this spec; existing checks and configuration are unchanged. Student browser observation: chose Rock, computer chose Paper, and the page displayed **Computer wins**; the student explained that paper beats rock. Student keyboard/replay observation: Tab cycled through the move buttons and browser controls; Enter on a selected move started a new round and displayed both moves and a result. The student also identified that the Rock-versus-Paper unit case would catch an incorrect result or reversed player/computer perspectives. Browser automation does not establish every aspect of usability or application performance.
