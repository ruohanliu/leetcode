from collections import defaultdict


class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        """
            #recursion #dfs #important

            if an ingredient is not in supplies then it should be a recipe.
        """
        def check(r):
            if r not in cache:
                # since two recipes can form a loop, we must initialize the result to False
                cache[r] = False
                cache[r] = all(i in supplies or (i in recipeMap and check(recipeMap[i])) for i in ingredients[r])
            return cache[r]

        n = len(recipes)
        recipeMap = {r:i for i,r in enumerate(recipes)}
        supplies = set(supplies)
        cache = {}
        return [recipes[r] for r in range(n) if check(r)]
        

    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        """
            #graph #topologicalsort
        """
        n = len(recipes)
        supplies = set(supplies)
        adjList = defaultdict(list)
        degree = defaultdict(int)
        for i in range(n):
            for ing in ingredients[i]:
                adjList[ing].append(recipes[i])
                degree[recipes[i]] += 1
        queue = [ing for ing in supplies if ing in adjList]
        ans = []
        while queue:
            ing = queue.pop()
            for recipe in adjList[ing]:
                degree[recipe] -= 1
                if degree[recipe] == 0:
                    queue.append(recipe)
                    ans.append(recipe)
            del adjList[ing]

        return ans
