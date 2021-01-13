from django import forms
class Feedback(forms.Form):
    name=forms.CharField()
    roll=forms.IntegerField()
    email=forms.EmailField()
    comments=forms.CharField(widget=forms.Textarea)
    def clean_name(self):
        n=self.cleaned_data['name']
        if(len(n)>10):
            raise forms.ValidationError("num of chars > 10")
            return n
    def clean_roll(self):
        r1=self.cleaned_data['roll']
        r=str(r1)
        if(len(r)>=4):
            raise forms.ValidationError("roll num should be < 4")
            return r
