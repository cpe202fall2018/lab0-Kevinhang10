def weight_on_planets():
   
   #Taking in user input & converting it into an integer
   weight = float(input("What do you weigh on earth? "))
   
   #Calculations for mars weight
   mars_weight = weight * 0.38
   #Calculations for jupiter weight
   jupiter_weight = weight * 2.34

   print("\nOn Mars you would weigh ", mars_weight ," pounds.","\nOn Jupiter you would weigh ", jupiter_weight , " pounds.", sep="")
   
if __name__ == '__main__':
   weight_on_planets()
