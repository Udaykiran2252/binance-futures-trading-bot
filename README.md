# Binance Futures Trading Bot (Testnet)

## Overview
This project is a simplified trading bot built using Python for Binance USD-M Futures Testnet.
It supports Market, Limit, and Stop-Limit orders with proper logging and CLI input.

## Features
- Binance USD-M Futures Testnet compatible
- Market, Limit, and Stop-Limit orders
- Buy and Sell support
- Command-line interface
- Logging of requests, responses, and errors
- Dry-run mode when API keys are not provided

## Setup
1. Install dependencies:
   pip install -r requirements.txt

2. (Optional) Add Binance Futures Testnet API keys in `config.py`

3. Run the bot:
   python bot.py

## Notes
Binance Futures Testnet API key UI may be restricted in some regions.
The bot is fully compatible with the official Binance Futures API and runs in dry-run mode without keys.

