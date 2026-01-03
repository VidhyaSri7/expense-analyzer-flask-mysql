# Smart Expense Analyzer

Smart Expense Analyzer is a web-based application designed to help users record, track, and analyze their daily financial transactions.  
The project focuses on providing a clear overview of income and expenses using a simple interface and visual insights.

This application was built to gain hands-on experience with full-stack development concepts, including backend logic, database interaction, and frontend rendering.

---

## Project Overview

Managing personal expenses without tracking often leads to poor financial awareness.  
This project allows users to:

- Record income and expense transactions
- Organize expenses by category
- View transaction history
- Analyze spending patterns visually
- Monitor overall balance

The application emphasizes **clarity, usability, and real-world data flow** rather than over-complicated features.

---

## Key Features

- User authentication (login & registration)
- Add income and expense transactions
- Category-wise expense tracking
- Automatic balance calculation
- Transaction history in tabular format
- Expense visualization using charts
- Clean and responsive user interface

---

## Tech Stack Used

### Backend
- Python
- Flask

### Frontend
- HTML5
- CSS3
- JavaScript

### Database
- MySQL

### Visualization
- Chart.js

### Tools
- Git
- GitHub
- VS Code

---

## Project Structure

SmartExpenseAnalyzer/
│
├── app.py # Flask application logic and routes
├── .gitignore # Ignored files and folders
├── README.md # Project documentation
│
├── templates/ # HTML templates
│ ├── index.html # Login page
│ ├── register.html # Registration page
│ ├── dashboard.html # Dashboard with analytics
│ ├── add_expense.html # Add income/expense page
│ └── transactions.html # Transaction list
│
├── static/
│ ├── style.css # Common styles
│ ├── dashboard.css # Dashboard-specific styles
│ └── js/
│ └── charts.js # Chart.js logic
│
└── screenshots/ # Application screenshots
├── login.png
├── dashboard.png
├── Add-transaction.png
└── Transactions-list.png

---

## How the Application Works

1. User registers or logs in securely
2. Transactions (income or expense) are added through a form
3. Data is stored in a MySQL database
4. Flask retrieves and processes transaction data
5. The dashboard displays:
   - Total income
   - Total expenses
   - Remaining balance
   - Category-wise expense charts
6. Users can view all past transactions in one place

This flow helped me understand backend-frontend communication and database operations in real scenarios.

---

## Screenshots

Screenshots of the application UI are included in the `screenshots/` folder to demonstrate the working and layout of the project.

---

## Learning Outcomes

- Implemented user authentication using Flask sessions
- Performed CRUD operations with MySQL
- Integrated backend data with frontend templates
- Used Chart.js for real-time data visualization
- Improved project structuring and code readability
- Understood secure handling of configuration using environment variables

---

## Future Enhancements

- Monthly and category-wise budget limits
- Budget vs actual expense comparison
- Alerts for overspending
- Export transactions to Excel or CSV
- Deployment on cloud platforms (AWS / Render)

---

## Project Classification

This project is currently an **Expense Analyzer**.  
Budget tracking features are planned as future enhancements.

---

## Author

**Vidhya Sri**  
Backend-focused developer (early career)

**Skills used in this project:**  
Python, Flask, MySQL, HTML, CSS, JavaScript

---