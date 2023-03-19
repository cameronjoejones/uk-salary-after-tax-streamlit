import streamlit as st
import pandas as pd

def calculate_progressive_tax(salary, tax_brackets):
    tax = 0
    for i, bracket in enumerate(tax_brackets):
        if salary > bracket["limit"]:
            tax += (bracket["limit"] - (tax_brackets[i-1]["limit"] if i > 0 else 0)) * bracket["rate"]
        else:
            tax += (salary - (tax_brackets[i-1]["limit"] if i > 0 else 0)) * bracket["rate"]
            break

    return tax

def calculate_ni(salary, ni_brackets):
    ni = 0
    for i, bracket in enumerate(ni_brackets):
        if salary > bracket["limit"]:
            ni += (bracket["limit"] - (ni_brackets[i-1]["limit"] if i > 0 else 0)) * bracket["rate"]
        else:
            ni += (salary - (ni_brackets[i-1]["limit"] if i > 0 else 0)) * bracket["rate"]
            break

    return ni

def calculate_salary_after_tax(salary, tax_brackets, ni_brackets):
    tax = calculate_progressive_tax(salary, tax_brackets)
    ni = calculate_ni(salary, ni_brackets)
    net_salary = salary - tax - ni
    return net_salary

def get_tax_brackets():
    return [
        {"limit": 12570, "rate": 0},
        {"limit": 50270, "rate": 0.2},
        {"limit": 150000, "rate": 0.4},
        {"limit": float('inf'), "rate": 0.45}
    ]

def get_ni_brackets():
    return [
        {"limit": 9500, "rate": 0},
        {"limit": 50000, "rate": 0.12},
        {"limit": float('inf'), "rate": 0.02}
    ]


def create_table():
    gross_income = annual_salary
    taxable_income = gross_income - calculate_ni(gross_income, ni_brackets)
    tax_breakdown = calculate_progressive_tax(gross_income, tax_brackets)
    ni_paid = calculate_ni(gross_income, ni_brackets)
    take_home_pay_yearly = calculate_salary_after_tax(gross_income, tax_brackets, ni_brackets)
    take_home_pay_monthly = take_home_pay_yearly / 12
    take_home_pay_weekly = take_home_pay_yearly / 52

    data = {
        'Title': ['Gross Income', 'Taxable Income', 'Tax Breakdown', 'National Insurance', '2022 Take Home'],
        'Yearly': [f'£{gross_income:,.2f}', f'£{taxable_income:,.2f}', f'£{tax_breakdown:,.2f}', f'£{ni_paid:,.2f}', f'£{take_home_pay_yearly:,.2f}'],
        'Monthly': [f'£{gross_income/12:,.2f}', f'£{taxable_income/12:,.2f}', f'£{tax_breakdown/12:,.2f}', f'£{ni_paid/12:,.2f}', f'£{take_home_pay_monthly:,.2f}'],
        'Weekly': [f'£{gross_income/52:,.2f}', f'£{taxable_income/52:,.2f}', f'£{tax_breakdown/52:,.2f}', f'£{ni_paid/52:,.2f}', f'£{take_home_pay_weekly:,.2f}']
    }

    df = pd.DataFrame(data)
    df.set_index('Title', inplace=True)

    df = df.loc[(df != '£0.00').any(axis=1)]

    return df



st.set_page_config(
    page_title="UK Salary After Tax Calculator",
    page_icon="💸",
    layout="centered",
    initial_sidebar_state="expanded",
)

st.markdown("<style> footer {visibility: hidden;} </style>", unsafe_allow_html=True)


st.title("💸 UK Salary After Tax Calculator")

annual_salary = st.number_input("Enter your annual salary (£)", min_value=0.0, step=100.0)

tax_brackets = get_tax_brackets()
ni_brackets = get_ni_brackets()

st.write("## Output Breakdown")
st.dataframe(create_table(), width=1000)

st.sidebar.markdown("## About")
st.sidebar.info("This app calculates your take home pay after tax and national insurance. ")
st.sidebar.info("Created by Cameron Jones. ")
st.sidebar.markdown("""
<div style='display: flex; justify-content: center; align-items: center;'>
  <a href="https://github.com/cameronjoejones/uk-salary-after-tax-streamlit.git" target="_blank">
    <img src="https://img.shields.io/badge/GitHub-181717.svg?style=for-the-badge&logo=GitHub&logoColor=white" alt="GitHub Badge">
  </a>
</div>
""", unsafe_allow_html=True)
