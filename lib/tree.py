class Tree:
  def __init__(self, root = None):
    self.root = root

  def get_element_by_id(self, id):
      if not self.root:
         return None
      
      nodes_to_visit = [self.root]

      while nodes_to_visit:
         node = nodes_to_visit.pop()
         if node.get('id') == id:
            return node
         
         nodes_to_visit.extend(node.get('children', []))

      return None
