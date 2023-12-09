from src.delete_linked_list_node import delete_node_rec, Node, LL


def test_delete_node_rec():
    # Create a linked list: 1 -> 2 -> 3 -> 4 -> 5
    ll = LL(Node(1, Node(2, Node(3, Node(4, Node(5))))))

    # Test deleting the first node
    assert delete_node_rec(0, ll) == True
    assert ll.head.val == 2

    # Test deleting a middle node
    assert delete_node_rec(2, ll) == True
    assert ll.head.nxt.val == 4

    # Test deleting the last node
    assert delete_node_rec(2, ll) == True
    assert ll.head.nxt.val == None

    # Test deleting a node from an empty list
    empty_ll = LL()
    assert delete_node_rec(1, empty_ll) == False

    # Test deleting a node with an index greater than the length of the list
    assert delete_node_rec(10, ll) == False
