# ============================================================
#  ONLINE BANKING SYSTEM - Like JINNAH Bank Website
#  Python + Tkinter GUI - Aesthetic + Professional
# ============================================================
import tkinter as tk
from tkinter import messagebox

# --- COLORS - JINNAH Bank Theme ---
GREEN = "#006633"
DARK_GREEN = "#004d26"
LIGHT_GREEN = "#e8f5e9"
WHITE = "#ffffff"
BLACK = "#1a1a1a"
GREY = "#666666"
LIGHT_GREY = "#f5f5f5"

# --- DATABASE ---
users = {
    "admin": {"name": "Ayesha", "password": "1234", "balance": 5000, "history": ["Account Opened: +Rs. 5000"]}
}
current_user = None

# --- MAIN WINDOW ---
root = tk.Tk()
root.title("JINNAH Bank - Online Banking System")
root.geometry("900x600")
root.configure(bg=WHITE)
root.resizable(False, False)

# ============================================================
#  HELPER FUNCTIONS
# ============================================================

def clear_frame():
    for widget in root.winfo_children():
        widget.destroy()

def show_home():
    clear_frame()
    # --- TOP HEADER ---
    header = tk.Frame(root, bg=GREEN, height=70)
    header.pack(fill="x")
    tk.Label(header, text="  JINNAH BANK", font=("Arial", 22, "bold"), bg=GREEN, fg=WHITE).pack(side="left", pady=15)
    tk.Label(header, text="Online Banking System  ", font=("Arial", 11), bg=GREEN, fg=WHITE).pack(side="right", pady=20)

    # --- HERO SECTION ---
    tk.Label(root, text="Bank with Confidence.", font=("Arial", 28, "bold"), bg=WHITE, fg=BLACK).pack(pady=(40, 5))
    tk.Label(root, text="Secure. Simple. Smart.", font=("Arial", 22, "bold"), bg=WHITE, fg=GREEN).pack(pady=5)
    tk.Label(root, text="Manage your accounts, transfer funds and check balance\nsafely with our secure online banking platform.", 
             font=("Arial", 12), bg=WHITE, fg=GREY, justify="center").pack(pady=10)

    # --- BUTTONS ---
    btn_frame = tk.Frame(root, bg=WHITE)
    btn_frame.pack(pady=20)
    tk.Button(btn_frame, text="  Create Account  ", font=("Arial", 14, "bold"), bg=GREEN, fg=WHITE, 
              relief="flat", padx=20, pady=12, cursor="hand2", command=show_create).pack(side="left", padx=10)
    tk.Button(btn_frame, text="  Login  ", font=("Arial", 14, "bold"), bg=WHITE, fg=GREEN, 
              relief="solid", bd=2, padx=30, pady=12, cursor="hand2", command=show_login).pack(side="left", padx=10)

    # --- FEATURES ---
    tk.Label(root, text="✓  Bank-level Encryption    •    24/7 Support    •    Trusted Banking", 
             font=("Arial", 11), bg=WHITE, fg=GREY).pack(pady=30)
    tk.Label(root, text="Total Users: " + str(len(users)) + "  |  Demo Login: admin / 1234", 
             font=("Arial", 10), bg=WHITE, fg=GREY).pack()

# ============================================================
#  CREATE ACCOUNT PAGE
# ============================================================

