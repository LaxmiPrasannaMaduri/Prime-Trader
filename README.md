🚀 Binance Futures Testnet Trading Bot

A structured and production-style Python CLI application that places Market and Limit orders on Binance USDT-M Futures Testnet, with proper validation, logging, and error handling.

This project demonstrates clean architecture, API integration, CLI interaction, and robust exception handling.

📌 Overview

This trading bot connects to Binance Futures Testnet (USDT-M) and allows users to:

Place MARKET orders

Place LIMIT orders

Execute both BUY and SELL trades

Validate user input via CLI

Log API requests, responses, and errors

The application is designed with separation of concerns and reusable components.

🏗 Architecture

The project follows a modular structure:

prime_trader/
│
├── cli.py                  # CLI entry point
├── requirements.txt
├── README.md
│
└── bot/
    ├── __init__.py
    ├── binance_client.py   # Binance API wrapper layer
    ├── orders.py           # Business logic layer
    ├── validators.py       # Input validation layer
    └── logging_config.py   # Logging configuration

Design Principles Used

Separation of concerns

Reusable API client abstraction

Centralized logging

Explicit input validation

Structured error handling

✨ Features

✔ Market Orders (BUY / SELL)
✔ Limit Orders (BUY / SELL)
✔ CLI argument validation
✔ Structured logging to file
✔ Clear order request & response summary
✔ Exception handling (validation, API errors, network failures)
✔ Clean, readable, extensible codebase

⚙️ Setup Instructions
1️⃣ Clone the Repository
git clone <your-repo-url>
cd prime_trader

2️⃣ Create Virtual Environment (Recommended)
python -m venv venv
venv\Scripts\activate     # Windows

3️⃣ Install Dependencies
pip install -r requirements.txt

🔑 Binance Futures Testnet Configuration

This project uses Binance USDT-M Futures Testnet.

Generate API Keys

Visit:
https://testnet.binancefuture.com

Register / Login

Go to API Management

Create a new API Key

Copy:

API Key

Secret Key

⚠ These are testnet keys (not real funds).

🔐 Environment Variables

Create a .env file in the project root:

BINANCE_API_KEY=your_testnet_api_key
BINANCE_API_SECRET=your_testnet_secret_key


⚠ Do NOT commit .env to version control.

▶️ Usage Examples
📌 Place Market Order
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.01

📌 Place Limit Order
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.01 --price 60000

🖥 Sample Output
=== ORDER REQUEST SUMMARY ===
Symbol: BTCUSDT
Side: BUY
Type: MARKET
Quantity: 0.01

=== ORDER RESPONSE ===
Order ID: 123456789
Status: FILLED
Executed Qty: 0.01
Avg Price: 59875.21

✅ Order placed successfully!

📝 Logging

All API interactions are logged to:

logs/trading_bot.log


The log file includes:

Order request parameters

API responses

Error messages

Exception stack traces

This ensures traceability and debugging support.

🛡 Error Handling

The application handles:

Invalid order side

Invalid order type

Missing price for LIMIT orders

Invalid quantity

Authentication failures

Binance API errors

Network-related issues

Clear error messages are shown in CLI and recorded in logs.

📌 Assumptions

Hedge mode disabled

Default leverage used

No symbol precision validation implemented

Orders executed only on USDT-M Futures Testnet

📦 Dependencies

python-binance

python-dotenv

🧠 Engineering Highlights

This project demonstrates:

Clean modular backend structure

API abstraction layer

CLI-based user interface

Defensive programming practices

Logging best practices

Production-style exception handling

🔒 Security Considerations

API credentials stored using environment variables

.env excluded via .gitignore

No secrets hardcoded in source code

🚀 Future Enhancements

Add Stop-Market / Stop-Limit order support

Add symbol precision validation

Implement retry strategy for API failures

Add unit tests

Build lightweight UI

Add strategy logic (e.g., moving average crossover)

📈 Learning Outcomes

This project strengthened understanding of:

REST API integration

Exchange trading workflows

Python CLI development

Logging systems

Structured application design