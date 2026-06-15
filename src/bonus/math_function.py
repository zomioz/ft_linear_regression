from load import load
from get_value import get_value

def calculate_precision():

    df = load("data.csv")
    T0, T1 = get_value("output_bonus.txt")

    true_price = df["price"]
    predicted_price = T0 + T1 * df["km"]

    mse = calculate_mse(true_price, predicted_price)
    rmse = mse ** 0.5
    r2 = calculate_r2(true_price, predicted_price)
    return mse, rmse, r2


def calculate_mse(true_price, predicted_price):

    total = 0
    n = len(true_price)

    for i in range(n):
        error = true_price[i] - predicted_price[i]
        total += error * error

    return total / n


def calculate_r2(true_price, predicted_price):

    n = len(true_price)

    total = 0
    for i in range(n):
        total += true_price[i]
    mean_true = total / n

    sse = 0
    sst = 0
    for i in range(n):
        error = true_price[i] - predicted_price[i]
        sse += error * error

        diff = true_price[i] - mean_true
        sst += diff * diff

    if sst == 0:
        return 0

    return 1 - (sse / sst)