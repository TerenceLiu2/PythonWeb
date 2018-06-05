
class SingleImg:
    def GET(self,name):
        print 'Img/' + name
        img = open('Img/' + name)
        return img

