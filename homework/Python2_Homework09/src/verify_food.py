"""
Make sure each animal eats at least one food.
"""
import mysql.connector
from database import login_info

if __name__ == "__main__":
    db = mysql.connector.Connect(**login_info)
    cursor = db.cursor()
    
    cursor.execute("""SELECT animal.id, anid FROM animal JOIN food""")
    result = cursor.fetchall()
    
    all_animals = set()
    animals_with_food = set()
    for id, anid in result:
        all_animals.add(id)
        animals_with_food.add(anid)
        
    animals_without_food = all_animals - animals_with_food
    if animals_without_food:
        for animal_id in animals_without_food:
            cursor.execute("""SELECT name, family FROM animal WHERE id=%s""", str(animal_id))
            name, family = cursor.fetchone()
            print("WARNING: %s the %s (id: %s) does not have a food listed." %(name, family, animal_id))
    else:
        print("All animals have at least one food.")