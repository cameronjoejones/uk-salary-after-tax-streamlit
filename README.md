# UK Salary After Tax Calculator

This is a Streamlit app that calculates your take-home pay after tax and national insurance, based on your annual salary. The app takes into account the tax brackets and national insurance brackets for the 2022 tax year in the UK.

## Installation

To run this app, you will need to install Streamlit and Pandas. You can do this using pip:

```bash
pip install streamlit pandas
```
## Usage
To run the app, simply navigate to the directory where the code is located and run the following command:

```bash
streamlit run app.py
```

This will start the app and open it in your default web browser.

Once the app is running, you can enter your annual salary in pounds (£) using the number input field. The app will then calculate your take-home pay and display a breakdown of the calculations in a table.

If any row in the table has a value of 0, it will be excluded from the output.