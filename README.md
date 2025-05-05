# LMS Portal 🎓

![LMS Portal](https://img.shields.io/badge/LMS_Portal-v1.0-blue.svg) ![GitHub](https://img.shields.io/badge/GitHub-LMS%20Portal-lightgrey.svg)

Welcome to the **LMS Portal**! This full-stack student management system allows users to enroll in courses, take exams, and access various resources. Additionally, it features an admin portal for teachers to manage their courses and students effectively.

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Features

- **Course Enrollment**: Students can easily enroll in various courses.
- **Exam Management**: Students can take exams and view their results.
- **Admin Portal**: Teachers can manage courses and track student progress.
- **User Authentication**: Secure login for both students and teachers.
- **Responsive Design**: Built with Tailwind CSS for a modern and clean interface.
- **Real-time Data**: Utilizes Redis for efficient data caching.

## Technologies Used

This project is built using a variety of technologies to ensure a smooth and efficient experience:

- **Frontend**: React, TypeScript, Axios, Tailwind CSS
- **Backend**: Django, Python, Django ORM
- **Database**: MySQL
- **Caching**: Redis
- **Cookies Management**: js-cookie
- **Server-side Rendering**: Next.js

## Installation

To set up the LMS Portal on your local machine, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/roshithbro56/LMS-Portal.git
   cd LMS-Portal
   ```

2. **Install backend dependencies**:
   Navigate to the backend directory and install the required packages.
   ```bash
   cd backend
   pip install -r requirements.txt
   ```

3. **Set up the database**:
   Ensure that MySQL is installed and create a database for the project. Update the database settings in `settings.py`.

4. **Run migrations**:
   Apply the migrations to set up the database schema.
   ```bash
   python manage.py migrate
   ```

5. **Run the server**:
   Start the Django server.
   ```bash
   python manage.py runserver
   ```

6. **Install frontend dependencies**:
   Navigate to the frontend directory and install the required packages.
   ```bash
   cd ../frontend
   npm install
   ```

7. **Run the frontend**:
   Start the React application.
   ```bash
   npm start
   ```

8. **Access the application**:
   Open your browser and navigate to `http://localhost:3000`.

## Usage

Once the application is running, you can access it through your web browser. Here are some key functionalities:

- **Student Login**: Use your credentials to log in as a student.
- **Course Dashboard**: View available courses and enroll in them.
- **Exam Section**: Take exams and check results.
- **Admin Panel**: Teachers can log in to manage courses and student data.

For a downloadable version of the latest release, visit [Releases](https://github.com/roshithbro56/LMS-Portal/releases). Download the necessary files and execute them to get started.

## Contributing

We welcome contributions to the LMS Portal! If you would like to contribute, please follow these steps:

1. **Fork the repository**.
2. **Create a new branch**:
   ```bash
   git checkout -b feature/YourFeature
   ```
3. **Make your changes** and commit them:
   ```bash
   git commit -m "Add your message here"
   ```
4. **Push to the branch**:
   ```bash
   git push origin feature/YourFeature
   ```
5. **Open a pull request**.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any inquiries or issues, feel free to reach out:

- **Author**: Roshith
- **Email**: roshith@example.com
- **GitHub**: [roshithbro56](https://github.com/roshithbro56)

## Final Note

We hope you find the LMS Portal useful. For updates and new releases, check the [Releases](https://github.com/roshithbro56/LMS-Portal/releases) section regularly.

Thank you for your interest! 🎉