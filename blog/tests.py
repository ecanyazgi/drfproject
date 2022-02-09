from django.test import TestCase
from django.contrib.auth.models import User
from .models import Category,Post
from . import enums

class Test_Create_Post(TestCase):

    @classmethod
    def setUpTestData(cls):
        test_category = Category.objects.create(name = 'django')
        testuser1 = User.objects.create_user(
            username = 'test_user1', password = '123456789')
        test_post = Post.objects.create(category_id=1,title='Title', 
        excerpt='asdasd',content = 'asdasd', slug = 'Title', author_id=1,status=enums.Options.PUBLISHED )

    def test_blog_content(self):
        post = Post.objects.get(id=1)
        cat = Category.objects.get(id=1)
        author = f'{post.author}'
        excerpt = f'{post.excerpt}'
        title = f'{post.title}'
        content = f'{post.content}'
        status = f'{post.status}'
        self.assertEqual(author,'test_user1')
        self.assertEqual(excerpt,'asdasd')
        self.assertEqual(title,'Title')
        self.assertEqual(content,'asdasd')
        self.assertEqual(status,'published')
        self.assertEqual(str(post),'Title')
        self.assertEqual(str(cat),'django')