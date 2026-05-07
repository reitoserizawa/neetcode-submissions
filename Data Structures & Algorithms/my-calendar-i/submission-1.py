class MyCalendar:
    
    def __init__(self):
        self.schedules = []

    def book(self, startTime: int, endTime: int) -> bool:
        if not self.schedules:
            self.schedules.append([startTime, endTime])
            return True
        
        for start, end in self.schedules:
            if startTime < end and start < endTime:
                return False
        
        self.schedules.append([startTime, endTime])
        return True
            
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)