# Binary Max-Heap

An array-backed binary max-heap that supports insertion, inspection, and
removal of the largest value.

## Run the tests

```shell
python -m unittest -v test_binary_max_heap.py
```

## Complexity

| Operation | Time |
| --- | --- |
| `add` | O(log n) |
| `peek` | O(1) |
| `remove` / `delete_max` | O(log n) |
