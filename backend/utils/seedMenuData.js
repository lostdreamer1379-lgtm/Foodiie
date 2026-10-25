const mongoose = require("mongoose");
const dotenv = require("dotenv");
const path = require("path");

dotenv.config({ path: path.join(__dirname, "../config/config.env") });

const Restaurant = require("../models/restaurant");
const FoodItem = require("../models/foodItem");
const Menu = require("../models/menu");

const sampleCategories = [
  {
    category: "Starters & Appetizers",
    items: [
      {
        name: "Paneer Tikka",
        price: 249,
        description: "Tender cottage cheese cubes marinated in tandoori spices and grilled to perfection.",
        stock: 50,
        images: [
          {
            public_id: "starter_1",
            url: "https://images.unsplash.com/photo-1599488615731-7e5c2823ff28?w=500&auto=format&fit=crop&q=60",
          },
        ],
      },
      {
        name: "Crispy Spring Rolls",
        price: 189,
        description: "Golden fried rolls stuffed with crunchy garden vegetables served with sweet chili dip.",
        stock: 40,
        images: [
          {
            public_id: "starter_2",
            url: "https://images.unsplash.com/photo-1548507200-d8a43697eb2f?w=500&auto=format&fit=crop&q=60",
          },
        ],
      },
      {
        name: "Crispy Chicken Wings",
        price: 299,
        description: "Succulent chicken wings tossed in spicy smoked BBQ sauce.",
        stock: 35,
        images: [
          {
            public_id: "starter_3",
            url: "https://images.unsplash.com/photo-1567620832903-9fc6debc209f?w=500&auto=format&fit=crop&q=60",
          },
        ],
      },
      {
        name: "Garlic Butter Bread",
        price: 149,
        description: "Toasted baguette topped with garlic herb butter and melted mozzarella.",
        stock: 60,
        images: [
          {
            public_id: "starter_4",
            url: "https://images.unsplash.com/photo-1619895092538-128341789043?w=500&auto=format&fit=crop&q=60",
          },
        ],
      },
    ],
  },
  {
    category: "Main Course",
    items: [
      {
        name: "Butter Chicken",
        price: 369,
        description: "Boneless chicken simmered in a rich, buttery, spiced tomato gravy.",
        stock: 45,
        images: [
          {
            public_id: "main_1",
            url: "https://images.unsplash.com/photo-1603894584373-5ac82b2ae398?w=500&auto=format&fit=crop&q=60",
          },
        ],
      },
      {
        name: "Paneer Butter Masala",
        price: 289,
        description: "Soft paneer cubes simmered in a luscious creamy cashew-tomato curry.",
        stock: 50,
        images: [
          {
            public_id: "main_2",
            url: "https://images.unsplash.com/photo-1631452180519-c014fe946bc7?w=500&auto=format&fit=crop&q=60",
          },
        ],
      },
      {
        name: "Hyderabadi Chicken Biryani",
        price: 329,
        description: "Aromatic basmati rice cooked with marinated chicken and traditional spices.",
        stock: 60,
        images: [
          {
            public_id: "main_3",
            url: "https://images.unsplash.com/photo-1563379091339-03b21ab4a4f8?w=500&auto=format&fit=crop&q=60",
          },
        ],
      },
      {
        name: "Dal Makhani",
        price: 239,
        description: "Slow-cooked black lentils simmered overnight with cream and clarified butter.",
        stock: 40,
        images: [
          {
            public_id: "main_4",
            url: "https://images.unsplash.com/photo-1546833999-b9f581a1996d?w=500&auto=format&fit=crop&q=60",
          },
        ],
      },
    ],
  },
  {
    category: "Pizzas & Burgers",
    items: [
      {
        name: "Classic Margherita Pizza",
        price: 319,
        description: "Italian plum tomatoes, fresh mozzarella, and aromatic basil on hand-stretched dough.",
        stock: 30,
        images: [
          {
            public_id: "pizza_1",
            url: "https://images.unsplash.com/photo-1604382355076-af4b0eb60143?w=500&auto=format&fit=crop&q=60",
          },
        ],
      },
      {
        name: "Farmhouse Veggie Pizza",
        price: 379,
        description: "Loaded with bell peppers, sweet corn, black olives, red onions, and mozzarella.",
        stock: 25,
        images: [
          {
            public_id: "pizza_2",
            url: "https://images.unsplash.com/photo-1513104890138-7c749659a591?w=500&auto=format&fit=crop&q=60",
          },
        ],
      },
      {
        name: "Double Cheese Chicken Burger",
        price: 249,
        description: "Crispy fried chicken breast, melted cheddar, lettuce, pickles, and secret house sauce.",
        stock: 35,
        images: [
          {
            public_id: "burger_1",
            url: "https://images.unsplash.com/photo-1568901346375-23c9450c58cd?w=500&auto=format&fit=crop&q=60",
          },
        ],
      },
    ],
  },
  {
    category: "Desserts & Drinks",
    items: [
      {
        name: "Molten Choco Lava Cake",
        price: 159,
        description: "Warm chocolate sponge cake with a rich liquid chocolate center.",
        stock: 40,
        images: [
          {
            public_id: "dessert_1",
            url: "https://images.unsplash.com/photo-1606313564200-e75d5e30476c?w=500&auto=format&fit=crop&q=60",
          },
        ],
      },
      {
        name: "Classic Cold Coffee",
        price: 129,
        description: "Rich blended espresso with cold milk and a scoop of vanilla ice cream.",
        stock: 50,
        images: [
          {
            public_id: "drink_1",
            url: "https://images.unsplash.com/photo-1517701550927-30cf4ba1dba5?w=500&auto=format&fit=crop&q=60",
          },
        ],
      },
      {
        name: "Fresh Mint Mojito",
        price: 139,
        description: "Zesty lime, fresh crushed mint leaves, cane sugar, and sparkling soda.",
        stock: 50,
        images: [
          {
            public_id: "drink_2",
            url: "https://images.unsplash.com/photo-1551024709-8f23befc6f87?w=500&auto=format&fit=crop&q=60",
          },
        ],
      },
    ],
  },
];

