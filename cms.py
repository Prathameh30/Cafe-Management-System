import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
from datetime import datetime
import json
import os

class CafeManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Cafe Management System")
        self.root.geometry("1200x800")
        self.root.configure(bg="#f0f0f0")

        # Initialize data
        self.menu_items = {
            "Beverages": {
                "Coffee": 120,
                "Tea": 80,
                "Cold Coffee": 150,
                "Hot Chocolate": 130,
                "Fresh Juice": 100
            },
            "Food": {
                "Sandwich": 180,
                "Burger": 220,
                "Pizza Slice": 200,
                "Pasta": 250,
                "Salad": 160
            },
            "Snacks": {
                "French Fries": 120,
                "Cookies": 60,
                "Muffin": 90,
                "Donut": 80,
                "Cake Slice": 150
            }
        }

        self.current_order = {}
        self.order_history = []

        # Load existing data if available
        self.load_data()

        # Create GUI
        self.create_widgets()

    def create_widgets(self):
        # Title
        title_frame = tk.Frame(self.root, bg="#2c3e50", height=60)
        title_frame.pack(fill="x")
        title_frame.pack_propagate(False)

        title_label = tk.Label(title_frame, text="CAFE MANAGEMENT SYSTEM",
                              font=("Arial", 24, "bold"), fg="white", bg="#2c3e50")
        title_label.pack(pady=15)

        # Main container
        main_frame = tk.Frame(self.root, bg="#f0f0f0")
        main_frame.pack(fill="both", expand=True, padx=10, pady=10)

        # Left frame - Menu and Orders
        left_frame = tk.Frame(main_frame, bg="#ecf0f1", relief="raised", bd=2)
        left_frame.pack(side="left", fill="both", expand=True, padx=(0, 5))

        # Right frame - Bill and Controls
        right_frame = tk.Frame(main_frame, bg="#ecf0f1", relief="raised", bd=2)
        right_frame.pack(side="right", fill="y", padx=(5, 0))
        right_frame.configure(width=400)

        self.create_menu_section(left_frame)
        self.create_order_section(right_frame)

    def create_menu_section(self, parent):
        # Menu section
        menu_label = tk.Label(parent, text="MENU", font=("Arial", 18, "bold"),
                             bg="#ecf0f1", fg="#2c3e50")
        menu_label.pack(pady=10)

        # Notebook for categories
        self.notebook = ttk.Notebook(parent)
        self.notebook.pack(fill="both", expand=True, padx=10, pady=10)

        for category, items in self.menu_items.items():
            self.create_category_tab(category, items)

    def create_category_tab(self, category, items):
        # Create frame for category
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame, text=category)

        # Create scrollable frame
        canvas = tk.Canvas(frame, bg="white")
        scrollbar = ttk.Scrollbar(frame, orient="vertical", command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas)

        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        # Header
        header_frame = tk.Frame(scrollable_frame, bg="#34495e")
        header_frame.pack(fill="x", padx=5, pady=5)

        tk.Label(header_frame, text="Item", font=("Arial", 12, "bold"),
                fg="white", bg="#34495e", width=20).pack(side="left", padx=5, pady=5)
        tk.Label(header_frame, text="Price (₹)", font=("Arial", 12, "bold"),
                fg="white", bg="#34495e", width=10).pack(side="left", padx=5, pady=5)
        tk.Label(header_frame, text="Quantity", font=("Arial", 12, "bold"),
                fg="white", bg="#34495e", width=10).pack(side="left", padx=5, pady=5)
        tk.Label(header_frame, text="Action", font=("Arial", 12, "bold"),
                fg="white", bg="#34495e", width=10).pack(side="left", padx=5, pady=5)

        # Menu items
        for item, price in items.items():
            self.create_menu_item(scrollable_frame, item, price, category)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

    def create_menu_item(self, parent, item, price, category):
        item_frame = tk.Frame(parent, bg="white", relief="groove", bd=1)
        item_frame.pack(fill="x", padx=5, pady=2)

        tk.Label(item_frame, text=item, font=("Arial", 11),
                bg="white", width=20, anchor="w").pack(side="left", padx=5, pady=5)
        tk.Label(item_frame, text=f"₹{price}", font=("Arial", 11),
                bg="white", width=10).pack(side="left", padx=5, pady=5)

        # Quantity spinbox
        quantity_var = tk.StringVar(value="1")
        quantity_spin = tk.Spinbox(item_frame, from_=1, to=10, width=8,
                                  textvariable=quantity_var)
        quantity_spin.pack(side="left", padx=5, pady=5)

        # Add button
        add_btn = tk.Button(item_frame, text="Add", bg="#27ae60", fg="white",
                           font=("Arial", 10, "bold"), width=8,
                           command=lambda: self.add_to_order(item, price, quantity_var.get()))
        add_btn.pack(side="left", padx=5, pady=5)

    def create_order_section(self, parent):
        # Current Order section
        order_label = tk.Label(parent, text="CURRENT ORDER", font=("Arial", 16, "bold"),
                              bg="#ecf0f1", fg="#2c3e50")
        order_label.pack(pady=10)

        # Order listbox with scrollbar
        order_frame = tk.Frame(parent)
        order_frame.pack(fill="both", expand=True, padx=10)

        self.order_listbox = tk.Listbox(order_frame, font=("Arial", 10), height=15)
        order_scrollbar = ttk.Scrollbar(order_frame, orient="vertical",
                                       command=self.order_listbox.yview)
        self.order_listbox.configure(yscrollcommand=order_scrollbar.set)

        self.order_listbox.pack(side="left", fill="both", expand=True)
        order_scrollbar.pack(side="right", fill="y")

        # Remove button
        remove_btn = tk.Button(parent, text="Remove Selected Item", bg="#e74c3c",
                              fg="white", font=("Arial", 12, "bold"),
                              command=self.remove_from_order)
        remove_btn.pack(pady=10)

        # Total section
        total_frame = tk.Frame(parent, bg="#34495e")
        total_frame.pack(fill="x", padx=10, pady=5)

        tk.Label(total_frame, text="TOTAL:", font=("Arial", 14, "bold"),
                fg="white", bg="#34495e").pack(side="left", padx=10, pady=10)

        self.total_label = tk.Label(total_frame, text="₹0", font=("Arial", 14, "bold"),
                                   fg="#f1c40f", bg="#34495e")
        self.total_label.pack(side="right", padx=10, pady=10)

        # Buttons
        button_frame = tk.Frame(parent, bg="#ecf0f1")
        button_frame.pack(fill="x", padx=10, pady=10)

        generate_bill_btn = tk.Button(button_frame, text="Generate Bill",
                                     bg="#3498db", fg="white",
                                     font=("Arial", 12, "bold"),
                                     command=self.generate_bill)
        generate_bill_btn.pack(fill="x", pady=2)

        clear_order_btn = tk.Button(button_frame, text="Clear Order",
                                   bg="#f39c12", fg="white",
                                   font=("Arial", 12, "bold"),
                                   command=self.clear_order)
        clear_order_btn.pack(fill="x", pady=2)

        # Admin section
        admin_frame = tk.LabelFrame(parent, text="Admin Panel", font=("Arial", 12, "bold"),
                                   bg="#ecf0f1", fg="#2c3e50")
        admin_frame.pack(fill="x", padx=10, pady=10)

        add_item_btn = tk.Button(admin_frame, text="Add Menu Item",
                                bg="#9b59b6", fg="white",
                                font=("Arial", 10, "bold"),
                                command=self.add_menu_item)
        add_item_btn.pack(fill="x", pady=2)

        view_history_btn = tk.Button(admin_frame, text="View Order History",
                                    bg="#95a5a6", fg="white",
                                    font=("Arial", 10, "bold"),
                                    command=self.view_order_history)
        view_history_btn.pack(fill="x", pady=2)

    def add_to_order(self, item, price, quantity):
        try:
            qty = int(quantity)
            if qty <= 0:
                messagebox.showerror("Error", "Quantity must be greater than 0")
                return

            if item in self.current_order:
                self.current_order[item]['quantity'] += qty
            else:
                self.current_order[item] = {'price': price, 'quantity': qty}

            self.update_order_display()
            messagebox.showinfo("Success", f"Added {qty} {item}(s) to order")

        except ValueError:
            messagebox.showerror("Error", "Invalid quantity")

    def remove_from_order(self):
        selected = self.order_listbox.curselection()
        if not selected:
            messagebox.showwarning("Warning", "Please select an item to remove")
            return

        selected_text = self.order_listbox.get(selected[0])
        item_name = selected_text.split(" - ")[0]

        if item_name in self.current_order:
            del self.current_order[item_name]
            self.update_order_display()
            messagebox.showinfo("Success", f"Removed {item_name} from order")

    def update_order_display(self):
        self.order_listbox.delete(0, tk.END)
        total = 0

        for item, details in self.current_order.items():
            price = details['price']
            quantity = details['quantity']
            subtotal = price * quantity
            total += subtotal

            display_text = f"{item} - ₹{price} x {quantity} = ₹{subtotal}"
            self.order_listbox.insert(tk.END, display_text)

        self.total_label.config(text=f"₹{total}")

    def clear_order(self):
        if messagebox.askyesno("Confirm", "Are you sure you want to clear the order?"):
            self.current_order.clear()
            self.update_order_display()
            messagebox.showinfo("Success", "Order cleared")

    def generate_bill(self):
        if not self.current_order:
            messagebox.showwarning("Warning", "No items in current order")
            return

        # Create bill window
        bill_window = tk.Toplevel(self.root)
        bill_window.title("Bill")
        bill_window.geometry("500x600")
        bill_window.configure(bg="white")

        # Bill content
        bill_text = tk.Text(bill_window, font=("Courier", 12), bg="white",
                           wrap="word", state="normal")
        bill_text.pack(fill="both", expand=True, padx=20, pady=20)

        # Generate bill content
        bill_content = self.create_bill_content()
        bill_text.insert("1.0", bill_content)
        bill_text.config(state="disabled")

        # Save and print buttons
        button_frame = tk.Frame(bill_window, bg="white")
        button_frame.pack(pady=10)

        save_btn = tk.Button(button_frame, text="Save Bill", bg="#27ae60",
                            fg="white", font=("Arial", 12, "bold"),
                            command=lambda: self.save_bill(bill_content))
        save_btn.pack(side="left", padx=10)

        confirm_btn = tk.Button(button_frame, text="Confirm Order", bg="#3498db",
                               fg="white", font=("Arial", 12, "bold"),
                               command=lambda: self.confirm_order(bill_window))
        confirm_btn.pack(side="left", padx=10)

    def create_bill_content(self):
        total = sum(details['price'] * details['quantity']
                   for details in self.current_order.values())
        tax = total * 0.18  # 18% GST
        grand_total = total + tax

        bill_content = f"""
{'='*50}
           CAFE MANAGEMENT SYSTEM
{'='*50}
Date: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
Bill No: {len(self.order_history) + 1:04d}
{'='*50}

{'Item':<20} {'Price':<8} {'Qty':<5} {'Amount':<10}
{'-'*50}
"""

        for item, details in self.current_order.items():
            price = details['price']
            quantity = details['quantity']
            amount = price * quantity
            bill_content += f"{item:<20} ₹{price:<7} {quantity:<5} ₹{amount:<9}\n"

        bill_content += f"""
{'-'*50}
{'Subtotal:':<35} ₹{total:.2f}
{'Tax (18%):':<35} ₹{tax:.2f}
{'='*50}
{'TOTAL:':<35} ₹{grand_total:.2f}
{'='*50}

        Thank you for visiting!
        Have a great day!
"""
        return bill_content

    def save_bill(self, bill_content):
        try:
            filename = f"bill_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
            with open(filename, 'w') as f:
                f.write(bill_content)
            messagebox.showinfo("Success", f"Bill saved as {filename}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save bill: {str(e)}")

    def confirm_order(self, bill_window):
        # Add to order history
        order_data = {
            'date': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'items': self.current_order.copy(),
            'total': sum(details['price'] * details['quantity']
                        for details in self.current_order.values())
        }
        self.order_history.append(order_data)

        # Save data
        self.save_data()

        # Clear current order
        self.current_order.clear()
        self.update_order_display()

        # Close bill window
        bill_window.destroy()

        messagebox.showinfo("Success", "Order confirmed successfully!")

    def add_menu_item(self):
        # Get category
        categories = list(self.menu_items.keys())
        category = simpledialog.askstring("Category",
                                         f"Enter category ({', '.join(categories)}) or new category:")
        if not category:
            return

        # Get item name
        item_name = simpledialog.askstring("Item Name", "Enter item name:")
        if not item_name:
            return

        # Get price
        try:
            price = float(simpledialog.askstring("Price", "Enter price (₹):"))
            if price <= 0:
                raise ValueError
        except (ValueError, TypeError):
            messagebox.showerror("Error", "Invalid price")
            return

        # Add item
        if category not in self.menu_items:
            self.menu_items[category] = {}

        self.menu_items[category][item_name] = price
        self.save_data()

        messagebox.showinfo("Success", f"Added {item_name} to {category} menu")

        # Refresh GUI (you might want to implement a refresh method)
        messagebox.showinfo("Info", "Please restart the application to see the new item")

    def view_order_history(self):
        if not self.order_history:
            messagebox.showinfo("Info", "No order history available")
            return

        # Create history window
        history_window = tk.Toplevel(self.root)
        history_window.title("Order History")
        history_window.geometry("800x600")
        history_window.configure(bg="white")

        # History content
        history_text = tk.Text(history_window, font=("Courier", 10), bg="white",
                              wrap="word")
        history_scrollbar = ttk.Scrollbar(history_window, orient="vertical",
                                         command=history_text.yview)
        history_text.configure(yscrollcommand=history_scrollbar.set)

        # Generate history content
        history_content = "ORDER HISTORY\n" + "="*80 + "\n\n"

        for i, order in enumerate(self.order_history, 1):
            history_content += f"Order #{i} - {order['date']}\n"
            history_content += "-" * 40 + "\n"

            for item, details in order['items'].items():
                history_content += f"{item}: ₹{details['price']} x {details['quantity']} = ₹{details['price'] * details['quantity']}\n"

            history_content += f"Total: ₹{order['total']:.2f}\n\n"

        history_text.insert("1.0", history_content)
        history_text.config(state="disabled")

        history_text.pack(side="left", fill="both", expand=True, padx=20, pady=20)
        history_scrollbar.pack(side="right", fill="y", pady=20)

    def save_data(self):
        data = {
            'menu_items': self.menu_items,
            'order_history': self.order_history
        }
        try:
            with open('cafe_data.json', 'w') as f:
                json.dump(data, f, indent=2)
        except Exception as e:
            print(f"Error saving data: {e}")

    def load_data(self):
        try:
            if os.path.exists('cafe_data.json'):
                with open('cafe_data.json', 'r') as f:
                    data = json.load(f)
                    if 'menu_items' in data:
                        self.menu_items = data['menu_items']
                    if 'order_history' in data:
                        self.order_history = data['order_history']
        except Exception as e:
            print(f"Error loading data: {e}")

# Create and run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = CafeManagementSystem(root)
    root.mainloop()
