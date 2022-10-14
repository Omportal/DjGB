from django.db import migrations

def forwards_func(apps, schema_editor):
    # We get the model from the versioned app registry;
    # if we directly import it, it'll be the wrong version
    News = apps.get_model("mainapp", "News")
    db_alias = schema_editor.connection.alias
    News.objects.using(db_alias).bulk_create([
        News(title="USA", preambule="us", body='body'),
        News(title="France", preambule="fr", body='body'),
    ])

def reverse_func(apps, schema_editor):
    # forwards_func() creates two Country instances,
    # so reverse_func() should delete them.
    News = apps.get_model("mainapp", "News")
    db_alias = schema_editor.connection.alias
    News.objects.using(db_alias).filter(title="USA", preambule="us", body='body').delete()
    News.objects.using(db_alias).filter(title="France", preambule="fr", body='body').delete()
class Migration(migrations.Migration):

    dependencies = [
        ('mainapp','0001_initial'),
    ]

    operations = [
            migrations.RunPython(forwards_func, reverse_func),
    ]