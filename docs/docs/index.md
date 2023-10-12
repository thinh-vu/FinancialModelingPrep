# Welcome to FMP Python

<div id="logo" align="center">
    <img src="./assets/fmp_logo.png" alt= "logo"/>
    <img src = "./assets/vnstock_logo_color.png" alt="vnstock_logo"/>
</div>

> In collaboration with FMP (Financial Modeling Prep), Vnstock is proud to introduce the FinancialModelingPrep Python Wrapper—an open-source project designed to empower the data-driven financial community. By bringing the capabilities of the Financial Modeling Prep API to the Python ecosystem, we aim to streamline access to valuable financial data, making it more accessible, user-friendly, and versatile.

## Quick Start Guide
### Obtain Your FMP API Key

Starting with the FinancialModelingPrep Python Wrapper is straightforward, and here's how you can do it with ease:

[Choose Your Plan :credit_card:](https://site.financialmodelingprep.com/developer/docs/pricing?utm_source=thinhvu&utm_medium=FMP_Python_Package_Docs){ .md-button }

1. **Sign Up with Google**: FMP offers a convenient signup/login option with Google. Simply use your Google account to streamline the registration process and get access to your FMP account.
    
2. **Setting Your API Key**: Once logged in, navigate to your [dashboard](https://site.financialmodelingprep.com/developer/docs/dashboard). Here, you can generate your unique API key. To make your experience even more seamless, set your API key as the `TOKEN` variable in your python code. This way, you can start using the package without having to manually input your API key each time. 
To safeguard your API key, it's recommended not to hard-code it directly into your project. Instead, consider following the section below to manage your API key using a YAML file.
    
3. **Free vs. Paid Plans**: As a free user, you can access limited features of the wrapper. However, to unlock the full range of capabilities, consider upgrading to one of FMP's paid plans.
    
4. **Pricing Details**: For more information on the pricing plans and what each plan offers, visit the [FMP Pricing Page](https://site.financialmodelingprep.com/developer/docs/pricing?utm_source=thinhvu&utm_medium=FMP_Python_Package_Docs). Here, you can explore the features available in each plan and choose the one that best suits your needs.
    
5. **API Key Usage**: With your API key set as the `TOKEN` variable, you can seamlessly authenticate your requests when using the FinancialModelingPrep Python Wrapper. Detailed documentation and code examples are available to help you get started.

### Manage API key with YAML
Utilizing a YAML file to securely manage your API key is the recommended and straightforward method. Here's a professional guide to implementing this approach:

1. **Create a YAML Configuration File**: Using a trusted text editor such as Visual Studio Code or Sublime Text, create a YAML configuration file named `fmp_api_key.yaml`. Store this file in a secure location, avoiding any unintentional inclusion in your Git repository. Refer to the template file included in this project [here](https://github.com/thinh-vu/FinancialModelingPrep/blob/main/docs/secret_template.yml)
    
2. **Configure Your YAML File**: In your chosen text editor, structure the content in a key-value pair manner. Specifically, use the format `TOKEN: your_api_key`, ensuring there are no backticks surrounding the `your_api_key` value.
    
3. **Save Your YAML File**: Save the YAML file once you've entered the necessary configuration.
    
4. **Retrieve the File Path**: Note the path to your YAML file as you'll need it for the following function.
    
5. **Incorporate the API Key Retrieval Code**: In your Python project or Jupyter Notebook, integrate the following code. If you're using the demo notebook, you may find this code already present. However, ensure that you replace `'REPLACE_WITH_THE_PATH_TO_YOUR_YAML_FILE'` with the actual path to your YAML file:

```python
from ur_gadget import yaml_cred
TOKEN = yaml_cred('TOKEN', 'YOUR_YAML_FILE_PATH')
```

By following these steps and incorporating the provided code, you'll securely manage your API key through a YAML file, enhancing the protection and accessibility of your financial data credentials.

### Install the package

To install the FinancialModelingPrep Python Wrapper package with the package name "FinancialModelingPrep_Python," follow these instructions:
Open your terminal or command prompt and run the following command, or just simply run the code cell in the Demo Notebook:

```
pip install FinancialModelingPrep-Python
```

### Demo Jupyter Notebook

We're delighted to provide a secure and efficient Quick Start Jupyter Notebook that allows you to swiftly launch your projects with confidence. This notebook serves as a rapid onboarding guide, ensuring that you can begin using the FinancialModelingPrep Python Wrapper securely and with ease.


[Launch Notebook :material-rocket-launch:](#){ .md-button }

## Key Features

- **Fundamental Data**: Delve deep into the core of financial analysis with access to a wide spectrum of fundamental data, including:
    - **Stock Listing**: Retrieve listings for a variety of stocks.
    - **Company Information**: Explore detailed information about companies, their financials, and key statistics.
    - **Statement Analysis**: Access financial statements, including income statements, balance sheets, and cash flow statements.
    - **Stock Calendar**: Stay updated on key events such as earnings, dividends, splits, and IPOs.
    - **News**: Access various news categories, including general news, stock news, crypto news, forex news, and press releases.
    - **Insider Trading**: Keep track of insider trading activities for deeper market insights.
- **Market Data**: Gain a holistic view of the financial landscape with market data that covers:
    - **Market Overview**: Get a bird's-eye view of the overall market conditions.
    - **Economics Data**: Access economic indicators and data that can influence your financial strategies.
    - **Stocks, Crypto, Forex, and Commodities**: Stay informed about the latest trends, prices, and historical data for various asset classes.
- **Quote Data**: Obtain real-time and historical quote data for stocks, crypto, forex, and commodities. Stay updated with the latest market prices and trends to make well-informed investment decisions.

With a focus on user-friendliness and customization, our FinancialModelingPrep Python Wrapper ensures that you can tailor API requests to meet your specific data requirements. Effortlessly integrate financial data into your Python projects and simplify data analysis with our Pandas DataFrame integration.

## Design Philosophy

The FinancialModelingPrep Python Wrapper is guided by key design principles.

- **Ease**: We make data access simple by using Pandas and requests to provide data in DataFrame format, favored in data science projects.
- **Integration**: Our wrapper seamlessly integrates with Python workflows, allowing you to transform and combine data with other tools and packages.
- **Comprehensive**: We maintain simplicity while offering a comprehensive view of financial data, ensuring you have the insights you need for informed decisions.
Experience an elegant, versatile, and powerful approach to financial data analysis with our wrapper.


## Applications

> The FinancialModelingPrep Python Wrapper offers a wealth of financial data and tools to transform how you make investment decisions. Explore its real-world applications, from trading bots to educational tools, and discover the potential of financial data in your projects.

1. **Automated Trading Bots**: Develop data-driven trading bots for financial markets.
2. **Portfolio Management**: Track and analyze investment portfolios.
3. **Financial Data Analysis**: Create interactive data apps for investment insights using Streamlit, Gradio, or Huggingface.
4. **Stock Screening Tools**: Build custom stock screeners for investment opportunities.
5. **Economic Indicator Tracking**: Monitor economic trends for investment decisions.
6. **Educational Tools**: Provide hands-on financial data analysis experiences.
7. **Financial Reporting**: Generate financial reports and insights.
8. **Risk Management**: Assess and manage investment risks.
9. **Automated Scripts**: Schedule data updates and analysis.
10. **Trading Strategy Research**: Analyze company financials and market news.
