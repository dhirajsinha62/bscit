import geometry
def pointyShapevolume(x,h,squarebase):
        if squarebase:
                base=geometry.squarearea(x)
        else:
                base=geometry.circlearea(x)
        return h*base/3.0
print(pointyShapevolume(4,2.6,True))
print(pointyShapevolume(4,2.6, False))
