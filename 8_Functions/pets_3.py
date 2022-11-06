def describe_pet(pet_name, animal_type='dog'):
    #We changed the definition of describe_pet() to include a default value, 'dog', for animal_type.
    
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet(pet_name='willie')