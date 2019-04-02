from django import forms


class AddStudent(forms.Form):
    std_email = forms.CharField()
    std_name = forms.CharField()
    std_bio = forms.CharField()
    std_contact = forms.CharField()
    ssc_int = forms.CharField()
    ssc_year = forms.CharField()
    ssc_cgpa = forms.CharField()
    hsc_int = forms.CharField()
    hsc_year = forms.CharField()
    hsc_cgpa = forms.CharField()
    honor_int = forms.CharField()
    honor_year = forms.CharField()
    honor_cgpa = forms.CharField()
    master_int = forms.CharField()
    master_year = forms.CharField()
    master_cgpa = forms.CharField()
    skills = forms.CharField()
    experience = forms.CharField()
    awards = forms.CharField()
    # picture = forms.ImageField(upload_to='pp/')


# class Company(forms.Form):
#     com_email = forms.EmailField()
#     com_name = forms.CharField()
#     com_bio = forms.CharField()
#     com_contact = forms.CharField()
#     skills = forms.CharField()

class AddJobs(forms.Form):
    com_name = forms.CharField()
    category = forms.CharField()
    post = forms.CharField()
    vacancy = forms.CharField()
    hours = forms.CharField()
    salary = forms.DecimalField()
    com_email = forms.EmailField()
    com_contact = forms.CharField()