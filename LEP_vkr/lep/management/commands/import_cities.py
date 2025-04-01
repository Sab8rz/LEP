import sqlite3
from django.core.management.base import BaseCommand
from lep.models import CityInfo


class Command(BaseCommand):
    def handle(self, *args, **options):
        conn = sqlite3.connect('cities_data.db')
        cursor = conn.cursor()

        cursor.execute('SELECT * FROM cities')
        cities = cursor.fetchall()

        for city in cities:
            CityInfo.objects.update_or_create(
                city=city[0],
                defaults={
                    'ice_zone': city[1],
                    'wind_zone': city[2],
                    'avg_year_temp': city[3],
                    'min_temp': city[4],
                    'max_temp': city[5]
                }
            )

        conn.close()