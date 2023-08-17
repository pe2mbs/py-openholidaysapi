from typing import List
from openholidaysapi.exceptions import IsoCodesDidNotMatch
from openholidaysapi.base import BaseTextsObject


class CountryObject( BaseTextsObject ):
    def __init__( self, isoCode: str, name: List[dict], officialLanguages: List[str] ):
        super().__init__( iso_code = isoCode, texts = name )
        self.__officialLanguages = officialLanguages
        return

    @property
    def OfficialLanguages( self ) -> list:
        return self.__officialLanguages

    def merge( self, obj: 'CountryObject' ):
        if obj.IsoCode != self.IsoCode:
            raise IsoCodesDidNotMatch( f"{obj.IsoCode} != {self.IsoCode}")

        for lang in obj.OfficialLanguages:
            if lang not in self.__officialLanguages:
                self.__officialLanguages.append( lang )

        super().merge( obj )
        return

    @staticmethod
    def mergeLists( items: list, target: list ):
        for item in items:
            item: CountryObject
            found = False
            for dest in target:
                dest: CountryObject
                if dest.IsoCode == item.IsoCode:
                    found = True
                    dest.merge( item )

            if not found:
                target.append( item )

        return target

    def dump( self ):
        languages = ", ".join( self.__officialLanguages )
        texts = ", ".join( text.Text for text in self.Texts )
        print( f"{self.IsoCode}: {languages} -> {texts}" )
        return