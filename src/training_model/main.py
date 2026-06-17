from load import load
from linear_function import linear_regression

def main() -> None:

    '''
    Main function it load the data file and execute an linear regression on it
    argument : None
    return : None
    '''

    df = load("data.csv")
    if df is None:
        return
    df_normalized = df.astype(float)
    
    mileage_min = df_normalized.iloc[:, 0].min()
    mileage_max = df_normalized.iloc[:, 0].max()
    mileage_range = mileage_max - mileage_min
    df_normalized.iloc[:, 0] = (df_normalized.iloc[:, 0] - mileage_min) / mileage_range
    
    price_min = df_normalized.iloc[:, 1].min()
    price_max = df_normalized.iloc[:, 1].max()
    price_range = price_max - price_min
    df_normalized.iloc[:, 1] = (df_normalized.iloc[:, 1] - price_min) / price_range
    
    number_of_iteration = 1000
    T0, T1 = linear_regression(df_normalized, number_of_iteration)


    T1_real = T1 * (price_range / mileage_range)
    T0_real = price_min + (price_range * T0) - (T1_real * mileage_min)

    print("After the linear regression", T0_real, T1_real)

    with open("output.txt", "w") as f:
        print(str(T0_real), file=f)
        print(str(T1_real), file=f)


if __name__ == "__main__":
    main()