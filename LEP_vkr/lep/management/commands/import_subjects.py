import sqlite3
from django.core.management.base import BaseCommand
from lep.models import SubjectInfo


class Command(BaseCommand):
    def handle(self, *args, **options):
        conn = sqlite3.connect('subjects_data.db')
        cursor = conn.cursor()

        cursor.execute('SELECT * FROM subjects')
        subjects = cursor.fetchall()

        for subject in subjects:
            SubjectInfo.objects.update_or_create(
                subject=subject[0],
                defaults={
                    'ice_zone': subject[1],
                    'wind_zone': subject[2],
                    'avg_year_temp': subject[3],
                    'min_temp': subject[4],
                    'max_temp': subject[5]
                }
            )

        conn.close()