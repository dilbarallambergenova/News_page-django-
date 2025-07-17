from  django import forms

from news.models import Category,New


class AddNewsForm(forms.ModelForm):
    title=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    image=forms.ImageField(widget=forms.FileInput(attrs={'class':'form-control'}))
    content=forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}))
    Category=forms.ModelChoiceField(widget=forms.Select(attrs={'class':'form-control'}),queryset=Category.objects.all())
    
    class Meta:
        model=New
        fields=['title','image','content','category']

class FilterForm(forms.ModelForm):
    title = forms.CharField(
        label="Sarlavha",
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Sarlavha bo‘yicha qidirish'})
    )
    
    category = forms.ModelChoiceField(
        label="Kategoriya",
        queryset=Category.objects.all(),
        required=False,
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    
    content = forms.CharField(
        label="Matn",
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Matn bo‘yicha qidirish'})
    )
    # class Meta:
    #     model=New
    #     fields=['title','content','category']
    



  
