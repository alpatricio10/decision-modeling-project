import pandas as pd
import model_utils

def calculate_negative_points(energy, saturated_fat, sugars, salt):
    """
    Calculate negative component N (0-55 points)
    Using only if/elif conditions based on the table.
    """
    points = 0

    # Energy points (0-10)
    if energy <= 335:
        energy_points = 0
    elif energy <= 670:
        energy_points = 1
    elif energy <= 1005:
        energy_points = 2
    elif energy <= 1340:
        energy_points = 3
    elif energy <= 1675:
        energy_points = 4
    elif energy <= 2010:
        energy_points = 5
    elif energy <= 2345:
        energy_points = 6
    elif energy <= 2680:
        energy_points = 7
    elif energy <= 3015:
        energy_points = 8
    elif energy <= 3350:
        energy_points = 9
    else:
        energy_points = 10
    points += energy_points

    # Fat points (0-10)
    if saturated_fat <= 1:
        sat_points = 0
    elif saturated_fat <= 2:
        sat_points = 1
    elif saturated_fat <= 3:
        sat_points = 2
    elif saturated_fat <= 4:
        sat_points = 3
    elif saturated_fat <= 5:
        sat_points = 4
    elif saturated_fat <= 6:
        sat_points = 5
    elif saturated_fat <= 7:
        sat_points = 6
    elif saturated_fat <= 8:
        sat_points = 7
    elif saturated_fat <= 9:
        sat_points = 8
    elif saturated_fat <= 10:
        sat_points = 9
    else:
        sat_points = 10
    points += sat_points

    # Sugar points (0-15)
    if sugars <= 3.4:
        sugar_points = 0
    elif sugars <= 6.8:
        sugar_points = 1
    elif sugars <= 10:
        sugar_points = 2
    elif sugars <= 14:
        sugar_points = 3
    elif sugars <= 17:
        sugar_points = 4
    elif sugars <= 20:
        sugar_points = 5
    elif sugars <= 24:
        sugar_points = 6
    elif sugars <= 27:
        sugar_points = 7
    elif sugars <= 31:
        sugar_points = 8
    elif sugars <= 34:
        sugar_points = 9
    elif sugars <= 37:
        sugar_points = 10
    elif sugars <= 41:
        sugar_points = 11
    elif sugars <= 44:
        sugar_points = 12
    elif sugars <= 48:
        sugar_points = 13
    elif sugars <= 51:
        sugar_points = 14
    else:
        sugar_points = 15
    points += sugar_points

    # Salt points (0-20)
    if salt <= 0.2:
        salt_points = 0
    elif salt <= 0.4:
        salt_points = 1
    elif salt <= 0.6:
        salt_points = 2
    elif salt <= 0.8:
        salt_points = 3
    elif salt <= 1.0:
        salt_points = 4
    elif salt <= 1.2:
        salt_points = 5
    elif salt <= 1.4:
        salt_points = 6
    elif salt <= 1.6:
        salt_points = 7
    elif salt <= 1.8:
        salt_points = 8
    elif salt <= 2.0:
        salt_points = 9
    elif salt <= 2.2:
        salt_points = 10
    elif salt <= 2.4:
        salt_points = 11
    elif salt <= 2.6:
        salt_points = 12
    elif salt <= 2.8:
        salt_points = 13
    elif salt <= 3.0:
        salt_points = 14
    elif salt <= 3.2:
        salt_points = 15
    elif salt <= 3.4:
        salt_points = 16
    elif salt <= 3.6:
        salt_points = 17
    elif salt <= 3.8:
        salt_points = 18
    elif salt <= 4.0:
        salt_points = 19
    else:
        salt_points = 20
    points += salt_points

    return points


def calculate_positive_points(protein, fiber, fvl_percent):
    """
    Calculate positive component P (0-17 points)
    Based on Table 2 from the document
    """
    points = 0
    
    # Protein points (0-7)
    if protein > 17: points += 7
    elif protein > 14: points += 6
    elif protein > 12: points += 5
    elif protein > 9.6: points += 4
    elif protein > 7.2: points += 3
    elif protein > 4.8: points += 2
    elif protein > 2.4: points += 1
    
    # Fiber points (0-7, but max combined is determined by formula)
    if fiber > 7.4: points += 5
    elif fiber > 6.3: points += 4
    elif fiber > 5.2: points += 3
    elif fiber > 4.1: points += 2
    elif fiber > 3.0: points += 1
    
    # Fruit/vegetable/legume points (0, 1, 2, or 5)
    if fvl_percent > 80: points += 5
    elif fvl_percent > 60: points += 2
    elif fvl_percent > 40: points += 1

    return points

def calculate_nutriscore(energy, saturated_fat, sugars, salt, 
                        protein, fiber, fvl_percent):
    """
    Calculate complete Nutri-Score
    Returns: (score, label)
    """
    N = calculate_negative_points(energy, saturated_fat, sugars, salt)
    P = calculate_positive_points(protein, fiber, fvl_percent)
    
    # Special rule: if N >= 11 and FVL <= 80%, don't count protein
    if N >= 11 and fvl_percent <= 80:
        P = calculate_positive_points(0, fiber, fvl_percent)

    score = N - P
    
    # Assign label based on score
    if score <= 0:
        label = 'A'
    elif score <= 2:
        label = 'B'
    elif score <= 10:
        label = 'C'
    elif score <= 18:
        label = 'D'
    else:
        label = 'E'
    
    return score, label, N, P

def apply_nutriscore_to_database(df):
    """Apply Nutri-Score calculation to entire database"""
    results = []
    
    for idx, row in df.iterrows():
        score, label, N, P = calculate_nutriscore(
            row['energy_100g'],
            row['saturated_fat_100g'],
            row['sugars_100g'],
            row['salt_100g'],
            row['proteins_100g'],
            row['fiber_100g'],
            row['fvl_percent']
        )
        results.append({'calculated_score': score, 'calculated_label': label, 'n': N, 'p': P})
    
    results_df = pd.DataFrame(results)
    df['calculated_nutri_score'] = results_df['calculated_score']
    df['calculated_nutri_label'] = results_df['calculated_label']
    df['calculated_negative'] = results_df['n']
    df['calculated_positive'] = results_df['p']    
    
    return df

# COMMENT OUT TO TEST THAT THE FUNCTION WORKS FOR THE GIVEN DATA
df = model_utils.load_food_database('data/food_database.xlsx')
df = apply_nutriscore_to_database(df)
print(df.head())

# Count matches between calculated and original Nutri-Score
matches = sum(df['calculated_nutri_score'] == df['nutri_score_value'])
total = len(df)
print(f"{matches} matches out of {total} total ({matches / total * 100:.2f}% accuracy)")