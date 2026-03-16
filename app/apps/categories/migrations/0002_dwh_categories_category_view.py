from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("categories", "0001_initial"),
    ]

    operations = [
        migrations.RunSQL("DROP VIEW IF EXISTS dwh_categories_category;"),
        migrations.RunSQL(
            """CREATE VIEW dwh_categories_category AS
                 SELECT uuid,
                    name,
                    slug,
                    public_name,
                    description_private,
                    description_public,
                    is_public_accessible,
                    is_active,
                    group_id
                   FROM categories_category;
            ;"""
        ),
    ]
