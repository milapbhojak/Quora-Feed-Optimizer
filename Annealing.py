def annealing_simulated(self, T=1000.0,cool=0.35):
    """
    perform the annealing simulated algorithm:
    1) start with a random solution.
    2) move to a neighbour solution.
    (favors better solutions, and accepts worst solutions with a certain probabilities
    to avoid local minimum until the temperature is totally down)
    """
    #order stories based on their proportioned score
    ordered_stories = sorted(self._stories, reverse=True)
    #produce a random solution
    current_solution, stories_in_current = self.random_solution(ordered_stories, self._len_stories)
    best_solution = Solution.clone(current_solution)
    while(T>0.1):
        temp_solution = Solution.clone(current_solution)
        stories_in_temp = copy.copy(stories_in_current)
        stories_at_true = [i for i in xrange(self._len_stories) if stories_in_temp[i]]
        #check if there is still stories
        if len(stories_at_true) == self._len_stories:
            break
        #choose a story and remove it
        if stories_at_true:
            indice = choice(stories_at_true)
            stories_in_temp[indice] = False
            temp_solution.remove(ordered_stories[indice])
        else:
            indice = -1
        #add any number of other stories available
        for i in xrange(indice+1, self._len_stories):
            if stories_in_temp[i]:
                continue
            story = ordered_stories[i]
            if self.addable((story,), temp_solution):
                stories_in_temp[i] = True
                temp_solution.add(story)
            elif temp_solution._height == self.__height:
                break
        #compare temp and current solutions
        if temp_solution > current_solution:
            current_solution = temp_solution
            stories_in_current = stories_in_temp
            #also since temp is better than current, compare it to best
            if current_solution > best_solution:
                best_solution = Solution.clone(current_solution)
        #current solution is better than temp
        #the algorithm states that we can still give it a try depending on a probability
        else:
            #since temp solution score is < current solution score
            #this probability will be near one at the beginning where T is high
            #but will get lower and lower as T cool down
            #hence will accept less and less bad solution
            p = pow(math.e,float(temp_solution._score - current_solution._score)/T)
            if p > random():
                current_solution = temp_solution
                stories_in_current = stories_in_temp
        #decrease the temperature
        T=T*cool
    return best_solution
