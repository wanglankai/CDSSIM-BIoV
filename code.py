import math
import numpy as np
import random


class RSUNode:
    def __init__(self, node_id, storage_capacity, distance, violations, mileage):
        self.node_id = node_id
        self.storage_capacity = storage_capacity
        self.distance = distance
        self.violations = violations
        self.mileage = mileage
        self.remaining_storage = storage_capacity
        self.incentive = 0
        self.driving_record = self.calculate_driving_record(alpha=0.7, beta=0.3)

    def calculate_driving_record(self, alpha, beta):
        return alpha * self.mileage - beta * self.violations

    def calculate_competitiveness(self, weights):
        competitiveness = (
                weights["storage"] * self.remaining_storage +
                weights["driving_record"] * self.driving_record -
                weights["distance"] * self.distance
        )
        return competitiveness

    def receive_incentive(self, value):
        self.incentive += value

    def offload_data(self, data_size):
        if data_size <= self.remaining_storage:
            self.remaining_storage += data_size
            self.incentive -= data_size
            return True
        return False

    def __str__(self):
        return (f"Node {self.node_id}: Storage={self.remaining_storage}/{self.storage_capacity}, "
                f"Incentive={self.incentive:.2f}, DrivingRecord={self.driving_record:.2f}")


def calculate_incentives(nodes, total_incentive_pool):
    competitiveness_scores = np.array([node.calculate_competitiveness({
        "storage": 0.4,
        "driving_record": 0.3,
        "distance": 0.3
    }) for node in nodes])

    normalized_scores = competitiveness_scores / competitiveness_scores.sum()
    for i, node in enumerate(nodes):
        node.receive_incentive(normalized_scores[i] * total_incentive_pool)


def collaborative_storage(nodes, data_blocks):

    sorted_nodes = sorted(nodes, key=lambda x: x.calculate_competitiveness({
        "storage": 0.4,
        "driving_record": 0.3,
        "distance": 0.3
    }), reverse=True)

    for block in data_blocks:
        for node in sorted_nodes:
            if node.remaining_storage >= block:
                node.remaining_storage -= block
                print(f"Block of size {block} stored in Node {node.node_id}")
                break
        else:
            print(f"Block of size {block} cannot be stored due to lack of capacity.")


def offload_data(nodes, lower_threshold, upper_threshold):
    for node in nodes:
        while True:
            competitiveness = node.calculate_competitiveness({
                "storage": 0.4,
                "driving_record": 0.3,
                "distance": 0.3
            })
            if competitiveness < lower_threshold:
                data_to_offload = min(node.remaining_storage, 10)
                if node.offload_data(data_to_offload):
                    print(f"Node {node.node_id} offloaded {data_to_offload} units of data.")
                else:
                    print(f"Node {node.node_id} cannot offload more data (insufficient storage).")
                    break
            elif competitiveness >= upper_threshold:
                print(f"Node {node.node_id} reached the upper threshold. Stop offloading.")
                break
            else:
                break


if __name__ == "__main__":
    random.seed(42)
    nodes = [
        RSUNode(
            node_id=i,
            storage_capacity=random.randint(80, 150),
            distance=random.randint(5, 20),
            violations=random.randint(0, 5),
            mileage=random.randint(200, 1000)
        )
        for i in range(1, 21)
    ]

    print("Initial State:")
    for node in nodes:
        print(node)

    total_incentive_pool = 500
    calculate_incentives(nodes, total_incentive_pool)
    print("\nAfter Incentive Allocation:")
    for node in nodes:
        print(node)

    data_blocks = [30, 40, 50, 60, 70]
    print("\nCollaborative Storage Process:")
    collaborative_storage(nodes, data_blocks)

    lower_threshold = 30
    upper_threshold = 90
    print("\nData Offloading Process:")
    offload_data(nodes, lower_threshold, upper_threshold)

    print("\nFinal State:")
    for node in nodes:
        print(node)
