from . import models


def get_all_works():
    return models.Work.objects.all()

def get_work(pk: int):
    try:
        return models.Work.objects.get(pk=pk)
    except models.Work.DoesNotExist:
        return None