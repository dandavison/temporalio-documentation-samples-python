from temporalio import workflow
from activities import ComposeGreetingInput
from temporalio.workflow import ParentClosePolicy

"""dacx
To spawn a Child Workflow Execution in Python, use the [`execute_child_workflow()`](https://python.temporal.io/temporalio.workflow.html#execute_child_workflow) function which starts the Child Workflow and waits for completion or
use the [`start_child_workflow()`](https://python.temporal.io/temporalio.workflow.html#start_child_workflow) function to start a Child Workflow and return its handle. 
This is useful if you want to do something after it has only started, or to get the Workflow/Run ID, or to be able to signal it while running.

:::note

`execute_child_workflow()` is a helper function for `start_child_workflow()` plus `await handle`.

:::
dacx"""

"""dacx
Set the `parent_close_policy` parameter inside the [`start_child_workflow`](https://python.temporal.io/temporalio.workflow.html#start_child_workflow) function or the [`execute_child_workflow()`](https://python.temporal.io/temporalio.workflow.html#execute_child_workflow) function to specify the behavior of the Child Workflow when the Parent Workflow closes.
dacx"""


@workflow.defn
class ComposeGreeting:
    @workflow.run
    async def run(self, input: ComposeGreetingInput) -> str:
        return f"{input.greeting}, {input.name}!"


@workflow.defn
class GreetingWorkflow:
    @workflow.run
    async def run(self, name: str) -> str:
        return await workflow.execute_child_workflow(
            ComposeGreeting.run,
            ComposeGreetingInput("Hello", name),
            id="hello-child-workflow-workflow-child-id",
            parent_close_policy=ParentClosePolicy.TERMINATE,
        )


""" @dacx
id: how-to-spawn-a-child-workflow-execution-in-python
title: How to spawn a Child Workflow Execution in Python
label: Child Workflow Execution
description: To spawn a Child Workflow Execution in Python use the execute_child_workflow() function which starts the Child Workflow and waits for completion or use the start_child_workflow() function to start a Child Workflow and return its handle.
lines: 5-15, 22-38
@dacx """

""" @dacx
id: how-to-set-a-parent-close-policy-in-python
title: How to set a Parent Close Policy in Python
label: Parent Close Policy
description: Create an instance of the `ParentClosePolicy` class.
lines: 3, 17-19, 22-38
@dacx """
