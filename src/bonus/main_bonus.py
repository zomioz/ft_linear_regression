import matplotlib.pyplot as plt
from get_value import get_value
from load import load
from math_function import calculate_mse, calculate_r2


def display_function(df, T0, T1):

    mileage = df['km'].values
    price = df['price'].values

    plt.scatter(mileage, price)
    plt.xlabel('mileage')
    plt.ylabel('price')
    plt.title('Price of a car based on his mileage')

    regression_function = T0 + T1 * mileage
    plt.plot(mileage, regression_function, color='red', label=f'Linear Regression Function')

    return


def calculate_precision(df, T0, T1):

    true_price = df["price"]
    predicted_price = T0 + T1 * df["km"]

    mse = calculate_mse(true_price, predicted_price)
    rmse = mse ** 0.5
    r2 = calculate_r2(true_price, predicted_price)
    return mse, rmse, r2


def main() -> None:

    df = load("data.csv")
    T0, T1 = get_value("output.txt")
    display_function(df, T0, T1)

    if T0 == 0 and T1 == 0:
        return print("θ0 and θ1 are set to 0, I can't calculate the precision of linear regression with this values")
    mse, rmse, r2 = calculate_precision(df, T0, T1)
    print("The difference between my prediciton and the reality of the market using RMSE is around ", "{:.2f}".format(rmse))
    print("My linear regression precision is: " "{:.1f}".format(r2 * 100), "%")
    try:
        plt.show()
    except KeyboardInterrupt:
        pass
    finally:
        plt.close("all")


if __name__ == "__main__":
    main()
