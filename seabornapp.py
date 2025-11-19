import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Descriptive Statistics")

file = st.file_uploader("Upload Inc_Exp_Data.csv", type=["csv"])
if not file:
    st.stop()

df = pd.read_csv(file)

# ---- choose which graphs to show (no dropdowns) ----
c1 = st.checkbox("Bar: Highest_Qualified_Member (counts)")
c2 = st.checkbox("Bar: No_of_Earning_Members (counts)")
c3 = st.checkbox("Income vs Expense (choose line/scatter below)")
style = st.radio("Plot style for Income vs Expense", ["Line", "Scatter"], horizontal=True)
c4 = st.checkbox("Histogram: Mthly_HH_Expense")
c5 = st.checkbox("Histogram: Mthly_HH_Income")

# ---- 1) Bar: Highest_Qualified_Member ----
if c1:
    if "Highest_Qualified_Member" in df.columns:
        fig, ax = plt.subplots()
        df["Highest_Qualified_Member"].value_counts().plot(kind="bar", ax=ax)
        ax.set_title("Highest_Qualified_Member (counts)")
        ax.set_xlabel("")
        st.pyplot(fig)
    else:
        st.warning("Column 'Highest_Qualified_Member' not found.")

# ---- 2) Bar: No_of_Earning_Members ----
if c2:
    if "No_of_Earning_Members" in df.columns:
        fig, ax = plt.subplots()
        df["No_of_Earning_Members"].value_counts().plot(kind="bar", ax=ax)
        ax.set_title("No_of_Earning_Members (counts)")
        ax.set_xlabel("")
        st.pyplot(fig)
    else:
        st.warning("Column 'No_of_Earning_Members' not found.")

# ---- 3) Income vs Expense (line or scatter) ----
if c3:
    needed = {"Mthly_HH_Income", "Mthly_HH_Expense"}
    if needed.issubset(df.columns):
        fig, ax = plt.subplots()
        if style == "Line":
            df.plot(x="Mthly_HH_Income", y="Mthly_HH_Expense", ax=ax)
        else:
            df.plot(kind="scatter", x="Mthly_HH_Income", y="Mthly_HH_Expense", ax=ax)
        ax.set_title(f"Income vs Expense ({style.lower()})")
        st.pyplot(fig)
    else:
        st.warning("Columns 'Mthly_HH_Income' and/or 'Mthly_HH_Expense' not found.")

# ---- 4) Histograms ----
if c4 and "Mthly_HH_Expense" in df.columns:
    fig, ax = plt.subplots()
    df["Mthly_HH_Expense"].plot(kind="hist", bins=10, ax=ax)
    ax.set_title("Histogram: Mthly_HH_Expense")
    st.pyplot(fig)

if c5 and "Mthly_HH_Income" in df.columns:
    fig, ax = plt.subplots()
    df["Mthly_HH_Income"].plot(kind="hist", bins=10, ax=ax)
    ax.set_title("Histogram: Mthly_HH_Income")
    st.pyplot(fig)