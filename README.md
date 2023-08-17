# OpenHolidaysApi for Python 
This is a Python interface to https://openholidaysapi.org/ 

# API
Currenly only implemented 
* Countries
* Languages
* PublicHolidays

## Todo
The following API calls need to be implmented
* PublicHolidaysByDate
* SchoolHolidays
* SchoolHolidaysByDate
* Subdivisions
* Statistics/PublicHolidays
* Statistics/SchoolHolidays

## class OpenHolidaysOrg()
This is the main class that provides the API calls

### OpenHolidaysOrg.__init__( proxies: Optional[dict] = None )
Setup the API class

#### Parameter
**proxies** a dictionary with keys **http** and/or **https** with the value set to the proxy URL.


### OpenHolidaysOrg.getHolidays( year:Union[int,str], iso_country_code: str, iso_language_code: Optional[Union[str,tuple,list]] ) -> List[HolidayObject]
Retrieves the holidays for a given country. 

#### Parameter
**year** a year number consisting out of 4 digits (2 digits is allowed, XX < 50 is 20XX else 190XX )
**iso_country_code** a string with the country code according ISO 3166-1 
**iso_language_code** a string, list or tuple with strings with language code according ISO-639-1

#### Returns
A list with HolidayObject's.

### getCountries( iso_language_code: Union[str,list,tuple] ) -> List[CountryObject]
Retrieves the available countries, when mulitple **iso_language_code**'s are passed the country object shall contain for those countries the names in the requisted language.

#### Parameter
**iso_language_code** a string, list or tuple with strings with language code according ISO-639-1

#### Returns
A list with CountryObject's.

### def getLanguages( iso_language_code: Union[str,list,tuple] ) -> List[LanguageObject]:
Retrieves the available languages, when mulitple **iso_language_code**'s are passed the country object shall contain for those countries the names in the requisted language.

#### Parameter
**iso_language_code** a string, list or tuple with strings with language code according ISO-639-1

#### Returns
A list with LanguageObject's.

# Classes

## LanguageObject
Contains the language name for a requested Language. It may contain multiple names in different languages

for example for IsoCode: 'NL' 
* NL: Nederlands
* EN: Dutch

### LanguageObject.__init__( isoCode: str, name: List[dict] )
Contructor used by the OpenHolidaysOrg class to initialize the object.

### property LanguageObject.Texts -> List[IsoTexts]
A list of IsoTexts objects with one or more languages 

### property LanguageObject.IsoCode -> str
The ISO 639-1 language code for this object

### LanguageObject.merge( obj: 'LanguageObject' )
Internal member function for merging language texts of the same language.

### staticmethod LanguageObject.mergeLists( items: list, target: list )
Internal function for merging language texts of the same language between two lists.

### LanguageObject.dump()
Test member function to simple dump the content of the object.

### LanguageObject.__repr__()
Member function to simple dump the content of the object with the object name.

### LanguageObject.__str__()
member function to simple dump the content of the object only the properies.

## CountryObject

### CountryObject.__init__( self, isoCode: str, name: List[dict], officialLanguages: List[str] ):
Contructor used by the OpenHolidaysOrg class to initialize the object.

### property CountryObject.IsoCode
Provides the language code according to ISO639-1

### property CountryObject.Language
Same as IsoCode

### property CountryObject.Text
Provides the text in the language of this object

### property CountryObject.OfficialLanguages
Provides a list with official languages for the country

### CountryObject.merge( self, obj: 'CountryObject' )
Internal member function for merging language texts of the same country.

### CountryObject.mergeLists( items: list, target: list )
Internal function for merging country texts of the same country between two lists.

### CountryObject.dump( self )
Test member function to simple dump the content of the object.

## HolidayObject


## IsoTexts

### IsoTexts.__init__( self, language: str, text: str ):

### property IsoTexts.IsoCode
Provides the language code according to ISO639-1

### property IsoTexts.Language
Same as IsoCode

### property IsoTexts.Text
Provides the text in the language of this object

### IsoTexts.clone( self ) -> 'IsoTexts':


# Example
The following example shows howto retrieve the holidays for the Netherlands

```python
from openholidaysapi import OpenHolidaysOrg

api = OpenHolidaysOrg()

for holiday in api.getHolidays( 2023, 'NL' ):
    holiday.dump()
```

The following example show howto retrieve the holidays for the Netherlands with both the Dutch and English name labels 
```python
from openholidaysapi import OpenHolidaysOrg

api = OpenHolidaysOrg()

for holiday in api.getHolidays( 2023, 'NL', ('NL', 'EN' ) ):
    holiday.dump()
```



