import sys 
sys.path.append('/home/www-data/web2py')
from gluon import DAL, Field

db4=DAL('postgres://postgres:ituser123@localhost:5433/vpak',migrate_enabled=False, pool_size=20, lazy_tables=True, fake_migrate_all=False)

db4.define_table('geocode',
                 Field('zip', 'string'),
                 Field('city', 'string'),
                 Field('state','string'),
                 Field('longitude','string'),
                 Field('latitude','string'))

flat = '88.10'
flon = '47.1'
fradius = 50

rows = db4.executesql("select city,longitude,latitude, radians(cast(latitude as float)),radians({0}), radians({1}) from geocode where city like 'Bolingbrook'".format(flat, flon))

print rows[1]
