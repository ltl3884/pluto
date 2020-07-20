from django import forms


class SearchForm(forms.Form):
    url = forms.CharField(label='url', widget=forms.TextInput(attrs={'placeholder': 'paste url here'}))

    def clean_url(self):
        url = self.cleaned_data.get('url')
        if not url.startswith('http'):
            self.add_error('url', "please input a valid url")
            # raise forms.ValidationError('please input a valid url')
        return url
