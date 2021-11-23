from django import forms

class BatchCostForm(forms.Form):

    newBatch = forms.CharField(label="newBatch", max_length=15)
    batchDate = forms.DateField(label="batchDate")
    supplier1 = forms.CharField(label="supplier1", max_length=30)
    weight1 = form.IntegerField(label="weight1", localize=False, min_value=0, max_value=10000)
    value1 = form.DecimalField(label="value1", localize=False, min_value=0, decimal_places=3)
    supplier2 = forms.CharField(label="supplier2", max_length=30)
    weight2 = form.IntegerField(label="weight2", localize=False, min_value=0, max_value=10000)
    value2 = form.DecimalField(label="value2", localize=False, min_value=0, decimal_places=3)
    supplier3 = forms.CharField(label="supplier3", max_length=30)
    weight3 = form.IntegerField(label="weight3", localize=False, min_value=0, max_value=10000)
    value3 = form.DecimalField(label="value3", localize=False, min_value=0, decimal_places=3)
    supplier4 = forms.CharField(label="supplier4", max_length=30)
    weight4 = form.IntegerField(label="weight4", localize=False, min_value=0, max_value=10000)
    value4 = form.DecimalField(label="value4", localize=False, min_value=0, decimal_places=3)
