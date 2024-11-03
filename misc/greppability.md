# Greppability

from: https://morizbuesing.com/blog/greppability-code-metric

## Don’t split up identifiers

```javascript
const getTableName = (addressType: 'shipping' | 'billing') => {
    return `${addressType}_addresses`
}
```

Though it looks nice and DRY, it’s not great for maintainenance: someone will inevitably search the code base for the table name `shipping_addresses` and miss this occurence.

```javascript
const getTableName = (addressType: 'shipping' | 'billing') => {
    if (addressType === 'shipping') {
        return 'shipping_addresses'
    }
    if (addressType === 'billing') {
        return 'billing_addresses'
    }
    throw new TypeError('addressType must be billing or shipping')
}
```

## Use the same names for things across the stack

## Flat is better than nested

