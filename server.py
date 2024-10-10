from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

cars = []  # To store car information


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get the form values from the HTML form
        name = request.form.get('name')
        car = request.form.get('car')
        car_type = request.form.get('type')
        model = request.form.get('model')

        # Validate if all fields are filled
        if not all([name, car, car_type, model]):
            return render_template('index.html', error="All fields are required!")

        # Create a car dictionary to store the form data
        car_info = {
            'name': name,
            'car': car,
            'car_type': car_type,
            'model': model
        }
        cars.append(car_info)  # Add the car info to the list

        return redirect(url_for('view_cars'))  # Redirect to the car view page

    return render_template('index.html')  # Render the form page


@app.route('/view_cars')
def view_cars():
    return render_template('view_cars.html', cars=cars)  # Render the cars in a card layout


if __name__ == '__main__':
    app.run(debug=True)