def show_create():
    clear_frame()
    tk.Label(root, text="Create Your Account", font=("Arial", 24, "bold"), bg=WHITE, fg=GREEN).pack(pady=(30, 5))
    tk.Label(root, text="Open your account in 1 minute", font=("Arial", 12), bg=WHITE, fg=GREY).pack(pady=5)

    card = tk.Frame(root, bg=LIGHT_GREY, padx=30, pady=20)
    card.pack(pady=20)

    tk.Label(card, text="Full Name", font=("Arial", 11, "bold"), bg=LIGHT_GREY).pack(anchor="w")
    name_entry = tk.Entry(card, font=("Arial", 12), width=35, relief="solid", bd=1)
    name_entry.pack(pady=(2, 10))

    tk.Label(card, text="Username", font=("Arial", 11, "bold"), bg=LIGHT_GREY).pack(anchor="w")
    user_entry = tk.Entry(card, font=("Arial", 12), width=35, relief="solid", bd=1)
    user_entry.pack(pady=(2, 10))

    tk.Label(card, text="Password", font=("Arial", 11, "bold"), bg=LIGHT_GREY).pack(anchor="w")
    pass_entry = tk.Entry(card, font=("Arial", 12), width=35, show="*", relief="solid", bd=1)
    pass_entry.pack(pady=(2, 10))

    tk.Label(card, text="Initial Deposit (Rs.)", font=("Arial", 11, "bold"), bg=LIGHT_GREY).pack(anchor="w")
    bal_entry = tk.Entry(card, font=("Arial", 12), width=35, relief="solid", bd=1)
    bal_entry.pack(pady=(2, 15))

    def do_create():
        name = name_entry.get().strip()
        username = user_entry.get().strip().lower()
        password = pass_entry.get().strip()
        try:
            balance = int(bal_entry.get() or 0)
        except:
            balance = 0
        if not name or not username or not password:
            messagebox.showerror("Error", "Please fill all fields!")
            return
        if username in users:
            messagebox.showerror("Error", "Username already exists!")
            return
        users[username] = {"name": name, "password": password, "balance": balance, "history": [f"Account Opened: +Rs. {balance}"]}
        messagebox.showinfo("Success", f"Welcome {name}! Account Created!\nNow Login with {username}")
        show_login()

    tk.Button(card, text="Create Account", font=("Arial", 13, "bold"), bg=GREEN, fg=WHITE, relief="flat", 
              padx=20, pady=10, cursor="hand2", command=do_create).pack(pady=5)
    tk.Button(root, text="← Back to Home", font=("Arial", 11), bg=WHITE, fg=GREEN, relief="flat", cursor="hand2", command=show_home).pack()

# ============================================================
#  LOGIN PAGE
# ============================================================

def show_login():
    clear_frame()
    tk.Label(root, text="Welcome Back", font=("Arial", 24, "bold"), bg=WHITE, fg=GREEN).pack(pady=(40, 5))
    tk.Label(root, text="Sign in to access your account", font=("Arial", 12), bg=WHITE, fg=GREY).pack(pady=5)

    card = tk.Frame(root, bg=LIGHT_GREY, padx=30, pady=20)
    card.pack(pady=20)

    tk.Label(card, text="Username", font=("Arial", 11, "bold"), bg=LIGHT_GREY).pack(anchor="w")
    user_entry = tk.Entry(card, font=("Arial", 12), width=35, relief="solid", bd=1)
    user_entry.pack(pady=(2, 10))

    tk.Label(card, text="Password", font=("Arial", 11, "bold"), bg=LIGHT_GREY).pack(anchor="w")
    pass_entry = tk.Entry(card, font=("Arial", 12), width=35, show="*", relief="solid", bd=1)
    pass_entry.pack(pady=(2, 15))

    def do_login():
        global current_user
        username = user_entry.get().strip().lower()
        password = pass_entry.get().strip()
        if username in users and users[username]["password"] == password:
            current_user = username
            show_dashboard()
        else:
            messagebox.showerror("Error", "Invalid Username or Password!")

    tk.Button(card, text="Login", font=("Arial", 13, "bold"), bg=GREEN, fg=WHITE, relief="flat", 
              padx=20, pady=10, cursor="hand2", command=do_login).pack(pady=5)
    tk.Label(root, text="Don't have an account? Create Account", font=("Arial", 11), bg=WHITE, fg=GREEN, cursor="hand2").pack(pady=5)
    tk.Button(root, text="← Back to Home", font=("Arial", 11), bg=WHITE, fg=GREEN, relief="flat", cursor="hand2", command=show_home).pack()

# ============================================================
#  DASHBOARD - After Login
# ============================================================

