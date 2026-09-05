# Pandas + Matplotlib Data Visualization 📊

Beginner Python practice project for reading employee data from an Excel file using **Pandas** and visualizing the data using **Matplotlib**.

## 📌 Project Overview

This project demonstrates how to read employee data from an Excel file and create different types of charts.

The project covers:

* Reading Excel files with Pandas
* Working with DataFrames
* Selecting DataFrame columns
* Creating Line Charts
* Creating Bar Charts
* Creating Scatter Plots
* Creating Pie Charts
* Counting categorical values with `value_counts()`
* Customizing chart titles and labels
* Rotating X-axis labels
* Improving chart layout

## 🛠️ Technologies Used

* Python
* Pandas
* Matplotlib
* Excel

## 📂 Project Structure

```text
pandas-matplotlib-data-visualization/
│
├── pandas_matplotlib_data_visualization.py
├── Employee.xlsx
├── requirements.txt
└── README.md
```

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/YOUR-USERNAME/pandas-matplotlib-data-visualization.git
```

Move into the project directory:

```bash
cd pandas-matplotlib-data-visualization
```

Install the required libraries:

```bash
pip install -r requirements.txt
```

## 📋 Requirements

The project uses:

```text
pandas
matplotlib
openpyxl
```

## ▶️ How to Run

Make sure `Employee.xlsx` is in the same folder as the Python file.

Then run:

```bash
python pandas_matplotlib_data_visualization.py
```

The program will read the employee data and display different charts.

## 📊 Charts Included

### 1. Line Chart

The Line Chart displays employee ages according to their names.

```python
plt.plot(
    df["Name"],
    df["Age"],
    marker="*"
)
```

* X-axis → Employee names
* Y-axis → Employee ages
* Marker → `*`

### 2. Bar Chart

The Bar Chart displays employee ages using vertical bars.

```python
plt.bar(
    df["Name"],
    df["Age"]
)
```

### 3. Scatter Plot

The Scatter Plot displays employee names and ages as individual points.

```python
plt.scatter(
    df["Name"],
    df["Age"]
)
```

### 4. Pie Chart

The Pie Chart shows the distribution of employees across departments.

First, the number of employees in each department is calculated:

```python
department_count = df["Department"].value_counts()
```

Then the results are displayed using:

```python
plt.pie(
    department_count,
    labels=department_count.index,
    autopct="%1.1f%%"
)
```

## 🔑 Important Functions

| Function             | Purpose                      |
| -------------------- | ---------------------------- |
| `pd.read_excel()`    | Read data from an Excel file |
| `plt.plot()`         | Create a Line Chart          |
| `plt.bar()`          | Create a Bar Chart           |
| `plt.scatter()`      | Create a Scatter Plot        |
| `plt.pie()`          | Create a Pie Chart           |
| `plt.title()`        | Add a chart title            |
| `plt.xlabel()`       | Label the X-axis             |
| `plt.ylabel()`       | Label the Y-axis             |
| `plt.xticks()`       | Customize X-axis ticks       |
| `plt.tight_layout()` | Improve chart layout         |
| `plt.show()`         | Display the chart            |
| `value_counts()`     | Count unique values          |

## 🎯 Learning Goals

After completing this project, you should understand:

* How Pandas works with Excel data
* How to select DataFrame columns
* How Matplotlib creates different charts
* The difference between Line, Bar, Scatter, and Pie Charts
* How to customize chart titles and axes
* How to visualize categorical data
* How to prepare a basic data visualization project

## 🚀 Future Improvements

Possible improvements for this project:

* Add more employee data
* Create charts for salary analysis
* Compare departments
* Add average salary visualization
* Add employee age distribution
* Customize chart styles
* Save charts as image files

## 👨‍💻 Author

Nader

## 📄 License

This project is created for learning and practice purposes.
