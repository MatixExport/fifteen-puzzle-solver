class AStarBoard:
    def __init__(self, table,path, gscore, fscore):
        self.table = table
        self.path = path
        self.gscore = gscore
        self.fscore = fscore