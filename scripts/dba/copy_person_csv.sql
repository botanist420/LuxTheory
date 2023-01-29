\COPY persons(first_name, last_name, dob, email)
FROM '/home/adminlucaslee/Documents/GitHub/LuxTheory/data/person_email.csv'
DELIMITER ','
CSV HEADER;
