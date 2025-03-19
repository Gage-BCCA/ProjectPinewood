from django.test import TestCase
from ..models import PostStatus, Post


class BlogTestCase(TestCase):

    def setUp(self):
        PostStatus.objects.create(status="New")

    def test_post_status_creation(self):
        PostStatus.objects.create(status="Testing")
        self.assertIsNotNone(PostStatus.objects.get(status="Testing"))

    def test_post_creation(self):
        Post.objects.create(
            title="Article 1",
            subtitle="The Best Article",
            body="Just playing around with my bros",
            status=PostStatus.objects.get(status="New"),
        )

        target_post = Post.objects.get(title="Article 1")
        self.assertIsNotNone(target_post)
        self.assertIsInstance(target_post, Post)
        self.assertEqual(target_post.title, "Article 1")

    def test_post_creation_slugify(self):
        target_post = Post.objects.create(
            title="Article 1",
            subtitle="The Best Article",
            body="Just playing around with my bros",
            status=PostStatus.objects.get(status="New"),
        )
        self.assertEqual(target_post.slug, "article-1")
