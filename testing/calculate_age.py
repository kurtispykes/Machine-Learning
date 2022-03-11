import datetime

def get_age(yyyy:int, m:int, d:int) -> int:
    dob = datetime.date(yyyy, m, d)
    today = datetime.date.today()
    age = round((today - dob).days / 365.25)
    return age