# Loading button

Problem:
When a user clicks a button the response may be slow.

Solution:

1. Display a loading indicator
1. Set aria-disabled="true" on the button (avoid disabled since it's unfriendly to screen readers)
1. Ignore additional button clicks while loading is in progress
1. Consider changing the label to clarify what's happening

## Example

Click here for the full source code: [loading-button-src.html](./loading-button-src.html)

```html
<div>
    <p id="response">The click me response will be displayed after this sentence. </p>
    <button class="btn"
        hx-get="https://hub.dummyapis.com/delay?seconds=5"
        hx-swap="beforeend"
        hx-target="#response"
        hx-indicator="#loading"
        hx-disabled-elt="this"
    >
        <span id="loading" class="loading loading-spinner my-indicator"></span>
        Click Me
    </button>
</div>
```

<iframe src="./loading-button-src.html" name="loading-button-src.html"></iframe>
