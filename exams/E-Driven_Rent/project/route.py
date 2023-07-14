class Route:
    def __init__(self, start_point: str, end_point: str, length: float, route_id: int):
        self.start_point = start_point
        self.end_point = end_point
        self.length = length
        self.route_id = route_id
        self.is_locked: bool = False
        
    @property
    def start_point(self):
        if self._start_point == '' or self._start_point.isspace():
            raise ValueError('Start point cannot be empty!')
        else:
            return self._start_point
    
    @start_point.setter
    def start_point(self, value):
        self._start_point = value

    @property
    def end_point(self):
        if self._end_point == '' or self._end_point.isspace():
            raise ValueError('End point cannot be empty!')
        else:
            return self._end_point

    @end_point.setter
    def end_point(self, value):
        self._end_point = value
        
    @property
    def length(self):
        if self._length < 1:
            raise ValueError('Length cannot be less than 1.00 kilometer!')
        else:
            return self._length
    
    @length.setter
    def length(self, value):
        self._length = value