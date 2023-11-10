<script src="https://unpkg.com/htmx.org@1.9.8"></script>
<link href="https://cdn.jsdelivr.net/npm/daisyui@3.9.4/dist/full.css" rel="stylesheet" type="text/css" />
<script src="https://cdn.tailwindcss.com"></script>
<style>
    .my-indicator {
        display: none;
    }

    .htmx-request .my-indicator {
        display: inline;
    }

    .htmx-request.my-indicator {
        display: inline;
    }
</style>

# Loading button

Problem:
When a user clicks a button the response may be slow.

Solution:

1. Display a loading indicator
1. Set aria-disabled="true" on the button (avoid disabled since it's unfriendly to screen readers)
1. Ignore additional button clicks while loading is in progress
1. Consider changing the label to clarify what's happening

## Example

<div>
    <p id="response">The click me response will be displayed after this sentence. </p>
    <button class="btn"
        hx-get="https://hub.dummyapis.com/delay?seconds=7"
        hx-swap="beforeend"
        hx-target="#response"
        hx-indicator="#loading"
        hx-disabled-elt="this"
    >
        <span id="loading" class="loading loading-spinner my-indicator"></span>
        Click Me
    </button>
</div>
