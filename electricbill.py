def generate_bill(units):
    if units <= 200:
        bill_amount = 0
        bill_status = "gruha jyothi sceme"
    else:
        bill_amount = (units - 200) * 5
        bill_status = "Charged"

    return bill_amount, bill_status

def main():
    try:
        # Input: number of units consumed
        units = float(input("Enter the number of units consumed: "))
        
        # Generate bill
        bill_amount, bill_status = generate_bill(units)
        
        # Output the bill
        print("\n--- Current Bill ---")
        print(f"Units Consumed: {units}")
        print(f"Bill Amount: ₹{bill_amount}")
        print(f"Status: {bill_status}")
    
    except ValueError:
        print("Please enter a valid number for units.")

if __name__ == "__main__":
    main()
