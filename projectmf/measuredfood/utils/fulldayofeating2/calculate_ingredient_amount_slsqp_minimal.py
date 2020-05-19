

def calculate_ingredient_amount_slsqp_minimal_1(
    # fulldayofeating2,
    minimize,
    np,
):
    """
    Minimal version to learn it.

    The scipy minimize algorithm with the option SLSQP is used.
    https://docs.scipy.org/doc/scipy/reference/tutorial/
    optimize.html#sequential-least-squares-programming-
    slsqp-algorithm-method-slsqp
    The purpose is to give the user more power in manipulating a full day of
    eating.
    np: numpy package python.
    minimize: scipy.optimize.minimize package python.
    :return:
    """

    """
    Detailed notes on the technical implementation:
    inequality constraint: f(x) >=0
    equality constraint: f(x) = 0
    
    """

    """
    Example code from https://www.youtube.com/watch?v=cXHvC_FGx24
    """

    def objective(x):
        x1 = x[0]
        x2 = x[1]
        x3 = x[2]
        x4 = x[3]
        return x1*x4*(x1+x2+x3)+x3

    def constraint1(x):
        return x[0]*x[1]*x[2]*x[3] - 25.0

    def constraint2(x):
        sum_sq = 40
        for i in range(4):
            sum_sq = sum_sq - x[i]**2
        return sum_sq

    x0 = [1, 5, 5, 1]
    print(objective(x0))

    b = (1.0, 5.0)
    bnds = (b, b, b, b)

    con1 = {'type': 'ineq', 'fun': constraint1}
    con2 = {'type': 'eq', 'fun': constraint2}

    cons = [con1, con2]

    sol = minimize(objective, x0, method='SLSQP', bounds=bnds, constraints=cons)

    print(sol)

    return None


def calculate_ingredient_amount_slsqp_minimal_2(
    # fulldayofeating2,
    minimize,
    np,
):
    """

    :param minimize:
    :param np:
    x is a vector with the calculated amount values for the ingredients.

    Use np.concatenate((a, b), axis=0) to combine the ingredient arrrays into
    a array (representing a matrix) that can be multiplied with the array
    representing the ingredient amounts.
    :return:
    """

    # Kidney beans
    beans_kidney_dict = {
        'FDC_ID': 173744,
        'name': 'Beans, kidney, red, mature seeds, raw',
        'Energy': 337,
        'Protein': 22.53,
        'Total lipid (fat)': 1.06,
        'Fiber, total dietary': 15.2,
        'Carbohydrate, by difference': 61.29,
    }

    # Pea protein
    pea_protein_dict = {
        'FDC_ID':  571972,
        'name': 'UNSWEETENED PEA PROTEIN POWDER',
        'Energy': 370,
        'Protein': 77.78,
        'Total lipid (fat)': 5.56,
        'Fiber, total dietary': 3.7,
        'Carbohydrate, by difference': 7.41,
    }

    rice_dict = {
        'FDC_ID':  169760,
        'name': 'Rice, white, medium-grain, raw, unenriched',
        'Energy': 360,
        'Protein': 6.61,
        'Total lipid (fat)': 0.58,
        'Fiber, total dietary': 0,
        'Carbohydrate, by difference': 79.34,
    }

    ingredient_dict_list = [
        # beans_kidney_dict,
        pea_protein_dict,
        rice_dict
    ]

    list_ingredient_array = []
    for k in range(len(ingredient_dict_list)):
        list_k = [
            ingredient_dict_list[k]['Energy']/100,
            ingredient_dict_list[k]['Protein'] / 100,
            # ingredient_dict_list[k]['Fiber, total dietary'] / 100,
        ]
        array_k = np.array(list_k)
        list_ingredient_array.append(array_k)

    ingredient_matrix_loop = np.vstack(list_ingredient_array)
    ingredient_matrix = ingredient_matrix_loop.T

    nutrient_target_dict = {
        'Energy': 2500,
        'Protein': 150,
        # 'Total lipid (fat)': 1.06,
        'Fiber, total dietary': 30,
        # 'Carbohydrate, by difference': 61.29,
    }

    nutrient_target_list = [
        nutrient_target_dict['Energy'],
        nutrient_target_dict['Protein'],
        # nutrient_target_dict['Fiber, total dietary']
    ]
    nutrient_target = np.vstack(nutrient_target_list)

    def objective(x):
        # The vector x must be vertical, not horizontal.
        x_vertical = np.vstack(x)
        deviation_each_nutrient_target = \
            np.dot(ingredient_matrix, x_vertical) - nutrient_target
        deviation_total = np.linalg.norm(deviation_each_nutrient_target)
        return deviation_total

    x0 = np.array([100, 100])
    print('\nobjective(x0)\n')
    print(objective(x0))

    b = (0, np.inf)
    bnds = (b, b)

    step_size = 10

    def constraint1(x):
        """Adapt the protein amount in steps."""
        return x[0] % step_size

    # TODO: the pea protein powder without step should be 146 g.

    con1 = {'type': 'eq', 'fun': constraint1}

    # cons = [con1, ]
    cons = []

    sol = minimize(objective, x0, method='SLSQP', bounds=bnds, constraints=cons)

    print(sol)

    return None
