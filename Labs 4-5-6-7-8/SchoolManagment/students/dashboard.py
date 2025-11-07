from django.utils.translation import gettext_lazy as _
from unfold.contrib import CountCard
from .models import Student

cards = [
    CountCard(
        title=_("Total Students"),
        queryset=Student.objects.all(),
        color="primary",
        icon="fa fa-users"
    ),
    CountCard(
        title=_("Active Students"),
        queryset=Student.objects.filter(status=True),
        color="success",
        icon="fa fa-check"
    ),
    CountCard(
        title=_("Inactive Students"),
        queryset=Student.objects.filter(status=False),
        color="danger",
        icon="fa fa-ban"
    ),
]
