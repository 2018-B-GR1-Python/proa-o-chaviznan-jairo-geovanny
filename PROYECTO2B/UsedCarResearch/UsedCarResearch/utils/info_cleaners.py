from UsedCarResearch.properties import data_properties


def clean_space(value, with_space=True):
    if not with_space:
        value = value.rstrip().lstrip()
        value = value.replace('\n', '')
    return value


def clean_type(value, data_type=data_properties.TEXT):
    if data_type == data_properties.TEXT:
        return str(value)
    elif data_type == data_properties.DATE:
        return str(value)
    else:
        return str(value)


def clean_data(array, index, with_space=True, data_type=data_properties.TEXT):
    if index < len(array):
        data = clean_type(array[index], data_type)
        if data_type == data_properties.TEXT:
            data = clean_space(data, with_space)
        return data
    return ''


def clean_only_text(value, with_space=True, data_type=data_properties.TEXT):
    if value is None:
        return ''
    data = clean_type(value, data_type)
    if data_type == data_properties.TEXT:
        data = clean_space(data, with_space)
    return data
