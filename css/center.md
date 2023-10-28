# How to center

```css
/* Horizontal Centering */
.horizontal-center {
    display: flex;
    justify-content: center;
}

.horizontal-center2 {
    text-align: center;
}

.horizontal-center3 {
    position: absolute;
    left: 50%;
    transform: translateX(-50%);
}

/* Vertical Centering */
.vertical-center {
    display: flex;
    align-items: center;
    height: 100vh; /* Center within viewport height */
}

.vertical-center2 {
    position: absolute;
    top: 50%;
    transform: translateY(-50%);
}

/* Centering both horizontally and vertically */
.center-both {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh; /* Center within viewport height */
}
```
