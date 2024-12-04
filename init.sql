USE ninjavan;

-- Create the 'users' table
CREATE TABLE users (
    id INT PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    metadata TEXT NOT NULL,
    -- Use TEXT instead of JSON
    created_at DATETIME NOT NULL
);

CREATE TABLE `groups` (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description VARCHAR(255) NOT NULL,
    created_at DATETIME NOT NULL
);

INSERT INTO
    users (id, username, metadata, created_at)
VALUES
    (
        1,
        'kat@email.com',
        '{"secret": "gQTKNMafpw", "provider": "google-oauth2"}',
        '2023-09-01 08:01:02'
    ),
    (
        2,
        'mani@email.com',
        '{"secret": "sjmaIS2EmA", "provider": "basic-auth"}',
        '2023-09-01 08:01:03'
    );

INSERT INTO
    `groups` (id, name, description, created_at)
VALUES
    (
        1,
        'SUPER_USER',
        'Full access to all functions.',
        '2015-01-01 04:05:06'
    ),
    (
        2,
        'DEFAULT_USER',
        'Initial role assigned to a new user.',
        '2015-01-01 05:06:07'
    );