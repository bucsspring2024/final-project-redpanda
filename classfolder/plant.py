class Plant:
    def __init__(self,name, x,y,img_file, waterfreq, ideallight, height, idealtemp, idealsoil, idealdrain, nutrientneeds, bloomtime, idealplanttime, pests):
        """
        args: 
        return: 
        """
        self.name = name
        self.x = x
        self.y =y
        self.img_file = img_file
        self.waterfreq = waterfreq
        self.ideallight = ideallight
        self.height = height
        self.idealtemp = idealtemp
        self.idealsoil = idealsoil
        self.idealdrain = idealdrain
        self.nutrientneeds = nutrientneeds
        self.bloomtime = bloomtime
        self.idealplanttime = idealplanttime
        self.pests = pests
        
    def tasknotif(self):
        """
        args: 
        return: 
        """
        
        