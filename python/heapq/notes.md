- heapq implementation is that of a minheap.
- children: `2*parent + 1` and `2*parent+2`

- `heappush(heap, item)`
- `heappop(heap)`
- `heapify(x)`
- `heappushpop(heap, item)`:
    - push item on heap then pop and return smallest element.
    - More efficient than separate `heappush()` followed by `heappop()`

- `heapreplace(heap, item)`
    - Pop top value, then insert new item in heap. Return popped value.
    - If heap is empty, `IndexError` is raised.
    - More efficient than separate `heappop()` followed by `heappush()`.
