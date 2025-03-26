# Reference commits using the commit message

You can reference commits using the commit message instead of the hash. The ":/" syntax accepts a regex that matches any part of the commit message, returning the youngest matching commit (see [docs](https://t.co/3vgL7zftHx?amp=1)).

```bash
git show :/add # shows the youngest commit with "add" in the message
```

from <https://twitter.com/offlinemark/status/1387833240321417222>
