from contextlib import suppress

import peewee as pw
from peewee_migrate import Migrator


with suppress(ImportError):
    import playhouse.postgres_ext as pw_pext


def migrate(migrator: Migrator, database: pw.Database, *, fake=False):
    Brand = migrator.orm['brand']
    @migrator.create_model
    class Car(pw.Model):
        brand = pw.ForeignKeyField(Brand)
        model = pw.CharField()
        color = pw.CharField()
    


def rollback(migrator: Migrator, database: pw.Database, *, fake=False):
    """Write your rollback migrations here."""
    
