# MyUtility-Django-Project

MyUtility-Django-Project is a comprehensive web application built using Django that integrates four main functionalities: a to-do list, notes, a calculator, and a weather app. This project aims to enhance productivity by providing essential tools on a single platform.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Features
- **To-Do List**: Add, edit, and delete tasks to keep track of your daily activities.
- **Notes**: Create, view, and manage notes with an easy-to-use interface. Preview your notes with a dedicated 'Preview' button.
- **Calculator**: Perform basic arithmetic calculations.
- **Weather**: Get the current weather information for any city.

## Installation

### Prerequisites
- Python 3.8+
- Django 3.2+
- Git

### Steps
1. Clone the repository:
   ```sh
   git clone https://github.com/Mridul-23/MyUtility-Django-Project.git
   cd MyUtility-Django-Project
   ```

2. Create and activate a virtual environment:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required dependencies:
   ```sh
   pip install -r requirements.txt
   ```

4. Apply migrations:
   ```sh
   python manage.py migrate
   ```

5. Create a superuser to access the admin interface:
   ```sh
   python manage.py createsuperuser
   ```

6. Run the development server:
   ```sh
   python manage.py runserver
   ```

7. Open your browser and navigate to `http://127.0.0.1:8000/` to access the application.

## Usage

### To-Do List
- Navigate to the To-Do List section to add new tasks.
- Use the edit and delete buttons to manage your tasks.

### Notes
- Navigate to the Notes section to create new notes.
- Each note row has a 'Preview' button for a quick view of the note's content.

### Calculator
- Navigate to the Calculator section to perform arithmetic calculations.

### Weather
- Navigate to the Weather section to get current weather information for any city by entering the city name.

## Project Structure

```
MyUtility-Django-Project/
│
├── manage.py
├── requirements.txt
├── README.md
├── todo/                   # To-Do List app
│   ├── migrations/
│   ├── templates/
│   ├── static/
│   ├── views.py
│   └── ...
├── notes/                  # Notes app
│   ├── migrations/
│   ├── templates/
│   ├── static/
│   ├── views.py
│   └── ...
├── calc/                   # Calculator app
│   ├── migrations/
│   ├── templates/
│   ├── static/
│   ├── views.py
│   └── ...
├── weather/                # Weather app
│   ├── migrations/
│   ├── templates/
│   ├── static/
│   ├── views.py
│   └── ...
└── MyUtility/
    ├── settings.py
    ├── urls.py
    └── ...
```

## Contributing
Contributions are welcome! Please follow these steps to contribute:
1. Fork the repository.
2. Create a new branch: `git checkout -b feature/your-feature-name`
3. Make your changes and commit them: `git commit -m 'Add some feature'`
4. Push to the branch: `git push origin feature/your-feature-name`
5. Open a pull request.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Feel free to explore, use, and contribute to the project!