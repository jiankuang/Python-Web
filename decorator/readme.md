```python
@timer.timedFunction
def sumUp(n):
  total = 0
  for x in range(n):
    total += x
  return total
# this is the same as 
sumUp = timer.timedFunction(sumUp)
```
https://classroom.udacity.com/courses/ud858/lessons/3887428705/concepts/39641689900923
