# Django urls

From Django's [design philosophies](https://docs.djangoproject.com/en/5.1/misc/design-philosophies/):

> ## Definitive URLs
>
> Technically, `foo.com/bar` and `foo.com/bar/` are two different URLs, and search-engine robots (and some web traffic-analyzing tools) would treat them as separate pages. Django should make an effort to “normalize” URLs so that search-engine robots don’t get confused.
>
> This is the reasoning behind the `APPEND_SLASH` setting.

and

> ## APPEND_SLASH
>
> Default: True
>
> When set to True, if the request URL does not match any of the patterns in the URLconf and it doesn’t end in a slash, an HTTP redirect is issued to the same URL with a slash appended. Note that the redirect may cause any data submitted in a POST request to be lost.
