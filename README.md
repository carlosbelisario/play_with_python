#migraciones con peewee orm y peewee-migrate 

renombrar .env.example a .env para tener tus variables de entorno 

en una concola instalar peewee y peewee migrate 

`pip install -r requirements.txt`

ejecutar migraciones 

`pw_migrate migrate` este comando ejecuta las migraciones creadas 

crear una nueva migracion 

`pw_migrate create create_new_table` donde create_new_table es el nombre del archivo que se va a generar en la carpeta migration


revisar la documentacion para entender un poco mas el ORM 
https://docs.peewee-orm.com/en/latest/
https://github.com/klen/peewee_migrate 