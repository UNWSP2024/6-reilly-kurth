#Reilly Kurth
#2/28/2025

def calculate_taxes(total_sales):
    state_tax_rate = 0.05
    county_tax_rate = 0.025
    state_tax = total_sales * state_tax_rate
    county_tax = total_sales * county_tax_rate
    total_tax = state_tax + county_tax
    return state_tax, county_tax, total_tax

def main ():
    total_sales = float(input("Enter total sales for the month:"))
    state_tax, county_tax, total_tax = calculate_taxes(total_sales)
    print("State taxes:", state_tax)
    print("County tax:", county_tax)
    print("Total sales tax (county plus state is:", + total_tax )

main()
