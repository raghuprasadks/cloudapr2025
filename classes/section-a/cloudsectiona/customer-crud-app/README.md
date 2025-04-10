# Customer CRUD Application

This is a simple Flask application that allows users to perform CRUD (Create, Read, Update, Delete) operations on customer data stored in a MySQL database. The application provides a user-friendly interface for managing customer information.

## Project Structure

```
customer-crud-app
├── static
│   └── styles.css          # CSS styles for the application
├── templates
│   ├── base.html           # Base template for the application
│   ├── home.html           # Home page template
│   ├── add_customer.html    # Form for adding a new customer
│   ├── edit_customer.html   # Form for editing an existing customer
│   └── view_customers.html  # Displays a list of all customers
├── app.py                  # Main application file
├── requirements.txt        # Project dependencies
└── README.md               # Project documentation
```

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd customer-crud-app
   ```

2. **Install dependencies:**
   It is recommended to use a virtual environment. You can create one using:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
   Then install the required packages:
   ```
   pip install -r requirements.txt
   ```

3. **Configure the database:**
   Make sure to set up a MySQL database and update the database connection details in `app.py`.

4. **Run the application:**
   ```
   python app.py
   ```
   The application will be accessible at `http://127.0.0.1:5000`.

## Usage

- Navigate to the home page to access different functionalities.
- Use the "Add Customer" link to add a new customer.
- View the list of customers and use the options to edit or delete customer records.

## License

This project is open-source and available under the MIT License.