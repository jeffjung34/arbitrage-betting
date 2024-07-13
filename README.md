# Arbitrage Betting Project

## Table of Contents
- [Motivation](#motivation)
- [Project Structure](#project-structure)
- [How to Run the Project](#how-to-run-the-project)
- [Dependencies](#dependencies)
- [Arbitrage Math](#arbitrage-math)
- [Arbitrage Profit Margin](#arbitrage-profit-margin)
- [Calculating Units to Bet](#calculating-units-to-bet)
- [Note](#note)

## Motivation
The goal of this project is to identify arbitrage opportunities in sports betting. Arbitrage betting guarantees a profit regardless of the event's outcome by placing bets on all possible outcomes at favorable odds.

Different bookmakers provide varying odds for the same event. By exploiting these discrepancies, we can secure a profit. This project automates the identification of such opportunities by fetching real-time odds data from multiple bookmakers and calculating potential arbitrage scenarios.

## Project Structure
- `fetch_data.py`: Handles fetching sports and odds data from the API.
- `find_arbitrage.py`: Contains the logic for finding arbitrage opportunities based on the fetched odds data.
- `main.py`: The main entry point to run the program.
- `sports_mapping.py`: Contains the mapping of sport keys to their full names and descriptions.
- `config.py`: Contains the API key configuration.

## How to Run the Project
1. **Clone the repository:**
   ```bash
   git clone https://github.com/jeffjung34/arbitrage-betting.git
   cd arbitrage-betting
   ```
2.  **Install Dependencies:**
   ```bash
   pip install request
   ```  
3. **Set Up your API Key**
- Generate your own API key from The Odds API: https://the-odds-api.com/
- Open config.py and add your API key
```bash 
API_KEY = "your_api_key_here"
```
4. **Run the main script**
```bash
python main.py
```

## Dependencies
- Python 3.x
- requests library: To install, run pip install requests

## Arbitrage Math
To determine if there is an arbitrage opportunity, we use the following formula:

$$\ \text{Arbitrage Profit Margin} = \left( \frac{1}{\text{Best Home Odds}} + \frac{1}{\text{Best Away Odds}} \right) \$$

If the sum of the inverses of the best odds for each outcome (home and away) is less than 1, there is an arbitrage opportunity. The smaller the sum, the larger the potential profit.

For example, if we have:
- Best home odds = 2.00 (+100)
- Best away odds = 2.50  (+150)

The arbitrage profit margin would be:

$$\ \text{Arbitrage Profit Margin} = \left( \frac{1}{2.00} + \frac{1}{2.50} \right) = 0.9 \$$

Since 0.9 < 1, this is an arbitrage opportunity.

## Arbitrage Profit Margin
The Arbitrage Profit Margin indicates the guaranteed return on investment. A margin of less than 1 indicates a profitable arbitrage opportunity. The exact profit can be calculated as:

$$ \text{Profit} = \left( \frac{1}{\text{Arbitrage Profit Margin}} - 1 \right) \times 100\% \$$

For the above example:

$$ \text{Profit} = \left( \frac{1}{0.9} - 1 \right) \times 100\% = 11.11\%  $$

This means you can expect an 11.11% return on your total bet amount.

## Calculating Units to Bet
Suppose we want to make a total bet of 1 Unit. We need to determine how to split the unit between betting on the home team and the away team to ensure a profit.

For example, if we have:
- Best home odds = 2.00 (+100)
- Best away odds = 2.50 (+150)

First, calculate the raw units to bet based on the odds:

$$ \text{Raw Units on Home Team} = \frac{1}{\text{Best Home Odds}} = \frac{1}{2.00} = 0.5 $$

$$ \text{Raw Units on Away Team} = \frac{1}{\text{Best Away Odds}} = \frac{1}{2.50} = 0.4 $$

The total raw units is the sum of these raw units:

$$ \text{Total Raw Units} = 0.5 + 0.4 = 0.9 $$

To ensure we bet the entire 1 unit, we scale these raw units proportionally:

$$ \text{Scaled Units on Home Team} = \frac{0.5}{0.9}  \approx 0.556 $$

$$ \text{Scaled Units on Away Team} = \frac{0.4}{0.9}\approx 0.444 $$

This means you should bet approximately 0.556 units on the home team and 0.444 units on the away team for a profit of .11 units per unit bet. 


## Note
- This project currently only supports H2H (moneyline) markets.

