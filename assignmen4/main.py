from chideraIbeh.assignmen4.priorityQueue import PriorityQueue


if __name__ == '__main__':
    pq = PriorityQueue()
    for item in [11, 7, 8, 6, 5, 9, 4]:
        pq.add(item, str(item))

    for _ in range(3):
        print(pq.remove())
