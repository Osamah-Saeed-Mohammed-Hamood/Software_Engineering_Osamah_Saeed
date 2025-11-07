from django import forms

class StudentForm(forms.Form):
    first_name = forms.CharField(max_length=50, label="الاسم الأول")
    last_name = forms.CharField(max_length=50, label="الاسم الأخير")
    age = forms.IntegerField(min_value=1, max_value=120, label="العمر")
    level = forms.ChoiceField(
        choices=[('freshman', 'أولى'), ('sophomore', 'ثانية'), ('junior', 'ثالثة'), ('senior', 'رابعة')],
        label="المرحلة الجامعية"
    )

    def clean_first_name(self):
        first_name = self.cleaned_data['first_name']
        if any(char.isdigit() for char in first_name):
            raise forms.ValidationError("الاسم الأول لا يمكن أن يحتوي على أرقام.")
        return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data['last_name']
        if any(char.isdigit() for char in last_name):
            raise forms.ValidationError("الاسم الأخير لا يمكن أن يحتوي على أرقام.")
        return last_name
