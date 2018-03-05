import marker


class CrayolaMarker(marker.Marker):
    def __init__(self, color):
        marker.Marker.__init__(self, color, 4, 0.01, False)