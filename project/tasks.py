from project.extensions import broker


@broker.actor()
def example_task():
    print("Hello world")
