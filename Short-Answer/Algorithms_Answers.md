#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n). At first glance it would appear like O(n^3) because the while loop
compares a to n^3 (so naturally you would iterate n^3 times) but a grows at a
rate of += n^2 so it will iterate only O(n) times.


b) O(n * log of n). We will at the very least iterate n times, and the internal
while loop will iterate for _roughly_ n / 2 (because the determinant grows at a
2x per iteration).

c) O(n) becuase even though the output will grow, the number of times it
recursively calls itself is actually linear.

## Exercise II

Big O notation of O(n * log n)

I would start by finding the middle floor so if n was 20, I would start at 10. I
would then drop an egg and determine if it did break. 

If it didn't, I would know that I am too low, and need to go higher, and if it did, I would know that I am
either at floor f, or above it.

If I was too low, I would take the middle of the current floor and n, so in this
case 15 and repeat until I found a floor where the egg broke.

If I landed on a floor where the egg broke, I would go to the floor of the
current floor I'm on divided by 2 (in this case if I started at 10 and it was
a breaking floor, I would go to 5).

If this was also a breaking floor, I would walk down until the first floor that
didn't break and I would know that the lowest break floor is the floor above.

If it wasn't a breaking floor I would walk up until it was a breaking floor.
