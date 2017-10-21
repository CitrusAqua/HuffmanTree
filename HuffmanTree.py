import HuffmanNode as hn


class HuffmanTree:
    def __init__(self, r = None):
        self.root = r
        self.code_map = []

    def get_code(self, char):
        for i in self.code_map:
            if i[0] == char:
                return i[1]
        return None

    @staticmethod
    def store_sub_tree(r, code, m_code_map):
        if r.isLeaf:
            m_code_map.append((r.char, code))
            return
        HuffmanTree.store_sub_tree(r.leftNode, code + '0', m_code_map)
        HuffmanTree.store_sub_tree(r.rightNode, code + '1', m_code_map)

    def store(self, m_code_map):
        HuffmanTree.store_sub_tree(self.root.leftNode, "0", m_code_map)
        HuffmanTree.store_sub_tree(self.root.rightNode, "1", m_code_map)

    @staticmethod
    def form(filename):
        data = []
        with open(filename,"r") as f:
            file_str = f.read()
            for code in range(128):
                count = file_str.count(chr(code))
                if count != 0:
                    data.append((chr(code), count))
        sorted_node = []
        for d in data:
            temp_node = hn.HuffmanNode(d[1], d[0])
            j = 0
            inserted = False
            for j in range(len(sorted_node)):
                if sorted_node[j].value < temp_node.value:
                    sorted_node.insert(j, temp_node)
                    inserted = True
                    break
            if not inserted:
                sorted_node.append(temp_node)
        while len(sorted_node) != 1:
            new_node = hn.HuffmanNode(sorted_node[-1].value + sorted_node[-2].value)
            new_node.leftNode = sorted_node[-1]
            new_node.rightNode = sorted_node[-2]
            sorted_node.pop()
            sorted_node.pop()
            j = 0
            inserted = False
            for j in range(len(sorted_node)):
                if sorted_node[j].value < new_node.value:
                    sorted_node.insert(j, new_node)
                    inserted = True
                    break
            if not inserted:
                sorted_node.append(new_node)
        tree = HuffmanTree(sorted_node[0])
        m_code_map = []
        tree.store(m_code_map)
        tree.code_map = m_code_map
        return tree

    @staticmethod
    def print_sub_tree(r, code):
        if r.isLeaf:
            print(r.char, r.value, code)
            return
        HuffmanTree.print_sub_tree(r.leftNode, code + '0')
        HuffmanTree.print_sub_tree(r.rightNode, code + '1')

    def print(self):
        HuffmanTree.print_sub_tree(self.root.leftNode, "0")
        HuffmanTree.print_sub_tree(self.root.rightNode, "1")

    @staticmethod
    def output_sub_tree(r, code, filename):
        if r.isLeaf:
            with open(filename,"a") as f:
                f.write(r.char)
                f.write(' ')
                f.write(str(r.value))
                f.write(' ')
                f.write(str(code))
                f.write('\n')
            return
        HuffmanTree.output_sub_tree(r.leftNode, code + '0', filename)
        HuffmanTree.output_sub_tree(r.rightNode, code + '1', filename)

    def output(self, filename):
        f = open(filename,"w")
        f.close()
        HuffmanTree.output_sub_tree(self.root.leftNode, "0", filename)
        HuffmanTree.output_sub_tree(self.root.rightNode, "1", filename)

    def decode(self, filename, out_filename):
        with open(filename,"r") as f:
            file_str = f.read()
        out_str = ''
        pNode = self.root
        while len(file_str) != 0:
            if file_str[0] == '0':
                pNode = pNode.leftNode
            else:
                pNode = pNode.rightNode
            if pNode.isLeaf:
                out_str += pNode.char
                pNode = self.root
            file_str = file_str[1:]
        with open(out_filename,"w") as f:
            f.write(out_str)

    def encode(self, filename, out_filename):
        with open(filename,"r") as f:
            file_str = f.read()
        out_str = ''
        for c in file_str:
            out_str += self.get_code(c)
        with open(out_filename,"w") as f:
            f.write(out_str)
