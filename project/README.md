# ETF Strategy Sustainability Evaluation

**Stage:** Problem Framing & Scoping (Stage 01)

## Problem Statement

The goal of this project is to evaluate whether a simple ETF trading 
strategy is likely to remain effective in the future. Historical market 
data will be used to analyze the strategy's performance, risk, and 
consistency over time.

This analysis is intended to help an investor or portfolio manager make a 
more informed decision about whether the strategy should continue to be 
used. The project will consider both expected performance and potential 
risks rather than relying only on historical returns.

## Stakeholder & User

* **Decision owner:** Portfolio manager or investor responsible for 
deciding whether to continue using the ETF strategy.
* **Tool/operator:** Quantitative analyst or investment analyst who runs 
the analysis, evaluates the results, and reports the findings to the 
decision owner.

## Decision Window

The strategy will be reviewed on a monthly basis. The portfolio manager 
will use the updated analysis to decide whether to continue, modify, or 
discontinue the ETF strategy.

## Useful Answer & Decision

* **Type of answer:** Predictive
* **Metric or artifact:** A performance report including expected return, 
volatility, drawdown, and risk-adjusted performance.
* **Decision:** Use the results to recommend whether the ETF strategy 
should be continued, modified, or discontinued.

## Assumptions & Constraints

* Historical market behavior is assumed to provide some useful information 
about future performance, although market conditions may change.
* The ETF is assumed to have sufficient liquidity for the strategy to be 
executed without large price impact.
* Transaction costs, bid-ask spreads, and possible slippage must be 
considered when evaluating performance.
* The analysis is limited by the amount and quality of historical data 
available.
* The strategy is evaluated under realistic capital and trading 
constraints rather than assuming unlimited capacity.

## Known Unknowns / Risks

* Future market conditions may differ substantially from historical 
conditions.
* The choice of benchmark, investment horizon, and evaluation period may 
affect the conclusion.
* Historical backtest performance may overstate future performance because 
of overfitting or data-snooping.
* Transaction costs and slippage may be higher in practice than assumed.
* Unexpected market events or structural changes could reduce the 
effectiveness of the strategy.

## Lifecycle Mapping

Goal → Stage → Deliverable

* Evaluate whether the ETF strategy is likely to remain effective → 
Problem Framing & Scoping (Stage 01) → Clearly defined problem statement, 
stakeholder needs, evaluation goals, assumptions, constraints, and risks.
* Prepare the project for later analysis → Problem Framing & Scoping 
(Stage 01) → Initial project scope and plan for future data collection, 
modeling, evaluation, and reporting.

## Environment

- Python 3.10.20
- Conda environment: `bootcamp_env`
- Dependencies are listed in `requirements.txt`.

## Repo Plan

The project repository will use the following structure:

* `data/` — Store project data.
* `src/` — Store reusable Python source code.
* `notebooks/` — Store analysis and modeling notebooks.
* `docs/` — Store stakeholder-facing documentation and supporting 
materials.

The repository will be updated as each stage of the project lifecycle is 
completed.
