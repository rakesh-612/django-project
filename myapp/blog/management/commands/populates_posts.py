from blog.models import Post, Category
from django.core.management.base import BaseCommand
from typing import Any
import random


class Command(BaseCommand):
    help = "This command inserts post data"

    def handle(self, *args: Any, **options: Any):

        Post.objects.all().delete()  # Delete existing datas

        titles = [
            "The Future of AI",
            "Climate Change Solutions",
            "Remote Work Trends",
            "Quantum Computing Explained",
            "Renewable Energy Innovations",
            "Deep Learning Demystified",
            "Post-Pandemic Economic Outlook",
            "Blockchain in Finance",
            "Storytelling in Marketing",
            "Medical Technology Advances",
            "Space Exploration Challenges",
            "Psychology of Decision Making",
            "Evolution of Social Media",
            "The Art of Cooking",
            "Cultural Diversity in Society",
            "Sustainable Development Investments",
            "Globalization Impact",
            "Power of Mindfulness",
            "Online Learning Revolution",
            "Art and Technology Fusion",
        ]

        contents = [
            "Exploring the future of artificial intelligence...",
            "Discovering solutions to combat climate change...",
            "Analyzing trends in remote work...",
            "Introduction to quantum computing...",
            "Latest innovations in renewable energy...",
            "Understanding deep learning...",
            "Economic outlook after pandemic...",
            "Blockchain technology in finance...",
            "Storytelling in marketing...",
            "Advancements in medical technology...",
            "Challenges in space exploration...",
            "Psychology behind decisions...",
            "Evolution of social media...",
            "Creativity in cooking...",
            "Cultural diversity importance...",
            "Sustainable development initiatives...",
            "Impact of globalization...",
            "Mindfulness practices...",
            "Online learning platforms...",
            "Art and technology fusion..."
        ]

        img_urls = [
            "https://picsum.photos/id/1/800/400",
            "https://picsum.photos/id/2/800/400",
            "https://picsum.photos/id/3/800/400",
            "https://picsum.photos/id/4/800/400",
            "https://picsum.photos/id/5/800/400",
            "https://picsum.photos/id/6/800/400",
            "https://picsum.photos/id/7/800/400",
            "https://picsum.photos/id/8/800/400",
            "https://picsum.photos/id/9/800/400",
            "https://picsum.photos/id/10/800/400",
            "https://picsum.photos/id/11/800/400",
            "https://picsum.photos/id/12/800/400",
            "https://picsum.photos/id/13/800/400",
            "https://picsum.photos/id/14/800/400",
            "https://picsum.photos/id/15/800/400",
            "https://picsum.photos/id/16/800/400",
            "https://picsum.photos/id/17/800/400",
            "https://picsum.photos/id/18/800/400",
            "https://picsum.photos/id/19/800/400",
            "https://picsum.photos/id/20/800/400",
        ]

        categories = Category.objects.all()

        for title, content, img_url in zip(titles, contents, img_urls):
            category = random.choice(categories)

            Post.objects.create(
                title=title,
                content=content,
                img_url=img_url,
                category=category
            )

        self.stdout.write(self.style.SUCCESS("Completed inserting data!"))
