from rest_framework import serializers
from .models import Author, Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        exclude = ['author']


class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, required=False)

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']

    def create(self, validated_data):
        if 'name' not in validated_data:
            raise serializers.ValidationError('Name field is required')
        books_data = validated_data.pop('books', [])
        author = Author.objects.create(**validated_data)
        for book_data in books_data:
            Book.objects.create(author=author, **book_data)
        return author
