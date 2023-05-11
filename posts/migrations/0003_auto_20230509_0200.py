# Generated by Django 4.2 on 2023-05-09 02:00

from django.db import migrations

def populate_status(apps, schemaeditor):
    statuses = {
        "published": "A post that is visible to all on the site",
        "draft": "A post thta only the author can see(and interact with)",
        "archived": "A post thta is only visible to all logged in users"
    }
    Status = apps.get_model("posts", "Status")
    for key, value in statuses.items():
        status_obj = Status(name=key, description=value)
        status_obj.save()

class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_status_post_status'),
    ]

    operations = [
        migrations.RunPython(populate_status)
    ]
