"""
chris.wiggins@gmail.com 
- 2024-04-08
- 2025-04-26 update for plotting to file

"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression

# Read the data from the file
data = pd.read_csv(
    "dates-chron.txt",
    sep=" ",
    header=None,
    names=["Date", "CumulativeCount"],
    parse_dates=["Date"],
)

# Define the reference date
reference_date = pd.Timestamp("2000-01-01")

# Renormalize dates to be the number of days since 2000-01-01
data["Days_Since_2000"] = (data["Date"] - reference_date).dt.days + 1

# Use only the second half of the data for fitting
halfway_point = len(data) // 2
fit_data = data.iloc[halfway_point:]

# Prepare data for linear regression in the log-log space
X = np.log(fit_data["Days_Since_2000"].values.reshape(-1, 1))
y = np.log(fit_data["CumulativeCount"].values)

# Perform linear regression
model = LinearRegression()
model.fit(X, y)

# Get the exponent (slope) and the constant (intercept) of the power-law fit
exponent = model.coef_[0]
constant = np.exp(model.intercept_)

# Create an array of ordinal dates for prediction
ordinal_dates = data["Days_Since_2000"].values.reshape(-1, 1)

# Predict using the model to get the fit line in the transformed space
log_y_fit = model.predict(np.log(ordinal_dates))
# Inverse the log to get the actual values
y_fit = np.exp(log_y_fit)

# Plot the actual data
plt.figure(figsize=(10, 6))
plt.plot(data["Date"], data["CumulativeCount"], ".-", label="Cumulative Count")
plt.scatter(
    data.iloc[3]["Date"],
    data.iloc[2]["CumulativeCount"],
    color="red",
    marker="x",
    s=100,
    label="Vaswani et al. (2017)",
)

# Plot the fit line with actual dates and counts
nu = round(exponent, 2)
plt.plot(
    data["Date"], y_fit, color="orange", label=f"Power-law Fit ($y \sim t^{{{nu}}}$)"
)

# Set the labels and title
plt.xlabel("Year")
plt.ylabel("Cumulative Count")
plt.title("...is all you need arXiv papers (cumulative) power law")
plt.legend()
plt.grid(True)
plt.tight_layout()

# Save the figure to a file
plt.savefig("all_you_need_plot.png", dpi=300, bbox_inches="tight")

# Show the plot on screen
plt.show()

# Output the parameters of the power-law fit
print(f"Power-law fit parameters: a={constant:.2f}, b={exponent:.2f}")
