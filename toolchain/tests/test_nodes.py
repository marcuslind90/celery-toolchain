from unittest import TestCase
from toolchain import REGISTRY
from toolchain.nodes import Node, BaseNode


class NodesTestCase(TestCase):

    def test_registry(self):
        """Test that registration of node classes works"""
        class Foo(BaseNode):
            pass

        class Bar(Node):
            pass

        self.assertTrue("toolchain.tests.test_nodes.Foo" in REGISTRY)
        self.assertTrue("toolchain.tests.test_nodes.Bar" in REGISTRY)
