# 🦞 ClawNegotiator: The Autonomous Agent for Smart Commerce

**ClawNegotiator** is an AI-powered agent built for the **Moltbook & USDC Agentic Commerce Hackathon**. It is designed to navigate the emerging "Agent Internet" by not only executing transactions but strategically negotiating them to optimize treasury efficiency.

---

## 🚀 Overview

In a world where AI agents trade with each other, fixed pricing is inefficient. **ClawNegotiator** acts as a smart procurement layer. It monitors service offerings, verifies its own USDC solvency on the **Base Network**, and engages in automated negotiation to secure the best possible deals.

### Key Features
* **On-Chain Solvency Intelligence:** Real-time balance tracking of USDC and ETH (Gas) on Base Mainnet.
* **Autonomous Negotiation Engine:** Implements a strategic discount logic (default 15%) to optimize purchasing power.
* **Modular Architecture:** Separation of concerns between the "Brain" (Logic) and the "Accountant" (Wallet/Security).
* **Security First:** Local transaction signing. Private keys are never hardcoded and remain in protected environment variables.

---

## 🛠 Technical Stack

* **Network:** Base (Layer 2)
* **Language:** Python 3.12+
* **Blockchain Library:** Web3.py
* **Environment Management:** Dotenv
* **Asset:** USDC (Native Base)

---

## 📦 Installation & Setup

### 1. Clone the repository
```bash
git clone [https://github.com/YOUR_USERNAME/agent-hackathon.git](https://github.com/YOUR_USERNAME/agent-hackathon.git)
cd agent-hackathon
