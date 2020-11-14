import random

class TreeNode:
    def __init__(self, value, adress = [], root = None):
        self.value = value
        self.children = []
        self.adress = adress
        self.root = root

roots_list = []
tree_dict = {}

class Table:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.contents = []
        colours = {0:"Red", 1:"Green", 2:"Blue"}
        for row in range(rows):
            row_list = []
            for column in range(columns):
                colour = colours[random.randint(0, 2)]
                new_tree_node = TreeNode(colour, [row, column])
                row_list.append(new_tree_node)
            self.contents.append(row_list)

    def print_table(self):
        for i_row in range(self.rows):
            row_list = self.contents[i_row]
            row_list_values = []
            for i_column in range(self.columns):
                row_list_values.append(row_list[i_column].value)
            print(row_list_values)

    def get_left_neighbor(self, adress):
        row = adress[0]
        column = adress[1]
        if column == 0:
            return None
        else:
            row_list = self.contents[row]
            return row_list[column - 1]

    def get_right_neighbor(self, adress):
        row = adress[0]
        column = adress[1]
        row_list = self.contents[row]
        try:
            return row_list[column + 1]
        except IndexError:
            pass

    def get_top_neighbor(self, adress):
        row = adress[0]
        column = adress[1]
        if row == 0:
            return None
        else:
            row_list = self.contents[row - 1]
            return row_list[column]

    def get_bottom_neighbor(self, adress):
        row = adress[0]
        column = adress[1]
        try:
            row_list = self.contents[row + 1]
            return row_list[column]
        except IndexError:
            pass

def in_tree_dict(current_node):
    for value in tree_dict.values():
        if current_node in value:
            return True
    return False

print("Incepe prin stabilirea numarului de randuri si coloane pentru tabel...")
numar_randuri = int(input("\n\nCate randuri?\n"))
numar_coloane = int(input("\n\nCate coloane?\n"))
tabel = Table(numar_randuri, numar_coloane)

print("\n\nAcesta este tabelul creat, completat automat in mod aleatoriu cu una dintre culorile Red, Green sau Blue\n")
tabel.print_table()

print(roots_list)

for row in tabel.contents:
    for tree_node in row:
        current_node = tree_node
        current_node_adress = current_node.adress
        current_node_color = current_node.value
        current_node_adress = current_node.adress
        bottom_neighbor = tabel.get_bottom_neighbor(current_node_adress)
        left_neighbor = tabel.get_left_neighbor(current_node_adress)
        top_neighbor = tabel.get_top_neighbor(current_node_adress)
        right_neighbor = tabel.get_right_neighbor(current_node_adress)
        neighbors_list = [bottom_neighbor, left_neighbor, top_neighbor, right_neighbor]
        if current_node_adress not in roots_list:
            if not in_tree_dict(current_node):
                for neighbor in neighbors_list:
                    try:
                        if neighbor.value == current_node.value:
                            if neighbor.adress in roots_list:
                                tree_dict[neighbor].append(neighbor)
                            elif in_tree_dict(neighbor):
                                tree_dict[neighbor.root].append(current_node)
                                current_node.root = neighbor.root
                        else:
                            roots_list.append(current_node.adress)
                            tree_dict[current_node] = []
                    except AttributeError:
                        pass
            else:
                for neighbor in neighbors_list:
                    try:
                        if neighbor.adress in roots_list or in_tree_dict(neighbor):
                            continue
                        else:
                            try:
                                if neighbor.value == current_node.value:
                                    current_node_root = current_node.root
                                    tree_dict[current_node_root].append(neighbor)
                                    neighbor.root = current_node_root
                            except AttributeError:
                                pass
                    except AttributeError:
                        pass
        for neighbor in neighbors_list:
            try:
                if neighbor.adress in roots_list or in_tree_dict(neighbor):
                    continue
                else:
                    try:
                        if neighbor.value == current_node.value:
                            tree_dict[current_node].append(neighbor)
                            neighbor.root = current_node
                    except AttributeError:
                        pass
            except AttributeError:
                pass
group_count = {"Red":0, "Blue":0, "Green":0}

#for key in tree_dict.keys():
#    colour = key.value
#    group_count[colour] += 1
#    group_size = len(tree_dict[key]) + 1
#    print("Grupul nr {0} din culoarea {1} are marimea {2}".format(group_count[colour], colour, group_size))

max_group = max(tree_dict.values(), key = len)
colour = max_group[0].value
root = max_group[0].root
root_adress = root.adress
print("\nCel mai mare grup este de culoarea {0}\nAre un total de {1} elemente\nRadacina grupului se afla pe pozitia {2}\n".format(colour, len(max_group) + 1, root_adress))
    
