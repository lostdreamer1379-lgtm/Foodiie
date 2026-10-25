const mongoose = require("mongoose");
const dotenv = require("dotenv");
const path = require("path");

dotenv.config({ path: path.join(__dirname, "../config/config.env") });

const Restaurant = require("../models/restaurant");
const FoodItem = require("../models/foodItem");
const Menu = require("../models/menu");

const newRestaurantsData = [
  {
    restaurant: {
      name: "Domino's Pizza",
      isVeg: false,
      address: "Shop 12, Ground Floor, Indiranagar 100ft Road, Bengaluru",
      ratings: 4.5,
      numOfReviews: 128,
      location: {
        type: "Point",
        coordinates: [77.6412, 12.9784],
      },
      reviewSentiment: "positive",
      reviewSummaryBullets: [
        "Fast 30-minute delivery and piping hot crusts",
        "Cheesy garlic bread and choco lava cake are crowd favorites",
        "Generous toppings and soft crust",
      ],
      reviewTopMentions: ["CheeseBurst", "GarlicBread", "ChocoLava", "FastDelivery"],
      images: [
        {
          public_id: "dominos_main",
          url: "https://images.unsplash.com/photo-1534308983496-4fabb1a015ee?w=700&auto=format&fit=crop&q=80",
        },
      ],
    },
    menuCategories: [
      {
        category: "Signature Pizzas",
        items: [
          {
            name: "Peppy Paneer Pizza",
            price: 459,
            description: "Chunky paneer cubes, crisp capsicum, and spicy red paprika with cheese burst.",
            stock: 40,
            images: [
              {
                public_id: "dom_1",
                url: "https://images.unsplash.com/photo-1565299624946-b28f40a0ae38?w=500&auto=format&fit=crop&q=70",
              },
            ],
          },
          {
            name: "Non-Veg Supreme Pizza",
            price: 579,
            description: "Loaded with black olives, grilled mushrooms, BBQ chicken, and peri-peri chicken.",
            stock: 35,
            images: [
              {
                public_id: "dom_2",
                url: "https://images.unsplash.com/photo-1628840042765-356cda07504e?w=500&auto=format&fit=crop&q=70",
              },
            ],
          },
          {
            name: "Indi Chicken Tikka Pizza",
            price: 529,
            description: "Tandoori chicken tikka slices with red paprika and mint mayo swirl.",
            stock: 30,
            images: [
              {
                public_id: "dom_3",
                url: "https://images.unsplash.com/photo-1513104890138-7c749659a591?w=500&auto=format&fit=crop&q=70",
              },
            ],
          },
        ],
      },
      {
        category: "Sides & Pasta",
        items: [
          {
            name: "Stuffed Garlic Bread",
            price: 179,
            description: "Freshly baked breadsticks stuffed with molten cheese, sweet corn, and jalapenos.",
            stock: 60,
            images: [
              {
                public_id: "dom_4",
                url: "https://images.unsplash.com/photo-1619895092538-128341789043?w=500&auto=format&fit=crop&q=70",
              },
            ],
          },
          {
            name: "Creamy Tomato Pasta Italiano",
            price: 219,
            description: "Penne pasta cooked in mixed red-and-white sauce with Italian seasoning.",
            stock: 25,
            images: [
              {
                public_id: "dom_5",
                url: "https://images.unsplash.com/photo-1551183053-bf91a1d81141?w=500&auto=format&fit=crop&q=70",
              },
            ],
          },
        ],
      },
      {
        category: "Desserts & Shakes",
        items: [
          {
            name: "Butterscotch Mousse Cake",
            price: 139,
            description: "Fluffy sponge cake with dark chocolate layers and crunchy butterscotch gems.",
            stock: 45,
            images: [
              {
                public_id: "dom_6",
                url: "https://images.unsplash.com/photo-1578985545062-69928b1d9587?w=500&auto=format&fit=crop&q=70",
              },
            ],
          },
        ],
      },
    ],
  },
  {
    restaurant: {
      name: "Burger King",
      isVeg: false,
      address: "Forum Mall, Hosur Road, Koramangala, Bengaluru",
      ratings: 4.3,
      numOfReviews: 94,
      location: {
        type: "Point",
        coordinates: [77.6148, 12.9352],
      },
      reviewSentiment: "positive",
      reviewSummaryBullets: [
        "Flame-grilled whopper patties have unmatched smokiness",
        "Value for money combos and crunchy fries",
        "Crispy chicken burger is fresh and filling",
      ],
      reviewTopMentions: ["Whopper", "FlameGrilled", "PeriPeriFries", "ValueMeal"],
      images: [
        {
          public_id: "bk_main",
          url: "https://images.unsplash.com/photo-1550547660-d9450f859349?w=700&auto=format&fit=crop&q=80",
        },
      ],
    },
    menuCategories: [
      {
        category: "Flame-Grilled Burgers",
        items: [
          {
            name: "Chicken Whopper",
            price: 239,
            description: "Signature flame-grilled chicken patty with sesame bun, fresh lettuce, mayo, and pickles.",
            stock: 50,
            images: [
              {
                public_id: "bk_1",
                url: "https://images.unsplash.com/photo-1568901346375-23c9450c58cd?w=500&auto=format&fit=crop&q=70",
              },
            ],
          },
          {
            name: "Veg Whopper with Cheese",
            price: 199,
            description: "Crispy plant-based patty with molten cheddar slice, crisp onions, and creamy mayo.",
            stock: 45,
            images: [
              {
                public_id: "bk_2",
                url: "https://images.unsplash.com/photo-1586190848861-99aa4a171e90?w=500&auto=format&fit=crop&q=70",
              },
            ],
          },
          {
            name: "Fiery Chicken Burger",
            price: 269,
            description: "Spicy fried chicken fillet dipped in hot ghost pepper sauce.",
            stock: 35,
            images: [
              {
                public_id: "bk_3",
                url: "https://images.unsplash.com/photo-1550547660-d9450f859349?w=500&auto=format&fit=crop&q=70",
              },
            ],
          },
        ],
      },
      {
        category: "Sides & Shakes",
        items: [
          {
            name: "King Fries with Peri-Peri",
            price: 129,
            description: "Extra thick crinkle-cut fries sprinkled with African peri-peri herb mix.",
            stock: 80,
            images: [
              {
                public_id: "bk_4",
                url: "https://images.unsplash.com/photo-1576107232684-1279f3908594?w=500&auto=format&fit=crop&q=70",
              },
            ],
          },
          {
            name: "Chocolate Thick Shake",
            price: 169,
            description: "Dense, creamy milkshake blended with Hershey's rich cocoa.",
            stock: 40,
            images: [
              {
                public_id: "bk_5",
                url: "https://images.unsplash.com/photo-1572490122747-3968b75cc699?w=500&auto=format&fit=crop&q=70",
              },
            ],
          },
        ],
      },
    ],
  },
  {
    restaurant: {
      name: "Saravanaa Bhavan",
      isVeg: true,
      address: "15, Church Street, Ashok Nagar, Bengaluru",
      ratings: 4.7,
      numOfReviews: 210,
      location: {
        type: "Point",
        coordinates: [77.6012, 12.9754],
      },
      reviewSentiment: "positive",
      reviewSummaryBullets: [
        "Pure vegetarian traditional South Indian delicacies",
        "Crispy Ghee Podi Dosa with 3 varieties of chutneys and sambar",
        "Filter coffee is unmissable and authentic",
      ],
      reviewTopMentions: ["GheeRoast", "FilterCoffee", "CrispyVada", "PureVeg"],
      images: [
        {
          public_id: "sb_main",
          url: "https://images.unsplash.com/photo-1610192244261-3f33de3f55e4?w=700&auto=format&fit=crop&q=80",
        },
      ],
    },
    menuCategories: [
      {
        category: "South Indian Tiffins",
        items: [
          {
            name: "Ghee Masala Dosa",
            price: 159,
            description: "Crispy golden crepe roasted in pure cow ghee, stuffed with seasoned potato masala.",
            stock: 60,
            images: [
              {
                public_id: "sb_1",
                url: "https://images.unsplash.com/photo-1668236543090-82eba5ee5976?w=500&auto=format&fit=crop&q=70",
              },
            ],
          },
          {
            name: "Steamed Idli & Crispy Medu Vada (Combo)",
            price: 119,
            description: "Two melt-in-mouth fluffy rice idlis and one crunchy lentil donut served with piping hot sambar.",
            stock: 80,
            images: [
              {
                public_id: "sb_2",
                url: "https://images.unsplash.com/photo-1589301760014-d929f3979dbc?w=500&auto=format&fit=crop&q=70",
              },
            ],
          },
          {
            name: "Rava Onion Dosa",
            price: 169,
            description: "Semolina crepe garnished with green chilies, ginger, roasted cumin, and chopped onions.",
            stock: 40,
            images: [
              {
                public_id: "sb_3",
                url: "https://images.unsplash.com/photo-1668236543090-82eba5ee5976?w=500&auto=format&fit=crop&q=70",
              },
            ],
          },
        ],
      },
      {
        category: "Traditional Meals & Beverages",
        items: [
          {
            name: "South Indian Special Thali",
            price: 269,
            description: "Rice, Poori, Sambar, Rasam, Kootu, Poriyal, Curd, Appalam, and Sweet Payasam.",
            stock: 50,
            images: [
              {
                public_id: "sb_4",
                url: "https://images.unsplash.com/photo-1610192244261-3f33de3f55e4?w=500&auto=format&fit=crop&q=70",
              },
            ],
          },
          {
            name: "Madras Filter Coffee",
            price: 69,
            description: "Brewed freshly with Chicory-blend coffee decoction and frothed milk.",
            stock: 100,
            images: [
              {
                public_id: "sb_5",
                url: "https://images.unsplash.com/photo-1514432324607-a09d9b4aefdd?w=500&auto=format&fit=crop&q=70",
              },
            ],
          },
        ],
      },
    ],
  },
  {
    restaurant: {
      name: "Bikanervala",
      isVeg: true,
      address: "24, Outer Ring Road, Bellandur, Bengaluru",
      ratings: 4.4,
      numOfReviews: 145,
      location: {
        type: "Point",
        coordinates: [77.6744, 12.9298],
      },
      reviewSentiment: "positive",
      reviewSummaryBullets: [
        "Grand North Indian chole bhature and street chaat",
        "Authentic desi ghee sweets and fresh snacks",
        "Pure vegetarian hygiene and quick counter service",
      ],
      reviewTopMentions: ["CholeBhature", "RajKachori", "Rasmalai", "DesiGhee"],
      images: [
        {
          public_id: "bv_main",
          url: "https://images.unsplash.com/photo-1601050690597-df0568f70950?w=700&auto=format&fit=crop&q=80",
        },
      ],
    },
    menuCategories: [
      {
        category: "Delhi Street Chaat & Snacks",
        items: [
          {
            name: "Special Chole Bhature (2 Pcs)",
            price: 199,
            description: "Spicy dark Amritsari chickpeas served with puffy bhaturas, pickled carrot, and fried chili.",
            stock: 65,
            images: [
              {
                public_id: "bv_1",
                url: "https://images.unsplash.com/photo-1626132647523-66f5bf380027?w=500&auto=format&fit=crop&q=70",
              },
            ],
          },
          {
            name: "Royal Raj Kachori",
            price: 149,
            description: "Crisp giant shell stuffed with lentil dumplings, sprouts, yogurt, sev, and tangy tamarind chutney.",
            stock: 50,
            images: [
              {
                public_id: "bv_2",
                url: "https://images.unsplash.com/photo-1601050690597-df0568f70950?w=500&auto=format&fit=crop&q=70",
              },
            ],
          },
          {
            name: "Pani Puri (8 Pcs)",
            price: 89,
            description: "Crispy puris filled with potato ragda and infused with spicy mint-coriander water.",
            stock: 75,
            images: [
              {
                public_id: "bv_3",
                url: "https://images.unsplash.com/photo-1606491956689-2ea866880c84?w=500&auto=format&fit=crop&q=70",
              },
            ],
          },
        ],
      },
      {
        category: "Traditional Sweets",
        items: [
          {
            name: "Kesar Rasmalai (2 Pcs)",
            price: 120,
            description: "Spongy cottage cheese discs soaked in saffron-infused thickened cardamom milk.",
            stock: 45,
            images: [
              {
                public_id: "bv_4",
                url: "https://images.unsplash.com/photo-1541781774459-bb2af2f05b55?w=500&auto=format&fit=crop&q=70",
              },
            ],
          },
        ],
      },
    ],
  },
  {
    restaurant: {
      name: "Taco Bell",
      isVeg: false,
      address: "Garuda Mall, Magrath Road, Ashok Nagar, Bengaluru",
      ratings: 4.2,
      numOfReviews: 87,
      location: {
        type: "Point",
        coordinates: [77.6084, 12.9702],
      },
      reviewSentiment: "positive",
      reviewSummaryBullets: [
        "Delicious crunchy tacos with zesty salsa and sour cream",
        "Loaded nachos topped with warm nacho cheese sauce",
        "Quick service and fun Mexican street food vibe",
      ],
      reviewTopMentions: ["CrunchyTacos", "LoadedNachos", "Burrito", "Quesadilla"],
      images: [
        {
          public_id: "tb_main",
          url: "https://images.unsplash.com/photo-1551504734-5ee1c4a1479b?w=700&auto=format&fit=crop&q=80",
        },
      ],
    },
    menuCategories: [
      {
        category: "Tacos & Burritos",
        items: [
          {
            name: "Crunchy Chicken Taco",
            price: 149,
            description: "Crispy corn shell packed with Mexican seasoned chicken, shredded lettuce, and real cheddar cheese.",
            stock: 40,
            images: [
              {
                public_id: "tb_1",
                url: "https://images.unsplash.com/photo-1551504734-5ee1c4a1479b?w=500&auto=format&fit=crop&q=70",
              },
            ],
          },
          {
            name: "7-Layer Veg Burrito",
            price: 219,
            description: "Warm flour tortilla rolled with seasoned rice, black beans, guacamole, sour cream, and pico de gallo.",
            stock: 35,
            images: [
              {
                public_id: "tb_2",
                url: "https://images.unsplash.com/photo-1626700051175-6818013e1d4f?w=500&auto=format&fit=crop&q=70",
              },
            ],
          },
        ],
      },
      {
        category: "Nachos & Sides",
        items: [
          {
            name: "Ultimate Loaded Nachos",
            price: 249,
            description: "Warm tortilla chips drenched in nacho cheese sauce, jalapenos, salsa, and black beans.",
            stock: 50,
            images: [
              {
                public_id: "tb_3",
                url: "https://images.unsplash.com/photo-1513456852971-30c0b8199d4d?w=500&auto=format&fit=crop&q=70",
              },
            ],
          },
        ],
      },
    ],
  },
  {
    restaurant: {
      name: "Starbucks Coffee",
      isVeg: true,
      address: "Phoenix Marketcity, Whitefield Main Road, Bengaluru",
      ratings: 4.6,
      numOfReviews: 172,
      location: {
        type: "Point",
        coordinates: [77.6974, 12.9961],
      },
      reviewSentiment: "positive",
      reviewSummaryBullets: [
        "Premium artisanal coffee beans and custom syrups",
        "Cozy ambience with fresh butter croissants and pastries",
        "Java Chip Frappuccino is rich, icy, and decadent",
      ],
      reviewTopMentions: ["JavaChip", "ColdBrew", "CaramelMacchiato", "Croissant"],
      images: [
        {
          public_id: "sbux_main",
          url: "https://images.unsplash.com/photo-1501339847302-ac426a4a7cbb?w=700&auto=format&fit=crop&q=80",
        },
      ],
    },
    menuCategories: [
      {
        category: "Frappuccinos & Cold Coffees",
        items: [
          {
            name: "Java Chip Frappuccino",
            price: 345,
            description: "Blended coffee with mocha sauce, rich chocolate chips, milk, and whipped cream.",
            stock: 50,
            images: [
              {
                public_id: "sbux_1",
                url: "https://images.unsplash.com/photo-1572490122747-3968b75cc699?w=500&auto=format&fit=crop&q=70",
              },
            ],
          },
          {
            name: "Signature Caramel Macchiato",
            price: 315,
            description: "Freshly steamed milk with vanilla-flavored syrup, marked with espresso and caramel drizzle.",
            stock: 45,
            images: [
              {
                public_id: "sbux_2",
                url: "https://images.unsplash.com/photo-1485808191679-5f86510681a2?w=500&auto=format&fit=crop&q=70",
              },
            ],
          },
        ],
      },
      {
        category: "Bakery & Desserts",
        items: [
          {
            name: "French Butter Croissant",
            price: 225,
            description: "Flaky, golden layered viennoiserie pastry with rich European butter aroma.",
            stock: 30,
            images: [
              {
                public_id: "sbux_3",
                url: "https://images.unsplash.com/photo-1555507036-ab1f4038808a?w=500&auto=format&fit=crop&q=70",
              },
            ],
          },
          {
            name: "New York Style Cheesecake",
            price: 295,
            description: "Classic velvety dense cheesecake on a crunchy graham cracker crust.",
            stock: 25,
            images: [
              {
                public_id: "sbux_4",
                url: "https://images.unsplash.com/photo-1533134242443-d4fd215305ad?w=500&auto=format&fit=crop&q=70",
              },
            ],
          },
        ],
      },
    ],
  },
];

