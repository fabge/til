# CloudFormation default values

The AWS Documentation for CloudFormation `Default` values says:

> A value of the appropriate type for the template to use if no value is specified when a stack is created. If you define constraints for the parameter, you must specify a value that adheres to those constraints.

This behaviour can be very pernicious, as default values are only set on stack **creation** and when no value is specified.

Meaning: **You cannot update the value by setting a new default value!**

Instead, set values by passing them in as parameters in a `samconfig.toml` file or by passing them in as parameters when you deploy the stack.
