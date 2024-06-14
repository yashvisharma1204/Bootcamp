CREATE DATABASE lms;
USE lms;
CREATE TABLE users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    user_type ENUM('student', 'instructor', 'admin') NOT NULL
);

CREATE TABLE courses (
    course_id INT AUTO_INCREMENT PRIMARY KEY,
    course_name VARCHAR(100) NOT NULL,
    instructor_id INT,
    FOREIGN KEY (instructor_id) REFERENCES users(user_id)
);

CREATE TABLE enrollments (
    enrollment_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    course_id INT,
    FOREIGN KEY (user_id) REFERENCES users(user_id),
    FOREIGN KEY (course_id) REFERENCES courses(course_id)
);

CREATE TABLE lessons (
    lesson_id INT AUTO_INCREMENT PRIMARY KEY,
    course_id INT,
    lesson_title VARCHAR(255) NOT NULL,
    content TEXT,
    FOREIGN KEY (course_id) REFERENCES courses(course_id)
);

CREATE TABLE assignments (
    assignment_id INT AUTO_INCREMENT PRIMARY KEY,
    course_id INT,
    title VARCHAR(255) NOT NULL,
    description TEXT,
    due_date DATE,
    FOREIGN KEY (course_id) REFERENCES courses(course_id)
);

CREATE TABLE tests (
    test_id INT AUTO_INCREMENT PRIMARY KEY,
    course_id INT,
    title VARCHAR(255) NOT NULL,
    test_date DATE,
    FOREIGN KEY (course_id) REFERENCES courses(course_id)
);

CREATE TABLE grades (
    grade_id INT AUTO_INCREMENT PRIMARY KEY,
    test_id INT,
    user_id INT,
    grade DECIMAL(5,2),
    FOREIGN KEY (test_id) REFERENCES tests(test_id),
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

CREATE TABLE timetable (
    entry_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    course_id INT,
    class_date DATE,
    start_time TIME,
    end_time TIME,
    FOREIGN KEY (user_id) REFERENCES users(user_id),
    FOREIGN KEY (course_id) REFERENCES courses(course_id)
);
