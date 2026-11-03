from flask import Flask, render_template, request
import re

app = Flask(__name__)

# Regular expression for robust server-side email validation
EMAIL_REGEX = re.compile(r"^[\w\.-]+@[\w\.-]+\.\w+$")

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    error = None
    name = ''
    email = ''
    message = ''

    if request.method == 'POST':
        # Retrieve and clean form data
        name = request.form.get('name', '').strip()
        email = request.form.get('email', '').strip()
        message = request.form.get('message', '').strip()

        # Server-side validation
        if not name:
            error = 'Name is required.'
        elif not email or not EMAIL_REGEX.match(email):
            error = 'A valid email address is required.'
        elif not message:
            error = 'Message is required.'
        else:
            # If all validations pass, render the confirmation page
            return render_template('success.html', name=name)

    # Render form (either on initial GET or if validation failed)
    return render_template('contact.html', error=error, name=name, email=email, message=message)

if __name__ == '__main__':
    app.run(debug=True)