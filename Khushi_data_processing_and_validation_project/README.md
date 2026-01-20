#  User Data Cleaning & Feature Engineering Pipeline

##  Overview
This project implements a **Python data processing pipeline** using **pandas** to:
- Load raw user data from CSV
- Validate and clean inconsistent values
- Engineer meaningful features
- Export a clean, analysis-ready dataset


## 🛠 Technologies Used
- Python
- Pandas
- NumPy

## Input Dataset
**File:** `users_raw.csv`

### Expected Columns
| Column Name        | Description                  |
|--------------------|------------------------------|
| user_id            | Unique user identifier       |
| name               | User full name               |
| age                | Age of the user              |
| email              | User email address           |
| city               | City of residence            |
| signup_date        | Account creation date        |
| monthly_income     | Monthly income               |

---

## Pipeline Steps

###  Step 1 — Load & Validate
- Load CSV using pandas
- Validate:
  - Age between **1–100**
  - Email format using regex
  - Non-null user name
  - Valid date format for signup date


### Step 2 — Clean Data
- Replace invalid ages with **median age**
- Fill missing income values with **mean income**
- Fill missing city values with **most frequent city**
- Drop rows with **invalid email addresses**

### Step 3 — Feature Engineering
#### New Features Created:
- **age_group**
  - `<18`, `18–25`, `26–35`, `36–50`, `50+`
- **income_category**
  - `Low`, `Medium`, `High`

### final dataset is saved as clean_users.csv
