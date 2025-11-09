# Github pages

When turning on [GitHub Pages](https://docs.github.com/en/pages/quickstart) for a repository, it will turn the contents of the repository into a very minimal website. I love the simplicity of having only a README.md and some auxiliary files turned into a minimal website with zero configuration needed.

To reproduce the rendered website locally, put the following content into a `gemfile`:

```text
source "https://rubygems.org"
gem "github-pages", group: :jekyll_plugins
```

and run:

```bash
bundle install
bundle exec jekyll serve
```
