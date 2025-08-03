# 🛍️ SmartShop – An Online Shopping Platform

**SmartShop** is a Django-powered e-commerce web application designed to empower small and medium-sized businesses (SMBs) with a secure, scalable, and user-friendly online store. It offers robust features for product management, order tracking, and customer interaction, all wrapped in a responsive and intuitive interface.

---

## 📌 Table of Contents

- [Demo Screenshots](#-demo-screenshots)
- [Key Features](#-key-features)
- [Technologies Used](#-technologies-used)
- [Project Objectives](#-project-objectives)
- [System Architecture](#-system-architecture)
- [Installation](#-installation)
- [Usage](#-usage)
- [Screenshots](#-screenshots)
- [Future Enhancements](#-future-enhancements)
- [License](#-license)

---

## 📸 Demo Screenshots

Screenshots of the user interface, admin panel, and shopping flow are available in the `/screenshots/` folder or embedded below.

---

## 🚀 Key Features

- 🧭 **User-friendly Navigation** with categories and filters  
- 🛒 **Cart Management** with real-time updates  
- 🔐 **Secure User Authentication** using Django's auth system  
- 💳 **Payment Integration** with PayPal (mocked for demo)  
- 📦 **Order Tracking** with status updates  
- 📈 **Admin Dashboard** for product, order, and user management  
- 📊 **Reports and Analytics** for decision-making  
- 💬 **Role-Based Access Control** for Admins, Customers, and Suppliers  

---

## 🧰 Technologies Used

| Layer             | Stack                      |
|------------------|----------------------------|
| Frontend         | HTML5, CSS3, Bootstrap, JS |
| Backend          | Python 3, Django           |
| Database         | SQLite (dev) / PostgreSQL (prod ready) |
| Version Control  | Git, GitHub                |
| Deployment Ready | Heroku / AWS / PythonAnywhere |
| Testing          | Selenium, Postman          |

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

- **Model**: Defines the database structure and business entities.
- **View**: Controls the UI using Django Templates and Bootstrap.
- **Controller**: Handles business logic, form validation, and routing.

---

## ⚙️ Installation

### Prerequisites

- Python 3.8+
- Git
- Virtualenv (recommended)

### Setup

```bash
# Clone the repo
git clone https://github.com/dharmender12/Smartshop.git
cd Smartshop

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows use venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py makemigrations
python manage.py migrate

# Create superuser for admin access
python manage.py createsuperuser

# Start the server
python manage.py runserver
