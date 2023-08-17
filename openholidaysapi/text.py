

class IsoTexts( object ):
    def __init__( self, language: str, text: str ):
        self.__language = language
        self.__text = text
        return

    @property
    def Language( self ):
        return self.__language

    @property
    def IsoCode( self ):
        return self.__language

    @property
    def Text( self ):
        return self.__text

    def clone( self ) -> 'IsoTexts':
        return IsoTexts( self.__language, self.__text )

    def __repr__(self):
        return f"<IsoTexts language={self.__language} text={self.__text}>"

    def __str__(self):
        return f"{self.__language}: {self.__text}"