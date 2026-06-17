# ft_linear_regression

A simple machine learning project that predicts car prices based on mileage using linear regression.

---

## Part 1: Train Model & Predict Program

### What is Linear Regression?

Linear regression finds a straight line that best fits your data. It answers: **"How do two variables relate?"**

In this project:
- **Input (X)**: Car mileage
- **Output (Y)**: Car price

The model learns: `Price = θ₀ + θ₁ × Mileage`

Where:
- `θ₀` = the base price (intercept)
- `θ₁` = how much price changes per km (slope)

### How It Works

The algorithm uses **gradient descent** to find the best parameters:

1. Start with random values for θ₀ and θ₁
2. Make predictions and calculate errors
3. Adjust θ₀ and θ₁ to reduce errors
4. Repeat X times until the model converges

Before training, data is **normalized** (scaled between 0-1) to improve performance.

### Quick Start

#### 1. Train the model

```bash
python3 src/train_model/main.py
```

This trains the model and saves parameters to `output.txt`

#### 2. Make predictions

```bash
python3 src/predict_program/main.py
```

Enter a mileage value and get a price prediction.

### File Structure

```
train_model/
  ├── main.py              # Loads data and trains model
  ├── load.py              # Loads CSV file
  └── linear_function.py   # Gradient descent algorithm

predict_program/
  ├── main.py              # Makes predictions
  └── get_value.py         # Reads trained parameters
```

---

## Part 2: Bonus Features

### GUI Application

An interactive interface with visualization and performance metrics.

```bash
python3 src/bonus/main_bonus.py
```

**Features**:
- Train model with one click
- View data visualization (scatter plot + regression line)
- Display performance metrics (RMSE, R²)
- Save and load trained models

### Key Concepts

| Term | Meaning |
|------|---------|
| **MSE** | Average squared error (lower is better) |
| **RMSE** | Square root of MSE (same units as price) |
| **R²** | How well the model fits (0-1, higher is better) |
| **Normalization** | Scaling data between 0 and 1 |
| **Gradient Descent** | Algorithm to find best parameters |

---

## Dataset Format

```csv
km,price
240000,3650
139800,3800
150500,4400
```

---

## References

- [Google ML Crash Course](https://developers.google.com/machine-learning/crash-course/linear-regression)
- [Overfitting Explained](https://medium.com/@rakeshandugala/the-art-of-balance-tackling-overfitting-and-underfitting-in-linear-regression-models-bc1517b892c8)
- [Regression Metrics](https://medium.com/analytics-vidhya/regression-and-performance-metrics-accuracy-precision-rmse-and-what-not-223348cfcafe)
- [PySimpleGUI Documentation](https://docs.pysimplegui.com/)