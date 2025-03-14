from django import forms
from .models import Trainers, DistrictChoices, QualificationChoices
from courses.models import Courses

class TrainerRegisterForm(forms.ModelForm):

    class Meta:

        model = Trainers

        exclude = ["employee_id", "uuid", "active_status", "profile"]
        
        widgets = {
            "first_name": forms.TextInput(attrs={
                "class": "block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 dark:focus:shadow-outline-gray form-input",
                "required": "required"
            }),
            "last_name": forms.TextInput(attrs={
                "class": "block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 dark:focus:shadow-outline-gray form-input",
                "required": "required"
            }),
            "photo": forms.FileInput(attrs={
                "class": "block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 dark:focus:shadow-outline-gray form-input",
                "required": "required"
            }),
            "email": forms.EmailInput(attrs={
                "class": "block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 dark:focus:shadow-outline-gray form-input",
                "required": "required"
            }),
            "contact_num": forms.TextInput(attrs={
                "class": "block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 dark:focus:shadow-outline-gray form-input",
                "required": "required"
            }),
            "house_name": forms.TextInput(attrs={
                "class": "block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 dark:focus:shadow-outline-gray form-input",
                "required": "required"
            }),
            "post_office": forms.TextInput(attrs={
                "class": "block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 dark:focus:shadow-outline-gray form-input",
                "required": "required"
            }),
            "pincode": forms.TextInput(attrs={
                "class": "block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 dark:focus:shadow-outline-gray form-input",
                "required": "required"
            }),
            "stream": forms.TextInput(attrs={
                "class": "block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 dark:focus:shadow-outline-gray form-input",
                "required": "required"
            }),
            "id_proof": forms.FileInput(attrs={
                "class": "block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 dark:focus:shadow-outline-gray form-input",
                "required": "required"
            }),
        }

    district = forms.ChoiceField(
        choices=DistrictChoices.choices,
        widget=forms.Select(attrs={
            "class": "block w-full mt-1 text-sm dark:text-gray-300 dark:border-gray-600 dark:bg-gray-700 form-select focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:focus:shadow-outline-gray",
            "required": "required"
        })
    )

    course = forms.ModelChoiceField(

        queryset=Courses.objects.all(),

        widget=forms.Select(attrs={

            "class": "block w-full mt-1 text-sm dark:text-gray-300 dark:border-gray-600 dark:bg-gray-700 form-select focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:focus:shadow-outline-gray",
            "required": "required"
        })
    )

    qualification = forms.ChoiceField(

        choices=QualificationChoices.choices,

        widget=forms.Select(attrs={

            "class": "block w-full mt-1 text-sm dark:text-gray-300 dark:border-gray-600 dark:bg-gray-700 form-select focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:focus:shadow-outline-gray",
            "required": "required"
        })
    )

    def clean(self):

        cleaned_data = super().clean()

        pincode = cleaned_data.get("pincode")

        email = cleaned_data.get("email")

        if Trainers.objects.filter(profile__username=email).exists():

            self.add_error("email", "This email is already registered. Please use another email.")


        if len(str(pincode)) != 6:

            self.add_error("pincode", "Pincode must be exactly 6 digits.")

        return cleaned_data

    def __init__(self, *args, **kwargs):

        super(TrainerRegisterForm, self).__init__(*args, **kwargs)

        if not self.instance:
            
            self.fields["photo"].widget.attrs["required"] = "required"  