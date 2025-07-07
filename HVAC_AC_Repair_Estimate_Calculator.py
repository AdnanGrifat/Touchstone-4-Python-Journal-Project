def get_yes_no(prompt):
    """
    Prompt the user with a yes/no question until a valid response is entered.
    Returns 'yes' or 'no' in lowercase.
    """
    while True:
        answer = input(prompt + " (yes/no): ").strip().lower()
        if answer in ['yes', 'no']:
            return answer
        print("Please enter 'yes' or 'no'.")

def get_refrigerant_type():
    """
    Prompt user for refrigerant type until a valid type (R22, R410a, R454b) is entered.
    Returns a tuple (type, cost per pound).
    """
    valid_types = {'r22': 250, 'r410a': 100, 'r454b': 200}
    while True:
        r_type = input("Enter refrigerant type (R22, R410a, R454b): ").strip().lower()
        if r_type in valid_types:
            return r_type, valid_types[r_type]
        print("Invalid refrigerant type. Please enter R22, R410a, or R454b.")

def get_positive_float(prompt):
    """
    Prompt user to enter a positive float value.
    Keeps asking until valid input is entered.
    """
    while True:
        try:
            val = float(input(prompt))
            if val > 0:
                return val
            else:
                print("Please enter a positive number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def main():
    """
    Main function to calculate HVAC repair estimate.
    Starts with mandatory service call charge, then adds optional repairs.
    Validates all user inputs.
    """
    service_call_cost = 150  # Mandatory service call charge
    capacitor_cost = 200
    total_cost = service_call_cost  # Always include service call charge

    print("Service call charge of $150 is mandatory.")

    # Ask if capacitor replacement is needed
    capacitor_replace = get_yes_no("Is capacitor replacement needed?")
    if capacitor_replace == 'yes':
        total_cost += capacitor_cost

    # Ask if refrigerant recharge is needed
    refrigerant_recharge = get_yes_no("Is refrigerant recharge needed?")
    if refrigerant_recharge == 'yes':
        r_type, cost_per_pound = get_refrigerant_type()
        pounds = get_positive_float(f"Enter pounds of {r_type.upper()} to recharge: ")
        total_cost += cost_per_pound * pounds

    print(f"Total estimated cost: ${total_cost:.2f} \n Plus Any additional issues we might find at time of diagnosis, we will let you know what will be the cost before we preform the repair service.")

if __name__ == "__main__":
    main()
