# 💰 Budget Manager

A simple terminal-based Python application to manage and track user expenses. It supports both **Admin** and **User** roles with distinct capabilities. Ideal for personal or small-scale multi-user budget tracking.

---

## 📋 Features

### 👤 User
- Secure login with username and password
- View all personal details including expenses and budget
- Add new expenses (with budget validation)
- Update credentials (username/password)
- View remaining budget
- List itemized expenses

### 🔐 Admin
- Login with admin password
- Add, remove, and update users
- Update users' budgets
- View data of all users or a specific user
- Update admin password

---

## 📁 File Structure

- `budgetManager.py` – Main application logic
- `userData.txt` – Stores user data in a structured format
- `adminData.txt` – Stores admin password

---

## 🔧 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/budget-manager.git
   cd budget-manager
   ```

2. **Install dependencies**
   ```bash
   pip install tabulate
   ```

3. **Prepare Data Files**
   - Create a `userData.txt` file with at least one user (format described below).
   - Create `adminData.txt` and set an initial password (e.g., `admin123`).

---

## 🧾 Data Format

### `userData.txt`
Each line represents a user:
```
username___password___allotedAmt___expendedAmt___remainingAmt___item1|price1_item2|price2_
```

### `adminData.txt`
Plain text file with the admin password:
```
admin123
```

---

## ▶️ Running the Application

```bash
python budgetManager.py
```

Choose your role:
```
+--------------+
| Who're You ? |
+--------------+
| 1 | Admin    |
| 2 | User     |
+--------------+
```
