In this repo, I used docker-compose to run python and mysql.

### Refer docker-compose.yml

When you do : “docker compose up” command in the directory.

It builds python app with port number 5000.

It pulls mysql if not already there and runs in port 3306.

sets password.

automatically creates two volumes following the below pattern.

1. docker-compose-demo-2_mysql : docker-compose-demo-2 is the folder name, mysql is we mentioned in volumes.
2. docker-compose-demo-2_mysql_config : docker-compose-demo-2 is the folder name, mysql_config is we mentioned in volumes.

Once the docker-compose completed, you can see a project in the containers in docker desktop and inside that two containers would be running..

For this project, I am trying to use DB colorsdb and table favorite_colors..

Hence I must have that in the DB..

So open another cmd prompt and go to mysql container by giving below command.

### docker exec -ti docker-compose-demo-2-db-1 mysql -u root -p

docker-compose-demo-2-db-1 - container name

create database colorsdb;

use colorsdb;

create table favorite_colors(name VARCHAR(20), color VARCHAR(20));

insert into favorite_colors values(‘grace’,‘green’)



Now run localhost 5000..

Python tries to connect to colorsdb ad fetches data..



