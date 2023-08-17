


class SubDivision( object ):
    def __init__( self, code, shortName ):
        self.__code = code
        self.__shortName = shortName
        return

    @property
    def Code( self ):
        return self.__code

    @property
    def ShortName( self ):
        return self.__shortName

