A hash table that hashes all values to the same slot is essentially equivalent to what other data structure?

A hash table that hashes all values to the same slot effectively creates a structure that behaves similarly to a linked list. This is because all the elements are stored in the same slot or bucket, resulting in a linear sequence of elements.

Analyze the hashing functions discussed in lecture slides. Elaborate on the benefits and drawbacks of each function.

Hashing functions are critical in distributing keys uniformly across the available slots in a hash table. Common hashing functions include:

Division method: Benefits include simplicity and fast computation. However, it may lead to clustering if the table size isn't a prime number or suitable for the dataset, leading to collisions and degraded performance.

Multiplication method: Offers better distribution properties compared to division method due to the multiplication of the key with a fractional part of a constant. However, it requires careful selection of the constant (usually close to, but not equal to, a power of 2) to avoid clustering.

Universal hashing: Involves selecting a random hash function from a family of hash functions. It provides good average-case performance and can significantly reduce the chance of collisions. The drawback is the computational overhead of selecting and applying these random hash functions.

Analyze the two methods for resolving collisions in hash tables discussed in lecture slides. Elaborate on the benefits and drawbacks of each method.

Collision resolution methods handle situations where different keys hash to the same slot. Two common methods are:

Chaining: In this method, each slot in the hash table holds a linked list of elements that hash to the same location. Benefits include simplicity and suitability for handling multiple collisions. However, it may lead to increased memory overhead and slower performance for larger linked lists.

Open addressing: Elements are placed in another open slot in the table if a collision occurs. Various techniques like linear probing, quadratic probing, or double hashing are used to find the next available slot. Benefits include reduced memory overhead and cache-friendly behavior. However, it can suffer from clustering and may require careful selection of the probing strategy to avoid performance degradation.

What strategies and issues should you consider when resizing a hash table? What are the likely complications? How would you address them?

Resizing a hash table involves increasing or decreasing the number of slots to accommodate more or fewer elements. Key considerations and potential complications include:

Rehashing: All elements need to be rehashed and moved to new slots, which can be computationally expensive.

Choosing a new size: Selecting an appropriate new size is essential. Often, doubling the size or using prime numbers can be beneficial to maintain good hashing properties.

Data migration: Moving data from the old table to the new one can cause performance issues, especially if the table is large. Incremental resizing or using load factor thresholds can help mitigate this issue.

Concurrency: Resizing a hash table in a concurrent environment can introduce synchronization challenges and potential race conditions. Using techniques like locks or concurrent data structures can address this issue.