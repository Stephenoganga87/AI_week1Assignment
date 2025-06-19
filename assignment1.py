# crypto_pilot.py
import time

crypto_db = {
    "Bitcoin": {
        "price_trend": "rising",
        "market_cap": "high",
        "energy_use": "high",
        "sustainability_score": 3
    },
    "Ethereum": {
        "price_trend": "stable",
        "market_cap": "high",
        "energy_use": "medium",
        "sustainability_score": 6
    },
    "Cardano": {
        "price_trend": "rising",
        "market_cap": "medium",
        "energy_use": "low",
        "sustainability_score": 8
    },
    "Solana": {
        "price_trend": "rising",
        "market_cap": "medium",
        "energy_use": "low",
        "sustainability_score": 7
    },
    "Polkadot": {
        "price_trend": "stable",
        "market_cap": "medium",
        "energy_use": "low",
        "sustainability_score": 9
    },
    "Algorand": {
        "price_trend": "rising",
        "market_cap": "medium",
        "energy_use": "very low",
        "sustainability_score": 10
    },
    "Tezos": {
        "price_trend": "stable",
        "market_cap": "medium",
        "energy_use": "low",
        "sustainability_score": 8
    },
    "Polygon": {
        "price_trend": "rising",
        "market_cap": "medium",
        "energy_use": "low",
        "sustainability_score": 7
    },
    "Avalanche": {
        "price_trend": "rising",
        "market_cap": "medium",
        "energy_use": "medium",
        "sustainability_score": 6
    },
    "Cosmos": {
        "price_trend": "stable",
        "market_cap": "medium",
        "energy_use": "low",
        "sustainability_score": 8
    },
    "Stellar": {
        "price_trend": "stable",
        "market_cap": "medium",
        "energy_use": "very low",
        "sustainability_score": 9
    },
    "Chainlink": {
        "price_trend": "rising",
        "market_cap": "medium",
        "energy_use": "medium",
        "sustainability_score": 5
    }
}

def calculate_profitability_score(coin):
    score = 0
    # Price trend weighting
    if crypto_db[coin]["price_trend"] == "rising":
        score += 9
    elif crypto_db[coin]["price_trend"] == "stable":
        score += 6
    else:
        score += 3
        
    # Market cap weighting
    if crypto_db[coin]["market_cap"] == "high":
        score += 8
    elif crypto_db[coin]["market_cap"] == "medium":
        score += 5
    else:
        score += 2
        
    return score

def get_sustainability_emoji(score):
    if score >= 8: return "🌿♻️"
    if score >= 6: return "🌱"
    return "⚡"

def get_advice(user_query):
    user_query = user_query.lower()
    
    # Profitability-focused recommendation
    if "profit" in user_query or "trend" in user_query or "grow" in user_query:
        profitable_coins = [coin for coin in crypto_db 
                          if crypto_db[coin]["price_trend"] == "rising"]
        profitable_coins.sort(key=lambda x: calculate_profitability_score(x), reverse=True)
        
        if not profitable_coins:
            return "Currently no coins show strong upward trends. Consider stable options like Ethereum."
        
        top_3 = profitable_coins[:3]
        return (f"🚀 Top trending coins for growth:\n"
                f"1. {top_3[0]} (Profit Score: {calculate_profitability_score(top_3[0])}/17)\n"
                f"2. {top_3[1]} (Profit Score: {calculate_profitability_score(top_3[1])}/17)\n"
                f"3. {top_3[2]} (Profit Score: {calculate_profitability_score(top_3[2])}/17)\n"
                "📈 Rising prices + strong market cap = growth potential!")

    # Sustainability-focused recommendation
    elif any(word in user_query for word in ["sustain", "green", "eco", "environment"]):
        sustainable_coins = [coin for coin in crypto_db 
                            if crypto_db[coin]["sustainability_score"] >= 7]
        sustainable_coins.sort(key=lambda x: crypto_db[x]["sustainability_score"], reverse=True)
        
        if not sustainable_coins:
            return "No highly sustainable coins in current database."
        
        response = "🌍 Top Eco-Friendly Cryptos:\n"
        for i, coin in enumerate(sustainable_coins[:5], 1):
            score = crypto_db[coin]["sustainability_score"]
            response += f"{i}. {coin}: {score}/10 {get_sustainability_emoji(score)}\n"
        response += "♻️ Low energy consumption + high sustainability scores"
        return response

    # Balanced recommendation
    elif any(word in user_query for word in ["long-term", "growth", "future", "hold"]):
        ranked_coins = []
        for coin in crypto_db:
            profit_score = calculate_profitability_score(coin)
            sustain_score = crypto_db[coin]["sustainability_score"]
            total_score = (profit_score * 0.65) + (sustain_score * 0.35)
            ranked_coins.append((coin, total_score, profit_score, sustain_score))
        
        ranked_coins.sort(key=lambda x: x[1], reverse=True)
        
        response = "🔮 Best Long-Term Investments:\n"
        for i, (coin, total, profit, sustain) in enumerate(ranked_coins[:5], 1):
            response += (f"{i}. {coin}: "
                         f"Total {total:.1f}/20 "
                         f"(Profit: {profit}/17, "
                         f"Eco: {sustain}/10) "
                         f"{get_sustainability_emoji(sustain)}\n")
        response += "💎 Balanced approach: 65% profit potential + 35% sustainability"
        return response

    # Specific coin inquiry
    for coin in crypto_db:
        if coin.lower() in user_query:
            details = crypto_db[coin]
            emoji = "🔥" if details["price_trend"] == "rising" else "🛡️"
            return (
                f"\n📊 {coin} Report {emoji}\n"
                f"Price Trend: {details['price_trend'].capitalize()}\n"
                f"Market Cap: {details['market_cap'].capitalize()}\n"
                f"Energy Use: {details['energy_use'].capitalize()}\n"
                f"Sustainability: {details['sustainability_score']}/10 {get_sustainability_emoji(details['sustainability_score'])}\n"
                f"Profit Score: {calculate_profitability_score(coin)}/17"
            )
    
    # Default response
    return (
        "\nI'm CryptoPilot, your AI co-pilot for crypto investments! ✈️\n\n"
        "Ask me about:\n"
        "- Profitable cryptocurrencies 📈\n"
        "- Sustainable eco-friendly coins 🌱\n"
        "- Long-term growth options 🚀\n"
        "- Specific coins (e.g. 'Tell me about Cardano')\n\n"
        "⚠️ DISCLAIMER: Crypto investments carry high risk. This is not financial advice. "
        "Always DYOR (Do Your Own Research)!"
    )

def main():
    print("""
    ✈️✈️✈️✈️✈️✈️✈️✈️✈️✈️✈️✈️✈️✈️✈️✈️✈️✈️
       Welcome to CRYPTO PILOT!       
    Your AI Co-Pilot for Crypto Investments
    ✈️✈️✈️✈️✈️✈️✈️✈️✈️✈️✈️✈️✈️✈️✈️✈️✈️✈️
    Type 'exit' anytime to end our session.
    """)
    
    while True:
        user_input = input("\nYou: ").strip()
        if not user_input:
            continue
        if user_input.lower() in ['exit', 'bye', 'quit', 'q']:
            print("\nCryptoPilot: Safe travels in the crypto skies! Remember to diversify your portfolio! ✈️💼")
            break
        
        print("\nCryptoPilot: ", end='')
        time.sleep(0.7)  # Simulate processing time
        response = get_advice(user_input)
        print(response)

if __name__ == "__main__":
    main()