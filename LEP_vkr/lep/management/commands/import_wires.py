import csv
from django.core.management.base import BaseCommand
from lep.models import WiresInfo


class Command(BaseCommand):
    def handle(self, *args, **options):
        file_path = 'wires_AC.csv'

        with open(file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile, delimiter=';')
            next(reader)

            for row in reader:
                wire = row[0]
                gen_cross_sec = float(row[1].replace(',', '.'))
                diametr = float(row[2].replace(',', '.'))
                weight = float(row[3].replace(',', '.'))
                coef_lin_exp = float(row[4].replace(',', '.'))
                mod_elast_mat = float(row[5].replace(',', '.'))
                max_vol = float(row[6].replace(',', '.'))
                avg_vol = float(row[7].replace(',', '.'))

                WiresInfo.objects.update_or_create(
                    wire=wire,
                    defaults={
                        'gen_cross_sec': gen_cross_sec,
                        'diametr': diametr,
                        'weight': weight,
                        'coef_lin_exp': coef_lin_exp,
                        'mod_elast_mat': mod_elast_mat,
                        'max_vol': max_vol,
                        'avg_vol': avg_vol
                    }
                )