class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

# ---------------- Funções auxiliares ----------------

def get_height(node):
    if not node:
        return 0
    return node.height

def get_balance(node):
    if not node:
        return 0
    return get_height(node.left) - get_height(node.right)

def right_rotate(y):
    x = y.left
    T2 = x.right
    x.right = y
    y.left = T2
    y.height = 1 + max(get_height(y.left), get_height(y.right))
    x.height = 1 + max(get_height(x.left), get_height(x.right))
    return x

def left_rotate(x):
    y = x.right
    T2 = y.left
    y.left = x
    x.right = T2
    x.height = 1 + max(get_height(x.left), get_height(x.right))
    y.height = 1 + max(get_height(y.left), get_height(y.right))
    return y

# ---------------- Inserção ----------------

def insert(node, key):
    if not node:
        return Node(key)
    elif key < node.key:
        node.left = insert(node.left, key)
    else:
        node.right = insert(node.right, key)

    node.height = 1 + max(get_height(node.left), get_height(node.right))
    balance = get_balance(node)

    # LL
    if balance > 1 and key < node.left.key:
        return right_rotate(node)
    # RR
    if balance < -1 and key > node.right.key:
        return left_rotate(node)
    # LR
    if balance > 1 and key > node.left.key:
        node.left = left_rotate(node.left)
        return right_rotate(node)
    # RL
    if balance < -1 and key < node.right.key:
        node.right = right_rotate(node.right)
        return left_rotate(node)

    return node

# ---------------- Remoção ----------------

def min_value_node(node):
    current = node
    while current.left is not None:
        current = current.left
    return current

def remove(node, key):
    if not node:
        return node
    elif key < node.key:
        node.left = remove(node.left, key)
    elif key > node.key:
        node.right = remove(node.right, key)
    else:
        # Nó com um ou nenhum filho
        if not node.left:
            return node.right
        elif not node.right:
            return node.left
        # Nó com dois filhos
        temp = min_value_node(node.right)
        node.key = temp.key
        node.right = remove(node.right, temp.key)

    node.height = 1 + max(get_height(node.left), get_height(node.right))
    balance = get_balance(node)

    # LL
    if balance > 1 and get_balance(node.left) >= 0:
        return right_rotate(node)
    # LR
    if balance > 1 and get_balance(node.left) < 0:
        node.left = left_rotate(node.left)
        return right_rotate(node)
    # RR
    if balance < -1 and get_balance(node.right) <= 0:
        return left_rotate(node)
    # RL
    if balance < -1 and get_balance(node.right) > 0:
        node.right = right_rotate(node.right)
        return left_rotate(node)

    return node

# ---------------- Busca com caminho ----------------

def search(node, key):
    path = []
    current = node
    while current:
        path.append(current.key)
        if key == current.key:
            print("Caminho:", " -> ".join(map(str, path)))
            print("Elemento encontrado!")
            return True
        elif key < current.key:
            current = current.left
        else:
            current = current.right
    print("Caminho:", " -> ".join(map(str, path)))
    print("Elemento não encontrado!")
    return False

# ---------------- Percursos ----------------

def pre_order(node):
    if node:
        print(node.key, end=' ')
        pre_order(node.left)
        pre_order(node.right)

def in_order(node):
    if node:
        in_order(node.left)
        print(node.key, end=' ')
        in_order(node.right)

def post_order(node):
    if node:
        post_order(node.left)
        post_order(node.right)
        print(node.key, end=' ')

# ---------------- Interface de comandos ----------------

def main():
    root = None
    print("Digite os comandos (i/r/b/pre/em/pos) ou 'sair' para encerrar:")
    while True:
        comando = input().strip().lower()
        if comando == "sair":
            break
        if not comando:
            continue

        partes = comando.split()
        op = partes[0]

        if op == "i" and len(partes) == 2:
            valor = int(partes[1])
            root = insert(root, valor)
            print("Árvore após inserção (Pré-Ordem):")
            pre_order(root)
            print("\n")
        elif op == "r" and len(partes) == 2:
            valor = int(partes[1])
            root = remove(root, valor)
            print("Árvore após remoção (Pré-Ordem):")
            pre_order(root)
            print("\n")
        elif op == "b" and len(partes) == 2:
            valor = int(partes[1])
            search(root, valor)
            print("\n")
        elif op == "pre":
            print("Pré-Ordem:")
            pre_order(root)
            print("\n")
        elif op == "em":
            print("Em-Ordem:")
            in_order(root)
            print("\n")
        elif op == "pos":
            print("Pós-Ordem:")
            post_order(root)
            print("\n")
        else:
            print("Comando inválido!")

if __name__ == "__main__":
    main()