class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

class BinaryTree:
    def __init__(self, root=None):
        self.root = root

    def print_structure(self):
        if self.root is None:
            print("El árbol está vacío.")
        else:
            self._print_node(self.root, level=0, prefix="Root: ")

    def _print_node(self, current_node, level, prefix):
        if current_node is not None:
            indent = "    " * level
            print(f"{indent}{prefix}{current_node.data}")

            if current_node.left or current_node.right:
                if current_node.left:
                    self._print_node(current_node.left, level + 1, "L--->")
                else:
                    print(f"{indent}.    L---> None")

            if current_node.right:
                self._print_node(current_node.right, level + 1, "R--->")
            else:
                print(f"{indent}.    R---> None")



print("\n=== PRUEBA BINARY TREE ===")
son_dev = TreeNode("Son (Dev)")
daughter_qa = TreeNode("Daughter (QA)")

father_manager = TreeNode("Father (Manager)", left=son_dev, right=daughter_qa)
uncle_director = TreeNode("Uncle (Director)")

grandpa_ceo = TreeNode("Grand_pa (CEO)", left=father_manager, right=uncle_director)

tree = BinaryTree(grandpa_ceo)
tree.print_structure()