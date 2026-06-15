import pandas as pd
from pandas import DataFrame as DataFrame

def load(path: str) -> DataFrame | None:

    '''
    Function to load a .csv file
    Argument: The path of .csv file
    Return: None on fail, a DataFrame on succes
    '''

    try:
        df = pd.read_csv(path)
    except (FileNotFoundError, PermissionError, IsADirectoryError):
        print("Error: unable to load csv file")
        return None

    return df

def linear_regression(df, number_of_iteration) -> tuple[float, float]:

    '''
    Function that execute an linear regression on a dataframe
    argument: Dirst: Dataframe. Second: number of iteration for the linear regression
    return: The two θ for the prediction
    '''

    learningRate = 0.1
    m = len(df)
    T0 = 0.0
    T1 = 0.0
    estimate_price = 0

    for x in range(number_of_iteration):

        TmpT0 = 0
        TmpT1 = 0

        for i in range(m):
            mileage = df.iloc[i, 0]
            price = df.iloc[i, 1]
            estimate_price = T0 + (T1 * mileage)
            TmpT0 += estimate_price - price
            TmpT1 += (estimate_price - price) * mileage

        T0 = T0 - learningRate * (1 / m) * TmpT0
        T1 = T1 - learningRate * (1 / m) * TmpT1

    return T0, T1

def training_model():

    '''
    Main function it load the data file and execute an linear regression on it
    argument : None
    return : None
    '''

    df = load("data.csv")
    if df is None:
        return False

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

    with open("output_bonus.txt", "w") as f:
        print(str(T0_real), file=f)
        print(str(T1_real), file=f)
    
    return True