from ..models.grid import Grid
from ..models.frontier import PriorityQueueFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node


class UniformCostSearch:
    @staticmethod
    def search(grid: Grid) -> Solution:
        """Find path between two points in a grid using Uniform Cost Search

        Args:
            grid (Grid): Grid of points

        Returns:
            Solution: Solution found
        """
        # Initialize a node with the initial position
        node = Node("", grid.start, 0)

        frontier = PriorityQueueFrontier()
        frontier.add(node, node.cost)

        # Initialize the explored dictionary to be empty
        explored = {node.state: node.cost}

        while not frontier.is_empty():
            current_node = frontier.pop()

            if current_node.state == grid.end:
                return Solution(current_node, explored)

            for action, neighbor in grid.get_neighbours(current_node.state).items():
                current_cost = current_node.cost + grid.get_cost(neighbor)

                if neighbor not in explored or current_cost < explored[neighbor]:
                    new_node = Node(
                        value="",
                        state=neighbor,
                        cost=current_cost,
                        parent=current_node,
                        action=action,
                    )

                    frontier.add(new_node, new_node.cost)
                    explored[new_node.state] = new_node.cost

        return NoSolution(explored)
