from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("groups", "0002_dwh_groups_group_view"),
    ]

    operations = [
        migrations.RunSQL("DROP VIEW IF EXISTS dwh_groups_group;"),
        migrations.RunSQL(
            """CREATE VIEW dwh_groups_group AS
                SELECT
                    uuid,
                    name
                FROM groups_group
            ;"""
        ),
    ]
