# Round 1: Data Detective 🕵️

**Time limit: 45 minutes**

## The scenario

You've just joined **Nimbus Gadgets Co.**, an online retailer. Someone on the old
data team left in a hurry, and the only record of the last six months of orders
is a single export file — `nimbus_orders_messy.csv` — that nobody ever cleaned up.

Before you can trust _anything_ in this file, you need to clean it. Then you can
answer the questions the (fictional) VP of Sales is asking.

## Rules

- Use Python only (pandas is allowed and recommended, but not required).
- Work as a team — divide up the questions, but cross-check each other's answers
  before submitting. Wrong answers cost you; there's no partial credit per question.
- You may not open the CSV in Excel/Sheets to hand-fix values — the point is to
  clean it in code. (Looking at it to understand the mess is fine!)
- Submit your final answers using the format at the bottom of this sheet before
  time is up. Whatever you have when time is called is what gets scored.
- **Watch out**: not everything in this file is trustworthy. Some columns exist
  but may be wrong. That's realistic — and part of the challenge.

## The questions

Answer all 10. Each is worth points; some are worth bonus points if you also
explain (in one sentence) _why_ the raw data would have given a wrong answer.

1. How many genuine orders are in this dataset once exact duplicate rows and
   junk/corrupt rows are removed?
2. How many orders came from customers in New York? (Careful — city names are
   not consistent.)
3. What is the total revenue across all valid orders?
4. Which product category generated the most total revenue, and how much?
5. What is the average order value for the Electronics category?
6. Which month had the most orders, and how many?
7. How many unique customers placed at least one order?
8. What is the total revenue from orders shipped to Seattle?
9. How many total units were sold in the Outdoor category?
10. **Data quality bonus**: how many exact duplicate rows and how many
    junk/corrupt rows did you find and remove? (State both numbers.)

## Scoring

- 10 points per correct main answer (1–9) = 90 points
- Bonus question (10) = 10 points if both numbers are correct, 5 if only one is
- +2 bonus per question (max +10 total) if your team can explain in one sentence
  what specifically in the raw data would have tricked a team that didn't clean
  it properly
- Fastest team to submit a fully correct answer sheet gets **+10 speed bonus**

## Submission format

Copy this into your shared doc / form and fill in your numbers:

```
Team name: ______
Q1 (valid orders): ______
Q2 (NY orders): ______
Q3 (total revenue): ______
Q4 (top category / revenue): ______ / ______
Q5 (avg Electronics order value): ______
Q6 (top month / count): ______ / ______
Q7 (unique customers): ______
Q8 (Seattle revenue): ______
Q9 (Outdoor units sold): ______
Q10 (duplicates found / junk rows found): ______ / ______
```

Good luck 🎉
