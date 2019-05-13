from toolchain import REGISTRY


class BaseNode:

    def __init_subclass__(cls, **kwargs):
        """Register each node"""
        super().__init_subclass__(**kwargs)
        key = f"{cls.__module__}.{cls.__name__}"
        if key not in REGISTRY:
            REGISTRY[key] = cls

    def _run(self):
        self.run()

    def run(self):
        """Public method that should be overriden by developer"""
        raise NotImplementedError()


class StartNode(BaseNode):
    """Each toolchain should start with a StartNode"""
    pass


class Node(BaseNode):
    pass


class EndNode(BaseNode):
    """Each toolchain should end with a EndNode"""
    pass
