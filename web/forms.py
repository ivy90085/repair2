# -*- coding: UTF-8 -*-
from django import forms
from web.models import Repair

# 日誌表單
class RepairForm(forms.ModelForm):
        class Meta:
                model = Repair
                fields = ['memo']