# Cafe Management System

A comprehensive GUI-based cafe management system built with Python's tkinter library. This system allows you to manage menu items, process orders, generate bills, and maintain order history.

## Features

### Core Functionality
- **Interactive Menu Display**: Organized in categories (Beverages, Food, Snacks)
- **Order Management**: Add items with quantities, view current order, remove items
- **Bill Generation**: Detailed bills with tax calculation (18% GST)
- **Order History**: Track and view past orders
- **Data Persistence**: Automatic saving and loading of menu items and order history

### Admin Features
- **Add Menu Items**: Dynamically add new items to existing or new categories
- **View Order History**: Complete history of all past orders
- **Data Management**: Automatic backup of all data in JSON format

### User Interface
- **Modern GUI**: Clean, professional design with color-coded sections
- **Tabbed Menu**: Easy navigation between different food categories
- **Real-time Updates**: Live total calculation and order display
- **Confirmation Dialogs**: Safe operations with user confirmations

## Requirements

- Python 3.6 or higher
- tkinter (usually comes pre-installed with Python)

## Installation

1. Ensure you have Python installed on your system
2. Download the `cafe_management_system.py` file
3. No additional packages need to be installed (uses standard Python libraries)

## Usage

### Running the Application
```bash
python cafe_management_system.py
```

### Using the System

#### 1. Menu Navigation
- The menu is organized in tabs: **Beverages**, **Food**, and **Snacks**
- Each tab displays items with their prices
- Use the quantity spinbox to select desired quantity
- Click **Add** to add items to your current order

#### 2. Order Management
- View your current order in the right panel
- Total is calculated automatically with tax
- Select items in the order list and click **Remove Selected Item** to remove
- Use **Clear Order** to remove all items

#### 3. Bill Generation
- Click **Generate Bill** to create a detailed bill
- The bill includes:
  - Item details with quantities and amounts
  - Subtotal
  - 18% GST calculation
  - Grand total
- **Save Bill** to save as a text file
- **Confirm Order** to complete the transaction and add to history

#### 4. Admin Functions
- **Add Menu Item**: Add new items to existing or new categories
- **View Order History**: See all past completed orders

## File Structure

```
cafe_management_system.py    # Main application file
cafe_data.json              # Automatic data storage (created on first run)
bill_YYYYMMDD_HHMMSS.txt   # Generated bill files
```

## Sample Menu Items

### Beverages
- Coffee: ₹120
- Tea: ₹80
- Cold Coffee: ₹150
- Hot Chocolate: ₹130
- Fresh Juice: ₹100

### Food
- Sandwich: ₹180
- Burger: ₹220
- Pizza Slice: ₹200
- Pasta: ₹250
- Salad: ₹160

### Snacks
- French Fries: ₹120
- Cookies: ₹60
- Muffin: ₹90
- Donut: ₹80
- Cake Slice: ₹150

## Key Features Explained

### Data Persistence
- All menu items and order history are automatically saved to `cafe_data.json`
- Data is loaded on startup, so your customizations persist between sessions

### Bill Format
```
==================================================
           CAFE MANAGEMENT SYSTEM
==================================================
Date: 2025-09-17 19:14:23
Bill No: 0001
==================================================

Item                 Price    Qty   Amount    
--------------------------------------------------
Coffee               ₹120     2     ₹240     
Sandwich             ₹180     1     ₹180     

--------------------------------------------------
Subtotal:                           ₹420.00
Tax (18%):                          ₹75.60
==================================================
TOTAL:                              ₹495.60
==================================================

        Thank you for visiting!
        Have a great day!
```

### Order History Format
- Each order includes timestamp, items with quantities, and total amount
- Accessible through the **View Order History** button in Admin Panel

## Customization

### Adding New Categories
- Use the **Add Menu Item** function in Admin Panel
- Enter a new category name when prompted
- The system will automatically create the new category

### Modifying Prices
- Edit the `self.menu_items` dictionary in the code
- Or use the Add Menu Item function to overwrite existing items

## Troubleshooting

### Common Issues
1. **Application won't start**: Ensure Python and tkinter are properly installed
2. **Data not saving**: Check file permissions in the application directory
3. **GUI appears distorted**: Try adjusting screen resolution or DPI settings

### Error Messages
- **"No items in current order"**: Add items to your order before generating a bill
- **"Invalid quantity"**: Enter a valid number for quantity
- **"Please select an item to remove"**: Click on an item in the order list before removing

## Future Enhancements

Potential features for future versions:
- Customer management system
- Inventory tracking
- Multiple payment methods
- Receipt printing
- Sales analytics and reports
- Multi-user support with login system

## Support

For issues or feature requests, please check:
1. Ensure you're using Python 3.6+
2. Verify all files are in the same directory
3. Check file permissions for data saving

## License

This project is provided as-is for educational and commercial use.

---

**Enjoy managing your cafe efficiently! ☕**
