from get_value import get_value


def main() -> None:


    try:
        mileage = float(input())
    except (ValueError, TypeError, KeyboardInterrupt, EOFError) as err:
        print("Error: thanks to enter a valid input\n", err)
        return
    if mileage < 0:
        print("Error: thanks to enter a valid input\n", " Value should be equal or greater than Zero")
        return

    T0, T1 = get_value("output.txt")
    price = (T0 + (T1 * mileage))
    price_formatted = "{:.2f}".format(price)
    mileage_formatted = "{:.0f}".format(mileage)
    if price < 0:
        return print("Error :Price should be :", price_formatted, "I will not give you money for this car")
    print("The price of a car with", mileage_formatted, "miles will be :", price_formatted)

if __name__ == "__main__":
    main()