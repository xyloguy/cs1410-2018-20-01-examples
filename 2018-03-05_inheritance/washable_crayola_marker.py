import crayolamarker


class WashableCrayolaMarker(crayolamarker.CrayolaMarker):
    def __init__(self, color, smell):
        crayolamarker.CrayolaMarker.__init__(self, color)
        self.erasable = True

        self.smell = smell
