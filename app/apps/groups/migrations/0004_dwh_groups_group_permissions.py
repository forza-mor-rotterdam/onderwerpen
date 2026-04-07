from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("groups", "0003_dwh_view_col_rename"),
    ]

    operations = [
        migrations.RunSQL("GRANT SELECT ON TABLE dwh_groups_group TO dwh;"),
        migrations.RunSQL(
            "GRANT SELECT ON TABLE dwh_groups_group TO CURRENT_ROLE;"
        ),
    ]
