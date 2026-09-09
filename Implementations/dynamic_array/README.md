# Dynamic Array

A dynamic array implemented with a fixed-capacity `ctypes` backing array. Its
capacity grows and shrinks as elements are added and removed.

## Run the tests

```shell
python -m unittest -v test_dynamic_array.py
```

## Complexity

| Operation | Time |
| --- | --- |
| `append` | O(1) amortized |
| `extend` | O(k) amortized |
| `index` | O(n) |
| `pop` from end | O(1) amortized |
| `pop` from arbitrary index | O(n) |
| reverse iteration | O(n) |
