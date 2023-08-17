from typing import List
from openholidaysapi.text import IsoTexts
from openholidaysapi.base import BaseTextsObject
from openholidaysapi.exceptions import IsoCodesDidNotMatch


class LanguageObject( BaseTextsObject ):
    def __init__( self, isoCode: str, name: List[dict] ):
        super().__init__( isoCode, texts=name)
        return

    def merge( self, obj: 'LanguageObject' ):
        super().merge( obj )
        return

    @staticmethod
    def mergeLists( items: list, target: list ):
        for item in items:
            item: LanguageObject
            found = False
            for dest in target:
                dest: LanguageObject
                if dest.IsoCode == item.IsoCode:
                    found = True
                    dest.merge( item )

            if not found:
                target.append( item )

        return target

    def dump( self ):
        print( self.__str__() )
        return

    def __repr__( self ):
        texts = ", ".join(text.Text for text in self.Texts)
        return f"<LanguageObject language={self.IsoCode} {texts}>"

    def __str__( self ):
        texts = ", ".join(text.Text for text in self.Texts)
        return f"{self.IsoCode}: {texts}>"

