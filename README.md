# 🍔 Foodiie - Full-Stack MERN Food Ordering Platform with AI Insights

[![Live Site](https://img.shields.io/badge/Live_Site-Vercel-black?style=for-the-badge&logo=vercel)](https://foodiie-two.vercel.app)
[![Backend API](https://img.shields.io/badge/Backend_API-Render-46E3B7?style=for-the-badge&logo=render)](https://foodiie-t2v0.onrender.com)
[![React](https://img.shields.io/badge/React_18-20232A?style=for-the-badge&logo=react&logoColor=61DAFB)](https://reactjs.org/)
[![Vite](https://img.shields.io/badge/Vite-646CFF?style=for-the-badge&logo=vite&logoColor=white)](https://vitejs.dev/)
[![Node.js](https://img.shields.io/badge/Node.js-339933?style=for-the-badge&logo=node.js&logoColor=white)](https://nodejs.org/)
[![Express.js](https://img.shields.io/badge/Express.js-000000?style=for-the-badge&logo=express&logoColor=white)](https://expressjs.com/)
[![MongoDB](https://img.shields.io/badge/MongoDB_Atlas-4EA94B?style=for-the-badge&logo=mongodb&logoColor=white)](https://www.mongodb.com/atlas)
[![Groq AI](https://img.shields.io/badge/AI_Powered-Groq_Llama_3.1-F55036?style=for-the-badge)](https://groq.com)

**Foodiie** is a modern, responsive, full-stack food delivery application built using the MERN stack (MongoDB, Express, React, Node.js) and enhanced with **Groq AI (Llama 3.1)** for smart review analysis and automated food metadata generation.

---

## 🌐 Live Deployments

* **Frontend (Vercel):** [https://foodiie-two.vercel.app](https://foodiie-two.vercel.app)
* **Backend API (Render):** [https://foodiie-t2v0.onrender.com](https://foodiie-t2v0.onrender.com)

---

## ✨ Features

### 🛒 Customer Experience
* **Restaurant Discovery**: Search restaurants by keyword, filter by pure vegetarian, and sort by ratings or review counts.
* **Interactive Menus**: Categorized restaurant menus (Starters, Main Course, Pizzas, Desserts, Beverages) with high-res food images and prices.
* **Smart Shopping Cart**: Real-time cart state management powered by Redux Toolkit; add, adjust quantities, and remove items with persistent storage.
* **Seamless Payments**: Secure checkout flow integrated with **Stripe**.
* **Order Management**: Order placement, order history tracking, and order details lookup.
* **User Authentication**: Secure signup, login, profile management, avatar uploads via Cloudinary, and password reset flows via email.

### 🤖 AI-Powered Capabilities (Groq Cloud)
* **💬 AI Review Summary & Sentiment Analysis**:
  * Real-time customer review processing using `llama-3.1-8b-instant`.
  * Generates an overall sentiment rating (`positive`, `negative`, `mixed`), 3 actionable bullet points, and trending keyword hashtag tags.
* **🏷️ Smart Dish Description & Classification**:
  * Generates appetizing descriptions, realistic allergen warnings, portion sizes, and meal timings (`Lunch`, `Dinner`) automatically.

### 🛡️ Admin & Store Management
* Add new restaurants and delete existing ones.
* Create custom menu categories and attach new food items directly through the UI.
* Trigger AI review analysis and dish classification metadata generation on demand.

---

## 🛠️ Tech Stack

### Frontend
* **Core:** React 18, Vite
* **State Management:** Redux Toolkit, React-Redux
* **Routing:** React Router DOM (v7)
* **Styling & UI:** React-Bootstrap, Styled Components, FontAwesome Icons, React-Toastify
* **HTTP Client:** Axios with `withCredentials` support

### Backend
* **Runtime & Framework:** Node.js, Express.js
* **Database & ODM:** MongoDB Atlas, Mongoose
* **Authentication:** JSON Web Tokens (JWT), HTTP-Only Cookies, Bcrypt.js
* **Cloud Storage:** Cloudinary (user avatars and restaurant images)
* **AI Provider:** Groq SDK / REST API (`llama-3.1-8b-instant`)
* **Payments:** Stripe API
* **Email Service:** Nodemailer (Mailtrap / SMTP)

---

## 📁 Project Structure

```text
FoodProject/
├── backend/
│   ├── config/
│   │   ├── config.env              # Environment configuration
│   │   ├── database.js             # MongoDB Atlas connection
│   │   └── cloudinary.js           # Cloudinary setup
│   ├── controllers/
│   │   ├── ai.controller.js        # AI review analysis & dish descriptions
│   │   ├── authController.js       # User auth & profile management
│   │   ├── cartController.js       # Cart operations
│   │   ├── foodItemController.js   # Food item operations
│   │   ├── menuController.js       # Menu categories & items
│   │   ├── orderController.js      # Orders & checkout
│   │   ├── paymentController.js    # Stripe payments
│   │   └── restaurantController.js # Restaurants CRUD
│   ├── models/
│   │   ├── foodItem.js             # Food schema
│   │   ├── menu.js                 # Menu schema
│   │   ├── order.js                # Order schema
│   │   ├── restaurant.js           # Restaurant schema
│   │   └── user.js                 # User schema
│   ├── routes/                     # Express API route declarations
│   ├── services/
│   │   ├── ai.service.js           # Groq food classification
│   │   └── aiReviewAnalyzer.js     # Groq review sentiment & summaries
│   ├── utils/
│   │   ├── seedMenuData.js         # Menu seeding script
│   │   └── addMoreRestaurants.js   # Restaurant seeding script
│   ├── app.js                      # Express middleware & CORS setup
│   ├── server.js                   # Server entrypoint
│   └── package.json
│
├── frontend/
│   ├── public/                     # Static assets & icons
│   ├── src/
│   │   ├── components/
│   │   │   ├── cart/               # Cart & checkout components
│   │   │   ├── layout/             # Header, Footer, Search, Loader
│   │   │   ├── order/              # Orders list & detail views
│   │   │   ├── user/               # Login, Register, Profile components
│   │   │   ├── Fooditem.jsx        # Individual dish card
│   │   │   ├── Home.jsx            # Restaurant listing & filters
│   │   │   ├── Menu.jsx            # Restaurant menu view
│   │   │   └── Restaurant.jsx      # Restaurant card with AI summary toggle
│   │   ├── redux/
│   │   │   ├── actions/            # Async thunks for API calls
│   │   │   ├── slices/             # Redux Toolkit state slices
│   │   │   └── store.js            # Redux store configuration
│   │   ├── utils/
│   │   │   └── api.js              # Centralized Axios instance
│   │   ├── App.jsx                 # Application routes
│   │   └── main.jsx                # React root mount
│   ├── vercel.json                 # Vercel SPA routing rewrites
│   ├── vite.config.js              # Vite configuration & dev proxy
│   └── package.json
│
└── README.md
```

---

## 🚀 Getting Started Locally

### Prerequisites
* [Node.js](https://nodejs.org/) (v18 or higher)
* [npm](https://www.npmjs.com/)
* A [MongoDB Atlas](https://www.mongodb.com/atlas) cluster
* A [Groq Cloud](https://console.groq.com) API Key
* A [Stripe](https://stripe.com) test account
* A [Cloudinary](https://cloudinary.com) account

---

### 1. Clone the Repository
```bash
git clone https://github.com/lostdreamer1379-lgtm/Foodiie.git
cd Foodiie
```

---

### 2. Backend Setup
1. Navigate to the backend directory and install dependencies:
   ```bash
   cd backend
   npm install
   ```

2. Create your environment configuration file at `backend/config/config.env`:
   ```env
   PORT=4000
   NODE_ENV=DEVELOPMENT

   # MongoDB
   DB_LOCAL_URI=mongodb+srv://<username>:<password>@cluster0.mongodb.net/?retryWrites=true&w=majority

   # JWT
   JWT_SECRET=your_jwt_secret_key
   JWT_EXPIRES_TIME=90
   JWT_EXPIRE=90d

   # Cloudinary
   CLOUDINARY_CLOUD_NAME=your_cloud_name
   CLOUDINARY_API_KEY=your_api_key
   CLOUDINARY_API_SECRET=your_api_secret

   # Email (Mailtrap/SMTP)
   EMAIL_USERNAME=your_smtp_username
   EMAIL_PASSWORD=your_smtp_password
   EMAIL_HOST=sandbox.smtp.mailtrap.io
   EMAIL_PORT=25
   EMAIL_FROM=noreply@foodiie.com

   # Stripe
   STRIPE_SECRET_KEY=sk_test_...
   STRIPE_API_KEY=pk_test_...

   # Groq AI
   GROQ_API_KEY=gsk_...

   # Frontend URL
   FRONTEND_URL=http://localhost:5173
   ```

3. Populate sample restaurants and menus into MongoDB:
   ```bash
   node utils/addMoreRestaurants.js
   ```

4. Start the backend development server:
   ```bash
   npm run dev
   ```
   *The server runs on `http://localhost:4000`.*

---

### 3. Frontend Setup
1. Open a new terminal and navigate to the frontend directory:
   ```bash
   cd frontend
   npm install
   ```

2. Create a `.env` file in `frontend/.env`:
   ```env
   VITE_API_URL=http://localhost:4000
   ```

3. Start the Vite development server:
   ```bash
   npm run dev
   ```
   *The application opens at `http://localhost:5173`.*

---

## 📡 Key API Endpoints

| Method | Endpoint | Description | Access |
| :--- | :--- | :--- | :--- |
| **GET** | `/api/v1/eats/stores` | Get all restaurants (supports search, sort, filters) | Public |
| **GET** | `/api/v1/eats/stores/:storeId/menus` | Get full menu & dishes for a restaurant | Public |
| **POST** | `/api/v1/users/signup` | Register new user account | Public |
| **POST** | `/api/v1/users/login` | Log in and receive HTTP-only JWT cookie | Public |
| **GET** | `/api/v1/users/me` | Fetch authenticated user profile | Private |
| **GET** | `/api/v1/eats/orders/me/myOrders` | Get order history of logged-in user | Private |
| **POST** | `/api/v1/payment/process` | Initiate Stripe checkout session | Private |
| **PUT** | `/api/v1/ai/admin/restaurants/:id/analyze` | Trigger Groq AI review sentiment analysis | Admin |
| **POST** | `/api/v1/ai/generate-food-ai` | Generate AI food descriptions & allergens | Admin |

---

## 🚢 Production Deployment

### Backend (Render)
* **Root Directory:** `backend`
* **Runtime:** `Node`
* **Build Command:** `npm install`
* **Start Command:** `node server.js`
* **Environment Variables:** Add all variables defined in `config.env`.

### Frontend (Vercel)
* **Framework Preset:** `Vite`
* **Root Directory:** `frontend`
* **Build Command:** `npm run build`
* **Output Directory:** `dist`
* **Environment Variables:**
  * `VITE_API_URL`: `https://foodiie-t2v0.onrender.com`
* **SPA Routing:** Managed automatically via `frontend/vercel.json`.

---

## 📄 License
This project is open-source and available under the [ISC License](LICENSE).

