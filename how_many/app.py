class convert_YDHM:
    def __init__(self, years=0, days=0, minutes=0,):
        self.years = years
        self.days = days
        self.minutes = minutes
        print(self)

    def __str__(self):
        outcome = "You have entered {} year".format(self.years)
        return outcome

    def calculate(self):
        years = int(self.years)
        months = years * 12
        days = years * 365
        hours = days * 24
        minutes = hours * 60
        seconds = minutes * 60
        outcome = {"years": years, "months": months, "days": days,
                   "hours": hours, "minutes": minutes, "seconds": seconds}
        return outcome

    def convert_years_to_months(self):
        months = self.calculate()["months"]
        outcome = "{} years is {} months".format(self.years, months)
        return outcome

    def convert_years_to_days(self):
        days = self.calculate()["days"]
        outcome = "{} years is {} days".format(self.years, days)
        return outcome

    def convert_years_to_hours(self):
        hours = self.calculate()["hours"]
        outcome = "{} years is {} hours".format(self.years, hours)
        return outcome

    def convert_years_to_minutes(self):
        minutes = self.calculate()["minutes"]
        outcome = "{} years is {} minutes".format(self.years, minutes)
        return outcome

    def convert_years_to_seconds(self):
        seconds = self.calculate()["seconds"]
        outcome = "{} years is {} seconds".format(self.years, seconds)
        return outcome



