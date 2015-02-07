class Story(object):
    """
    Story object 
    
    @type _cpt: int
    @param _cpt: counts the number of instance created.
    
    @type _height: int
    @param _height: The stroy's height.
        
    @type _time: int
    @param _time: The time of publication.
    
    @type _id: int
    @param _id: The story's id.
    
    @type _score: int
    @param _score: The story's score.
    
    @type _height: int
    @param _height: The stroy's height.   
    
    @type _proportioned_score: float
    @param _proportioned_score: The stroy's _score proportioned to height.    
    """
    __cpt = 0
    
    def __init__(self, time=-1, score=-1, height=-1):                
        self._id = Story.__cpt
        self._time = time
        self._score = score
        self._height = height     
        self._proportioned_score = float(score)/height
        Story.__cpt += 1        
    
    def __repr__(self):
        return "id: %s, time: %s" % (self._id, self._time)    
    
    def __gt__(self, story):
        if(self._proportioned_score > story._proportioned_score):
            return True
        if(self._proportioned_score < story._proportioned_score):
            return False
        if(self._id < story._id):
            return True
        return False
    
    def _better_score(self, story):
        if(self._score > story._score):
            return True
        if(self._score < story._score):
            return False
        if(self._id < story._id):
            return True
        return False