async function addMoreRestaurants() {
  try {
    console.log("Connecting to MongoDB Atlas...");
    await mongoose.connect(process.env.DB_LOCAL_URI);
    console.log("Connected successfully!");

    for (const entry of newRestaurantsData) {
      // Check if restaurant already exists
      let restaurant = await Restaurant.findOne({ name: entry.restaurant.name });

      if (!restaurant) {
        restaurant = await Restaurant.create(entry.restaurant);
        console.log(`Created new restaurant: ${restaurant.name} (${restaurant._id})`);
      } else {
        console.log(`Restaurant '${restaurant.name}' already exists.`);
      }

      // Check if menu exists
      const existingMenu = await Menu.findOne({ restaurant: restaurant._id });
      if (existingMenu && existingMenu.menu.length > 0) {
        console.log(`Menu already exists for '${restaurant.name}'. Skipping menu creation.`);
        continue;
      }

      const createdCategories = [];

      for (const cat of entry.menuCategories) {
        const itemIds = [];

        for (const item of cat.items) {
          const foodItem = await FoodItem.create({
            name: item.name,
            price: item.price,
            description: item.description,
            stock: item.stock,
            images: item.images,
            restaurant: restaurant._id,
            ratings: (Math.random() * 0.8 + 4.1).toFixed(1),
            numOfReviews: Math.floor(Math.random() * 40) + 10,
          });

          itemIds.push(foodItem._id);
        }

        createdCategories.push({
          category: cat.category,
          items: itemIds,
        });
      }

      if (existingMenu) {
        existingMenu.menu = createdCategories;
        await existingMenu.save();
      } else {
        await Menu.create({
          restaurant: restaurant._id,
          menu: createdCategories,
        });
      }

      console.log(`✅ Menu successfully created for: ${restaurant.name}`);
    }

    const totalRestaurants = await Restaurant.countDocuments();
    console.log(`\n🎉 Completed! Total restaurants now in database: ${totalRestaurants}`);
    process.exit(0);
  } catch (error) {
    console.error("❌ Error adding restaurants:", error);
    process.exit(1);
  }
}

addMoreRestaurants();

