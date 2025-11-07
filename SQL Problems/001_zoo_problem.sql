insert into animals(name, type, country_id)
values('Slim', 'Giraffe', 1);


select a.name, a.type, c.country from animals as a
inner join countries as c on
a.country_id=c.id order by c.country;