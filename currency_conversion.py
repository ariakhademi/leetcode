"""
Parameters:

- array of currency conversion rates. 
E.g. ['USD', 'GBP', 0.77] which means 1 USD is equal to 0.77 GBP
- an array containing a 'from' currency and a 'to' currency
Given the above parameters, find the conversion rate that maps to 
the 'from' currency to the 'to' currency.
Your return value should be a number.

Example:
You are given the following parameters:

Rates: ['USD', 'JPY', 110] ['US', 'AUD', 1.45] ['JPY', 'GBP', 0.0070]
To/From currency ['GBP', 'AUD']
Find the rate for the 'To/From' currency. In this case, the correct result is 1.89.
"""

def find_conversion_rate(rates, query):
    # Step 1: Build graph
    graph = {}
    
    for src, dest, rate in rates:
        if src not in graph:
            graph[src] = []
        if dest not in graph:
            graph[dest] = []
        
        graph[src].append((dest, rate))
        graph[dest].append((src, 1 / rate))  # Add reverse conversion

    return graph

# Example Usage
rates = [
    ['USD', 'JPY', 110],
    ['USD', 'AUD', 1.45],
    ['JPY', 'GBP', 0.0070]
]

query = ['GBP', 'AUD']

print(find_conversion_rate(rates, query))  # Output: 1.89