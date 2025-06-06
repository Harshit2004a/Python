# Multithreaded Priority Queue
import threading
import heapq
import time
import threading

class PriorityQueue:
    def __init__(self):
        self.heap = []
        self.lock = threading.Lock()

    def put(self, priority, task):
        with self.lock:
            heapq.heappush(self.heap, (priority, task))

    def get(self):
        with self.lock:
            if self.heap:
                return heapq.heappop(self.heap)
            return None

def worker(pq, worker_id):
    while True:
        item = pq.get()
        if item is None:
            break
        priority, task = item
        print(f"Worker {worker_id} processing: {task} (priority {priority})")
        time.sleep(0.5)

def main():
    pq = PriorityQueue()
    tasks = [
        (2, "Low priority"),
        (1, "High priority"),
        (3, "Very low priority"),
        (1, "Another high priority"),
        (2, "Another low priority"),
    ]
    for priority, task in tasks:
        pq.put(priority, task)

    threads = []
    for i in range(3):
        t = threading.Thread(target=worker, args=(pq, i))
        t.start()
        threads.append(t)

    # Waiting all tasks to be processed
    while True:
        with pq.lock:
            if not pq.heap:
                break
        time.sleep(0.1)

    # Stoping workers
    for _ in threads:
        pq.put(100, None)
    for t in threads:
        t.join()

    print("All tasks completed.")

if __name__ == "__main__":
    main()

# Code by Harshit
