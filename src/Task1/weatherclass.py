class Weather:

    def __init__(self=None, date=None, temp=None, pressure=None, precipitation=None):
        self.date = date
        self.tempavg = temp
        self.pressure = pressure
        self.precipitation = precipitation

    def __str__(self):
        return f"date: {self.date}\ntempavg: {self.tempavg} degree C\npressure: {self.pressure} mmHg\nprecipitation: {self.precipitation}"