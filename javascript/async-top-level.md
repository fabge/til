# Run async function on top level

```javascript
(async() => {
  console.log('before start');
  await start();
  console.log('after start');
})();
```
