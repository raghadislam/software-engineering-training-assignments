# **Django E-Commerce Site**

An e-commerce platform built with Django to allow users to browse products, add items to their cart, and complete purchases via a checkout process.

---

## **Features**

- **User Accounts**:
  - Registration, login, and logout functionality.
  - Validation to ensure unique usernames during registration.
  - User profile and order history (if extended).

- **Product Management**:
  - A product catalog where users can browse items.
  - Each product includes a name, description, price, and image.

- **Shopping Cart**:
  - Add, remove, and update items in the shopping cart.
  - Dynamic total price calculation.

- **Checkout Process**:
  - Enter shipping details and simulate payment processing.
  - Order confirmation page with order summary.

- **Responsive Design**:
  - Fully responsive layout using Bootstrap for styling.
  - Works on desktops, tablets, and mobile devices.

- **Admin Panel**:
  - Admin interface for managing products, users, and orders.

---

## **Project Setup**

### **Requirements**
- Python 3.8+
- Django 4.2+
- Virtual environment (`venv`)
- SQLite (default database)
- Required Python packages (listed in `requirements.txt`)

### **Installation Instructions**

1. **Clone the Repository**:
   ```bash
   git clone <repository_url>
   cd ecommerce_project
   ```

2. **Set Up a Virtual Environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply Migrations**:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Run the Development Server**:
   ```bash
   python manage.py runserver
   ```

6. **Access the Application**:
   Open your browser and go to: [http://127.0.0.1:8000](http://127.0.0.1:8000).

---

## **Usage**

### **1. Register and Login**
- Go to the registration page: `/store/register/`.
- Register with a unique username and password.
- Log in with the same credentials.

### **2. Browse Products**
- Visit the products page at `/store/products/`.
- Browse the product catalog.

### **3. Add to Cart**
- Click the "Add to Cart" button on a product to add it to the shopping cart.

### **4. View Cart**
- Go to `/store/cart/` to view items in your cart.
- Remove items or proceed to checkout.

### **5. Checkout**
- Go to `/store/checkout/` to enter shipping details and complete the purchase.

### **6. Admin Panel**
- Access the admin interface at `/admin/` to manage products and orders.

---

## **Project Structure**

```plaintext
ecommerce_project/
├── ecommerce/
│   ├── settings.py       # Project settings
│   ├── urls.py           # Project URL configuration
│   ├── wsgi.py           # WSGI entry point for deployment
│   ├── asgi.py           # ASGI entry point for deployment
│
├── store/
│   ├── models.py         # Database models for products, orders, etc.
│   ├── views.py          # Logic for product listing, cart, checkout, etc.
│   ├── urls.py           # URL patterns for the store app
│   ├── templates/
│       ├── store/
│           ├── base.html           # Base template for consistent layouts
│           ├── product_list.html   # Product catalog page
│           ├── cart.html           # Shopping cart page
│           ├── checkout.html       # Checkout page
│           ├── order_success.html  # Order confirmation page
│           ├── register.html       # User registration page
│           ├── login.html          # User login page
│
├── media/                 # Directory for uploaded product images
├── static/                # Static files (CSS, JS, etc.)
├── manage.py              # Django management commands
└── requirements.txt       # Python dependencies
```

---

## **Technologies Used**

- **Frontend**:
  - HTML5, CSS3, Bootstrap 5 (for responsiveness)
- **Backend**:
  - Django 4.2 (Python web framework)
- **Database**:
  - SQLite (default for development)




