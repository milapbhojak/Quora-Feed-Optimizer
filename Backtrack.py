def brute_force(self):
    """
    check all possibilities:
    1) best solution for combination of 2 stories (if it exists).
    2) best solution for combination of 3 stories (if it exists).
    .
    .
    l-1) best solution for combination of l-1 stories (if it exists).
    l : being the length of the current stories.
    """
    best_solution = Solution()
    best_solution.add(self._best_story)
    for i in xrange(2, self._len_stories+1):
        for tuple_stories in itertools.combinations(self._stories, i):
            if self.addable(tuple_stories):
                current_solution = Solution()
                for story in tuple_stories:
                    current_solution.add(story)
                if current_solution > best_solution:
                    best_solution = current_solution
    return best_solution
