unit=int(input("Enter the unit:"))
if(unit<100):
    print("No charge below 100 units:")
elif(unit>100 and unit<200):
    print("The charge =",(unit-100)*5)
elif(unit>200):
    print("The charge is=",(unit-100)*5+(unit-200)*10)
    