def show_dashboard():
    global current_user
    user = users[current_user]
    clear_frame()

    header = tk.Frame(root, bg=GREEN, height=70)
    header.pack(fill="x")
    tk.Label(header, text=f"  Welcome, {user['name']}", font=("Arial", 18, "bold"), bg=GREEN, fg=WHITE).pack(side="left", pady=15)
    tk.Button(header, text="Logout", font=("Arial", 11, "bold"), bg=WHITE, fg=GREEN, relief="flat", cursor="hand2", command=show_home).pack(side="right", padx=15, pady=15)

    # Balance Card
    bal_card = tk.Frame(root, bg=GREEN, padx=30, pady=20)
    bal_card.pack(pady=25, fill="x", padx=60)
    tk.Label(bal_card, text="Total Balance", font=("Arial", 12), bg=GREEN, fg=WHITE).pack()
    tk.Label(bal_card, text=f"Rs. {user['balance']}", font=("Arial", 28, "bold"), bg=GREEN, fg=WHITE).pack()
    tk.Label(bal_card, text=f"Account: {current_user}  •  Available", font=("Arial", 10), bg=GREEN, fg=WHITE).pack()

    # Buttons
    btns = tk.Frame(root, bg=WHITE)
    btns.pack(pady=10)
    tk.Button(btns, text="Deposit", font=("Arial", 12, "bold"), bg=GREEN, fg=WHITE, relief="flat", padx=20, pady=10, cursor="hand2", command=lambda: do_transaction("Deposit")).pack(side="left", padx=8)
    tk.Button(btns, text="Withdraw", font=("Arial", 12, "bold"), bg=WHITE, fg=GREEN, relief="solid", bd=2, padx=20, pady=10, cursor="hand2", command=lambda: do_transaction("Withdraw")).pack(side="left", padx=8)
    tk.Button(btns, text="Transfer", font=("Arial", 12, "bold"), bg=WHITE, fg=GREEN, relief="solid", bd=2, padx=20, pady=10, cursor="hand2", command=lambda: do_transaction("Transfer")).pack(side="left", padx=8)

    # History
    tk.Label(root, text="Recent Transactions", font=("Arial", 14, "bold"), bg=WHITE, fg=BLACK).pack(pady=(15, 5))
    hist_box = tk.Listbox(root, font=("Arial", 11), width=60, height=8, relief="solid", bd=1)
    hist_box.pack()
    for h in user["history"]:
        hist_box.insert("end", "  •  " + h)

def do_transaction(type_):
    global current_user
    user = users[current_user]
    # Simple popup window for amount
    win = tk.Toplevel(root)
    win.title(type_)
    win.geometry("350x220")
    win.configure(bg=WHITE)
    tk.Label(win, text=f"{type_} Money", font=("Arial", 16, "bold"), bg=WHITE, fg=GREEN).pack(pady=15)
    entry = tk.Entry(win, font=("Arial", 14), width=20, justify="center")
    entry.pack(pady=10)
    if type_ == "Transfer":
        tk.Label(win, text="Receiver Username", font=("Arial", 10), bg=WHITE).pack()
        rec_entry = tk.Entry(win, font=("Arial", 12), width=20, justify="center")
        rec_entry.pack(pady=5)
    def confirm():
        try:
            amt = int(entry.get())
        except:
            messagebox.showerror("Error", "Enter valid amount!"); return
        if amt <= 0:
            messagebox.showerror("Error", "Amount must be > 0"); return
        if type_ == "Deposit":
            user["balance"] += amt
            user["history"].append(f"Deposit: +Rs. {amt}")
        elif type_ == "Withdraw":
            if amt > user["balance"]:
                messagebox.showerror("Error", "Insufficient Balance!"); return
            user["balance"] -= amt
            user["history"].append(f"Withdraw: -Rs. {amt}")
        elif type_ == "Transfer":
            rec = rec_entry.get().strip().lower()
            if rec not in users:
                messagebox.showerror("Error", "User not found!"); return
            if amt > user["balance"]:
                messagebox.showerror("Error", "Insufficient Balance!"); return
            user["balance"] -= amt
            users[rec]["balance"] += amt
            user["history"].append(f"Transfer to {rec}: -Rs. {amt}")
            users[rec]["history"].append(f"Received from {current_user}: +Rs. {amt}")
        win.destroy()
        messagebox.showinfo("Success", f"{type_} Successful!")
        show_dashboard()
    tk.Button(win, text="Confirm", font=("Arial", 12, "bold"), bg=GREEN, fg=WHITE, relief="flat", padx=20, pady=8, command=confirm).pack(pady=10)

# --- START ---
show_home()
root.mainloop()