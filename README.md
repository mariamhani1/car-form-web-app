# Car Information Form Project

## Overview

This project is a simple web application that allows users to submit car information via a form. It displays the entered car details on a separate page. The application is built using the Flask framework for Python and includes basic HTML and CSS for the frontend.

## Features

- Users can fill out a form to provide car owner information, car brand, type (Manual/Automatic), and model year.
- After submitting the form, the data is validated to ensure all fields are filled in.
- The car information is stored in a list and displayed on a separate page in a card format.
- Users can add multiple cars, and each entry will be listed dynamically.

## Technologies Used

- **Python**: Flask framework for handling routes and logic.
- **HTML/CSS**: For creating the frontend form and displaying the car information.
- **Jinja2**: For rendering dynamic content in HTML templates.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/car-info-form.git
   ```
2. Navigate to the project directory:
   ```bash
   cd car-info-form
   ```
3. Install the required dependencies:
   ```bash
   pip install flask
   ```

## Running the Project

1. Start the Flask application by running the following command:
   ```bash
   python app.py
   ```
2. Open your web browser and go to:
   ```
   http://127.0.0.1:5000/
   ```

## Project Structure

```
car-info-form/
│
├── static/
│   └── css/
│       └── style.css  # Styling for the form and car details page
│
├── templates/
│   ├── index.html     # Form page where users enter car details
│   └── view_cars.html # Page displaying the entered car information
│
├── app.py             # Main Flask application file
└── README.md          # Project readme file
```

## Routes

- **`/`**: The main page with the form for car entry. Accepts both GET and POST requests.
- **`/view_cars`**: Displays all submitted cars in a card format.

## Form Fields

- **Owner Name**: The name of the car owner.
- **Car Brand**: The brand of the car (e.g., Toyota, Ford).
- **Car Type**: A dropdown menu to select either "Manual" or "Automatic".
- **Model**: The model year of the car.

## How to Use

1. Open the form and fill in the required fields.
2. After submitting, you will be redirected to a page displaying the car details.
3. Click "Add Another Car" to submit more cars.

## Contributing

Feel free to fork this repository and submit pull requests with any improvements, such as adding a database, enhancing the form validation, or extending the functionality.

## License

This project is licensed under the MIT License.

