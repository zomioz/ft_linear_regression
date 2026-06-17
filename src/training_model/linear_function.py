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

        if x % (number_of_iteration / 10) == 0:
            print("for", x, "iterations -> θ0 =", "{:.4f}".format(T0), "θ1 =", "{:.4f}".format(T1))

    return T0, T1