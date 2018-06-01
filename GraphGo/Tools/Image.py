

import GraphGo.Config
from GraphGo.Tools import SQLTools,LittleTools



class SingleImg:
    def GET(self,name):
        img = open('Img/' + name)
        return img

