def simple_spread_filter(bid: float, ask: float, max_spread: float) -> bool:
    spread = ask - bid
    return spread <= max_spread
