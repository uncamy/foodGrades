import pandas as pd
from pygeocoder import Geocoder
from time import sleep

zipcodes =pd.read_csv('./data/Zip_code_breakdowns.csv')
df = zipcodes[['JURISDICTION NAME']]
manhattan_zips= df[(df['JURISDICTION NAME'] < 10041)]


def geocode(address):
        lat_lon = Geocoder.geocode(address)
        sleep(2)
        return(lat_lon[0].coordinates)

def zip2geocode():
    print 'Starting geocode'
    manhattan_zips['geocode'] = manhattan_zips['JURISDICTION NAME'].map(geocode)
    print 'end geocoding'

zip2geocode()

manhattan_zips.to_csv('data/geocoded_zips.csv')
