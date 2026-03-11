from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("groups", "0001_initial"),
    ]

    operations = [
        migrations.RunSQL(
            """CREATE VIEW dwh_groups_group AS
                SELECT
                    uuid,
                    name AS naam
                FROM groups_group
            ;"""
        ),
    ]
