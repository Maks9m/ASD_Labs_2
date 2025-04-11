import math
import random
import matplotlib.pyplot as plt

random.seed(4217)

def draw_graph(matrix, directed=False, title=None, graph_type=None, steps=None, weight_matrix=None):
    order = 0
    R = 10  # Radius of the circular layout
    angle_step = 2 * math.pi / (len(matrix) - 1) # Angle between nodes
    # Calculate node positions
    positions = []
    for i in range(len(matrix)):
        if i == 0:
            positions.append((0, 0))  # Center node
            continue
        angle = i * angle_step
        x = R * math.cos(angle)
        y = R * math.sin(angle)
        positions.append((x, y))

    node_R = 0.8  # Node radius

    # Helper function to adjust for node boundary
    def adjust_for_R(x1, y1, x2, y2, offset):
        dx, dy = x2 - x1, y2 - y1
        length = math.sqrt(dx ** 2 + dy ** 2)
        if length == 0:
            return x1, y1, x2, y2
        scale = (length - offset) / length
        return x1 + dx * (1 - scale), y1 + dy * (1 - scale), x2 - dx * (1 - scale), y2 - dy * (1 - scale)

    # Function to draw a single step
    def draw_step(step, step_index, prev_active_node=None, order=0):
        if len(matrix) > 1:
            visited = step.get("visited", [])
            queue_or_stack = step.get("queue", [])
            active_node = queue_or_stack[0] if queue_or_stack else None
            order += 1
            print(f"{active_node} -> {order}")
            
            # BFS specific information
            levels = step.get("levels", [-1] * len(matrix))
            
            plt.figure(figsize=(8, 8))
            plt.title(f"{title} - Step {step_index + 1}", fontsize=14)

            # Plot nodes
            for i, (x, y) in enumerate(positions):
                # BFS: Color by level with fixed colors per level
                if graph_type == "bfs":
                    if i + 1 == prev_active_node:
                        color = "#FF0000"  # Red for previously active node
                    elif levels[i] >= 0:
                        # Fixed colors based on level (won't change as traversal progresses)
                        level_colors = [
                            "#FF0000",   # Level 3 - Red
                            "#FF8C00",  # Level 1 - Dark Orange
                            "#FFD700",  # Level 0 - Gold
                        ]
                        color_index = min(levels[i], len(level_colors) - 1)
                        color = level_colors[color_index]
                    else:
                        color = 'lightgray'  # Unvisited
                # DFS: Use existing coloring
                else:
                    if i + 1 == active_node:
                        color = "#FF6347"  # Tomato for DFS active node
                    elif i + 1 in visited:
                        color = "#FFD700"  # Gold for visited nodes
                    else:
                        color = 'lightgray'  # Unvisited nodes
                
                plt.scatter(x, y, s=500, color=color, edgecolor="black", linewidth=1, zorder=2)
                plt.text(x, y, str(i + 1), fontsize=12, ha="center", va="center", zorder=4)

            # Plot edges with highlighting for active paths
            for i in range(len(matrix)):
                for j in range(len(matrix)):
                    if matrix[i][j]:
                        x1, y1 = positions[i]
                        x2, y2 = positions[j]
                        x1, y1, x2, y2 = adjust_for_R(x1, y1, x2, y2, node_R)
                        
                        # For BFS, use fixed level-based edge coloring
                        if graph_type == "bfs" and levels[i] >= 0 and levels[j] >= 0:
                            # Edges between any two levels
                            level_diff = abs(levels[i] - levels[j])
                            if level_diff == 1:  # Connections between adjacent levels
                                edge_color = "#FF6347"  # Tomato for level transitions
                                edge_width = 2.5
                            elif level_diff == 0:  # Connections within the same level
                                edge_color = "#FFD700"  # Gold for same level
                                edge_width = 2.0
                            else:
                                edge_color = "gray"  # Gray for other connections
                                edge_width = 1.0
                        else:
                            # Use the existing edge coloring logic for DFS
                            is_active_edge = (i+1 == active_node and j+1 in visited) or (j+1 == active_node and i+1 in visited)
                            is_traversed_edge = (i+1 in visited and j+1 in visited)
                            
                            if is_active_edge:
                                edge_color = "#FF6347"  # Tomato for active edges
                                edge_width = 2.5
                            elif is_traversed_edge:
                                edge_color = "#FFD700"  # Gold for traversed edges
                                edge_width = 2.0
                            else:
                                edge_color = "gray"  # Gray for untraversed edges
                                edge_width = 1.0
                        
                        plt.plot([x1, x2], [y1, y2], color=edge_color, linewidth=edge_width, zorder=1)
                        
                        if directed:
                            plt.arrow(
                                x1, y1, x2 - x1, y2 - y1, 
                                head_width=0.30, length_includes_head=True, 
                                color=edge_color, linewidth=edge_width, zorder=3
                            )

            plt.xlim(-15, 15)
            plt.ylim(-15, 15)
            plt.axis("off")
            plt.show()

    # If steps are provided, draw each step
    if steps:
        prev_active_node = None
        for step_index, step in enumerate(steps):
            draw_step(step, step_index, prev_active_node, order)
            order += 1
            if graph_type == "bfs":
                prev_active_node = step.get("queue", [None])[0] if step.get("queue") else None
    else:
        plt.figure(figsize=(8, 8))
        for i, (x, y) in enumerate(positions):
            plt.scatter(x, y, s=500, color='lightgray', edgecolor='black', linewidth=1, zorder=2)  # Draw node
            plt.text(x, y, str(i + 1), fontsize=12, ha="center", va="center", zorder=4)  # Label node

        # Draw edges
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                if matrix[i][j] and i <= j:
                    # Choose edge color based on graph type or random
                    edge_color = (random.randint(0, 235) / 255, random.randint(0, 235) / 255, random.randint(0, 235) / 255)
                    
