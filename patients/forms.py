from django import forms
from . import models


class SearchForm(forms.Form):

    pass

class CreateImageForm(forms.ModelForm):
    class Meta:
        model = models.Image
        fields = ('file',)

    def save(self, pk, *args, **kwargs):
        image = super().save(commit=False)
        patient = models.Patient.objects.get(pk=pk)
        image.patient = patient
        image.save()


class CreatePatientForm(forms.ModelForm):
    class Meta:
        model = models.Patient
        fields = (
            "name",
            "id",
            "age",
            "gender",
            "doctor",
            "description",
            "disease1",
            "disease2",
            "disease3",
            "seriousness",
            "area",
        )
    def save(self, *args, **kwargs):
        patient = super().save(commit=False)
        return patient