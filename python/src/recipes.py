'''Given 3 lists, recipes, ingredients and supplies, find out which meals we can prepare with the infinite supplies we have'''
from common import time_execution


def topological_sort_dfs(G: dict[str, list[str]]) -> list[str]:
    '''This version of topo sort does not work for cycles but we know there can't be cycles in this problem'''
    topo_sorted = []
    visited = set()

    def helper(V: str) -> None:
        if V in visited:
            return
        if V not in G:  # It's a supply, not a recipe, can just return
            return

        visited.add(V)

        for E in G[V]:
            helper(E)

        topo_sorted.append(V)

    for V in G:
        helper(V)

    return topo_sorted[::-1]


def topological_sort_bfs(G: dict[str, list[str]]) -> list[str]:
    '''This version of topo sort does not work for cycles but we know there can't be cycles in this problem'''
    topo_sorted = []
    indegree_dict = {V: 0 for V in G}

    # Construct an indegree dictionary
    for V in G:
        for E in G[V]:
            indegree_dict[E] += 1

    stack = [V for V, D in indegree_dict.items() if D == 0]
    while stack:
        V = stack.pop()
        topo_sorted.append(V)

        # Decrement indegree for each vert that this vert leads to, if it's now 0 then add it to the stack to visit
        for E in G[V]:
            indegree_dict[E] -= 1
            if indegree_dict[E] == 0:
                stack.append(E)

    return topo_sorted


@time_execution()
def find_recipes(recipes: list[str], ingredients: list[str], supplies: list[str]) -> list[str]:
    possible_recipes = []

    def helper(ingredient: str):
        # Ingredient is also a recipe, check if we can make it
        if ingredient in recipes:
            return all(helper(i) for i in ingredients[recipes.index(ingredient)])
        elif ingredient in supplies:
            return True
        else:
            return False

    for i, recipe in enumerate(recipes):
        if all(helper(ingredient) for ingredient in ingredients[i]):
            possible_recipes.append(recipe)

    return possible_recipes


@time_execution()
def find_recipes_topological_dfs(recipes: list[str], ingredients: list[str], supplies: list[str]) -> list[str]:
    possible_recipes = []
    supplies = set(supplies)

    # Create a dependecy graph
    G = {recipes[i]: ingredients[i] for i in range(len(recipes))}

    # Sort topologically
    order = topological_sort_dfs(G)

    # Then traverse and add newly created supplies from the recipes we had
    for recipe in order:
        if all(ingredient for ingredient in supplies):
            supplies.add(recipe)
            possible_recipes.append(recipe)

    return possible_recipes


@time_execution()
def find_recipes_topological_bfs(recipes: list[str], ingredients: list[str], supplies: list[str]) -> list[str]:
    possible_recipes = []
    supplies = set(supplies)

    # Unlike graph needed for dfs where recipe depends on ingredients "chicken burger"->"buns"
    # We need a graph like this "buns"->"chicken burger", that means chicken burger depends on buns
    # Because if we start from buns we wouldn't know where to go as the edges from buns lead to supplies not recipes
    G = {E: [V for V in recipes if E in ingredients[i]]
         for i, E in enumerate(recipes)}

    # Sort topologically
    order = topological_sort_bfs(G)

    # Then traverse and add newly created supplies from the recipes we had
    for recipe in order:
        if all(ingredient for ingredient in supplies):
            supplies.add(recipe)
            possible_recipes.append(recipe)

    return possible_recipes


recipes: list[str] = ["chicken burger", "buns", "crispy chicken"]
ingredients: list[str] = [["buns", "crispy chicken", "lettuce", "cheese"], [
    "yeast", "flour"], ["chicken", "breadcrumbs"]]
supplies: list[str] = ["yeast", "flour", "cheese",
                       "breadcrumbs", "milk", "lettuce", "chicken"]

print('Possible recipes are:', find_recipes(recipes, ingredients, supplies))
print('Possible recipes are:', find_recipes_topological_dfs(
    recipes, ingredients, supplies))
print('Possible recipes are:', find_recipes_topological_bfs(
    recipes, ingredients, supplies))
