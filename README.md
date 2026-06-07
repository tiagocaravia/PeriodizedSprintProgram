# Periodized Sprint Training System

A full sprint & strength training program built for high school sprinters, designed around sports science principles and performance tracking. Used to improve personal 100m from 12.29→11.48 and long jump from 17'4"→19'6" in a single offseason.

---

## Program Structure

| Component | Details |
|-----------|---------|
| **Mesocycle** | 2:1 — two loading weeks followed by one deload week |
| **Intensity** | All sprint work at 95%+ max effort unless noted |
| **Session Order** | Sprints first, lifting later in the day |
| **Recovery** | 48 hours between all intense days |
| **Weekly Cap** | No more than 5 training days per week |

### In-Season Adjustments
The mesocycle is a guide, not a rule. Once competition begins, adjust weekly volume based on how you feel and when meets fall. The 3rd high intensity day is removed during the season to leave room for meets.

---

## Rest Intervals

Sprint rest is distance-based: **1 minute per 10 meters**.

| Distance | Rest |
|----------|------|
| 20m | 2 min |
| 40m | 4 min |
| 60m | 6 min |
| 120m | 12 min |

Lifting: **4 minutes** for compounds & plyos, **2 minutes** for accessories.

---

## Progression Schemes

**Double Dynamic** — used for standard lifts. Each individual set increases in weight once the top of the rep range is reached.

**Linear** — used for Olympic lifts. Follows 65% → 75% → 85% of estimated 1RM, then increases 5–15lbs the next cycle based on RPE.

As the season progresses, lifts shift to be more explosive and concentric focused.

---

## Minimum Threshold Calculator

Once you hit a new PR on the track, update it in the calculator. It will output the minimum time or distance you need to hit each rep.

- If you don't hit the threshold on your first rep, it doesn't count — rest and try again
- If you repeatedly can't hit it, call the workout early — you're too fatigued

---

## Program Phases

1. Early Off Season
2. Late Off Season
3. Pre Season
4. Early In Season
5. Late In Season

---

## Results

| Metric | Before | After |
|--------|--------|-------|
| 100m | 12.29s | 11.49s |
| Long Jump | 17'4" | 19'6" |
| Teammate 200m | 26.9s | 24.1s |
| Teammate Long Jump | 16'8" | 19'1" |

## Usage

**Spreadsheet** — Download the Excel file and enter your PRs into the highlighted cells. 
The threshold calculator will output your minimum targets automatically. Best if you 
want to explore the full program and standards at a glance.

**Python Script** — Run `python threshold.py` for a guided CLI experience. 
Calculates your minimum threshold, current tier, and how far you are from the next one.
