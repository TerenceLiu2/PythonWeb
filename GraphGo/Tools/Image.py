class SingleImg:
    def GET(self,name):
        img = open('Img/' + name)
        return img

