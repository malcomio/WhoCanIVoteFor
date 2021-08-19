# Generated by Django 2.2.20 on 2021-06-04 12:45

from django.db import migrations
from django.db.models import OuterRef, Subquery
from django.utils import timezone

REFORM_UK_ID = "party:7931"
CHANGE_DATE = timezone.datetime(2021, 1, 6).date()


def add_party_name(apps, schema_editor):

    PersonPost = apps.get_model("people", "PersonPost")

    brexit_candidacies = PersonPost.objects.filter(
        party__party_id=REFORM_UK_ID,
        post_election__election__election_date__lt=CHANGE_DATE,
    )
    brexit_candidacies.update(party_name="Brexit Party")

    # update the rest
    subquery = PersonPost.objects.filter(pk=OuterRef("pk")).values(
        "party__party_name"
    )[:1]
    PersonPost.objects.filter(party_name="").update(
        party_name=Subquery(subquery)
    )


def remove_party_names(apps, schema_editor):
    PersonPost = apps.get_model("people", "PersonPost")
    PersonPost.objects.update(party_name="")


class Migration(migrations.Migration):

    dependencies = [
        ("people", "0037_auto_20210604_1245"),
    ]

    operations = [
        migrations.RunPython(
            code=add_party_name,
            reverse_code=remove_party_names,
        )
    ]