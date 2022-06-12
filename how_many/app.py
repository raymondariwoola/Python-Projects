class convert_YDHM:
    def __init__(self, years=0, days=0, minutes=0,):
        self.years = years
        self.days = days
        self.minutes = minutes
        print(self)

    def __str__(self):
        outcome = "You have entered {} year".format(self.years)
        return outcome
    
    def convert_years_to_days(self):
        years = int(self.years)
        days = years * 365
        outcome = "{} years is {} days".format(years, hours)
        return outcome
    

    def convert_years_to_hours(self):
        years = int(self.years)
        days = years * 365
        hours = days * 24
        outcome = "{} years is {} hours".format(years, hours)
        return outcome


    def convert_years_to_Minutes(self):
        years = int(self.years)
        days = years * 365
        hours = days * 24
        minutes = hours * 60
        outcome = "{} years is {} minutes".format(years, minutes)
        return outcome


convert = convert_YDHM(2)
convert.convert_years_to_hours()

# TODO
# ! refactor class