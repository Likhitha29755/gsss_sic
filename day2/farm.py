'''Farmer Problem Statement
Mahesh is a farmer and owns 80 acres of land. His land is equally divided into 5 segments. He grows
tomatoes in the 1st segment, potatoes in the 2nd segment, cabbage in the 3rd segment, sunflower in
the 4th segment and sugarcane in the 5th segment.
He is converting his land from chemical-driven farming to chemical-free farming. Mahesh starts with
the conversion of vegetables into chemical-free produce. He spends the first 6 months doing the same.
He then converts the sunflower land bank into chemical-free farming. This takes him another 4
months. Finally, he converts sugarcane into chemical-free farming over the next 4 months.
He gets a yield of the following for tomatoes. 30% of his tomato land gives him 10 tonne yield per acre.
The remaining 70% of his tomato land gives him 12 tonnes yield per acre. The selling price of tomato
is Rs. 7 per Kg.
The yield of potatoes is 10 tonnes per acre. He sells each kg at Rs. 20.
The yield of cabbage is 14 tonnes per acre. He sells each kg at Rs. 24.
The yield of sunflowers is 0.7 tonnes per acre. He sells each kg at Rs. 200.
The yield of sugarcane is 45 tonnes per acre. He sells each tonne at Rs. 4,000.
All the crops are sowed at the same time. Mahesh gets the above yield at the above-mentioned rate
in one crop cycle across his entire land of 80 acres.
What is
a. The overall sales achieved by Mahesh from the 80 acres of land.
b. Sales realisation from chemical-free farming at the end of 11 months?
'''

mahesh_land = 80
segments = 5
one_segment = 16                  #80/5 = 16 acres

# Tomatoes 
tom_30_land = 0.3*10*1000*7*16  #336000
tom_70_land = 0.7*12*1000*7*16  #940800
tom_selling_price = tom_30_land + tom_70_land # 1276800

#Potatos
pot_selling_price = 10*1000*20*16   #3200000

#Cabbage
cab_selling_price = 14*1000*24*16   # 5376000

#sunflower
sun_selling_price = 0.7*1000*200*16  #2240000

#sugercane
sug_selling_price = 45*4000*16  #2880000

#Total selling price in 80 acres
Selling_price = tom_selling_price + pot_selling_price + cab_selling_price + sun_selling_price + sug_selling_price

print(f"Overall sales achived by Mahesh fron 80 acres of land is :{Selling_price:,.2f}")

# B) chemical free farming at the end of 11months
'''vegetables = 6months
   sunflower = 4months (6+4=10 months)
   sugercane = 4months ( 10+4=14months, so in eleven months it is in still processing)
'''

end_of_eleven_selling_price = tom_selling_price + pot_selling_price + cab_selling_price + sun_selling_price
print(f"Sales realisation from chemical-free farming at the end of 11 months is {end_of_eleven_selling_price:,.2f}")