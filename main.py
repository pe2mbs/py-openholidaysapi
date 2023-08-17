import traceback
from openholidaysapi import OpenHolidaysOrg


if __name__ == '__main__':
    proxies = {
            'http': 'http://ssoproxy.internal.zone:8080',
            'https': 'http://ssoproxy.internal.zone:8080',
        }
    try:
        api = OpenHolidaysOrg()
        # for country in api.getCountries( ( 'NL','EN' ) ):
        #     country.dump()
        #
        # for language in api.getLanguages( 'NL' ):
        #     language.dump()

        for holiday in api.getHolidays( 2023, 'NL', ( 'NL', 'EN' ) ):
            holiday.dump()

    except Exception:
        print( traceback.format_exc() )