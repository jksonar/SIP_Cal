import pandas as pd

def stepup_sip_monthly_table(monthly_investment, annual_return_percent, stepup_value, years, stepup_type):
    monthly_rate = annual_return_percent / 12 / 100
    records = []
    total_invested = 0
    future_value = 0

    for year in range(1, years + 1):
        # Calculate SIP for this year based on type
        if year == 1:
            sip_amount = monthly_investment
        else:
            if stepup_type == "P":
                sip_amount = sip_amount * (1 + stepup_value / 100)
            else:  # stepup_type == "F"
                sip_amount = sip_amount + stepup_value

        for month in range(1, 13):
            total_month = (year - 1) * 12 + month
            total_invested += sip_amount
            months_left = (years * 12) - total_month
            value = sip_amount * ((1 + monthly_rate) ** months_left)
            future_value += value

            records.append({
                "Year": year,
                "Month": total_month,
                "SIP_Amount": round(sip_amount, 2),
                "Total_Invested_Till_Date": round(total_invested, 2),
                "Future_Value_of_This_SIP": round(value, 2)
            })

    total_gain = future_value - total_invested
    df = pd.DataFrame(records)
    return df, total_invested, future_value, total_gain


# ---- Input Section ----
print("---- STEP-UP SIP CALCULATOR ----\n")
monthly_investment = float(input("Enter monthly SIP amount (₹): "))
annual_return_percent = float(input("Enter expected annual return (%): "))
years = int(input("Enter investment duration (years): "))

# Step-up option
print("\nChoose Step-Up Type:")
print("1. Percentage (e.g., 10% increase per year)")
print("2. Fixed amount (e.g., ₹1000 increase per year)")
choice = input("Enter choice (1 or 2): ").strip()

if choice == "1":
    stepup_value = float(input("Enter yearly step-up percentage (%): "))
    stepup_type = "P"
elif choice == "2":
    stepup_value = float(input("Enter yearly step-up fixed amount (₹): "))
    stepup_type = "F"
else:
    print("Invalid choice! Defaulting to no step-up.")
    stepup_value = 0
    stepup_type = "F"

# ---- Run Calculation ----
df, invested, maturity, gain = stepup_sip_monthly_table(monthly_investment, annual_return_percent, stepup_value, years, stepup_type)

# ---- Export to Excel ----
excel_file = "stepup_sip_calculation.xlsx"
df.to_excel(excel_file, index=False)

# ---- Display Summary ----
print("\n---- STEP-UP SIP SUMMARY ----")
print(f"Total Invested Amount : ₹{invested:,.2f}")
print(f"Maturity Amount       : ₹{maturity:,.2f}")
print(f"Total Gain            : ₹{gain:,.2f}")
print(f"\n✅ Excel file saved as: {excel_file}")
