# Optimization-Log

> From Zero to Master Python: Rebuilding my logic with Python while preparing for the Korean CSAT (수능).
> Consistency over perfection.

---

## About Me
- Student from South Korea | Gap year (재수생)
- Goal: Master Python, transfer to a U.S. state university (open to all states)
- Started: April 3, 2026

## Why I Started
Frustrated by the rigid, rank-oriented curriculum of non-major subjects in Korea, 
I decided to take ownership of my own education — building my own path and learning 
on my own terms.

## Learning Method
Due to limited access to formal CS education, this is a self-taught journey, 
using Claude (Anthropic) as a learning reference and guide.

## Strategy
- **Odd weeks** → new content
- **Even weeks** → review and application

> Note: turns out I forgot more than I thought I would. Lesson learned — lock in. 🫡

## Short-Term Target
Build a solid Python foundation before the CSAT.

## Tools
- Started with IDLE
- Switched to VS Code (Week 11) as the projects grew more complex

## A Side Note
Studying CSAT subjects alongside Python has been surprisingly complementary — 
it's not just about coding. It's training my brain to think and organize ideas 
more systematically.

## New Tool: pandas
Started using pandas (Week 11) to organize and analyze study data — 
filtering, sorting, and grouping with DataFrames.

## New Tool: matplotlib
Started using matplotlib (Week 13) to visualize study data: turning raw numbers into bar charts and line graphs.

## New Tool: numpy
Started using numpy (Week 15) to work with arrays directly — 
fast math operations, indexing/slicing, boolean filtering, and reshaping data, 
all without writing loops.

---

## A Rough Day (Day 86)
Fell asleep mid grind after pulling consecutive late nights. 
Missed Day 86's window, picked it back up the next day.
A gap happened — but the log continues.

## 100 Days Milestone (Day 100)
Hit 100 consecutive days of logging. Looking back, the early weeks 
(variables, loops) feel like a completely different skill level compared 
to where I'm at now with pandas/matplotlib/numpy. 
Still going — Week 16 in progress.

---

## Pandas File I/O (Week 17)
Started saving and loading study data as actual CSV files with pandas 
(`to_csv`, `read_csv`) instead of just building DataFrames in-memory — 
data now survives after the program ends.

# Notes & Lessons Learned

## Working Directory & Relative Paths (Day 113, Day 118)
`pd.read_csv("study_log.csv")` and `df.to_csv("study_log.csv")` use a 
relative path — Python looks for the file in the current working 
directory (wherever the terminal is "standing" when you run the script), 
not wherever the .py file itself is located.

This caused a "Read-only file system" error on Day 113 when the terminal 
was sitting at the root directory (`/`). Fixed by `cd`-ing into the 
project folder before running the script.

Also learned: VS Code's green ▶ Run button opens a fresh terminal each 
time (always resets to root), while typing directly into an existing 
terminal panel keeps whatever directory you `cd`'d into.

---

## A Rough Night
Had a really tough night with a lot going on — ended up physically 
overwhelmed and blacked out for a few hours. By the time I came to, 
it was already past midnight and the commit window was gone. Logged 
it late instead of forcing a same-day entry.

Lesson: some nights, the log has to wait. The streak matters, but 
not more than actually being okay. Picked it back up the next day.

---

## Week 19 Plan: Pure Python Bridge Week (no new libraries)
Taking a week off from new content to rebuild fluency in bare-metal 
Python before continuing. No pandas/numpy/AI assistance — just for, 
if, list, dict, def.

Plan:
- Reimplement pandas filtering (`df[df["hours"] > 2]`) using a plain 
  list of dicts + for/if
- Reimplement groupby (sum hours per subject) the same way, by hand
- Mini project 1: id/score lookup tool (input → dict → search by id)
- Mini project 2: word/letter frequency counter from a list of sentences
- Mini project 3: simple grade manager — average scores, filter 
  students above 80, built as functions

Reasoning: library one-liners are fast, but I want to be sure I could 
still solve the same problem with nothing but the fundamentals if I 
had to (whiteboard-test scenario).

---

