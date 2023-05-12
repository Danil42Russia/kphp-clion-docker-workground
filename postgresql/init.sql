create table Teams(team_id int, team_name varchar(12));
create table Workers(worker_id int, name varchar(30), team_id int);
insert into Teams(team_id, team_name)
values
    (1, 'Compiler'),
    (2, 'Runtime'),
    (3, 'Plugin');
select team_id, team_name from Teams;
update Teams set team_name = 'PhpStorm' where team_id = 3;
insert into Workers(worker_id, name, team_id)
values
    (1, 'Vadim', 2),
    (2, 'Denis', 2),
    (3, 'Danil', 3),
    (4, 'Vlad', 2),
    (5, 'Misha', 1),
    (6, 'Slava', 2);
