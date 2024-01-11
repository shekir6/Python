pens_price = 5.80
markers_price = 7.20
detergent = 1.20

pens = int(input())
markers = int(input())
liters_detergent = int(input())
reduction_per = int(input())

price_pak_pen = pens * pens_price
price_pak_markers = markers * markers_price
price_detergent = liters_detergent * detergent
total_price = price_pak_pen + price_pak_markers + price_detergent

discountetd_price = total_price - (total_price * (reduction_per / 100))

print(discountetd_price)
