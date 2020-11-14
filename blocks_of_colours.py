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
        for tree_nodes in range(rows):
            row_list = []
            for column in range(columns):
                colour = colours[random.randint(0, 2)]
                new_tree_node = TreeNode(colour, [tree_nodes, column])
                row_list.append(new_tree_node)
            self.contents.append(row_list)

    def print_table(self):
        # for i_row in range(self.rows):
        #     row_list = self.contents[i_row]
        #     row_list_values = []
        #     for i_column in range(self.columns):
        #         row_list_values.append(row_list[i_column].value)
        #     print(row_list_values)
        for tree_nodes in self.contents:
            print(' '.join([tree_node.value.ljust(7) for tree_node in tree_nodes]))

    def get_left_neighbor(self, adress):
        tree_nodes = adress[0]
        column = adress[1]
        if column == 0:
            return None
        else:
            row_list = self.contents[tree_nodes]
            return row_list[column - 1]

    def get_right_neighbor(self, adress):
        tree_nodes = adress[0]
        column = adress[1]
        row_list = self.contents[tree_nodes]
        try:
            return row_list[column + 1]
        except IndexError:
            pass

    def get_top_neighbor(self, adress):
        tree_nodes = adress[0]
        column = adress[1]
        if tree_nodes == 0:
            return None
        else:
            row_list = self.contents[tree_nodes - 1]
            return row_list[column]

    def get_bottom_neighbor(self, adress):
        tree_nodes = adress[0]
        column = adress[1]
        try:
            row_list = self.contents[tree_nodes + 1]
            return row_list[column]
        except IndexError:
            pass
    
    def get_neighbors(self, adress):
        return [self.get_bottom_neighbor(adress), self.get_left_neighbor(adress), self.get_top_neighbor(adress), self.get_right_neighbor(adress)]

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

def get_max_coverage():

    for tree_nodes in tabel.contents:
        for tree_node in tree_nodes:
            current_node = tree_node

            current_node_adress = current_node.adress
            current_node_color = current_node.value
            current_node_adress = current_node.adress

            # filter None
            neighbors_list = [neighbor for neighbor in table.get_neighbors(current_node_adress) if neighbor]

            # unpaking
            # bottom_neighbor, left_neighbor, top_neighbor, right_neighbor = table.get_neighbors(current_node_adress)

            if current_node_adress not in roots_list:
                if not in_tree_dict(current_node):
                    for neighbor in neighbors_list:
                        if neighbor.value == current_node.value:
                            if neighbor.adress in roots_list:
                                tree_dict[neighbor].append(neighbor)
                            elif in_tree_dict(neighbor):
                                tree_dict[neighbor.root].append(current_node)
                                current_node.root = neighbor.root
                        else:
                            roots_list.append(current_node.adress)
                            tree_dict[current_node] = []
                        
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
    max_group = max(tree_dict.values(), key = len)
    colour = max_group[0].value
    root = max_group[0].root
    root_adress = root.adress
    
    return (colour, root_adress, len(max_group) + 1)
    

colour, root_adress, group_lenght = get_max_coverage()

print(f"\nCel mai mare grup este de culoarea {colour}\nAre un total de {group_lenght} elemente\nRadacina grupului se afla pe pozitia {root_adress}\n")
    
