# Idempotence

Idempotence (UK: /ˌɪdɛmˈpoʊtəns/, US: /ˈaɪdəm-/) - operations can be applied multiple times without changing the result beyond the initial application.

This property is especially relevant in distributed systems, where a message may be delivered multiple times. The message handler has got to be be idempotent.  
It is generally difficult/rare to implement exactly-once semantics. Usually it is at-least-once (from [@nodirt_](https://twitter.com/nodirt_/status/1530297313473617920)).

There are many useful nuggets in this thread, this one I found particularly helpful:

> Unlike state in a single process, most of the time, you can't make mutations in two systems atomically, e.g. marking a purchase order as placed in the database and sending a confirmation email is not atomic.  
You might successfully mutate first system, but fail on the second one.  
If your storage system supports Change Data Capture, like @dynamodb, only place the purchase order, and in the background listen to committed changes and send the email there. This assumes that sending the email is idempotent.
