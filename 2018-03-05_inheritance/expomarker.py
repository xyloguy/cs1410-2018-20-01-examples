import marker


class ExpoMarker(marker.Marker):
    def __init__(self, color):
        cap = 5
        marker.Marker.__init__(self, color, cap, 0.01, True)


class BlueExpoMarker(ExpoMarker):
    def __init__(self):
        ExpoMarker.__init__(self, (0, 0, 255))