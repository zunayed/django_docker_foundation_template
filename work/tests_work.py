from django.core.urlresolvers import resolve
from django.http import HttpRequest
from nose import with_setup

from work.views import work_page
from work.models import Post


def test_work_url_resolves_to_people_page_view():
    '''
    test if websites get resolved
    '''
    found = resolve('/work/')
    assert found.func == work_page


def test_work_page_returns_correct_html():
    '''
    See if page returns some html with proper headline
    '''
    request = HttpRequest()
    response = work_page(request)
    assert 'html class="no-js" lang="en">' in response.content
    assert 'Work' in response.content


def set_up():
    '''
    create some sample blog post
    '''
    first_post = Post()
    second_post = Post()

    first_post.createPost('Zunayed', 'Ali', 'title 1', 'Test content')
    second_post.createPost('Mike', 'Dory', 'title 2', 'Test content')
    first_post.save()
    second_post.save()


@with_setup(set_up)
def test_blog_post():
    """
    A blog post must have a created date, last modified and content fields
    """
    saved_post = Post.objects.all()

    assert saved_post.count() == 2

    first_post = saved_post[0]
    assert first_post.first_name == 'Zunayed'
    assert first_post.last_name == 'Ali'
    assert first_post.title == 'title 1'

    print first_post
    assert first_post.__unicode__() == 'Zunayed - title 1'

