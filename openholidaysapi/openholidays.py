from typing import Optional, Union, List
import requests
from openholidaysapi.countries import CountryObject
from openholidaysapi.holidays import HolidayObject
from openholidaysapi.languages import LanguageObject
from openholidaysapi.exceptions import OpenHolidaysOrgException


class OpenHolidaysOrg( object ):
    def __init__( self, proxies: Optional[dict] = None ):
        self.session = requests.session()
        self.session.proxies = proxies if isinstance( proxies, dict ) else {}
        self.session.headers = {}
        return

    def __execute( self, url, params, cls, **kwargs ) -> list:
        resultList = []
        result = self.session.get( url, params = params )
        if result.status_code == 200:
            for record in result.json():
                kwargs.update( **record )
                resultList.append( cls( **kwargs ) )

        else:
            raise OpenHolidaysOrgException(result.text, result.status_code)

        return resultList

    def getCountries( self, iso_language_code: Union[str,list,tuple] ) -> List[CountryObject]:
        if isinstance( iso_language_code, ( list, tuple ) ):
            resultList = []
            for country_code in iso_language_code:
                CountryObject.mergeLists( self.getCountries( country_code ), resultList )

            return resultList


        if not isinstance( iso_language_code, str ) or len( iso_language_code ) != 2:
            raise ValueError( "language_code must a s string of 2 characters" )

        return self.__execute( "https://openholidaysapi.org/Countries",
                               {
                                   'languageIsoCode': iso_language_code,
                               },
                               CountryObject )

    def getLanguages( self, iso_language_code: Union[str,list,tuple] ) -> List[LanguageObject]:
        if isinstance(iso_language_code, (list, tuple)):
            resultList = []
            for lang in iso_language_code:
                LanguageObject.mergeLists(self.getLanguages(lang), resultList)

            return resultList

        if not isinstance( iso_language_code, str ) or len( iso_language_code ) != 2:
            raise ValueError( "language_code must a s string of 2 characters" )

        return self.__execute("https://openholidaysapi.org/Languages",
                              {
                                  'languageIsoCode': iso_language_code,
                              },
                              LanguageObject)


    def getHolidays( self, year: int, iso_country_code: str, iso_language_code: Union[str,list,tuple] = None ) -> List[HolidayObject]:
        if not isinstance( iso_country_code, str ) or len( iso_country_code ) != 2:
            raise ValueError( "country_code must be a string of 2 chaccters")

        if iso_language_code is None:
            iso_language_code = iso_country_code

        if not isinstance( iso_language_code, (str,list,tuple)):
            raise ValueError( "language_code must be str, list or tuple" )

        if not isinstance( year, ( int, str ) ):
            raise ValueError( "year must be int or str of 4 digits" )

        elif isinstance( year, int ):
            if year < 50:
                year = 2000 + year

            elif year < 100:
                year = 1900 + year

        elif isinstance( year, str ):
            if not year.isdigit() or len( year ) != 4:
                raise ValueError( "year must be a int or str of 4 digits" )

        if isinstance( iso_language_code, ( list, tuple ) ):
            resultList = []
            for lang in iso_language_code:
                HolidayObject.mergeLists( self.getHolidays(year, iso_country_code, lang ), resultList)

            return resultList

        if not isinstance( iso_language_code, str ) or len( iso_language_code ) != 2:
            raise ValueError( "language_code must be a string of 2 chaccters")

        return self.__execute("https://openholidaysapi.org/PublicHolidays",
                              {
                                  'countryIsoCode': iso_country_code,
                                  'languageIsoCode': iso_language_code,
                                  'validFrom': f'{year}-01-01',
                                  'validTo': f'{year}-12-31'
                              },
                              HolidayObject,
                              isoCode = iso_country_code )
