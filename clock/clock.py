class Clock:

    def __init__(self, hour, minute):
        self.minute = 0
        self.hour = 0
        self.add(hour * 60 + minute)

    def __str__(self):
        return "{0:02d}:{1:02d}".format(self.hour, self.minute)
    
    def add(self, incr):
        total_min = self.hour * 60 + self.minute + incr
        self.hour, self.minute = divmod(total_min, 60)
        self.hour = self.hour % 24
        return self 

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.hour == other.hour and self.minute == other.minute
        return False

