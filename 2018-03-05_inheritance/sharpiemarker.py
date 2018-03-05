from marker import Marker


class SharpieMarker(Marker):
    def __init__(self, color):
        Marker.__init__(self, color, 3, 0.005, False)
