from django.core.urlresolvers import resolve
from django.http import HttpRequest
from nose import with_setup

from people.views import people_page
from people.models import People


def test_people_url_resolves_to_people_page_view():
    '''
    test if websites get resolved
    '''
    found = resolve('/people/')
    assert found.func == people_page


def test_people_page_returns_correct_html():
    '''
    See if page returns some html with proper headline
    '''
    request = HttpRequest()
    response = people_page(request)
    assert 'html class="no-js" lang="en">' in response.content
    assert 'People' in response.content


def set_up():
    '''
    create some sample people
    '''
    first_person = People()
    first_person.first_name = 'Zunayed'
    first_person.last_name = 'Ali'
    first_person.title = 'Dev'
    first_person.save()

    second_person = People()
    second_person.first_name = 'Mike'
    second_person.last_name = 'Dory'
    second_person.title = 'boss'
    second_person.save()


@with_setup(set_up)
def test_retrieving_people():
    '''
    check if employees were created and saved + unicode function
    '''
    saved_items = People.objects.all()
    assert saved_items.count() == 2

    first_saved_item = saved_items[0]
    second_saved_item = saved_items[1]
    assert first_saved_item.first_name == 'Zunayed'
    assert first_saved_item.last_name == 'Ali'
    assert first_saved_item.title == 'Dev'

    assert second_saved_item.first_name == 'Mike'

    assert first_saved_item.__unicode__() == 'Zunayed Ali'
