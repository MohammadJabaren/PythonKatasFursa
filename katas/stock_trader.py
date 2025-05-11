def max_profit(prices):
    """
    Finds the maximum profit that can be achieved by buying and selling the stock ONCE.

    Aim for O(n)

    Args:
        prices: a list of prices on each day

    Returns:
        the maximum profit, or 0 if no profit can be achieved
    """
    min_price = float('inf')
    max_price_to_sell = 0

    for i in prices:
        if i < min_price:
            min_price = i
        if i - min_price > max_price_to_sell:
            max_price_to_sell = i - min_price
    return max_price_to_sell


if __name__ == '__main__':
    stock_prices = [7, 1, 5, 3, 6, 4]
    profit = max_profit(stock_prices)
    print(f"Maximum Profit: {profit}")  # should be 5

    # Additional test cases
    prices1 = [7, 6, 4, 3, 1]
    print(f"Maximum Profit: {max_profit(prices1)}")  # should be 0 (no profit possible)

    prices2 = [1, 2, 3, 4, 5]
    print(f"Maximum Profit: {max_profit(prices2)}")  # should be 4 (buy at 1, sell at 5)