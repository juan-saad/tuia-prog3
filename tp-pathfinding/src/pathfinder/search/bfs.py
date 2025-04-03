from ..models.grid import Grid
from ..models.frontier import QueueFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node


class BreadthFirstSearch:
    @staticmethod
    def search(grid: Grid) -> Solution:
        """Find path between two points in a grid using Breadth First Search

        Args:
            grid (Grid): Grid of points

        Returns:
            Solution: Solution found
        """
        # Initialize a node with the initial position
        start_node = Node("", grid.start, 0)

        # Initialize the frontier with the start node
        frontier = QueueFrontier()
        frontier.add(start_node)

        # Initialize the explored dictionary to be empty
        explored = {}

        while not frontier.is_empty():
            # Remove a node from the frontier
            current_node = frontier.remove()

            # If the goal is found, reconstruct the path
            if current_node.state == grid.end:
                return Solution(current_node, explored)

            # Mark the current node as explored
            explored[current_node.state] = True

            # Expand the current node and add neighbors to the frontier
            for action, neighbor in grid.get_neighbours(current_node.state).items():
                if neighbor not in explored and not frontier.contains_state(neighbor):
                    child_node = Node(
                        value="",
                        state=neighbor,
                        cost=current_node.cost + 1,
                        parent=current_node,
                        action=action,
                    )
                    frontier.add(child_node)

        # If no solution is found, return NoSolution
        return NoSolution(explored)
