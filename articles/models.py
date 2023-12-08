from django.db import models

class Subsections(models.Model):
    SECTION = (
        ('Python', 'Python'),
        ('LibraryPy', 'Library Py'),
        ('OOP', 'OOP'),
        ('Django', 'Django'),
        ('Tools', 'Tools'),
        ('SQL&DB', 'SQL & DB'),
        ('Algorithms', 'Algorithms'),
    )

    name = models.CharField(max_length=70, blank=True, null=False)
    section = models.CharField(max_length=10, choices=SECTION, blank=True)

    def __str__(self):
        return f'{self.section}: {self.name}'

class Items(models.Model):
    name = models.CharField(max_length=70, blank=True, null=False)
    subsection = models.ForeignKey(Subsections, on_delete=models.PROTECT, blank=True, null=False)

    def __str__(self):
        return f'{self.subsection} - {self.name}'


class Questions(models.Model):
    name = models.CharField(max_length=250, blank=True, null=False)
    answer = models.TextField(null=True)
    item = models.ForeignKey(Items, on_delete=models.PROTECT, blank=True, null=False)

    def __str__(self):
        return f'{self.item}: {self.name}'
