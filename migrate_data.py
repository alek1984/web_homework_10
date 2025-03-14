from django.core.management.base import BaseCommand
from quotes.models import Quote, Author
from pymongo import MongoClient

class Command(BaseCommand):
    help = 'Міграція даних з MongoDB у PostgreSQL'

    def handle(self, *args, **kwargs):
        client = MongoClient('mongodb://localhost:27017/')
        db = client.quotes_mongo

        for author in db.authors.find():
            Author.objects.get_or_create(
                id=str(author['_id']),
                name=author['name'],
                bio=author.get('bio', '')
            )

        for quote in db.quotes.find():
            author = Author.objects.get(id=str(quote['author']))
            Quote.objects.create(
                text=quote['text'],
                author=author,
                tags=quote['tags']
            )

        self.stdout.write(self.style.SUCCESS('Міграція завершена!'))
