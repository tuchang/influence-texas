from django import forms

from . import models


class OpenStatesLegislatorForm(forms.ModelForm):

    class Meta:
        model = models.Legislator
        fields = ('name', 'first_name', 'last_name', 'party', 'district', 'chamber',
                  'openstates_updated_at', 'openstates_leg_id', 'url', 'photo_url')
