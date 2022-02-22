from django.db import models


def image_modifier_function(file):
    # This is where you would need to call a Python or external
    # function to create a modified image.
    return file


class Blog(models.Model):
    title = models.CharField(max_length=150)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class UserImages(models.Model):
    original_file = models.ImageField()
    modified_file = models.ImageField(blank=True, null=True)

    def calculate_modified_file(self):
        self.modified_file = image_modifier_function(original_file)
        self.save()
