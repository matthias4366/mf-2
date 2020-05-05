

def calculate_total_daily_energy_expenditure(
    age,
    biological_sex,
    height,
    bodymass,
    activity_level,
):
    """
    :return: total daily energy expenditure tdee
    """

    """
    math used:
    
    Source:
    https://steelfitusa.com/2018/10/calculate-tdee/
    
    Researchers have determined a set of “activity multipliers, known as 
    the Katch-McArdle multipliers.

To calculate your approximate TDEE, simply multiply these activity factors by 
your BMR:

    Sedentary (little to no exercise + work a desk job) = 1.2
    Lightly Active (light exercise 1-3 days / week) = 1.375
    Moderately Active (moderate exercise 3-5 days / week) = 1.55
    Very Active (heavy exercise 6-7 days / week) = 1.725
    Extremely Active (very heavy exercise, hard labor job, training 2x / day) 
    = 1.9
    """
    activity_level_multiplier_all = {
        'Sedentary': 1.2,
        'Light Exercise': 1.375,
        'Moderate Exercise': 1.55,
        'Heavy Exercise': 1.725,
        'Athlete': 1.9,
    }
    activity_level_multiplier = activity_level_multiplier_all[
        activity_level
    ]

    s_all = {
        'male': +5,
        'female': -151,
    }
    s = s_all[biological_sex]

    # Mifflin-St Jeor Equation
    # https://www.ncbi.nlm.nih.gov/pubmed/15883556
    basal_metabolic_rate_mifflin = 10 * bodymass + 6.25 * height - 5 * age + s
    # bodymass has to be in kg
    # height has to be in cm
    # age has to be in years

    total_daily_energy_expenditure = \
        basal_metabolic_rate_mifflin * activity_level_multiplier

    return total_daily_energy_expenditure
