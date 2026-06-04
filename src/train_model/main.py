from load import load
from linear_function import linear_regression

def main() -> None:
    df = load("data.csv")
    df_normalized = df.astype(float)
    
    mileage_min = df_normalized.iloc[:, 0].min()
    mileage_max = df_normalized.iloc[:, 0].max()
    df_normalized.iloc[:, 0] = (df_normalized.iloc[:, 0] - mileage_min) / (mileage_max - mileage_min)
    
    price_min = df_normalized.iloc[:, 1].min()
    price_max = df_normalized.iloc[:, 1].max()
    df_normalized.iloc[:, 1] = (df_normalized.iloc[:, 1] - price_min) / (price_max - price_min)
    
    T0, T1 = linear_regression(df_normalized)
    print(T0, T1)

    with open("../output.txt", "w") as f:
        print(str(T0), file=f)
        print(str(T1), file=f)

    mileage_input = 100000
    mileage_normalized = (mileage_input - mileage_min) / (mileage_max - mileage_min)
    price_normalized = T0 + (T1 * mileage_normalized)
    price_real = (price_normalized * (price_max - price_min)) + price_min
    print(f"Estimated price: ${price_real}")

    with open("output.txt") as f:
        tmp = f.read()
        splt = tmp.split('\n')
        print(float(splt[1]))
if __name__ == "__main__":
    main()