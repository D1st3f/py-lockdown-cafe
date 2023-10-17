from datetime import date

from app.errors import (
    NotVaccinatedError,
    NotWearingMaskError,
    OutdatedVaccineError
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("All friends should be vaccinated")
        if visitor["vaccine"]["expiration_date"] < date.today():
            raise OutdatedVaccineError("Friends have vaccines, but some "
                                       "of them have them expired")
        if not visitor["wearing_a_mask"]:
            raise NotWearingMaskError("Friends should wear masks")
        return f"Welcome to {self.name}"
