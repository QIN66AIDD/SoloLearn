'''
You are in a hat store in Argentina! The prices are listed in US Dollars and Argentinian Pesos. You have both, but you want to make sure you pay the lower price! Do you pay in Dollars or Pesos? The exchange rate is 2 cents for every Peso.

Task:
Create a program that takes two prices and tells you which one is lower after conversion.
'''

one_dollar_in_pesos = 50

pesos  = int(input())
dollar = int(input())

if (dollar * one_dollar_in_pesos) > pesos:
    print('Pesos')
else: print('Dollars')