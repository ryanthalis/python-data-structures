# AVL Tree

A pointer-based self-balancing binary search tree with parent references,
height tracking, four rotation cases, insertion, search, and deletion.

## Run the tests

```shell
python -m unittest -v test_avl_tree.py
```

## Complexity

| Operation | Time |
| --- | --- |
| `search` | O(log n) |
| `insert` | O(log n) |
| `delete` | O(log n) |
| inorder iteration | O(n) |
