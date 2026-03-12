from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("categories", "0001_initial"),
    ]

    operations = [
        migrations.RunSQL(
            """CREATE VIEW dwh_categories_category AS
                SELECT
                    uuid,
                    name AS naam,
                    group_id AS group_uuid
                FROM categories_category
            ;"""
        ),
    ]
