CREATE DATABASE mynewdatabase;
USE mynewdatabase;
CREATE TABLE student_info(
	st_id int(3) primary key,
	st_name varchar(30) not null,
    st_address varchar(300) not null,
    st_phone_no bigint not null,
    st_major varchar(50)
);

INSERT INTO student_info (st_id, st_name, st_address, st_phone_no, st_major) VALUES
(1, 'Aarav Sharma', '123 MG Road, Delhi', 9876543210, 'Computer Science'),
(2, 'Vivaan Gupta', '456 Lal Bagh, Mumbai', 9876543211, 'Mechanical Engineering'),
(3, 'Aditya Patel', '789 Sector 21, Noida', 9876543212, 'Electrical Engineering'),
(4, 'Arjun Singh', '101 Indira Nagar, Lucknow', 9876543213, 'Civil Engineering'),
(5, 'Ananya Mehta', '202 Banjara Hills, Hyderabad', 9876543214, 'Information Technology'),
(6, 'Diya Kapoor', '303 Whitefield, Bangalore', 9876543215, 'Chemical Engineering'),
(7, 'Ishaan Desai', '404 Marine Drive, Mumbai', 9876543216, 'Biotechnology'),
(8, 'Kavya Nair', '505 Salt Lake, Kolkata', 9876543217, 'Aerospace Engineering'),
(9, 'Laksh Jain', '606 Anna Nagar, Chennai', 9876543218, 'Environmental Science'),
(10, 'Meera Roy', '707 Gariahat, Kolkata', 9876543219, 'Physics');
