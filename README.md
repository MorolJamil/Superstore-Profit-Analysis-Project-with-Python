# What Drives Sales and Profit in a Retail Business?
A quantitative analysis of the Sample Superstore dataset.

## Question
Which parts of a retail business make money, how do sales trend
over time, and does discounting help or hurt profit?

## Data
Sample Superstore dataset, 9,994 order lines, 2014-2017.
Source: a public, no-login GitHub mirror of the dataset
(https://raw.githubusercontent.com/Ayon-coder/FUTURE_ML_01/main/Sample%20-%20Superstore.csv)

## Method
Pure quantitative analysis in Python (pandas, matplotlib): totals,
averages, growth rates, a correlation coefficient, and profit-margin
ratios. No machine learning.

## Findings
Q1 -- Sales grew 51.4% from 2014 ($484K) to 2017 ($733K), unevenly:
       2015 was flat (-2.8%), then 2016 (+29.5%) and 2017 (+20.4%)
       accelerated. Sales peak in November by total monthly volume.

Q2 -- Pearson r = -0.219 between discount and profit. A 10% discount
       is the most profitable point ($96 avg profit, 16.6% margin).
       Profit turns negative once discounts pass 30%.

Q3 -- West is the strongest region (14.9% margin), Central the
       weakest (7.9% margin, driven by a 24% average discount).
       Technology leads category margin (17.4%); Furniture sells
       well but earns almost nothing (2.5% margin).

## Key insight
High sales do not equal high profit. Margin -- not revenue --
reveals what actually makes money, and heavy discounting is a
hidden profit killer.

## Project structure