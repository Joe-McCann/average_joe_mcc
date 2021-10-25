# Problem statement
# Given a list of coins and a money value
# Provide the smallest list of coins needed
# to create that amount of money


# Recursive solution is exponential time, not very good
def make_change_recursive(money, coin_vals):
    if money < 0:
        return None
    elif money == 0:
        return []

    min_list = None
    for coin in coin_vals:
        prev_change = make_change_recursive(money-coin, coin_vals)
        if prev_change != None:
            if min_list == None or len(prev_change)+1 <= len(min_list):
                min_list = prev_change
                min_list.append(coin)
    
    return min_list

# Making change using Dynamic Programming
# This algorithm runs in O(c*m) where 
# c is the number of coins, m is the amount of money 
# we want to make change for. 
# This is at worst O(max(c,m)^2)
def make_change_DP(money, coin_vals):
    # Initialize that $0 needs no coins
    change_table = [[]]

    # Run through making change for every value including our money
    for i in range(1, money+1):
        min_list = None

        # Iterate through each coin.
        # This loop can be done with list comp, but wanted to avoid too much python shit
        for coin in coin_vals:

            # If coin too big for current money val
            if i - coin < 0:
                continue

            # If its not possible to make change for a certain money val
            elif change_table[i-coin] == None:
                continue

            else:
                # List to actually make our change
                # Its the coin, plus the change to make the money-coin
                # Ie. To make $.30 with a nickle, its one nickle + change to make $.25
                change = change_table[i-coin] + [coin]

                # If this is better than our current best try
                if (min_list == None) or (len(change) < len(min_list)):
                    min_list = change
        
        # Add the best way to make this money to our table
        change_table.append(min_list)
    
    # Send back our change val
    return change_table[~0]

print(make_change_DP(139, [57, 42, 32, 13, 1]))
