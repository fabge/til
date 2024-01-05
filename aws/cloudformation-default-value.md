# CloudFormation default values

The AWS Documentation for CloudFormation `Default` values says:

> A value of the appropriate type for the template to use if no value is specified when a stack is created. If you define constraints for the parameter, you must specify a value that adheres to those constraints.

This behaviour can be very pernicious, as it means that default values are only set on stack **creation** and when no value is specified.

If you update the stack and change the default value of a parameter, the new default value will not be applied to the stack.
