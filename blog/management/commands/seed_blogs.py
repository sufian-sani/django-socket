# blog/management/commands/seed_blogs.py
from django.core.management.base import BaseCommand
from blog.models import Blog
from django.contrib.auth.models import User
from faker import Faker
import random

class Command(BaseCommand):
    help = 'Seed the database with blogs'

    def handle(self, *args, **kwargs):
        fake = Faker()
        users = list(User.objects.all())
        if not users:
            self.stdout.write(self.style.ERROR("No users found. Create some first."))
            return

        categories = ['Tech', 'Lifestyle', 'Travel', 'Food', 'Business']

        for i in range(20):  # number of blogs to create
            user = random.choice(users)
            blog = Blog.objects.create(
                title=fake.sentence(nb_words=6),
                content=fake.paragraph(nb_sentences=10),
                author=user,
                category=random.choice(categories)
            )
            blog.save()
            self.stdout.write(self.style.SUCCESS(f'Blog "{blog.title}" created by {user.username}'))
