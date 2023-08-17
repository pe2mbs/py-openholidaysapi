from typing import Optional, List
from datetime import datetime, date
from openholidaysapi.languages import LanguageObject
from openholidaysapi.subdivisions import SubDivision


class HolidayObject( LanguageObject ):
    def __init__( self,
                  isoCode: str,
                  endDate: str,
                  id: str,
                  name: List[dict],
                  nationwide: bool,
                  startDate: str,
                  type: str,
                  subdivisions: Optional[List[dict]] = None,
                  comment: Optional[str] = None):
        ## type: [Public, Bank, School, BackToSchool, EndOfLessons]
        super().__init__( isoCode, name )
        self.__comment      = comment
        self.__startDate    = datetime.strptime( startDate, '%Y-%m-%d')
        self.__endDate      = datetime.strptime( endDate, '%Y-%m-%d')
        self.__id           = id
        self.__nationwide   = nationwide
        self.__type         = type
        if isinstance( subdivisions, list ):
            self.__subdivisions = [ SubDivision( **dev ) for dev in subdivisions ]

        else:
            self.__subdivisions = []

        return

    @property
    def StartDate( self ) -> date:
        return self.__startDate.date()

    @property
    def EndDate( self ) -> date:
        return self.__endDate.date()

    @property
    def Type( self ) -> str:
        return self.__type

    @property
    def NationWide( self ) -> bool:
        return self.__nationwide

    @property
    def SubDivisions( self ) -> List[ SubDivision ]:
        return self.__subdivisions

    def dump( self ):
        print( f"{self.__startDate.date()} - {self.__endDate.date()} {self.__type:12} nation wide: {self.__nationwide} {self.Texts}" )
        return

    def merge( self, obj ):
        LanguageObject.mergeLists( obj.Texts, self.Texts )
        return

    @staticmethod
    def mergeLists( source: List['HolidayObject'], target: List['HolidayObject'] ) -> List['HolidayObject']:
        for src in source:
            found = False
            for dst in target:
                if dst.IsoCode == src.IsoCode and dst.StartDate == src.StartDate and dst.EndDate == src.EndDate:
                    found = True
                    dst.merge( src )
                    break

            if not found:
                target.append( src )

        return target
