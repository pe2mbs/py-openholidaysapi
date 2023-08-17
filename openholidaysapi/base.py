from typing import List
from openholidaysapi.text import IsoTexts

class BaseTextsObject( object ):
    def __init__( self, iso_code: str,  texts: List[dict] ):
        self.__isoCode  = iso_code
        self.__texts    = [ IsoTexts( **text ) for text in texts ]
        return

    @property
    def Texts( self ) -> List[IsoTexts]:
        return self.__texts

    @property
    def IsoCode(self):
        return self.__isoCode

    def merge( self, src: 'BaseTextsObject' ):
        for d in src.Texts:
            found = False
            for s in self.Texts:
                if s.Language == d.Language:
                    found = True
                    break

            if not found:
                self.Texts.append( d.clone() )

        return

    def __repr__(self):
        return f"<BaseTextsObject {self.__isoCode}: {self.__texts}>"

    def __str__(self):
        return f"{self.__isoCode}: {self.__texts}"
