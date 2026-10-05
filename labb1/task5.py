distance = float(input())
consumption = float(input())
price = float(input())

fuel = distance * consumption / 100
cost = fuel * price
print("топливо:", fuel, "л")
print("стоимость:", cost, "руб")