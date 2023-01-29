COPY persons(first_name, last_name, dob, email)
FROM 'person_email.csv'
DELIMITER ','
CSV HEADER;
