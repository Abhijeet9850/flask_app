# Flask + MongoDB Form Submission & JSON API

This project is a Flask web application with the following features:

- An `/api` route that returns a JSON list from a local file.
- A frontend form that submits data to **MongoDB Atlas**.
- A success page on successful submission and inline error display on failure.

---

## Features

1. **GET /api**  
   Returns a JSON list read from `data.json`.

2. **Form Submission**
   - Submits user data (Name, Email) to MongoDB Atlas.
   - Redirects to a success page if successful.
   - Displays error inline on the same page if submission fails.
