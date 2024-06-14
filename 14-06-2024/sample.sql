-- DDL 
CREATE TABLE Books (
    book_id INT PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    author VARCHAR(100),
    price DECIMAL(10, 2),
    published_year YEAR
);


CREATE TABLE Members (
    member_id INT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    address VARCHAR(255),
    phone VARCHAR(15),
    join_date DATE
);

CREATE TABLE Rent (
    rent_id INT PRIMARY KEY,
    book_id INT,
    member_id INT,
    rent_date DATE,
    return_date DATE,
    FOREIGN KEY (book_id) REFERENCES Books(book_id),
    FOREIGN KEY (member_id) REFERENCES Members(member_id)
);

-- DML
INSERT INTO Books (book_id, title, author, price, published_year)
VALUES
(1, 'To Kill a Mockingbird', 'Harper Lee', 10.99, 1960),
(2, '1984', 'George Orwell', 9.99, 1949),
(3, 'The Great Gatsby', 'F. Scott Fitzgerald', 12.99, 1925);


INSERT INTO Members (member_id, name, address, phone, join_date)
VALUES
(1, 'John Doe', '123 Elm St', '555-1234', '2024-01-01'),
(2, 'Jane Smith', '456 Oak St', '555-5678', '2024-02-01');


INSERT INTO Rent (rent_id, book_id, member_id, rent_date, return_date)
VALUES
(1, 1, 1, '2024-03-01', '2024-03-15'),
(2, 2, 2, '2024-03-05', NULL);

-- Grant SELECT permission to a user 
GRANT SELECT ON Books TO 'library_user';
