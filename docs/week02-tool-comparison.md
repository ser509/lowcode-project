# Week 2 – AI Tool Comparison

## 1. Correctness
Both Claude and Gemini solutions were tested locally.

Both applications:
•⁠  ⁠Accepted valid name, email and message inputs.
•⁠  ⁠Rejected invalid email addresses.
•⁠  ⁠Displayed error messages when required fields were empty.
•⁠  ⁠Displayed a confirmation page when all inputs were valid.

Both solutions passed the main functional tests.

## 2. Code Quality
Both solutions used Python and Flask.

Claude provided a structured validation function and included an additional check to ensure that email addresses did not exceed 254 characters.

Gemini provided a simpler implementation that was easy to understand.

## 3. Completeness
Both solutions implemented the requested contact form with name, email and message fields, server-side validation and a confirmation page.

Both required HTML files to be placed inside Flask's templates folder for the applications to run correctly.

## 4. Security
Both solutions performed server-side input validation, including email validation.

Neither solution stores submitted information in a database, as requested.

This is a basic exercise and does not include advanced security features such as CSRF protection or rate limiting.

## 5. Conclusion
Claude is the preferred solution because its validation logic is more structured and includes an additional email-length check.

The Claude implementation was integrated into the main Flask application and successfully tested.