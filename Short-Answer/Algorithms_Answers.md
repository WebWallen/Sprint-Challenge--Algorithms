#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) Time barely increments as input increases. There are no loops outside of while. A and N have a direct correlation.
Ran test to time. N = 10: 0:00:00:00. N = 100,000: 0:00:00:042. Thus, I would classify this as O(N).

b) As input grows, the operations barely increase (but it doesn't appear to be as simple as returning once). Two loops.
Ran test to time. N = 10: 0:00:00:00. N = 100,000: 0:00:00:26. Thus, I would classify this as O(logn).

c) There is extra work required for every single additional input. Get errors RE: too much recurssion with small inputs.
Ran test to time. N = 10: 0:00:00:00. Tests fail with inputs as low as 1,000. Can only do with inputs in the hundreds. Thus, I would classify this as O(nlogn).

## Exercise II

The easiest way to minimize the amount of necessary steps is to divide n in half. Drop the egg at the halfway mark. 
If it breaks, run another test at the midpoint on lower end of ranges. If it doesn't, run test on higher end of ranges. This seems similar to the recursive sorting algorithm merge sort, which has a best/worst case run time of O(nlogn).