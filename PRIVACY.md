# Privacy Notice

This document explains how data is handled in the Customer Service AI demo app.

## What This App Does

- This app sends the text of user questions to the Anthropic Claude API in order to generate a response.
- Responses are generated based on a small, local, fictional knowledge base for a made-up company, Northstar Outfitters.

## What This App Does Not Do

- This app does not collect or store real customer personal information.
- This app does not use a database in the MVP version — nothing is saved after your session ends.
- This app does not store user conversations by default.
- This app is a demo, not a production customer support system, and should not be used with real customer data.

## Recommendations for Users

- Please avoid entering sensitive personal information (names, addresses, payment details, account numbers, etc.) when testing this app.
- Treat all example questions and answers as fictional and for demonstration purposes only.

## API Keys

- This app requires an Anthropic API key to function.
- API keys must be kept private and should never be shared, hard-coded, or committed to GitHub.
- The `.env` file containing your API key must never be committed to version control. It is excluded via `.gitignore`.

## Summary

This is a portfolio demo project built around fictional data. No real customer information is collected, stored, or processed.
