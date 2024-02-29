def describe_pet(animal_type ='harry', pet_name='dog'):
    """반려동물 정보를 표시합니다"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

def get_name(first_name , last_name,  middle_name = ""):
    if middle_name: #빈 스트링이면 false로 간주
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
         full_name = f"{first_name} {last_name}"
    return full_name.title()

friend = get_name('sam','sung','apple')