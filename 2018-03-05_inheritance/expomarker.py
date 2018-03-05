import marker


class ExpoMarker(marker.Marker):
    def __init__(self, color):
        cap = 5
        marker.Marker.__init__(self, color, cap, 0.01, True)
