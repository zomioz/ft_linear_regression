import matplotlib.pyplot as plt
from get_value import get_value
from load import load
from get_value import get_value

def create_image():

    df = load("data.csv")
    T0, T1 = get_value("output_bonus.txt")

    mileage = df['km'].values
    price = df['price'].values

    plt.scatter(mileage, price)
    plt.xlabel('mileage')
    plt.ylabel('price')
    plt.title('Car prices based on mileage data from a CSV file')
    plt.savefig("bonus_regression_scatter.png", dpi=100, bbox_inches="tight", pad_inches=0.3)

    regression_function = T0 + T1 * mileage

    plt.clf()
    plt.plot(mileage, regression_function, color='red')
    plt.xlabel('mileage')
    plt.ylabel('price')
    plt.title('Car prices based on mileage from linear regression function')
    plt.savefig("bonus_regression_linearfunction.png", dpi=100, bbox_inches="tight", pad_inches=0.3)

    plt.scatter(mileage, price)
    plt.xlabel('mileage')
    plt.ylabel('price')
    plt.title('Price of a car based on his mileage')
    plt.savefig("bonus_regression_all.png", dpi=100, bbox_inches="tight", pad_inches=0.3)
    plt.close("all")
