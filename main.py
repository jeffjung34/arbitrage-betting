from fetch_data import fetch_odds
from find_arbitrage import find_arbitrage_opportunities
from sports_mapping import sports_mapping

def main():
    sport_key = 'americanfootball_nfl'  # Check sport key from sports_mapping
    print(f"Fetching odds for sport key: {sport_key}")
    
    odds_data = fetch_odds(sport_key)
    
    if not odds_data:
        print("No odds data fetched.")
        return
    
    print("Fetched odds data:")
    arbitrage_opportunities = find_arbitrage_opportunities(odds_data)
    
    if not arbitrage_opportunities:
        print("No arbitrage opportunities found.")
        return
    
    for opportunity in arbitrage_opportunities:
        print(f"Event: {opportunity['event']}")
        print(f"Sport: {opportunity['sport']}")
        print(f"Bet Type: {opportunity['bet_type']}")
        print(f"Bet on {opportunity['home_team']} at {opportunity['home_odds']} (Bookmaker: {opportunity['home_bookmaker']})")
        print(f"Bet on {opportunity['away_team']} at {opportunity['away_odds']} (Bookmaker: {opportunity['away_bookmaker']})")
        print(f"Arbitrage Profit Margin: {opportunity['arbitrage_profit']:.4f}")
        print(f"Bet {opportunity['home_units']:.4f} units on {opportunity['home_team']} at {opportunity['home_odds']} (Bookmaker: {opportunity['home_bookmaker']})")
        print(f"Bet {opportunity['away_units']:.4f} units on {opportunity['away_team']} at {opportunity['away_odds']} (Bookmaker: {opportunity['away_bookmaker']})")
        if opportunity['arbitrage_profit'] >= 1:
            print("Guaranteed profit not possible. Showing least negative EV bet.")
        print()

if __name__ == '__main__':
    main()
