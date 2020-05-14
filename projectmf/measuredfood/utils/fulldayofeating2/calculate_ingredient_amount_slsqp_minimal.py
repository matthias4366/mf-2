

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
    :return:
    """

    # Kidney beans
    beans_kidney_dict = {
        'FDC_ID': 173744,
        'Energy': 337,
        'Protein': 22.53,
        'Total lipid (fat)': 1.06,
        'Fiber, total dietary': 15.2,
        'Carbohydrate, by difference': 61.29,
    }
    beans_kidney = beans_kidney_dict['Energy']

    nutrient_target_dict = {
        'Energy': 2500,
        'Protein': 150,
        # 'Total lipid (fat)': 1.06,
        'Fiber, total dietary': 30,
        # 'Carbohydrate, by difference': 61.29,
    }

    nutrient_target = nutrient_target_dict['Energy']

    print('beans_kidney')
    print(beans_kidney)
    print('nutrient_target')
    print(nutrient_target)

    def objective(x):
        amount_beans = x[0]
        return abs(amount_beans / 100.0 * 337.0 - 2500)
        # return amount_beans / 100.0 * beans_kidney - nutrient_target

    x0 = [100]
    print(objective(x0))

    b = (0, np.inf)
    bnds = (b, )

    cons = []

    sol = minimize(objective, x0, method='SLSQP', bounds=bnds, constraints=cons)

    print(sol)

    return None
