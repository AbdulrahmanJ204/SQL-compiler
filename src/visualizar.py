from antlr4 import *
import tkinter as tk
from tkinter import ttk

class InteractiveTreeVisualizer:
    def __init__(self, tree, parser, title="ANTLR4 Parse Tree"):
        self.tree = tree
        self.parser = parser
        self.positions = {}
        self.node_boxes = {}
        
        # Layout parameters
        self.x_spacing = 150
        self.y_spacing = 80
        self.node_width = 120
        self.node_height = 40
        
        # View parameters
        self.zoom = 1.0
        self.offset_x = 0
        self.offset_y = 0
        self.drag_start_x = 0
        self.drag_start_y = 0
        
        # Create window
        self.root = tk.Tk()
        self.root.title(title)
        self.root.geometry("1200x800")
        
        # Create canvas with scrollbars
        self.canvas = tk.Canvas(self.root, bg='white', highlightthickness=0)
        
        # Add scrollbars
        v_scroll = ttk.Scrollbar(self.root, orient=tk.VERTICAL, command=self.canvas.yview)
        h_scroll = ttk.Scrollbar(self.root, orient=tk.HORIZONTAL, command=self.canvas.xview)
        
        self.canvas.configure(yscrollcommand=v_scroll.set, xscrollcommand=h_scroll.set)
        
        # Layout
        self.canvas.grid(row=0, column=0, sticky='nsew')
        v_scroll.grid(row=0, column=1, sticky='ns')
        h_scroll.grid(row=1, column=0, sticky='ew')
        
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        
        # Add control panel
        self._create_controls()
        
        # Bind events
        self.canvas.bind("<MouseWheel>", self._on_mousewheel)
        self.canvas.bind("<Button-4>", self._on_mousewheel)  # Linux scroll up
        self.canvas.bind("<Button-5>", self._on_mousewheel)  # Linux scroll down
        self.canvas.bind("<ButtonPress-1>", self._on_drag_start)
        self.canvas.bind("<B1-Motion>", self._on_drag_motion)
        
        # Keyboard shortcuts
        self.root.bind("<plus>", lambda e: self.zoom_in())
        self.root.bind("<equal>", lambda e: self.zoom_in())  # + without shift
        self.root.bind("<minus>", lambda e: self.zoom_out())
        self.root.bind("<Key-0>", lambda e: self.reset_view())
        
        # Calculate and draw
        self.calculate_positions(self.tree)
        self.draw_tree()
        
    def _create_controls(self):
        """Create control panel"""
        control_frame = ttk.Frame(self.root)
        control_frame.grid(row=2, column=0, columnspan=2, pady=5)
        
        ttk.Button(control_frame, text="Zoom In (+)", command=self.zoom_in).pack(side=tk.LEFT, padx=5)
        ttk.Button(control_frame, text="Zoom Out (-)", command=self.zoom_out).pack(side=tk.LEFT, padx=5)
        ttk.Button(control_frame, text="Reset View (0)", command=self.reset_view).pack(side=tk.LEFT, padx=5)
        
        self.zoom_label = ttk.Label(control_frame, text=f"Zoom: {self.zoom:.0%}")
        self.zoom_label.pack(side=tk.LEFT, padx=10)
        
        ttk.Label(control_frame, text="| Drag to pan | Mouse wheel to zoom").pack(side=tk.LEFT, padx=10)
    
    def get_node_text(self, node):
        """Get display text for a node"""
        if isinstance(node, TerminalNode):
            text = node.getText()
            if len(text) > 20:
                text = text[:17] + "..."
            return f'"{text}"'
        else:
            rule_index = node.getRuleIndex()
            return self.parser.ruleNames[rule_index]
    
    def calculate_positions(self, node, x=0, depth=0):
        """Calculate positions for all nodes"""
        if isinstance(node, TerminalNode):
            self.positions[id(node)] = (x, depth)
            return x + 1
        
        # Process children
        child_x = x
        children = [node.getChild(i) for i in range(node.getChildCount())]
        child_positions = []
        
        for child in children:
            child_x = self.calculate_positions(child, child_x, depth + 1)
            child_positions.append(self.positions[id(child)][0])
        
        # Place parent at midpoint
        if child_positions:
            parent_x = (child_positions[0] + child_positions[-1]) / 2
        else:
            parent_x = x
            
        self.positions[id(node)] = (parent_x, depth)
        return child_x
    
    def transform_coords(self, x, y):
        """Transform logical coordinates to canvas coordinates"""
        canvas_x = (x * self.x_spacing + self.offset_x) * self.zoom
        canvas_y = (y * self.y_spacing + self.offset_y) * self.zoom
        return canvas_x, canvas_y
    
    def draw_tree(self):
        """Draw the complete tree"""
        self.canvas.delete("all")
        self.node_boxes.clear()
        
        # Draw edges first
        self._draw_edges(self.tree)
        
        # Draw nodes on top
        self._draw_nodes(self.tree)
        
        # Update scroll region
        bbox = self.canvas.bbox("all")
        if bbox:
            self.canvas.configure(scrollregion=bbox)
    
    def _draw_edges(self, node):
        """Draw edges recursively"""
        if isinstance(node, TerminalNode):
            return
        
        parent_pos = self.positions[id(node)]
        px, py = self.transform_coords(parent_pos[0], parent_pos[1])
        
        for i in range(node.getChildCount()):
            child = node.getChild(i)
            child_pos = self.positions[id(child)]
            cx, cy = self.transform_coords(child_pos[0], child_pos[1])
            
            self.canvas.create_line(px, py, cx, cy, 
                                   fill='#666', 
                                   width=max(1, 2 * self.zoom),
                                   tags="edge")
            
            self._draw_edges(child)
    
    def _draw_nodes(self, node):
        """Draw nodes recursively"""
        pos = self.positions[id(node)]
        x, y = self.transform_coords(pos[0], pos[1])
        
        text = self.get_node_text(node)
        
        # Scale node size with zoom
        w = self.node_width * self.zoom
        h = self.node_height * self.zoom
        
        # Different colors for terminals and non-terminals
        if isinstance(node, TerminalNode):
            color = '#90EE90'
            outline = '#2E7D32'
        else:
            color = '#87CEEB'
            outline = '#1565C0'
        
        # Draw box
        box = self.canvas.create_rectangle(
            x - w/2, y - h/2, x + w/2, y + h/2,
            fill=color, outline=outline, 
            width=max(1, 2 * self.zoom),
            tags="node"
        )
        
        # Draw text
        font_size = max(8, int(10 * self.zoom))
        self.canvas.create_text(
            x, y, text=text,
            font=('Arial', font_size, 'bold'),
            tags="node"
        )
        
        self.node_boxes[id(node)] = (x, y, w, h)
        
        # Recursively draw children
        if not isinstance(node, TerminalNode):
            for i in range(node.getChildCount()):
                self._draw_nodes(node.getChild(i))
    
    def zoom_in(self):
        """Zoom in"""
        self.zoom *= 1.2
        self.zoom = min(self.zoom, 5.0)
        self.zoom_label.config(text=f"Zoom: {self.zoom:.0%}")
        self.draw_tree()
    
    def zoom_out(self):
        """Zoom out"""
        self.zoom /= 1.2
        self.zoom = max(self.zoom, 0.1)
        self.zoom_label.config(text=f"Zoom: {self.zoom:.0%}")
        self.draw_tree()
    
    def reset_view(self):
        """Reset zoom and pan"""
        self.zoom = 1.0
        self.offset_x = 100
        self.offset_y = 50
        self.zoom_label.config(text=f"Zoom: {self.zoom:.0%}")
        self.draw_tree()
    
    def _on_mousewheel(self, event):
        """Handle mouse wheel zoom"""
        if event.num == 5 or event.delta < 0:
            self.zoom_out()
        elif event.num == 4 or event.delta > 0:
            self.zoom_in()
    
    def _on_drag_start(self, event):
        """Start dragging"""
        self.drag_start_x = event.x
        self.drag_start_y = event.y
    
    def _on_drag_motion(self, event):
        """Handle drag motion"""
        dx = (event.x - self.drag_start_x) / self.zoom
        dy = (event.y - self.drag_start_y) / self.zoom
        
        self.offset_x += dx
        self.offset_y += dy
        
        self.drag_start_x = event.x
        self.drag_start_y = event.y
        
        self.draw_tree()
    
    def show(self):
        """Show the window"""
        self.reset_view()
        self.root.mainloop()


def visualize_parse_tree(parser, tree, title="ANTLR4 Parse Tree"):
    """
    Create interactive visualization of ANTLR4 parse tree
    
    Args:
        parser: Your ANTLR4 parser instance
        tree: Parse tree from parser
        title: Window title
    
    Controls:
        - Mouse drag: Pan around
        - Mouse wheel: Zoom in/out
        - +/= key: Zoom in
        - - key: Zoom out
        - 0 key: Reset view
        - Use scrollbars to navigate
    """
    viz = InteractiveTreeVisualizer(tree, parser, title)
    viz.show()

