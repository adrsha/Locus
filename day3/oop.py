# OOPS!

class Manche:
    def __init__(this):
        this.lat = 0
        this.long = 0

    def walk(this, new_lat, new_long):
        this.lat = new_lat
        this.long = new_long


nabin_dai = Manche()
nabin_dai.walk(12, 50)
print(nabin_dai.lat, nabin_dai.long)


class Nepalese(Manche):  # inheritance
    pass
