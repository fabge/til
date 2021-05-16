# How to cheat at unit tests

Again - [Simon Willison](https://simonwillison.net/2020/Feb/11/cheating-at-unit-tests-pytest-black/):

## How to cheat at unit tests with pytest and Black

In pure test-driven development you write the tests first, and don’t start on the implementation until you’ve watched them fail.

Most of the time I find that this is a net loss on productivity. I tend to prototype my way to solutions, so I often find myself with rough running code before I’ve developed enough of a concrete implementation plan to be able to write the tests.

So… I cheat. Once I’m happy with the implementation I write the tests to match it. Then once I have the tests in place and I know what needs to change I can switch to using changes to the tests to drive the implementation. 

In particular, I like using a rough initial implementation to help generate the tests in the first place. 

Here’s how I do that with pytest. I’ll write a test that looks something like this:

```python
def test_some_api(client):
    response = client.get("/some/api/") 
    assert False == response.json() 
```

Note that I’m using the pytest-django `client` fixture here, which magically passes a fully configured Django test client object to my test function.

I run this test, and it fails: 

```python
pytest -k test_some_api 
```

(`pytest -k blah` runs just tests that contain `blah` in their name)

Now… I run the test again, but with the `--pdb` option to cause pytest to drop me into a debugger at the failure point:

```bash
$ pytest -k test_some_api --pdb
== test session starts ===
platform darwin -- Python 3.7.5, pytest-5.3.5, py-1.8.1, pluggy-0.13.1
django: settings: config.test_settings (from ini)
...
client = <django.test.client.client object="" at="" 0x10cfdb510="">

    def test_some_api(client):
        response = client.get("/some/api/")
>       assert False == response.json()
E       assert False == {'this': ['is', 'an', 'example', 'api']}
core/test_docs.py:27: AssertionError
>> entering PDB >>
>> PDB post_mortem (IO-capturing turned off) >>
> core/test_docs.py(27)test_some_api()
-> assert False == response.json()
(Pdb) response.json()
{'this': ['is', 'an', 'example', 'api'], 'that_outputs': 'JSON'}
(Pdb)
```

Running `response.json()` in the debugger dumps out the actual value to the console.

Then I copy that output—in this case `{'this': ['is', 'an', 'example', 'api'], 'that_outputs': 'JSON'}`—and paste it into the test:

```python
def test_some_api(client):
    response = client.get("/some/api/")
    assert {'this': ['is', 'an', 'example', 'api'], 'that_outputs': 'JSON'} == response.json()
```

Finally, I run `black .` in my project root to reformat the test:

```python
def test_some_api(client):
    response = client.get("/some/api/")
    assert {
        "this": ["is", "an", "example", "api"],
        "that_outputs": "JSON",
    } == response.json()
```

This last step means that no matter how giant and ugly the test comparison has become I’ll always get a neatly formatted test out of it.

I always eyeball the generated test to make sure that it’s what I would have written by hand if I wasn’t so lazy—then I commit it along with the implementation and move on to the next task.</django.test.client.client></a> <a id="Cheating_at_unit_tests_10">

I’ve used this technique to write many of the tests in both</a> [Datasette](https://github.com/simonw/datasette) and [sqlite-utils](https://github.com/simonw/sqlite-utils), and those are by far the best tested pieces of software I’ve ever released.

I started doing this around two years ago, and I’ve held off writing about it until I was confident I understood the downsides. I haven’t found any yet: I end up with a robust, comprehensive test suite and it takes me less than half the time to write the tests than if I’d been hand-crafting all of those comparisons from scratch.