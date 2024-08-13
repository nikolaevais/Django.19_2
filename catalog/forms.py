from django.forms import ModelForm, forms, BooleanField

from catalog.models import Product, Version


class StyleFormMixin:

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for fild_name, fild in self.fields.items():
            if isinstance(fild, BooleanField):
                fild.widget.attrs['class'] = "form-check-input"
            else:
                fild.widget.attrs['class'] = "form-control"


class ProductForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Product
        exclude = ('created_at', 'updated_at',)


    def clean_name(self):
        clean_name = self.cleaned_data['name']

        forbidden_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']

        for word in forbidden_words:
            if word in clean_name.lower():
                raise forms.ValidationError('Данное слово нельзя использовать в названии')
        return clean_name


    def clean_description(self):
        clean_description = self.cleaned_data['description']

        forbidden_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']

        for word in forbidden_words:
            if word in clean_description.lower():
                raise forms.ValidationError(f'{word} - это слово нельзя использовать в описании')
        return clean_description



class VersionForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Version
        fields = "__all__"