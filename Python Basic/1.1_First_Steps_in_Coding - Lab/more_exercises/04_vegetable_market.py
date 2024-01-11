vegetables_kg = float(input())
fruits_kg = float(input())
total_vegetables_kg = float(input())
total_fruits_kg = float(input())
euro = 1.94

price_vegetables = vegetables_kg * total_vegetables_kg
price_fruits = fruits_kg * total_fruits_kg
total_sum = price_vegetables + price_fruits
print(format(total_sum / euro, '.2f'))