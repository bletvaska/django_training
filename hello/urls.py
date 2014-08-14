from django.conf.urls import patterns, url


urlpatterns = patterns('hello.views',
    url(r'^(/(?P<name>\w+))?$', 'greetings'),
)







# urlpatterns = patterns('hello.views',
#     url(r'^(?P<name>\w+)$', 'greetings'),
# )
