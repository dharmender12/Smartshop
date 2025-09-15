# SmartShop – An Online Shopping Platform

**SmartShop** is a Django-powered e-commerce web application designed to empower small and medium-sized businesses (SMBs) with a secure, scalable, and user-friendly online store. It offers robust features for product management, order tracking, and customer interaction, all wrapped in a responsive and intuitive interface.

---

## 📌 Table of Contents

* [Demo Screenshots](#-demo-screenshots)
* [Key Features](#-key-features)
* [Technologies Used](#-technologies-used)
* [Project Objectives](#-project-objectives)
* [System Architecture](#-system-architecture)
* [Installation](#-installation)
* [Usage](#-usage)
* [Screenshots](#-screenshots)
* [Future Enhancements](#-future-enhancements)
* [License](#-license)
* 
---

## 📸 Demo Screenshots

Screenshots of the user interface, admin panel, and shopping flow are available in the `/screenshots/` folder or embedded below.

### 🏠 Home Page

![Home Page](https://github.com/dharmender12/Smartshop/blob/main/screenshots/home_page.png?raw=true)

### 🛒 Checkout Page

![Checkout Page](https://github.com/dharmender12/Smartshop/blob/main/screenshots/checkout.png?raw=true)

---

## 🚀 Key Features

* 🗭 **User-friendly Navigation** with categories and filters
* 🛒 **Cart Management** with real-time updates
* 🔐 **Secure User Authentication** using Django's auth system
* 💳 **Payment Integration** with PayPal (mocked for demo)
* 📦 **Order Tracking** with status updates
* 📈 **Admin Dashboard** for product, order, and user management
* 📊 **Reports and Analytics** for decision-making
* 💬 **Role-Based Access Control** for Admins, Customers, and Suppliers

---

## 🧰 Technologies Used

| Layer           | Stack                              |
| --------------- | ---------------------------------- |
| Frontend        | HTML5, CSS3, Bootstrap, JavaScript |
| Backend         | Python 3, Django                   |
| Database        | SQLite (dev) / PostgreSQL (prod)   |
| Version Control | Git, GitHub                        |
| Deployment      | Heroku / AWS / PythonAnywhere      |
| Testing         | Selenium, Postman                  |

---

## 🎯 Project Objectives

1. Provide a seamless shopping experience to customers.
2. Empower SMBs with low-cost, customizable online platforms.
3. Offer secure and scalable architecture.
4. Enable real-time product and order management.
5. Support integration with payment gateways and logistics APIs.

---

## 🧱 System Architecture

SmartShop follows the **Model-View-Controller (MVC)** pattern:

* **Model**: Defines the database structure and business entities.
* **View**: Controls the UI using Django Templates and Bootstrap.
* **Controller**: Handles business logic, form validation, and routing.

It supports three main user roles:

* **Admin**: Full control over products, users, and orders.
* **Customer**: Browse products, manage cart, place and track orders.
* **Supplier**: Optional role to manage inventory.

---

## ⚙️ Installation

### Prerequisites

* Python 3.8+
* Git
* Virtualenv (recommended)

### Setup Instructions

```bash
# Clone the repo
git clone https://github.com/dharmender12/Smartshop.git
cd Smartshop

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py makemigrations
python manage.py migrate

# Create superuser for admin access
python manage.py createsuperuser

# Start the server
python manage.py runserver
```

Then open your browser and go to: [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 🧪 Usage

### Admin

* Login via `/admin`
* Add/edit/delete products
* Manage users and orders

### Customer

* Register or login
* Browse and search products
* Add items to cart and place orders
* Track past and current orders

### Supplier (optional)

* Manage product stock and availability

---

## 🖼️ Screenshots

See the [Demo Screenshots](#-demo-screenshots) section above for UI visuals.

---

## 🚧 Future Enhancements

* Integrate real payment gateways (Razorpay, Stripe, etc.)
* SMS and email order notifications
* AI-based product recommendations
* Order cancellation and return system
* Progressive Web App (PWA) version
* Invoice generation and download

---

## 📜 License

This project was developed by [Dharmender](https://github.com/dharmender12) as part of the NIELIT 'A' Level course.

Feel free to fork or adapt it for learning and development purposes. Attribution appreciated.
