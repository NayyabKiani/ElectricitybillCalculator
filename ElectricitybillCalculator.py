# write a programme to calculate the electrictiy bill.
# should as the user to enter usage in kWh and print out the cost in pound

# Criteria:
# first 100 units = no charge
# next 100 units = 34p per kWh
# after 200 units = 45p per kWh

print("Today we are going to calculate your electricity bill!")
units = float(input("Enter the units of electricity you used in kWh: "))
cost_1 = 0
cost_2 = 0.34
cost_3 = 0.45

if units <= 100 :
    bill1 = float(units*cost_1)
    print (f"Your electricity bill is {bill1}!!!")
elif units >100 and units <=200:
    extraHours = (units-100)
    bill2 = (extraHours*cost_2) + (units*cost_1)
    print (f"Your electricity bill is {bill2}!!!")
else :
    remainderHours = (units-200)
    bill3 = (remainderHours*cost_3) + (100*cost_2) + (units*cost_1) 
    print (f"Your electricity bill is {bill3}!!!")