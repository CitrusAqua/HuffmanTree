import HuffmanTree as ht

my_tree = ht.HuffmanTree.form("inputfile.txt")
my_tree.output("table.txt")
my_tree.encode("inputfile.txt", "encoded.txt")
my_tree.decode("encoded.txt", "decoded.txt")
