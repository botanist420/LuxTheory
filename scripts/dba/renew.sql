CREATE TABLE users(
    id serial primary key,
    player varchar(255) not null,
    score real,
    team varchar(255)
);

INSERT INTO users(player, score, team) VALUES
('Curry', 28.3, 'Warriors'),
('Harden', 30.2, 'Rockets'),
('Leborn', 27.8, 'Cavs');

