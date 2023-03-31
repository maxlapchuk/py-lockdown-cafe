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
        if not visitor.get("vaccine"):
            raise NotVaccinatedError("Visitor isn't vaccinated!")

        if visitor.get("vaccine").get("expiration_date") < date.today():
            raise OutdatedVaccineError("Visitor's vaccine is outdated")

        if not visitor.get("wearing_a_mask"):
            raise NotWearingMaskError("Visitor should wear a mask!")

        return f"Welcome to {self.name}"