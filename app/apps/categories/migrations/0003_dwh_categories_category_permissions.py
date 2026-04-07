from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("categories", "0002_dwh_categories_category_view"),
    ]

    operations = [
        migrations.RunSQL("GRANT SELECT ON TABLE dwh_categories_category TO dwh;"),
        migrations.RunSQL(
            "GRANT SELECT ON TABLE dwh_categories_category TO CURRENT_ROLE;"
        ),
    ]
