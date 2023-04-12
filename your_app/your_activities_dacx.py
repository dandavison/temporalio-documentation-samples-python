from temporalio import activity

from your_dataobject_dacx import YourParams

"""dacx
You can develop an Activity Definition by using the `@activity.defn` decorator.
Register the function as an Activity with a custom name through a decorator argument, for example `@activity.defn(name="your_activity")`.
dacx"""

"""dacx
Activity parameters are the function parameters of the function decorated with `@activity.defn`.
These can be any data type Temporal can convert, including dataclasses when properly type-annotated.
Technically this can be multiple parameters, but Temporal strongly encourages a single dataclass parameter containing all input fields.
dacx"""

"""dacx
An Activity Execution can return inputs and other Activity values.

The following example defines an Activity that takes a string as input and returns a string.
dacx"""

"""dacx
You can customize the Activity name with a custom name in the decorator argument. For example, `@activity.defn(name="your-activity")`.
If the name parameter is not specified, the Activity name defaults to the function name.
dacx"""

@activity.defn(name="your_activity")
async def your_activity(input: YourParams) -> str:
    return f"{input.greeting}, {input.name}!"


""" @dacx
id: how-to-develop-an-activity-definition-in-python
title: How to develop an Activity Definition in Python
label: Activity Definition
description: In the Temporal Go SDK programming model, an Activity Definition is an exportable function or a struct method.
lines: 1, 5-8, 27-29
@dacx """

""" @dacx
id: how-to-define-activity-parameters-in-python
title: How to do define Activity parameters in Python
label: Activity parameters
description: The only required parameter is `context.Context`, but Activities can support many custom parameters.
lines: 1-3, 10-14, 27-29
@dacx """

""" @dacx
id: how-to-define-activity-return-values-in-python
title: How to define Activity return values in Python
label: Activity return values
description: To return a value of the Workflow, use `return` to return an object.
lines: 16-20, 27-29
@dacx """

""" @dacx
id: how-to-customize-activity-type-in-python
title: How to customize Activity Type in Python
label: Customize Activity Type
description: Customize your Activity Type.
lines: 22-25, 27-29
@dacx """
