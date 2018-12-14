# SynchroSort
Sorting algorithm with threads and no list comparisions

#...Why?
Well, I was having a conversation on Twitter with a friend when I jokingly came said we should come up with the worst possible sorting algorithm. After a few hours, here is what I came up with.

#Why it's bad
Highly unreliable because threads take time to make, throwing the system in complete wack. 
I guess you'd need a computer that can parralel process and be very strong to use this properly.

#How it works
It splits each element into its own thread. 
Each thread decays after a certain time, and this is returned as a sorted list.
