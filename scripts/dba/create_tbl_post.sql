CREATE TABLE post(
    title varchar(255),
    content text CHECK(length(content) > 8)
);