# Get weight if available
                    weight_label = ""
                    if weight_matrix is not None and weight_matrix[i][j] != 0:
                        weight_label = str(weight_matrix[i][j])
                    
                    # Draw self-loop if a node connects to itself
                    if matrix[i][i] and weight_matrix == None:
                        x, y = positions[i]
                        loop_radius = 1  # Adjust for better visibility
                        if(x != 0 and y != 0):
                            vector_length = math.sqrt(x ** 2 + y ** 2)
                            x += x * loop_radius / vector_length
                            y += y * loop_radius / vector_length
                        else:
                            y += loop_radius
                        loop = plt.Circle((x, y), loop_radius, color=edge_color, fill=False, zorder=1)
                        plt.gca().add_patch(loop)
                        
                    x1, y1 = positions[i]
                    x2, y2 = positions[j]

                    dx, dy = x2 - x1, y2 - y1
                    length = math.sqrt(dx ** 2 + dy ** 2)
                    x1, y1, x2, y2 = adjust_for_R(x1, y1, x2, y2, node_R)
                    
                    # Draw edges that would pass through center
                    if (length >= 2*(R - node_R) and length <= 2*(R + node_R)):
                        norm_dx, norm_dy = dx / length, dy / length
                        perp_x, perp_y = -norm_dy, norm_dx
                        curve_factor = 3.0 + random.uniform(-0.5, 0.5)
                        midx = (x1 + x2) / 2 + perp_x * curve_factor
                        midy = (y1 + y2) / 2 + perp_y * curve_factor
                        t_values = [0, 0.25, 0.5, 0.75, 1.0]
                        curve_x = []
                        curve_y = []
                        
                        for t in t_values:
                            bx = (1-t)**2 * x1 + 2*(1-t)*t * midx + t**2 * x2
                            by = (1-t)**2 * y1 + 2*(1-t)*t * midy + t**2 * y2
                            curve_x.append(bx)
                            curve_y.append(by)
                        
                        if directed:
                            plt.plot(curve_x[:-1], curve_y[:-1], color=edge_color, zorder=3)
                            last_segment_x = curve_x[-2]
                            last_segment_y = curve_y[-2]
                            plt.arrow(last_segment_x, last_segment_y, 
                                    curve_x[-1] - last_segment_x, 
                                    curve_y[-1] - last_segment_y, 
                                    head_width=0.30, length_includes_head=True, 
                                    color=edge_color, zorder=4)
                        else:
                            plt.plot(curve_x, curve_y, color=edge_color, zorder=3)

                        # Calculate the actual midpoint of the curve (at t=0.5)
                        mid_t = 0.5
                        label_x = (1-mid_t)**2 * x1 + 2*(1-mid_t)*mid_t * midx + mid_t**2 * x2
                        label_y = (1-mid_t)**2 * y1 + 2*(1-mid_t)*mid_t * midy + mid_t**2 * y2
                        plt.text(label_x, label_y, weight_label, fontsize=10, ha="center", va="center", 
                                bbox=dict(facecolor=edge_color, alpha=0.6, edgecolor=edge_color), zorder=5)
                        continue
                    
                    # Draw direct edges
                    if directed:
                        plt.arrow(x1, y1, x2 - x1, y2 - y1, head_width=0.30, length_includes_head=True, color=edge_color, zorder=4)
                        continue
                    label_x = (x1 + x2) / 2
                    label_y = (y1 + y2) / 2
                    # Add weight label for straight edge
                    plt.text(label_x, label_y, weight_label, fontsize=10, ha="center", va="center", bbox=dict(facecolor=edge_color, alpha=0.7, edgecolor=edge_color), zorder=5)
                    plt.plot([x1, x2], [y1, y2], color=edge_color, zorder=3)
        plt.xlim(-15, 15)
        plt.ylim(-15, 15)
        plt.axis("off")
        plt.show()
