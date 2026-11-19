# Hostel-Concierge

A multi-agent AI concierge system for Sunrise Hostel.

## Overview

Hostel-Concierge is a conversational assistant designed to help
logged-in hostel guests manage their bookings and kitchen orders.

The system will use:
- An Orchestrator Agent
- A Booking Specialist Agent
- A Kitchen Specialist Agent
- MCP servers for specialist tools
- Human approval for risky operations
- Application-level security and policy enforcement

## Technology Stack

- Python
- LangGraph
- Model Context Protocol (MCP)
- Ollama
- SQLite
- Pytest

## Setup

Install dependencies:

    uv sync

Run the application:

    uv run hostel-concierge

## Project Status

Currently implementing the initial CLI application.