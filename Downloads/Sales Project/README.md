# 📊 Sales Performance Dashboard

[![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)](https://www.python.org/)
[![Made with Pandas](https://img.shields.io/badge/Made%20with-Pandas-150458.svg?logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This project is a Python-based data analytics dashboard built using the popular **Sample Superstore** dataset. It analyzes sales performance by month, region, product, and discount impact — helping extract actionable business insights.

---

## 📁 Dataset
- File: `Sample_Superstore.xls`
- Format: Microsoft Excel (.xls)
- Source: Tableau Sample Dataset

---

## 🎯 Key Objectives
- Analyze monthly sales trends
- Identify top-selling products
- Explore regional sales distribution
- Visualize how discounts affect profit

---

## 🛠️ Tools & Technologies
- **Python** (Pandas, Matplotlib)
- **Excel** (.xls data source)
- **Git & GitHub** for version control
- **VS Code** for development

---

## 📊 Visualizations

| Chart | Description |
|-------|-------------|
| `monthly_sales_trend.png` | Monthly sales trend line chart |
| `top_10_products.png` | Bar chart of top 10 best-selling products |
| `sales_by_region.png` | Sales by region visualization |
| `discount_vs_profit.png` | Scatter plot showing effect of discounts on profit |

All charts are saved to the `dashboard_output/` folder.

---

## 🚀 How to Run This Project

```bash
# Clone the repo
git clone https://github.com/Srayareddy-tech/sales-performance-dashboard.git
cd sales-performance-dashboard

# (Optional) Create virtual environment
python -m venv venv
source venv/bin/activate    # On Windows: venv\Scripts\activate

# Install required libraries
pip install -r requirements.txt

# Run the script
python sales_dashboard.py