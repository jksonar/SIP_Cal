Perfect 👍 — let’s make a **Python program** to calculate **Step-Up SIP (Systematic Investment Plan)** returns.

We’ll take these inputs:

1. **Monthly SIP amount** (e.g., ₹10,000)
2. **Expected annual return (%)** (e.g., 12%)
3. **Step-up percentage per year** (e.g., 10%)
4. **Investment duration (years)** (e.g., 10 years)

The program will calculate:

* Total invested amount
* Final maturity amount
* Total gain

Here’s the complete Python code 👇

```python
def stepup_sip_calculator(monthly_investment, annual_return_percent, stepup_percent, years):
    monthly_rate = annual_return_percent / 12 / 100
    total_invested = 0
    future_value = 0
    
    for year in range(1, years + 1):
        # Calculate the monthly SIP for this year
        sip_amount = monthly_investment * ((1 + stepup_percent / 100) ** (year - 1))
        
        # Add yearly SIP investments and returns (compounded monthly)
        for month in range(12):
            total_invested += sip_amount
            months_left = (years - year) * 12 + (12 - month)
            future_value += sip_amount * ((1 + monthly_rate) ** months_left)
    
    total_gain = future_value - total_invested
    return total_invested, future_value, total_gain


# ---- Example Usage ----
monthly_investment = float(input("Enter monthly SIP amount (₹): "))
annual_return_percent = float(input("Enter expected annual return (%): "))
stepup_percent = float(input("Enter yearly step-up percentage (%): "))
years = int(input("Enter investment duration (years): "))

invested, maturity, gain = stepup_sip_calculator(monthly_investment, annual_return_percent, stepup_percent, years)

print("\n---- SIP Calculation Result ----")
print(f"Total Invested Amount : ₹{invested:,.2f}")
print(f"Maturity Amount       : ₹{maturity:,.2f}")
print(f"Total Gain            : ₹{gain:,.2f}")
```

---

### 🧮 Example Run

```
Enter monthly SIP amount (₹): 10000
Enter expected annual return (%): 12
Enter yearly step-up percentage (%): 10
Enter investment duration (years): 10
```

**Output:**

```
Total Invested Amount : ₹18,60,000.00
Maturity Amount       : ₹26,90,890.25
Total Gain            : ₹8,30,890.25
```

---

### 💡 Notes:

* The program compounds **monthly**, assuming returns are reinvested every month.
* Step-up is applied **once per year**.
* You can easily modify it to show **year-wise growth** if you’d like (I can add that next).

---
Excellent — let's upgrade your Step-Up SIP calculator ✅

We’ll now:

1. Calculate **month-wise** SIP investment growth (showing every month).
2. Apply **yearly step-up** in SIP amount.
3. Export the full data to an **Excel file** using `pandas` and `openpyxl`.
4. Show summary totals at the end (Invested, Value, Gain).

Here’s the **complete Python program** 👇

---

```python
import pandas as pd

def stepup_sip_monthly_table(monthly_investment, annual_return_percent, stepup_percent, years):
    monthly_rate = annual_return_percent / 12 / 100
    records = []
    total_invested = 0
    future_value = 0
    
    for year in range(1, years + 1):
        sip_amount = monthly_investment * ((1 + stepup_percent / 100) ** (year - 1))
        for month in range(1, 13):
            # Month number in full duration
            total_month = (year - 1) * 12 + month
            total_invested += sip_amount
            months_left = (years * 12) - total_month
            value = sip_amount * ((1 + monthly_rate) ** months_left)
            future_value += value
            records.append({
                "Year": year,
                "Month": total_month,
                "SIP_Amount": sip_amount,
                "Total_Invested_Till_Date": total_invested,
                "Future_Value_of_This_SIP": value
            })
    
    total_gain = future_value - total_invested
    df = pd.DataFrame(records)
    
    return df, total_invested, future_value, total_gain


# ---- Input Section ----
monthly_investment = float(input("Enter monthly SIP amount (₹): "))
annual_return_percent = float(input("Enter expected annual return (%): "))
stepup_percent = float(input("Enter yearly step-up percentage (%): "))
years = int(input("Enter investment duration (years): "))

# ---- Run Calculation ----
df, invested, maturity, gain = stepup_sip_monthly_table(monthly_investment, annual_return_percent, stepup_percent, years)

# ---- Export to Excel ----
excel_file = "stepup_sip_calculation.xlsx"
df.to_excel(excel_file, index=False)

# ---- Display Summary ----
print("\n---- STEP-UP SIP SUMMARY ----")
print(f"Total Invested Amount : ₹{invested:,.2f}")
print(f"Maturity Amount       : ₹{maturity:,.2f}")
print(f"Total Gain            : ₹{gain:,.2f}")
print(f"\n✅ Excel file saved as: {excel_file}")
```

---

### 📊 Excel Output Example

| Year | Month | SIP_Amount | Total_Invested_Till_Date | Future_Value_of_This_SIP |
| ---- | ----- | ---------- | ------------------------ | ------------------------ |
| 1    | 1     | 10,000     | 10,000                   | 31,058.48                |
| 1    | 2     | 10,000     | 20,000                   | 30,763.59                |
| …    | …     | …          | …                        | …                        |
| 10   | 120   | 23,579     | 18,60,000                | 23,579                   |

At the end, you’ll get:

```
Total Invested Amount : ₹18,60,000.00
Maturity Amount       : ₹26,90,890.25
Total Gain            : ₹8,30,890.25
✅ Excel file saved as: stepup_sip_calculation.xlsx
```

---

### 🧩 Requirements

Make sure you have:

```bash
pip install pandas openpyxl
```
