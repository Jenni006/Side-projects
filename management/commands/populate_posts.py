from typing import Any
from blog.models import Post, Category
from django.core.management.base import BaseCommand
import random

class Command(BaseCommand):
    help = "This command inserts data"

    def handle(self, *args: Any, **options: Any ):
        Post.objects.all().delete() 



        titles = [
            "Exploring the Beauty of Nature",
            "10 Tips for Staying Productive",
            "The Future of Artificial Intelligence",
            "Travel Guide to Paris",
            "Healthy Eating Habits",
            "Top 5 Programming Languages for 2024",
            "Mindfulness and Mental Health",
            "Innovations in Renewable Energy",
            "The History of Space Exploration",
            "Mastering Photography Basics"
        ]

        contents = [
            "Discover the wonders of untouched landscapes, serene forests, and breathtaking mountain views that refresh the soul.",
            "Boost your productivity with these simple yet effective tips that help you manage time and tasks more efficiently.",
            "Dive into the advancements in AI, exploring how machine learning and robotics are shaping the future.",
            "A comprehensive guide to exploring the romantic city of Paris, from iconic landmarks to hidden gems.",
            "Learn about balanced diets, meal planning, and tips for maintaining a healthy lifestyle.",
            "Explore the top programming languages in demand this year, with tips on where to start learning.",
            "Understand the importance of mindfulness practices and their impact on mental well-being.",
            "Explore the latest innovations in solar, wind, and other renewable energy sources transforming the world.",
            "Journey through time as we explore humanity's incredible milestones in space exploration.",
            "Learn the essential techniques for capturing stunning photographs, from composition to lighting."
        ]

        img_urls = [
            'https://picsum.photos/id/28/800/400',
            "https://picsum.photos/id/9/800/400",
            "https://picsum.photos/id/180/800/400",
            "https://picsum.photos/id/195/800/400",
            "https://picsum.photos/id/102/800/400",
            "https://picsum.photos/id/60/800/400",
            "https://picsum.photos/id/103/800/400",
            "https://picsum.photos/id/182/800/400",
            "https://picsum.photos/id/120/800/400",
            "https://picsum.photos/id/91/800/400"
            ]
        categories = Category.objects.all()
        for title, content, img_url in zip(titles, contents, img_urls):
            category = random.choice(categories) 
            Post.objects.create(title=title, content=content, image_url=img_url, category=category)

        self.stdout.write(self.style.SUCCESS("Completed insterting Data!"))