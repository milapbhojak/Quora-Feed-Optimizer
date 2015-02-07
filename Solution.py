class Solution(object):
    """
    Potential solution for the upcoming reload
    
    @type _stories: list
    @param _stories: The list of potential items.

    @type _len_stories : int
    @param _len_stories: The length of the list of stories.    
    
    @type _score: int
    @param _score: The current solution's score.
    
    @type _height: int
    @param _height: The current solution's height.    
    """
    
    def __init__(self):
        self._stories = []
        self._len_stories = 0
        self._score = 0
        self._height = 0          
    
    def __repr__(self):
        return "%s %s %s" % (self._score, self._len_stories, ' '.join(sorted([str(story._id) for story in self._stories])))
    
    def __gt__(self, solution):
        #check who's score is better
        if self._score > solution._score:
            return True
        if self._score < solution._score:
            return False
        #same score; check who has less stories
        if self._len_stories < solution._len_stories:
            return True
        if self._len_stories > solution._len_stories:
            return False
        #same score, same number of stories; check who has smaller lexicographically
        if sorted([story._id for story in self._stories]) <= sorted([story._id for story in solution._stories]):
            return True
        else:
            return False
 
    @classmethod
    def clone(cls, solution):
        clone_solution = cls()
        clone_solution._stories = copy.copy(solution._stories)
        clone_solution._len_stories = solution._len_stories
        clone_solution._score = solution._score
        clone_solution._height = solution._height
        return clone_solution
    
    def add(self, story):    
        """
        add story to the solution
        """
        self._stories.append(story)
        self._score += story._score
        self._height += story._height 
        self._len_stories += 1
        
    def remove(self, story):
        """
        remove story from the solution
        """    
        self._stories.remove(story)
        self._score -= story._score
        self._height -= story._height
        self._len_stories -= 1 
