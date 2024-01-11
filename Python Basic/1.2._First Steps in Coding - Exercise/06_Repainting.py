nylon = 1.50    
paint = 14.50
paint_thinner = 5.00

additionally = 2
bags = 0.40

rq_amount_nylon = int(input())
rq_amount_paint = int(input())
rq_amount_paint_thinner = int(input())
hours = int(input())

sum_nylon = (rq_amount_nylon + additionally) * nylon
sum_paint = (11 + 11 * 0.1) * paint
sum_paint_thinner = rq_amount_paint_thinner * paint_thinner
total_sum_materials = sum_nylon + sum_paint + sum_paint_thinner + bags 
amount_for_masters =  (total_sum_materials * 0.3) * 8
total_sum = total_sum_materials + amount_for_masters

print(total_sum)


