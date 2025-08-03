CREATE TABLE sellers
    (
        id serial primary key,
        name varchar not null,
        surname varchar not null,
        age int not null,
        experience int not null,
        sales int
    );

INSERT INTO sellers (name, surname, age, experience, sales) VALUES
    ('alex', 'aasf', 12, 324, 44);

CREATE TABLE cars
(
    id serial primary key,
    mark varchar not null,
    technical_condition varchar not null,
    kilometerage int,
    number_of_owners int,
    traffic_accidents boolean
);

INSERT INTO cars (mark, technical_condition, kilometerage, number_of_owners, traffic_accidents) VALUES
    ('ar12','good', 2421, 2, true);