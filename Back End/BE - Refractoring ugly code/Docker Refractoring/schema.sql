drop table if exists one;
create table one (
    id integer PRIMARY KEY,
    body text,
    created_at datetime default current_timestamp
);

drop table if exists two;
create table two (
    id integer PRIMARY KEY,
    body text,
    body_len integer,
    created_at datetime default current_timestamp
);

drop table if exists three;
create table three (
    id integer PRIMARY KEY,
    keywords text,
    keywords_stats text,
    cost real not null,
    created_at datetime default current_timestamp
);

drop table if exists sms;
CREATE TABLE sms (
    id integer PRIMARY KEY,
    message text NOT NULL,
    phone_number text not null,
    created_at datetime default current_timestamp
);