from django.db import models


CATEGORY_CHOICES = (
    ('Action and Adventure', 'Action and Adventure'),
    ('Classics', 'Classics'),
    ('Comic', 'Comic'),
    ('Graphic', 'Graphic'),
    ('Fantasy', 'Fantasy'),
    ('Historical Fiction', 'Historical Fiction'),
    ('Horror', 'Horror'),
    ('Literary Fiction', 'Literary Fiction'),
    ('Romance', 'Romance'),
    ('Science Fiction', 'Science Fiction'),
    ('Short Stories', 'Short Stories'),
    ('Women\'s Fiction', 'Women\'s Fiction'),
    ('Cookbooks', 'Cookbooks'),
    ('Science', 'Science'),
)



class Booklist(models.Model):
    title = models.CharField(max_length=100)
    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES,
        default='action_adventure'
    )


    def __str__(self):
        return self.title
    
    
     