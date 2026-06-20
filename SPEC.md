# Project Specification: Customer Service AI

## Project Overview

Customer Service AI is a beginner-friendly portfolio project that simulates an AI-powered customer support assistant for a fictional outdoor gear company, Northstar Outfitters. The app uses the Claude API to answer customer questions, grounded in a small local knowledge base, and includes basic escalation logic for questions it cannot confidently answer.

## Problem Statement

Many companies receive repetitive customer support questions (shipping times, return policies, order status, etc.) that could be answered instantly with an AI assistant grounded in accurate company information. This project demonstrates a simple, safe way to build such an assistant without hallucinating policies or overcomplicating the architecture.

## Target Users

- Recruiters and hiring managers reviewing an AI/ML portfolio
- Other developers learning how to build small, grounded AI applications
- The project author, as a practical learning exercise

## Main User Flow

1. User opens the Streamlit app
2. User reads a short intro about Northstar Outfitters and the assistant
3. User types a customer support question (or selects an example question)
4. User optionally selects a support category
5. App sends the question + relevant knowledge base content to Claude
6. Claude returns a grounded answer, or indicates the question should be escalated
7. App displays the answer, with an option to copy or download it

## MVP Scope

The MVP must be realistic for a beginner to build in a few days. It includes:

- Single fictional company (Northstar Outfitters)
- Text input for customer questions
- Optional support category selection
- Static local knowledge base (Markdown or JSON)
- Claude API integration for answer generation
- Basic escalation detection and messaging
- Example questions for quick testing
- Copy/download of the generated response

## Out-of-Scope Features (MVP)

- Databases of any kind
- User authentication / accounts
- Multiple company profiles
- LangChain or other agent frameworks
- Vector databases / RAG
- Conversation history or memory across sessions
- Deployment/hosting setup
- Docker

These are listed as future improvements, not MVP requirements.

## Functional Requirements

- The app must accept free-text customer questions
- The app must load knowledge base content from local files
- The app must send the question and relevant knowledge base context to Claude
- The app must display Claude's response in the UI
- The app must allow the user to copy or download the response
- The app must provide a set of example questions

## Non-Functional Requirements

- Code should be simple and readable for a beginner
- The app should respond within a few seconds under normal conditions
- The app must not expose the API key in the UI, logs, or source control
- The app should handle common errors gracefully (see Error Handling Requirements)

## AI Behavior Requirements

- The assistant must be professional, friendly, and concise
- The assistant must answer only using information present in the knowledge base
- The assistant must never invent policies, prices, or facts not in the knowledge base
- If the assistant does not know an answer, it must say so clearly and recommend escalation
- The assistant should avoid overly long or overly formal responses

## Knowledge Base Requirements

The knowledge base must cover, at minimum:

- Shipping policy
- Return policy
- Warranty policy
- Order tracking information
- Product troubleshooting guidance
- Damaged item policy
- Refund timeline
- Contact/escalation rules

The knowledge base should be stored as simple Markdown or JSON files that are easy to read and edit without a database.

## Escalation Requirements

The assistant should recommend escalation to a human support agent when:

- The question is unrelated to the knowledge base
- The question involves account-specific or order-specific details the app cannot verify
- The question involves a complaint, refund dispute, or anything sensitive
- The knowledge base does not contain a confident answer

Escalation responses should be polite and clearly state that a human agent should be contacted.

## Error Handling Requirements

- If the API key is missing or invalid, show a clear, friendly error message
- If the user submits an empty question, prompt them to enter a question
- If the input is extremely long, truncate or warn the user instead of crashing
- If the Claude API call fails (timeout, rate limit, etc.), show a graceful fallback message

## Success Criteria

The MVP is considered successful if:

- A user can ask a variety of realistic support questions and get accurate, grounded answers
- The assistant correctly escalates questions outside the knowledge base
- The assistant never fabricates policy details
- The app runs locally without errors using the setup instructions in `README.md`
- The codebase remains simple enough for a beginner to understand and extend
