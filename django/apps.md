# Django apps

## app design

James Bennett, a Django core developer, on Django app design:

> The art of creating and maintaining a good Django app is that it should follow the truncated Unix philosophy according to Douglas McIlroy: 'Write programs that do one thing and do it well.'

In essence, each app should be tightly focused on its task. If an app can’t be explained in a single sentence of moderate length, or you need to say 'and' more than once, it probably means the app is too big and should be broken up.

## app naming conventions

As a general rule, the app’s name should be a plural version of the app’s main model, but there are many good exceptions to this rule, `blog` being one of the most common ones.

Don't just consider the app's main model, though. You should also consider how you want your URLs to appear when choosing a name. If you want your site's blog to appear at http://www.example.com/weblog/, then consider naming your app `weblog` rather than `blog`, `posts`, or `blogposts`, even if the main model is `Post`, to make it easier for you to see which app corresponds with which part of the site.
