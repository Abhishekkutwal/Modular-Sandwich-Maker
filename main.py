import data
from sandwich_maker import SandwichMaker
from cashier import Cashier

# Create instances of SandwichMaker and Cashier
resources = data.resources
recipes = data.recipes
sandwich_maker_instance = SandwichMaker(resources)
cashier_instance = Cashier()


def main():
    is_on = True
    while is_on:
        choice = input("What size sandwich would you like? (small/medium/large): ").lower()
        if choice in recipes:
            sandwich = recipes[choice]
            if sandwich_maker_instance.check_resources(sandwich["ingredients"]):
                cost = sandwich["cost"]
                print(f"That will cost ${cost}.")
                coins = cashier_instance.process_coins()
                if cashier_instance.transaction_result(coins, cost):
                    sandwich_maker_instance.make_sandwich(choice, sandwich["ingredients"])
            else:
                print("Sorry, we cannot make that sandwich.")
        else:
            print("Invalid choice, please choose a valid size.")

        another = input("Would you like to order another sandwich? (yes/no): ").lower()
        if another == "no":
            is_on = False


if __name__ == "__main__":
    main()
