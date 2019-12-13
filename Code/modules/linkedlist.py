#!python


class Node(object):

    def __init__(self, data):
        """Initialize this node with the given data."""
        self.data = data
        self.next = None

    def __repr__(self):
        """Return a string representation of this node."""
        return 'Node({!r})'.format(self.data)


class LinkedList(object):

    def __init__(self, items=None):
        """Initialize this linked list and append the given items, if any."""
        self.head = None  # First node
        self.tail = None  # Last node
        self.count = 0
        # Append given items
        if items is not None:
            for item in items:
                self.append(item)

    def __str__(self):
        """Return a formatted string representation of this linked list."""
        items = ['({!r})'.format(item) for item in self.items()]
        return '[{}]'.format(' -> '.join(items))

    def __repr__(self):
        """Return a string representation of this linked list."""
        return 'LinkedList({!r})'.format(self.items())

    def __iter__(self):
        """Returns an interable representation of this linked list"""
        return iter([value for value in self.items()])


    def items(self):
        """Return a list (dynamic array) of all items in this linked list.
        Best and worst case running time: O(n) for n items in the list (length)
        because we always need to loop through all n nodes to get each item."""
        items = []  # O(1) time to create empty list
        # Start at head node
        node = self.head  # O(1) time to assign new variable
        # Loop until node is None, which is one node too far past tail
        while node is not None:  # Always n iterations because no early return
            items.append(node.data)  # O(1) time (on average) to append to list
            # Skip to next node to advance forward in linked list
            node = node.next  # O(1) time to reassign variable
        # Now list contains items from all nodes
        return items  # O(1) time to return list

    def is_empty(self):
        """Return a boolean indicating whether this linked list is empty."""
        return self.head is None

    def count_length(self):
        """Return the length of this linked list by traversing its nodes.
        Running time: O(n) because we traverse through all nodes."""
        # Loop through all nodes and count one for each
        count = 0
        current_node = self.head
        while current_node is not None:
            count += 1
            current_node = current_node.next

        return count

    def length(self):
        """ Return count for the length of the linked list."""
        return self.count

    def append(self, item):
        """Insert the given item at the tail of this linked list.
         Running time: O(1) under any circumstances because you add new node after the tail."""
        #  Create new node to hold given item
        #  Append node after tail, if it exists
        new_node = Node(item)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            current_node = self.tail
            current_node.next = new_node
            self.tail = current_node.next

        self.count += 1

    def prepend(self, item):
        """Insert the given item at the head of this linked list.
         Running time: O(1) because you add new item at the beginning of the list"""
        #  Create new node to hold given item
        #  Prepend node before head, if it exists
        new_node = Node(item)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

        self.count += 1

    def find(self, quality):
        """Return an item from this linked list satisfying the given quality.
         Best case running time: O(1) when first item satisfies the given quality
         Worst case running time: O(n) because you have to traverse through all nodes when the last item satisfiesthe given quality or there is no item"""
        #  Loop through all nodes to find item where quality(item) is True
        #  Check if node's data satisfies given quality function
        current_node = self.head
        while current_node is not None:
            if quality(current_node.data):
                return current_node.data
            current_node = current_node.next
        return None

    def delete(self, item):
        """Delete the given item from this linked list, or raise ValueError.
         Best case running time: O(1) when given item is equal to the head.
         Worst case running time: O(n) when given item is equal to the tail or there is no item in list"""
        #  Loop through all nodes to find one whose data matches given item
        #  Update previous node to skip around node with matching data
        #  Otherwise raise error to tell user that delete has failed
        # Hint: raise ValueError('Item not found: {}'.format(item))
        list_len_1 = self.length()
        current_node = self.head
        previous_node = None
        while current_node is not None:
            if current_node.data == item:
                self.count -= 1
                if previous_node is not None:
                    previous_node.next = current_node.next
                    if self.tail.data == item:
                        self.tail = previous_node

                else:
                    # if it's the only node in list
                    if current_node.next is None:
                        self.tail = None
                        self.head = None
                        break
                    # if it's the first node in list
                    else:
                        self.head = current_node.next
                        current_node = self.head


            previous_node = current_node
            current_node = current_node.next

        list_len_2 = self.length()
        # no item has been deleted
        if list_len_1 == list_len_2:
            raise ValueError('Item not found: {}'.format(item))

    def replace(self, item, new_item):
        """Replace the given item from the linked list with a new item."""
        # node = self.find(lambda value: value == item)
        # if node is not None:
        #     node = new_item
        node = self.head
        while node is not None:
            if node.data == item:
                node.data = new_item
                return

            node = node.next

def test_linked_list():
    ll = LinkedList()
    print('list: {}'.format(ll))

    print('\nTesting append:')
    for item in ['A', 'B', 'C']:
        print('append({!r})'.format(item))
        ll.append(item)
        print('list: {}'.format(ll))

    print('head: {}'.format(ll.head))
    print('tail: {}'.format(ll.tail))
    print('length: {}'.format(ll.length()))

    # Enable this after implementing delete method
    delete_implemented = True
    if delete_implemented:
        print('\nTesting delete:')
        for item in ['B', 'C', 'A']:
            print('delete({!r})'.format(item))
            ll.delete(item)
            print('list: {}'.format(ll))

        print('head: {}'.format(ll.head))
        print('tail: {}'.format(ll.tail))
        print('length: {}'.format(ll.length()))


if __name__ == '__main__':
    test_linked_list()
