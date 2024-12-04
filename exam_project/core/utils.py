from exam_project.posts.models import Post
from exam_project.author.models import Author


def get_profile():
    return Author.objects.first()


def get_all_records():
    return Post.objects.all() if Post.objects.all() else None
