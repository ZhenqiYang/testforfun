import pandas as pd

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','Dublin_bus.settings')

import django
django.setup()

from Dublin_map.models import BookInfo

def add_data(data1, data2):
    d, created = BookInfo.objects.get_or_create(btitle =data1, bpub_date=data2)
    print("- Data: {0}, Created: {1}".format(str(d), str(created)))
    return d


def populate():
    # data is a list of lists
    df = pd.read_csv('rt_trips_2017_I_DB_1000.txt', keep_default_na=True, sep=',\s+', delimiter=';',
                     skipinitialspace=True)
    print(df.head(5))
    data=df
    for index, row in data.iterrows():
        data1 = row['lineid']
        data2 = "1988-09-25"
        add_data(data1, data2)


if __name__ == "__main__":
    populate()