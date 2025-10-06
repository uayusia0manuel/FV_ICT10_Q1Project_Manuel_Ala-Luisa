from pyscript import display

#string
cafe_name= "Kitty Coffee☕"
owner_name= "Luisa Manuel"
business_house= "OPEN FROM 10:00 AM - 10:00 PM"

#integer (changed from string to integer)
year_established = 2025

#float (changed from string to float)
popular_item_price = 135 #price of popular item
tax_rate = 0.08 #tax rate

#list
items = ["Americano", "Mocha Frappucino", "Caramel Latte", "Cold Brew", "Matcha Latte"] #items on menu
allergens = ["Milk", "Soy", "Wheat"] #allergens

#dictionary (item-price duos)
prices = {
    "Americano": 130,
    "Mocha Frappucino": 135,
    "Caramel Latte": 135,
    "Cold Brew": 130,
    "Matcha Latte": 135
}

#boolean
has_delivery= True

#to display
display(cafe_name, target= "cafeName")
display(owner_name, target= "ownerName")
display(year_established, target= "yearFounded")
display(popular_item_price, target="popular")
display(business_house, target="hours")
display(has_delivery, target="deliver")
display(", ".join(allergens), target="allergen")
display(tax_rate*100, target="tax")