async function seedMenus() {
  try {
    console.log("Connecting to MongoDB Atlas...");
    await mongoose.connect(process.env.DB_LOCAL_URI);
    console.log("Connected successfully!");

    const restaurants = await Restaurant.find();
    console.log(`Found ${restaurants.length} restaurants in the database.`);

    if (restaurants.length === 0) {
      console.log("No restaurants found to seed menus for.");
      process.exit(0);
    }

    for (const restaurant of restaurants) {
      // Check if menu already exists
      const existingMenu = await Menu.findOne({ restaurant: restaurant._id });
      if (existingMenu && existingMenu.menu.length > 0) {
        console.log(`Restaurant '${restaurant.name}' already has a menu. Skipping.`);
        continue;
      }

      console.log(`Seeding menu for restaurant: ${restaurant.name} (${restaurant._id})`);

      const menuCategories = [];

      for (const cat of sampleCategories) {
        const itemIds = [];

        for (const item of cat.items) {
          const foodItem = await FoodItem.create({
            name: item.name,
            price: item.price,
            description: item.description,
            stock: item.stock,
            images: item.images,
            restaurant: restaurant._id,
            ratings: (Math.random() * 1.5 + 3.5).toFixed(1),
            numOfReviews: Math.floor(Math.random() * 50) + 5,
          });

          itemIds.push(foodItem._id);
        }

        menuCategories.push({
          category: cat.category,
          items: itemIds,
        });
      }

      if (existingMenu) {
        existingMenu.menu = menuCategories;
        await existingMenu.save();
      } else {
        await Menu.create({
          restaurant: restaurant._id,
          menu: menuCategories,
        });
      }

      console.log(`✅ Successfully created menu for: ${restaurant.name}`);
    }

    console.log("\n🎉 All restaurants have been populated with menus and food items!");
    process.exit(0);
  } catch (error) {
    console.error("❌ Error seeding menu data:", error);
    process.exit(1);
  }
}

seedMenus();

