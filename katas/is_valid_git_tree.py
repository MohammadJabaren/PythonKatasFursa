from collections import deque
from operator import truediv


def is_valid_git_tree(tree_map):
    """
    Determines if a given tree structure represents a valid Git tree.

    A valid Git tree should:
    1. Have exactly one root (no parent).
    2. Contain no cycles.

    Args:
        tree_map: a dictionary representing the Git tree (commit ID to list of child commit IDs)

    Returns:
        True if the tree is a valid Git tree, False otherwise
    """
    childrens = set(ch for set_ch in tree_map.values() for ch in set_ch)
    all_nodes = set(tree_map.keys()) | childrens
    roots = all_nodes - childrens

    if len(roots) != 1:
        return False

    root = roots.pop()
    visited = {child: False for child in all_nodes}
    queue = deque([root])
    visited[root] = True

    while queue:
        ch = queue.popleft()

        for child in tree_map.get(ch,[]):
            if visited[child]:
                return False
            visited[child] = True
            queue.append(child)

    return all(visited.values())



if __name__ == '__main__':
    valid_tree = {
        "A": ["B", "C"],
        "B": ["D"],
        "C": [],

    }

    invalid_tree = {
        "A": ["B"],
        "B": ["C"],
        "C": ["A"]  # cycle
    }

    print(f"Is valid tree: {is_valid_git_tree(valid_tree)}")  # Should be True
    print(f"Is valid tree: {is_valid_git_tree(invalid_tree)}")  # Should be False