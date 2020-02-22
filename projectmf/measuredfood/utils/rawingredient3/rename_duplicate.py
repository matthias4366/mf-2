

def rename_duplicate(
    model,
    field_name,
    user_,
    re,
):
    """
    This function is written for the RawIngredient3 model and the field 'name'.
    There are several instances were RawIngredient3 objects can be created
    when a RawIngredient3 object with the same name already exists in the
    user's collection. That has to be avoided, as it makes it impossible for
    the user to know which RawIngredient3 object is related to which
    SpecificIngredient. Therefore, they do not know which of the excess
    RawIngredient3 objects to delete without affecting their FullDayOfEating
    objects.
    :param model: Model which fields are considered. The function was written
    for the RawIngredient3 model, but was written generally.
    :param field_name: Field where the duplicate names are renamed. The field
    name the function is written for is 'name'.
    :param user_: The user is the owner of the model objects.
    :param re: Python module regular expression.
    :return:
    """

    changed = set()
    rawingredient3_objects_from_user = model.objects.filter(
        author=user_
    )

    for obj in rawingredient3_objects_from_user:
        value = getattr(obj, field_name)
        duplicates = model.objects.filter(
            author=user_,
            **{field_name: value}
        ).exclude(
            pk=obj.pk
        )
        for i, dupe in enumerate(duplicates):
            if dupe.pk in changed:
                continue
            changed.add(obj.pk)
            changed.add(dupe.pk)
            # print(f'Fixing duplicate %s.%s:' % (obj.__class__.__name__,
            #                                     field_name), obj.pk,
            #       obj.name, '-', dupe.pk, dupe.name)

            original_name = dupe.name
            current_number_at_end_list = re.findall('([0-9]+)$', original_name)

            if len(current_number_at_end_list) == 0:
                new_number = 1
                original_name_stem = original_name
            else:
                current_number_at_end = current_number_at_end_list[0]
                new_number = int(current_number_at_end) + 1
                n_chars_in_original_name_stem = \
                    len(original_name) - len(str(current_number_at_end))
                original_name_stem = original_name[
                                     0:n_chars_in_original_name_stem
                                     ]
            name_of_duplicate = original_name_stem + str(new_number)

            n_increases_new_number = 0
            n_increment_new_number_max = 1000

            while model.objects.filter(
                    author=user_,
                    name=name_of_duplicate
            ).exists():
                new_number = new_number + 1
                name_of_duplicate = original_name_stem + str(new_number)

                n_increases_new_number = n_increases_new_number + 1
                if n_increases_new_number > n_increment_new_number_max:
                    break

            setattr(dupe, field_name, name_of_duplicate)
            dupe.save()

