def linear_regression(df) -> tuple[float, float]:

    learningRate = 0.1
    m = len(df)
    T0 = 0.0
    T1 = 0.0
    estimate_price = 0

    for x in range(1000):

        TmpT0 = 0
        TmpT1 = 0

        for x in range(m):
            mileage = df.iloc[x, 0]
            price = df.iloc[x, 1]
            estimate_price = T0 + (T1 * mileage)
            TmpT0 += estimate_price - price
            TmpT1 += (estimate_price - price) * mileage

        T0 = T0 - learningRate * (1 / m) * TmpT0
        T1 = T1 - learningRate * (1 / m) * TmpT1

    return T0, T1