class instagram:
    def __init__(self,datas):
        self.datas = self.preprocess(datas)  # Initialize an empty list for datas

    def preprocess(self, datas):
        # TO-DO
        return datas;
    
    def get_datas(self):
        return self.datas

    def set_datas(self, new_datas):
        self.datas = new_datas