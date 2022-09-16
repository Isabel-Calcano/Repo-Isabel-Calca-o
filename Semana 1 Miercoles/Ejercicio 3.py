Money_in_account = float (input("how much money do you have un the deposit?"))
Profit = Money_in_account * 0.04
year1 = Money_in_account + Profit
Profit = year1 * 0.04
Year2 = year1 + Profit
Profit = Year2 * 0.04
Year3 = Year2 + Profit
print(f"in the first year you will have $ {round(year1,2)} overall")
print(f"in the second year you will have $ {round(Year2,2)} overall")
print(f"in the third year you will have $ {round(Year3,2)} overall")