from collections import defaultdict
# This solution is not meant to be optimal or even correct. What I was exercising here was testing first.
# An solution can be easily achieved by finding the connected components of the dependency graph
def transitive_dependencies(lists_of_dependencies):
    # A list is of dependencies is understood as the first element depends on the rest
    dependencies = defaultdict(set)
    updated_dependencies = defaultdict(set)
    for list_of_dependencies in lists_of_dependencies:
        updated_dependencies[list_of_dependencies[0]]|=set(list_of_dependencies[1:])
    
    while updated_dependencies != dependencies:
        dependencies |= updated_dependencies
        for key in list(updated_dependencies.keys()):
            added = set()
            for dependency in updated_dependencies[key]:
                added |= updated_dependencies[dependency]
            updated_dependencies[key]|= added - {key}
    return dependencies

    

