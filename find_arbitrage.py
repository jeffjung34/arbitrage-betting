from sports_mapping import sports_mapping

def convert_to_american_odds(decimal_odds):
    if decimal_odds >= 2.0:
        american_odds = (decimal_odds - 1) * 100
    else:
        american_odds = -100 / (decimal_odds - 1)
    return round(american_odds)

def find_arbitrage_opportunities(odds_data):
    arbitrage_opportunities = []
    
    if not odds_data:
        print("No odds data to process.")
        return arbitrage_opportunities

    for event in odds_data:
        print(event)
        home_team = event['home_team']
        away_team = event['away_team']
        best_home_odds = float('-inf')
        best_away_odds = float('-inf')
        best_home_bookmaker = None
        best_away_bookmaker = None

        for bookmaker in event['bookmakers']:
            for market in bookmaker['markets']:
                if market['key'] == 'h2h':  
                    for outcome in market['outcomes']:
                        if outcome['name'] == home_team:
                            if outcome['price'] > best_home_odds:
                                best_home_odds = outcome['price']
                                best_home_bookmaker = bookmaker['title']
                        elif outcome['name'] == away_team:
                            if outcome['price'] > best_away_odds:
                                best_away_odds = outcome['price']
                                best_away_bookmaker = bookmaker['title']
        
        if best_home_odds > 0 and best_away_odds > 0:
            arbitrage_profit = 1/best_home_odds + 1/best_away_odds
            home_units = 1 / best_home_odds
            away_units = 1 / best_away_odds
            total_units = home_units + away_units
            arbitrage_opportunity = {
                'event': f"{home_team} vs {away_team}",
                'sport': f"{sports_mapping.get(event['sport_key'], event['sport_key'])} - {event.get('description', '')}",
                'bet_type': 'outcomes',
                'home_team': home_team,
                'home_odds': f"{'+' if convert_to_american_odds(best_home_odds) > 0 else ''}{convert_to_american_odds(best_home_odds)}",
                'home_bookmaker': best_home_bookmaker,
                'away_team': away_team,
                'away_odds': f"{'+' if convert_to_american_odds(best_away_odds) > 0 else ''}{convert_to_american_odds(best_away_odds)}",
                'away_bookmaker': best_away_bookmaker,
                'arbitrage_profit': arbitrage_profit,
                'home_units': home_units / total_units,
                'away_units': away_units / total_units
            }
            arbitrage_opportunities.append(arbitrage_opportunity)
            print("Found arbitrage opportunity:")
            print(arbitrage_opportunity)
    
    return arbitrage_opportunities
