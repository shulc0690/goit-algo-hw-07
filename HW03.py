class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
        self.height = 1

# Функція для вставки елемента у дерево
def insert(root, key):
    if not root:
        return TreeNode(key)
    elif key < root.val:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)

    root.height = 1 + max(get_height(root.left), get_height(root.right))

    balance = get_balance(root)

    # Лівий лівий випадок
    if balance > 1 and key < root.left.val:
        return right_rotate(root)

    # Правий правий випадок
    if balance < -1 and key > root.right.val:
        return left_rotate(root)

    # Лівий правий випадок
    if balance > 1 and key > root.left.val:
        root.left = left_rotate(root.left)
        return right_rotate(root)

    # Правий лівий випадок
    if balance < -1 and key < root.right.val:
        root.right = right_rotate(root.right)
        return left_rotate(root)

    return root

# Функція для знаходження висоти вузла
def get_height(root):
    if not root:
        return 0
    return root.height

# Функція для обчислення балансу вузла
def get_balance(root):
    if not root:
        return 0
    return get_height(root.left) - get_height(root.right)

# Функція для правого повороту піддерева
def right_rotate(z):
    y = z.left
    T3 = y.right

    y.right = z
    z.left = T3

    z.height = 1 + max(get_height(z.left), get_height(z.right))
    y.height = 1 + max(get_height(y.left), get_height(y.right))

    return y

# Функція для лівого повороту піддерева
def left_rotate(z):
    y = z.right
    T3 = y.left

    y.left = z
    z.right = T3

    z.height = 1 + max(get_height(z.left), get_height(z.right))
    y.height = 1 + max(get_height(y.left), get_height(y.right))

    return y

# Функція для знаходження суми всіх значень у дереві
def sum_tree(root):
    if root is None:
        return 0
    return root.val + sum_tree(root.left) + sum_tree(root.right)

# Приклад використання
root = None
values = [50, 30, 20, 40, 70, 60, 80]
for value in values:
    root = insert(root, value)

print("Сума всіх значень в AVL-дереві:", sum_tree(root))
