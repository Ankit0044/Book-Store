import json
import tkinter as tk
from tkinter import messagebox

# Book Catalog Management
class BookCatalog:
    def __init__(self):
        self.books = []

    def add_book(self, title, author, price):
        self.books.append({"title": title, "author": author, "price": price})

    def get_book_info(self, title):
        for book in self.books:
            if book['title'] == title:
                return book
        return None

# Customer Management
class CustomerManagement:
    def __init__(self):
        self.customers = []

    def add_customer(self, name, email):
        self.customers.append({"name": name, "email": email})

    def get_customer_info(self, name):
        for customer in self.customers:
            if customer['name'] == name:
                return customer
        return None

# Order Management
class OrderManagement:
    def __init__(self):
        self.orders = []
        self.order_id = 1

    def create_order(self, customer_name, book_title, status):
        customer_info = customers.get_customer_info(customer_name)
        book_info = catalog.get_book_info(book_title)
        if customer_info and book_info:
            order = {
                'order_id': self.order_id,
                'customer': customer_info,
                'book': book_info,
                'status': status,
                'shipping_cost': None,
                'total_price': book_info['price'],
            }
            self.orders.append(order)
            self.order_id += 1
            return order
        return None

# Shipping Integration
def calculate_shipping_cost(order):
    # Simplified shipping cost calculation (fixed per item)
    return len(order['book']['title']) * 2

# Payment Processing (Simplified for cash payment)
def process_payment(order):
    payment_window = tk.Toplevel(window)
    payment_window.title("Payment")
    total_price_label = tk.Label(payment_window, text=f"Total Amount: ${order['total_price']:.2f}")
    total_price_label.pack()
    cash_payment_button = tk.Button(payment_window, text="Cash Payment", command=lambda: finalize_order(order, payment_window))
    cash_payment_button.pack()

def finalize_order(order, payment_window):
    order['status'] = 'Paid'
    order['shipping_cost'] = calculate_shipping_cost(order)
    order['total_price'] = order['total_price'] + order['shipping_cost']
    payment_window.destroy()
    update_order_list()

# GUI Functions
def add_book_gui():
    title = title_entry.get()
    author = author_entry.get()
    price = float(price_entry.get())
    catalog.add_book(title, author, price)
    update_catalog_list()
    clear_entries()

def add_customer_gui():
    name = name_entry.get()
    email = email_entry.get()
    customers.add_customer(name, email)
    update_customer_list()
    clear_entries()

def create_order_gui():
    selected_customer = customer_listbox.get(customer_listbox.curselection())
    selected_book = catalog_listbox.get(catalog_listbox.curselection())
    status = "Pending"
    order = orders.create_order(selected_customer, selected_book, status)
    if order:
        process_payment(order)

def update_catalog_list():
    catalog_listbox.delete(0, tk.END)
    for book in catalog.books:
        catalog_listbox.insert(tk.END, f"{book['title']} by {book['author']}")

def update_customer_list():
    customer_listbox.delete(0, tk.END)
    for customer in customers.customers:
        customer_listbox.insert(tk.END, f"{customer['name']} ({customer['email']})")

def update_order_list():
    order_listbox.delete(0, tk.END)
    for order in orders.orders:
        order_listbox.insert(tk.END, f"{order['customer']['name']} - {order['book']['title']} - {order['status']}")

def clear_entries():
    title_entry.delete(0, tk.END)
    author_entry.delete(0, tk.END)
    name_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    price_entry.delete(0, tk.END)

# Initialize the GUI
window = tk.Tk()
window.title("Book Store Management")

# Create and set up GUI elements
catalog = BookCatalog()
customers = CustomerManagement()
orders = OrderManagement()

# Create catalog management section
catalog_label = tk.Label(window, text="Book Catalog Management")
title_label = tk.Label(window, text="Title:")
author_label = tk.Label(window, text="Author:")
price_label = tk.Label(window, text="Price:")
title_entry = tk.Entry(window)
author_entry = tk.Entry(window)
price_entry = tk.Entry(window)
add_book_button = tk.Button(window, text="Add Book", command=add_book_gui)
catalog_listbox = tk.Listbox(window)
update_catalog_list()

# Create customer management section
customer_label = tk.Label(window, text="Customer Management")
name_label = tk.Label(window, text="Name:")
email_label = tk.Label(window, text="Email:")
name_entry = tk.Entry(window)
email_entry = tk.Entry(window)
add_customer_button = tk.Button(window, text="Add Customer", command=add_customer_gui)
customer_listbox = tk.Listbox(window)
update_customer_list()

# Create order management section
order_label = tk.Label(window, text="Order Management")
customer_list_label = tk.Label(window, text="Select a Customer:")
catalog_list_label = tk.Label(window, text="Select a Book:")
customer_listbox = tk.Listbox(window)
update_customer_list()
catalog_listbox = tk.Listbox(window)
update_catalog_list()
create_order_button = tk.Button(window, text="Create Order", command=create_order_gui)
order_listbox = tk.Listbox(window)
update_order_list()

# Grid layout
catalog_label.grid(row=0, column=0)
title_label.grid(row=1, column=0, padx=10, pady=5)
author_label.grid(row=2, column=0, padx=10, pady=5)
price_label.grid(row=3, column=0, padx=10, pady=5)
title_entry.grid(row=1, column=1, padx=10, pady=5)
author_entry.grid(row=2, column=1, padx=10, pady=5)
price_entry.grid(row=3, column=1, padx=10, pady=5)
add_book_button.grid(row=4, column=0, columnspan=2, padx=10, pady=5)
catalog_listbox.grid(row=5, column=0, columnspan=2, padx=10, pady=5)

customer_label.grid(row=0, column=2)
name_label.grid(row=1, column=2, padx=10, pady=5)
email_label.grid(row=2, column=2, padx=10, pady=5)
name_entry.grid(row=1, column=3, padx=10, pady=5)
email_entry.grid(row=2, column=3, padx=10, pady=5)
add_customer_button.grid(row=3, column=2, columnspan=2, padx=10, pady=5)
customer_listbox.grid(row=4, column=2, columnspan=2, padx=10, pady=5)

order_label.grid(row=0, column=4)
customer_list_label.grid(row=1, column=4, padx=10, pady=5)
catalog_list_label.grid(row=1, column=5, padx=10, pady=5)
customer_listbox.grid(row=2, column=4, padx=10, pady=5)
catalog_listbox.grid(row=2, column=5, padx=10, pady=5)
create_order_button.grid(row=3, column=4, columnspan=2, padx=10, pady=5)
order_listbox.grid(row=4, column=4, columnspan=2, padx=10, pady=5)

window.mainloop()
