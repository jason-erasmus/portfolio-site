from django.db import models


class Tag(models.Model):
    """
    The code snippet defines a model with a CharField named
    'name' and a __str__ method that returns the 'title'
    attribute.
    :return: The `__str__` method is returning the `title`
    attribute of the model instance.
    """

    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Project(models.Model):
    """
    The code snippet defines a Django model with fields
    for title, description, tags, and link, along with
    a method to return the title as a string.
    :return: The `__str__` method in the code snippet
    is returning the `title` attribute of the model
    instance.
    """

    title = models.CharField(max_length=200)
    description = models.TextField()
    tags = models.ManyToManyField(Tag, related_name="projects")
    link = models.URLField(max_length=200, blank=True)

    def __str__(self):
        return self.title


class ProjectImage(models.Model):
    """
    The code defines a model with a ForeignKey
    relationship to a Project model and an
    ImageField for storing images related to the
    project.
    :return: The `__str__` method in the code
    snippet is returning a formatted string that
    includes the title of the project associated
    with the image followed by the word "Image".
    """

    project = models.ForeignKey(
        Project, related_name="images", on_delete=models.CASCADE
    )
    image = models.ImageField(upload_to="project_images/")

    def __str__(self):
        return f"{self.project.title} Image"
