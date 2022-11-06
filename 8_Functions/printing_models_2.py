#this code does the same as printing_models but it is more carefully structured
def print_models(unprinted_designs, completed_models):
    """Simulate printing each design, until none are left.
    Move each design to completed_models after printing.
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)
def show_completed_models(completed_models):
    """Show all the models that were printed."""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)


#body of the program below
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)


#This program has the same output as the version without functions, but
#the code is much more organized. The code that does most of the work has
#been moved to two separate functions, which makes the main part of the
#program easier to understand. Look at the body of the program to see how
#much easier it is to understand what this program is doing.