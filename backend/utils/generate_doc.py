import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn

def set_cell_background(cell, fill_hex):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{fill_hex}"/>')
    tcPr.append(shd)

def set_cell_margins(cell, top=100, bottom=100, left=150, right=150):
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = OxmlElement('w:tcMar')
    for m, val in [('top', top), ('bottom', bottom), ('left', left), ('right', right)]:
        node = OxmlElement(f'w:{m}')
        node.set(qn('w:w'), str(val))
        node.set(qn('w:type'), 'dxa')
        tcMar.append(node)
    tcPr.append(tcMar)

def create_document():
    doc = docx.Document()

    # Set page margins (1 inch)
    sections = doc.sections
    for section in sections:
        section.top_margin = Inches(1.0)
        section.bottom_margin = Inches(1.0)
        section.left_margin = Inches(1.0)
        section.right_margin = Inches(1.0)

    PRIMARY_COLOR = RGBColor(230, 81, 0)     # Warm Orange / #E65100
    SECONDARY_COLOR = RGBColor(38, 50, 56)   # Slate Navy / #263238
    TEXT_COLOR = RGBColor(55, 71, 79)        # Charcoal / #37474F
    ACCENT_COLOR = RGBColor(2, 136, 209)     # Blue / #0288D1

    # Normal Style
    normal_style = doc.styles['Normal']
    normal_style.font.name = 'Calibri'
    normal_style.font.size = Pt(11)
    normal_style.font.color.rgb = TEXT_COLOR
    normal_style.paragraph_format.line_spacing = 1.15
    normal_style.paragraph_format.space_after = Pt(6)

    # -------------------------------------------------------------
    # COVER / HEADER TITLE
    # -------------------------------------------------------------
    title_p = doc.add_paragraph()
    title_p.paragraph_format.space_before = Pt(36)
    title_p.paragraph_format.space_after = Pt(4)
    title_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run_title = title_p.add_run("FOODIIE: FULL-STACK MERN FOOD DELIVERY PLATFORM")
    run_title.font.name = 'Arial'
    run_title.font.size = Pt(24)
    run_title.font.bold = True
    run_title.font.color.rgb = PRIMARY_COLOR

    subtitle_p = doc.add_paragraph()
    subtitle_p.paragraph_format.space_after = Pt(24)
    subtitle_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run_sub = subtitle_p.add_run("System Architecture, User Flowcharts, UI Wireframes & Technical Specification\nEnhanced with Groq Llama 3.1 AI Capabilities")
    run_sub.font.size = Pt(13)
    run_sub.font.color.rgb = SECONDARY_COLOR

    # Meta Table
    meta_table = doc.add_table(rows=5, cols=2)
    meta_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    meta_data = [
        ("Project Name", "Foodiie - MERN Food Ordering Platform"),
        ("Live Web Application", "https://foodiie-two.vercel.app"),
        ("Production API Backend", "https://foodiie-t2v0.onrender.com"),
        ("GitHub Repository", "https://github.com/lostdreamer1379-lgtm/Foodiie"),
        ("Author / Maintainer", "Aditya (LostDreamer)")
    ]
    for i, (k, v) in enumerate(meta_data):
        row = meta_table.rows[i]
        c0, c1 = row.cells[0], row.cells[1]
        c0.width = Inches(2.2)
        c1.width = Inches(4.3)
        c0.paragraphs[0].add_run(k).bold = True
        c0.paragraphs[0].runs[0].font.color.rgb = SECONDARY_COLOR
        c1.paragraphs[0].add_run(v)
        set_cell_background(c0, "F5F5F5")
        set_cell_background(c1, "FAFAFA")
        set_cell_margins(c0, 60, 60, 100, 100)
        set_cell_margins(c1, 60, 60, 100, 100)

    doc.add_page_break()

    # Helper function for Section Headings
    def add_h1(text):
        h = doc.add_paragraph()
        h.paragraph_format.space_before = Pt(18)
        h.paragraph_format.space_after = Pt(6)
        run = h.add_run(text)
        run.font.name = 'Arial'
        run.font.size = Pt(16)
        run.font.bold = True
        run.font.color.rgb = PRIMARY_COLOR
        return h

    def add_h2(text):
        h = doc.add_paragraph()
        h.paragraph_format.space_before = Pt(12)
        h.paragraph_format.space_after = Pt(4)
        run = h.add_run(text)
        run.font.name = 'Arial'
        run.font.size = Pt(13)
        run.font.bold = True
        run.font.color.rgb = SECONDARY_COLOR
        return h

    def add_code_block(code_text):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(4)
        p.paragraph_format.space_after = Pt(8)
        run = p.add_run(code_text)
        run.font.name = 'Consolas'
        run.font.size = Pt(9)
        run.font.color.rgb = RGBColor(33, 33, 33)
        return p

    # -------------------------------------------------------------
    # 1. PROJECT BRIEF & OBJECTIVES
    # -------------------------------------------------------------
    add_h1("1. Project Brief & Objectives")
    
    add_h2("1.1 Executive Summary & Purpose")
    doc.add_paragraph(
        "Foodiie is an end-to-end, full-stack food ordering platform designed to address the challenges "
        "faced by both local food businesses and modern consumers. The application bridges the gap between "
        "diners seeking rapid, transparent food discovery and culinary establishments requiring digital storefronts "
        "with dynamic menu structuring, review intelligence, and secured online billing."
    )
    doc.add_paragraph(
        "While conventional food delivery platforms feature heavy overhead and rigid interfaces, Foodiie delivers "
        "a lightweight, blazing-fast single page application (SPA) built on React 18 and Vite, coupled with an Express/Node.js "
        "backend and MongoDB Atlas cloud database. Crucially, Foodiie introduces Groq-powered Large Language Model (Llama 3.1) "
        "inference to extract instant sentiment summaries and trending culinary hashtags from customer reviews, as well as "
        "automated nutritional and allergen classification for cataloged dishes."
    )

    add_h2("1.2 Project Objectives")
    objectives = [
        ("Frictionless Discovery: ", "Provide multi-faceted restaurant filtering (pure-vegetarian toggles, keyword search, rating sort, and review volume sorting) with zero page reload latency."),
        ("Dynamic Menu Architecture: ", "Support hierarchical restaurant menus segmented into custom categories (Starters, Main Course, Pizzas, Desserts, Beverages) with item-level pricing, inventory tracking, and image galleries."),
        ("AI-Augmented Customer Intelligence: ", "Integrate Groq Cloud API (Llama 3.1 8B Instant) to process customer reviews into three actionable summary bullets, top hashtag mentions, and polarity sentiments (positive/negative/mixed)."),
        ("End-to-End E-Commerce Workflow: ", "Provide Redux-managed shopping cart sessions, synchronized item counters, Stripe Checkout integration for payment processing, and comprehensive order history logs."),
        ("Enterprise-Grade Cloud Deployment: ", "Deploy an optimized hybrid cloud topology featuring global edge CDN caching for the React client on Vercel and persistent, secure API containerization on Render.")
    ]
    for title, desc in objectives:
        p = doc.add_paragraph(style='List Bullet')
        r_title = p.add_run(title)
        r_title.bold = True
        r_title.font.color.rgb = SECONDARY_COLOR
        p.add_run(desc)

    add_h2("1.3 Core Functional Modules")
    modules_table = doc.add_table(rows=1, cols=3)
    modules_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    hdr = modules_table.rows[0].cells
    hdr[0].paragraphs[0].add_run("Module").bold = True
    hdr[1].paragraphs[0].add_run("Target Persona").bold = True
    hdr[2].paragraphs[0].add_run("Primary Capabilities").bold = True
    for c in hdr:
        set_cell_background(c, "E0E0E0")
        set_cell_margins(c, 80, 80, 100, 100)

    modules_data = [
        ("Authentication & Profile", "All Users", "JWT signup/login, HTTP-only cookie sessions, Cloudinary avatar management, password reset tokens via Nodemailer/SMTP."),
        ("Restaurant Discovery", "Customers", "Search by culinary name, Pure Veg filter, Rating sort (>4.5), Review count sort, interactive cards with live AI sentiment badges."),
        ("Interactive Menu & Cart", "Customers", "Accordion-style menu categories, real-time item counter, Redux-backed cart state, tax/delivery fee calculation, persistent storage."),
        ("Stripe Payment & Orders", "Customers", "Hosted Stripe checkout session, card authentication, webhook reconciliation, order history list, itemized order receipt."),
        ("Admin Menu Management", "Admins", "Direct UI creation of restaurant profiles, custom menu categories (+ Add Menu), food items with price and stock controls, delete capabilities."),
        ("AI Review & Dish Analysis", "Admins & Customers", "Llama 3.1 sentiment analyzer on customer feedback, automated allergen detection, serving size calculations, and meal timing tags.")
    ]
    for mod, persona, cap in modules_data:
        row = modules_table.add_row().cells
        row[0].paragraphs[0].add_run(mod).bold = True
        row[1].paragraphs[0].add_run(persona)
        row[2].paragraphs[0].add_run(cap)
        for c in row:
            set_cell_background(c, "FAFAFA")
            set_cell_margins(c, 60, 60, 80, 80)

    # -------------------------------------------------------------
    # 2. USER INTERACTION FLOWCHARTS
    # -------------------------------------------------------------
    add_h1("2. User Interaction Flowcharts")
    doc.add_paragraph(
        "User interactions within Foodiie follow structured, state-driven pathways ensuring predictability, "
        "data integrity, and responsive visual feedback at each transition point."
    )

    add_h2("2.1 Customer Food Ordering & Checkout Flowchart")
    ordering_flow = """[Customer Lands on Home Page (Vercel CDN)]
                   │
                   ▼
       [Apply Search / Veg-Only Filter / Sort]
                   │
                   ▼
      [Select Restaurant Card (e.g. KFC, Domino's)]
                   │
                   ▼
  [Load Menu via /api/v1/eats/stores/:id/menus] ◄─── (MongoDB Atlas Query)
                   │
                   ▼
     [View Categories: Starters, Mains, Desserts]
                   │
                   ▼
      [Click '+' to Add Items to Cart (Redux)]
                   │
                   ▼
      [Review Cart (Taxes, Delivery, Total)]
                   │
                   ▼
           Is User Authenticated?
          ├── No  ──► [Redirect to /users/login] ──► [Issue JWT Cookie]
          └── Yes ──► [Initiate Stripe Checkout Session]
                            │
                            ▼
                [Complete Payment on Stripe]
                            │
                            ▼
              [Render /success Order Receipt Page]
                            │
                            ▼
             [Persist Order to MongoDB Atlas]"""
    add_code_block(ordering_flow)

    add_h2("2.2 Admin Management & Groq AI Analysis Flowchart")
    admin_flow = """[Admin Logs In (role: "admin")]
                   │
                   ▼
        [Navigate to Target Restaurant]
                   │
                   ▼
     [Access Admin Controls: '+ Add Menu' & '+ item']
                   │
                   ▼
  [Input Category Name & Dish Details (Name, Price, Stock)]
                   │
                   ▼
     [Optional: Trigger Groq AI Dish Classification]
                   │
                   ▼
   [Groq API (Llama 3.1) Returns: Allergens, Servings, Tags]
                   │
                   ▼
 [Persist to 'fooditems' & Link to 'menus' in MongoDB Atlas]
                   │
                   ▼
     [Submit Customer Review / Feedback via API]
                   │
                   ▼
   [Trigger /api/v1/ai/admin/restaurants/:id/analyze]
                   │
                   ▼
 [Groq Analyzes Review Texts ──► Extracts Sentiments & Bullets]
                   │
                   ▼
  [Update Restaurant Document ──► Display Live AI Badge on UI]"""
    add_code_block(admin_flow)

    # -------------------------------------------------------------
    # 3. FRONT-END WIREFRAMES
    # -------------------------------------------------------------
    add_h1("3. Detailed Front-End Wireframes")
    doc.add_paragraph(
        "The Foodiie user interface was architected for mobile-first responsiveness, minimal cognitive load, "
        "and clear visual hierarchy using modern CSS grid layouts and card-based components."
    )

    add_h2("3.1 Wireframe 1: Home Page & Restaurant Catalog")
    wf1 = """┌────────────────────────────────────────────────────────────────────────┐
│ [Logo: Foodiie]    [ Search dishes, restaurants... 🔍 ]    [🛒 Cart (3)] [Profile 👤]│
├────────────────────────────────────────────────────────────────────────┤
│  Banner: "Delicious Food Delivered Hot to Your Doorstep"              │
│  [ Filter: Veg Only 🌿 ]    [ Sort By: Ratings ⭐ ]    [ Sort By: Reviews 💬 ] │
├────────────────────────────────────────────────────────────────────────┤
│  RESTAURANTS (14 Available)                                            │
│                                                                        │
│  ┌───────────────────────┐  ┌───────────────────────┐  ┌─────────────┐ │
│  │ [Restaurant Image]    │  │ [Restaurant Image]    │  │ [Image]     │ │
│  │ Domino's Pizza        │  │ Burger King           │  │ Saravanaa...│ │
│  │ Indiranagar, Bengaluru│  │ Koramangala           │  │ Church St   │ │
│  │ ⭐ 4.5 (128 reviews)  │  │ ⭐ 4.3 (94 reviews)   │  │ ⭐ 4.7 (210) │ │
│  │ [💬 View AI Summary]  │  │ [💬 View AI Summary]  │  │ [💬 View]   │ │
│  │ ┌───────────────────┐ │  └───────────────────────┘  └─────────────┘ │
│  │ │ 😊 Sentiment: Pos │ │                                             │
│  │ │ • Fast delivery   │ │                                             │
│  │ │ • Hot garlic bread│ │                                             │
│  │ │ #CheeseBurst #Lava│ │                                             │
│  │ └───────────────────┘ │                                             │
│  └───────────────────────┘                                             │
├────────────────────────────────────────────────────────────────────────┤
│ Footer: © 2026 Foodiie Delivery Inc. | Terms | Privacy | Help Support │
└────────────────────────────────────────────────────────────────────────┘"""
    add_code_block(wf1)

    add_h2("3.2 Wireframe 2: Restaurant Menu & Food Items View")
    wf2 = """┌────────────────────────────────────────────────────────────────────────┐
│ [Logo: Foodiie]                           [ Search... ]   [🛒 Cart (3)] [👤]│
├────────────────────────────────────────────────────────────────────────┤
│ ◄ Back to Restaurants                                                  │
│ Domino's Pizza  -  ⭐ 4.5 (128 Reviews)  -  Indiranagar, Bengaluru     │
│ [ + Add Menu (Admin Only) ]                                            │
├────────────────────────────────────────────────────────────────────────┤
│ CATEGORY: Signature Pizzas                                             │
│ ────────────────────────────────────────────────────────────────────── │
│ ┌──────────────────────────────────┐ ┌───────────────────────────────┐ │
│ │ [Image] Peppy Paneer Pizza       │ │ [Image] Non-Veg Supreme Pizza │ │
│ │ Chunky paneer cubes, capsicum,   │ │ Black olives, BBQ chicken,    │ │
│ │ and spicy red paprika burst.     │ │ mushrooms & peri-peri sauce.  │ │
│ │ Price: ₹459      Stock: In Stock │ │ Price: ₹579   Stock: In Stock │ │
│ │ [ - ]  1  [ + ]   [ Add to Cart] │ │ [ - ]  0  [ + ] [ Add to Cart]│ │
│ └──────────────────────────────────┘ └───────────────────────────────┘ │
│                                                                        │
│ CATEGORY: Sides & Pasta                                                │
│ ────────────────────────────────────────────────────────────────────── │
│ ┌──────────────────────────────────┐ ┌───────────────────────────────┐ │
│ │ [Image] Stuffed Garlic Bread     │ │ [Image] Creamy Tomato Pasta   │ │
│ │ Baked breadsticks with cheese.   │ │ Penne in Italian mixed sauce. │ │
│ │ Price: ₹179      [ Add to Cart ] │ │ Price: ₹219   [ Add to Cart ] │ │
│ └──────────────────────────────────┘ └───────────────────────────────┘ │
└────────────────────────────────────────────────────────────────────────┘"""
    add_code_block(wf2)

    add_h2("3.3 Wireframe 3: Cart & Checkout Overview")
    wf3 = """┌────────────────────────────────────────────────────────────────────────┐
│ [Logo: Foodiie]                           [ Search... ]   [🛒 Cart (2)] [👤]│
├────────────────────────────────────────────────────────────────────────┤
│ YOUR SHOPPING CART                                                     │
│                                                                        │
│ Item Name              Unit Price    Quantity      Subtotal     Action │
│ ────────────────────────────────────────────────────────────────────── │
│ Peppy Paneer Pizza     ₹459           [ - ] 1 [ + ]   ₹459      [🗑️]   │
│ Stuffed Garlic Bread   ₹179           [ - ] 2 [ + ]   ₹358      [🗑️]   │
│ ────────────────────────────────────────────────────────────────────── │
│                                                                        │
│                           ORDER SUMMARY                                │
│                           ───────────────────────────                  │
│                           Items Subtotal:       ₹817                   │
│                           Delivery Fee:          ₹40                   │
│                           Taxes (GST 5%):        ₹41                   │
│                           ───────────────────────────                  │
│                           Grand Total:          ₹898                   │
│                                                                        │
│                           [ 💳 Proceed to Stripe Checkout ]           │
└────────────────────────────────────────────────────────────────────────┘"""
    add_code_block(wf3)

    # -------------------------------------------------------------
    # 4. TECHNICAL ARCHITECTURE & COMPONENT INTERACTION
    # -------------------------------------------------------------
    add_h1("4. Technical Architecture Diagram")
    doc.add_paragraph(
        "Foodiie is architectured as a decoupled 3-Tier Web Application deployed across specialized "
        "cloud infrastructure providers for maximum scalability, security, and response speeds."
    )

    arch_diagram = """+-------------------------------------------------------------------------+
|                         CLIENT LAYER (Vercel CDN)                       |
|                                                                         |
|  +-------------------+   +--------------------+   +------------------+  |
|  | React 18 SPA (Vite)|   | Redux Toolkit Store|   | React Router v7  |  |
|  | - Home & Menus    |   | - cartSlice        |   | - /eats/stores   |  |
|  | - Cart & Orders   |   | - restaurantSlice  |   | - /cart, /login  |  |
|  | - AI Insights Box |   | - userSlice        |   | - vercel.json    |  |
|  +-------------------+   +--------------------+   +------------------+  |
+-------------------------------------------------------------------------+
                                    │  HTTPS / CORS Credentials
                                    ▼
+-------------------------------------------------------------------------+
|                        API GATEWAY (Render Container)                   |
|                                                                         |
|  Express.js Server (Node.js runtime on Port 4000/10000)                |
|  ├── CORS Middleware (Allowing foodiie-two.vercel.app & withCredentials)|
|  ├── Cookie Parser (HTTP-Only JWT Token Extraction)                     |
|  ├── Express FileUpload / Multer                                        |
|  └── Centralized Error Handling Middleware (catchAsyncErrors)           |
+-------------------------------------------------------------------------+
                                    │
           ┌────────────────────────┼────────────────────────┐
           ▼                        ▼                        ▼
+---------------------+  +---------------------+  +---------------------+
|   DATABASE LAYER    |  |     AI ENGINE       |  |  EXTERNAL SERVICES  |
|                     |  |                     |  |                     |
| MongoDB Atlas Cloud |  |   Groq Cloud API    |  | Stripe Payment API  |
| - users             |  | - Llama 3.1 8B      |  | - Checkout Sessions |
| - restaurants       |  | - Review Sentiment  |  |                     |
| - menus             |  | - Bullet Summaries  |  | Cloudinary Storage  |
| - fooditems         |  | - Dish Allergen Tag |  | - User/Food Media   |
| - orders            |  +---------------------+  |                     |
| - carts             |                           | Mailtrap / SMTP     |
+---------------------+                           | - Password Reset    |
                                                  +---------------------+"""
    add_code_block(arch_diagram)

    add_h2("4.1 Component Interaction Sequence")
    seq_diagram = """Client (React/Redux)       Express API (Render)     Groq AI Cloud     MongoDB Atlas
        │                          │                      │                 │
        │─── 1. GET /stores ──────►│                      │                 │
        │                          │─── 2. Restaurant.find() ──────────────►│
        │                          │◄── 3. Return 14 Documents ─────────────│
        │◄── 4. JSON Array ────────│                      │                 │
        │                          │                      │                 │
        │─── 5. View Review AI ───►│                      │                 │
        │                          │─── 6. Prompt (Reviews) ──►             │
        │                          │◄── 7. Sentiment & Bullets ─┘           │
        │                          │─── 8. Cache in Doc ───────────────────►│
        │◄── 9. Return AI Data ────│                      │                 │
        │                          │                      │                 │
        │─── 10. POST /order ─────►│                      │                 │
        │                          │─── 11. Create Stripe Session ──►(Stripe)
        │◄── 12. Checkout URL ─────│                                        │"""
    add_code_block(seq_diagram)

    # -------------------------------------------------------------
    # 5. DATABASE SCHEMA & RELATIONSHIPS
    # -------------------------------------------------------------
    add_h1("5. Database Schema & Data Dictionary")
    doc.add_paragraph(
        "The persistence layer is modeled using MongoDB and Mongoose, striking an optimal balance between "
        "normalization (for entity independence like Users and Restaurants) and hierarchical embedding "
        "(for Menu categories and review subdocuments)."
    )

    add_h2("5.1 Entity-Relationship (ER) Overview")
    erd = """┌────────────────────────┐         1:N         ┌────────────────────────┐
│         USER           │────────────────────►│         ORDER          │
├────────────────────────┤                     ├────────────────────────┤
│ _id (PK)               │                     │ _id (PK)               │
│ name: String           │                     │ user (FK -> User)      │
│ email: String (Unique) │                     │ orderItems: Array      │
│ password: Hash         │                     │ paymentInfo: Object    │
│ role: 'user' | 'admin' │                     │ totalPrice: Number     │
│ avatar: Object         │                     │ orderStatus: String    │
└────────────────────────┘                     └────────────────────────┘
            │                                              ▲
            │ 1:1                                          │ 1:N
            ▼                                              │
┌────────────────────────┐                                 │
│         CART           │                                 │
├────────────────────────┤                                 │
│ _id (PK)               │                                 │
│ user (FK -> User)      │                                 │
│ items: [{ foodItem }]  │                                 │
└────────────────────────┘                                 │
                                                           │
┌────────────────────────┐         1:1         ┌───────────┴────────────┐
│       RESTAURANT       │────────────────────►│          MENU          │
├────────────────────────┤                     ├────────────────────────┤
│ _id (PK)               │                     │ _id (PK)               │
│ name: String           │                     │ restaurant (FK)        │
│ isVeg: Boolean         │                     │ menu: [                │
│ address: String        │                     │   category: String,    │
│ location: GeoJSON      │                     │   items: [FK->FoodItem]│
│ ratings: Number        │                     │ ]                      │
│ reviews: [Subdocument] │                     └────────────────────────┘
│ reviewSentiment: String│                                 ▲
│ reviewSummaryBullets:[]│                                 │ 1:N
│ images: [{url}]        │                                 │
└────────────────────────┘                     ┌───────────┴────────────┐
            │                                  │        FOODITEM        │
            │ 1:N                              ├────────────────────────┤
            └─────────────────────────────────►│ _id (PK)               │
                                               │ restaurant (FK)        │
                                               │ name: String           │
                                               │ price: Number          │
                                               │ stock: Number          │
                                               │ images: [{url}]        │
                                               │ aiDescription: String  │
                                               │ aiAllergens: [String]  │
                                               └────────────────────────┘"""
    add_code_block(erd)

    add_h2("5.2 Data Dictionary")
    schema_table = doc.add_table(rows=1, cols=4)
    schema_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    s_hdr = schema_table.rows[0].cells
    s_hdr[0].paragraphs[0].add_run("Collection").bold = True
    s_hdr[1].paragraphs[0].add_run("Field Name").bold = True
    s_hdr[2].paragraphs[0].add_run("Data Type").bold = True
    s_hdr[3].paragraphs[0].add_run("Constraints / Description").bold = True
    for c in s_hdr:
        set_cell_background(c, "E0E0E0")
        set_cell_margins(c, 80, 80, 100, 100)

    schema_data = [
        ("User", "email", "String", "Unique, Required, Lowercase, Validator email format"),
        ("User", "password", "String", "Min 6 chars, select: false, Bcrypt hashed (cost 12)"),
        ("User", "role", "String", "Enum: ['user', 'restaurant-owner', 'admin'], default: 'user'"),
        ("Restaurant", "name", "String", "Required, Trimmed, Max 100 chars"),
        ("Restaurant", "location", "Object", "GeoJSON Point { type: 'Point', coordinates: [lng, lat] }, 2dsphere index"),
        ("Restaurant", "reviewSentiment", "String", "Enum: ['positive', 'negative', 'mixed'], generated by Groq Llama 3.1"),
        ("Menu", "restaurant", "ObjectId", "Ref: 'Restaurant', Required, 1-to-1 association"),
        ("Menu", "menu.$.items", "Array[ObjectId]", "Ref: 'FoodItem', dynamic category grouping"),
        ("FoodItem", "price", "Number", "Required, Float, represents currency in INR (₹)"),
        ("FoodItem", "aiAllergens", "Array[String]", "Extracted via Groq AI classification (e.g. Dairy, Gluten)"),
        ("Order", "totalPrice", "Number", "Calculated grand total including GST (5%) & delivery charge")
    ]
    for coll, fld, typ, desc in schema_data:
        row = schema_table.add_row().cells
        row[0].paragraphs[0].add_run(coll).bold = True
        row[1].paragraphs[0].add_run(fld)
        row[2].paragraphs[0].add_run(typ)
        row[3].paragraphs[0].add_run(desc)
        for c in row:
            set_cell_background(c, "FAFAFA")
            set_cell_margins(c, 60, 60, 80, 80)

    # -------------------------------------------------------------
    # 6. SERVER-SIDE OPERATIONS & API SPECIFICATION
    # -------------------------------------------------------------
    add_h1("6. Server-Side Operations & API Catalog")
    doc.add_paragraph(
        "All incoming HTTP requests pass through security gates and custom controller layers before touching "
        "the database. Asynchronous operations are wrapped in catchAsyncErrors handlers to eliminate uncaught promise "
        "rejections and standardize JSON error responses."
    )

    api_table = doc.add_table(rows=1, cols=4)
    api_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    a_hdr = api_table.rows[0].cells
    a_hdr[0].paragraphs[0].add_run("Method & Route").bold = True
    a_hdr[1].paragraphs[0].add_run("Access").bold = True
    a_hdr[2].paragraphs[0].add_run("Controller Operation").bold = True
    a_hdr[3].paragraphs[0].add_run("Key Request / Response Payload").bold = True
    for c in a_hdr:
        set_cell_background(c, "E0E0E0")
        set_cell_margins(c, 80, 80, 100, 100)

    api_endpoints = [
        ("GET /api/v1/eats/stores", "Public", "getAllRestaurants", "Params: keyword, sort. Returns: { count, restaurants: [] }"),
        ("GET /api/v1/eats/stores/:id/menus", "Public", "getAllMenus", "Populates menu.items. Returns: { data: [ { category, items } ] }"),
        ("POST /api/v1/users/signup", "Public", "signup", "Body: { name, email, password, phoneNumber, avatar }. Sets JWT cookie."),
        ("POST /api/v1/users/login", "Public", "login", "Body: { email, password }. Returns user doc and sets HTTP-only cookie."),
        ("GET /api/v1/users/me", "Private", "getUserProfile", "Reads req.cookies.jwt or Bearer token. Returns logged-in profile."),
        ("POST /api/v1/payment/process", "Private", "processPayment", "Body: { items: [] }. Creates and returns Stripe Checkout URL."),
        ("PUT /api/v1/ai/admin/restaurants/:id/analyze", "Admin", "analyzeRestaurantReviews", "Sends reviews to Groq. Returns { sentiment, summaryBullets, topMentions }."),
        ("POST /api/v1/ai/generate-food-ai", "Admin", "generateFoodAI", "Body: { name, category, spiceLevel, price }. Returns dish metadata.")
    ]
    for mth, acc, ctrl, pl in api_endpoints:
        row = api_table.add_row().cells
        row[0].paragraphs[0].add_run(mth).bold = True
        row[1].paragraphs[0].add_run(acc)
        row[2].paragraphs[0].add_run(ctrl)
        row[3].paragraphs[0].add_run(pl)
        for c in row:
            set_cell_background(c, "FAFAFA")
            set_cell_margins(c, 60, 60, 80, 80)

    # -------------------------------------------------------------
    # 7. DESIGN RATIONALE & JUSTIFICATION
    # -------------------------------------------------------------
    add_h1("7. Design Decisions & Architectural Rationale")
    
    decisions = [
        ("MERN Stack Architecture: ", 
         "JavaScript across both client and server promotes code reuse (such as shared validation logic and data models) "
         "and minimizes context switching. Node.js's non-blocking asynchronous event loop effortlessly handles thousands "
         "of simultaneous client connections for live order tracking."),
        
        ("Vite over Create-React-App (CRA): ", 
         "CRA is deprecated and uses sluggish Webpack bundling. Vite utilizes native ES modules (ESM) in development "
         "and lightning-fast Rollup builds for production, cutting production build times from minutes to under 4 seconds."),
        
        ("Redux Toolkit for State Management: ", 
         "A food ordering application requires synchronized state across isolated components—the cart icon in the header, "
         "the add-to-cart buttons on dish cards, and the checkout summary page all require consistent access to cart totals. "
         "Redux Toolkit provides predictable slice-based state mutations without prop drilling."),
        
        ("Groq Cloud (Llama 3.1 8B Instant) Integration: ", 
         "Traditional LLM endpoints (like GPT-4) exhibit response times of 3 to 6 seconds, making live UI toggles sluggish. "
         "Groq's Language Processing Unit (LPU) architecture yields inference speeds exceeding 300 tokens/second at negligible "
         "token cost, enabling instant rendering of review summaries and tags on restaurant cards."),
        
        ("Decoupled Hybrid Cloud Deployment (Vercel + Render): ", 
         "Vercel's global Edge CDN is purpose-built for ultra-low latency delivery of static assets and client-side routing (configured via vercel.json). "
         "In contrast, long-running Node.js APIs requiring persistent MongoDB connection pooling and cookie transactions run best on dedicated container services like Render."),
        
        ("Cross-Domain Cookie Security: ", 
         "Because the client (https://foodiie-two.vercel.app) and server (https://foodiie-t2v0.onrender.com) reside on different domains, "
         "authentication cookies must enforce 'SameSite=None' and 'Secure=true' in production. This prevents Cross-Site Scripting (XSS) "
         "theft of tokens while satisfying modern browser cross-origin cookie policies.")
    ]
    for title, desc in decisions:
        p = doc.add_paragraph(style='List Bullet')
        r = p.add_run(title)
        r.bold = True
        r.font.color.rgb = SECONDARY_COLOR
        p.add_run(desc)

    # -------------------------------------------------------------
    # 8. CONCLUSION & FUTURE ROADMAP
    # -------------------------------------------------------------
    add_h1("8. Conclusion & Future Roadmap")
    doc.add_paragraph(
        "Foodiie successfully demonstrates the practical implementation of modern software engineering methodologies, "
        "robust 3-tier cloud architecture, and real-world generative AI integration. By prioritizing clean separation of concerns, "
        "bulletproof error handling, and intuitive user experiences, the platform provides a production-ready template for scalable "
        "e-commerce systems."
    )
    doc.add_paragraph(
        "Future planned enhancements include WebSockets/Socket.io integration for live delivery driver GPS tracking, "
        "personalized AI dish recommendations based on ordering patterns, and PWA (Progressive Web App) offline caching capabilities."
    )

    doc.save("Foodiie_Project_Documentation.docx")
    print("Successfully generated Foodiie_Project_Documentation.docx")

if __name__ == '__main__':
    create_document()

