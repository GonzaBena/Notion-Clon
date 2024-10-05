import reflex as rx


def card(*args, **kwargs):
    # Attributes to extract
    keys_to_extract = ['min_height', "class_name"]

    # Extract the specified keys using pop
    extracted_data = {key: kwargs.pop(key)
                      for key in keys_to_extract if key in kwargs}

    # The remaining data will now be in 'data'
    remaining_data = kwargs
    for i in extracted_data:
        print(i)

    return rx.card(
        args,
        **remaining_data,
        min_height=extracted_data["min_height"] if "min_height" in extracted_data
        else "200px",
        class_name=(extracted_data["class_name"] if "class_name" in extracted_data
                    else "") + "w-full p-5 gap-5 rounded-xl border flex-col",
        display="flex",
        spacing="2",
        variant="classic",
    )
