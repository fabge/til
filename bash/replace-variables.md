# Replace variables

`sed` is an often used pattern to replace variables in bash files. I find `sed` commands to be very hard to read though. An easier way is using `envsubst`:

`test.sh`

```bash
foo=$FOO
bar=$BAR
```

`envsubst` replaces the variables in `test.sh`. Defining `$BAR` afterwards, replaces only this variable.

```bash
BAR=foo envsubst '$BAR'< test.sh

foo=$FOO
bar=foo
```

Sourcing an environment beforehands makes it possible to store all values which should be replaced in a file.
With `>` the content can be written to a new file. Caution: Overwriting the same file *does not work*.

```bash
source .env
envsubst < test.sh > destination.sh

foo=$FOO
bar=foo
```
