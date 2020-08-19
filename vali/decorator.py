from django.contrib import admin


def vali_models_group(groupname=''):
    """
    assign menu_group name to ModalAdmin instance,
    admin index display registered models group by menu_group
    :param groupname:
    :return:
    """
    def _models_group(cls):
        if issubclass(cls, admin.ModelAdmin) and groupname:
            cls.model_group = groupname
        return cls
    return _models_group
