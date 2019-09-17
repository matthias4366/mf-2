

def check_if_author(
        request_,
        model_,
        id_model,
        user_is_not_author_error,
):
    """
    Check if the user authored the given Model instance.
    """

    author_id_user_request = request_.user.id

    queryset_model = \
        model_.objects.filter(id=id_model).values()
    dict_model = list(queryset_model)[0]
    author_id_model = dict_model['author_id']

    user_is_author = \
        (author_id_user_request == author_id_model)

    if not user_is_author:
        raise user_is_not_author_error
