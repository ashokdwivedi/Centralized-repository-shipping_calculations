# Simple Interest Calculator

A lightweight, efficient script designed to calculate simple interest earned or paid on a principal investment over a specified time period and interest rate.

---

## Overview

Simple interest is a quick, straightforward method of calculating the interest charge on a loan or financial investment. Unlike compound interest, simple interest is calculated solely on the original principal amount, without compounding across periods.

---

## Financial Formula

The calculation uses the standard simple interest formula:

$$\text{Simple Interest} = \frac{P \times R \times T}{100}$$

Where:
* **$P$ (Principal):** The initial amount of money borrowed or invested (in USD or local currency).
* **$R$ (Rate of Interest):** The annual interest rate as a percentage (e.g., $5$ for $5\%$).
* **$T$ (Time Period):** The duration of the loan or investment in years.

### Total Accrued Value:
$$\text{Total Amount} = P + \text{Simple Interest}$$

---

## Features

* **Instant Calculation:** Calculates interest accrued and total return with minimal input.
* **Input Validation:** Prevents negative values and zero-duration calculations.
* **Open Source:** Licensed under the Apache License 2.0.

---

## Usage Instructions

### Running via Bash Shell (`simple-interest.sh`)

1. Ensure the script has execute permissions:
   ```bash
   chmod +x simple-interest.sh
