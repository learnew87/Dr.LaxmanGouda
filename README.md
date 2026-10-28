# Python Portfolio Website

A personal portfolio and landing page built with **Python** and **Flask**.

## Features
- **Responsive & Modern Design**: Works on mobile, tablet, and desktop screens.
- **Dark / Light Mode**: Instant toggle with `localStorage` memory.
- **Dynamic Content**: Easy configuration of profile, skills, and projects in `app.py`.
- **Working Contact Form**: Flask route with input validation and flash alerts.
- **Zero Heavy Frontend Dependencies**: Fast, lightweight vanilla CSS and JavaScript.

## How to Run

1. Navigate to the project directory:
   ```bash
   cd d:\Projects\portfolio
   ```

2. Create and activate a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   .\venv\Scripts\activate
   ```

3. Install requirements:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:
   ```bash
   python app.py
   ```

5. Open [http://127.0.0.1:5000](http://127.0.0.1:5000) in your web browser.

## Customizing Your Information
Open `app.py` and modify the `PROFILE`, `SKILLS`, and `PROJECTS` data structures to match your personal details.
