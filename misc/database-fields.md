# Database Fields

❌ emailVerified
✅ emailVerifiedAt

❌ isDeleted
✅ deletedAt

A interesting anti-under-engineering trick is to use timestamps instead of booleans in the database.

That way it is possible to  know when it was set to true, useful for debugging later. (from https://x.com/Swizec/status/1842312883721621562)
