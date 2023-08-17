
class LanguageDoesntExists( Exception ):
    def __init__( self, message, code = None ):
        self.__code = code
        super().__init__( message )
        return


class OpenHolidaysOrgException( Exception ): pass


class IsoCodesDidNotMatch( Exception ): pass

