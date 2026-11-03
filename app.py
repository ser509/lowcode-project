import re
from flask import Flask, render_template, request


app = Flask(__name__)
EMAIL_PATTERN = re.compile(
    r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9-]+(\.[A-Za-z0-9-]+)*\.[A-Za-z]{2,}$"
)
def validate_form(name, email, message):
    """Return a list of error messages. An empty list means the input is valid."""
    errors = []

    if not name:
        errors.append("Please enter your name.")

    if not email:
        errors.append("Please enter your email address.")
    elif len(email) > 254 or not EMAIL_PATTERN.match(email):
        errors.append("Please enter a valid email address.")

    if not message:
        errors.append("Please enter a message.")

    return errors

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        # .strip() removes spaces at the start/end, so "   " counts as empty
        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip()
        message = request.form.get("message", "").strip()

        errors = validate_form(name, email, message)

        if errors:
            # Show the form again with the errors and keep what the user typed.
            # 400 means "bad request" -- the browser still displays the page.
            return (
                render_template(
                    "contact.html",
                    errors=errors,
                    name=name,
                    email=email,
                    message=message,
                ),
                400,
            )

        # Valid input: show the confirmation page.
        # Nothing is saved anywhere -- the data only exists during this request.
        return render_template("confirmation.html", name=name)

    # GET request: show an empty form
    return render_template("contact.html", errors=[], name="", email="", message="")


@app.route("/")

def home():

    return "<h1>Hello from Serena</h1>"
    
if __name__ == "__main__":
        app.run(debug=True)