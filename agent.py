import wallet
import time

class NegotiationAgent:
    def __init__(self, agent_name):
        self.name = agent_name
        self.max_budget = 2.0 # Maximum USDC the agent is willing to spend

    def run_trading_logic(self, service_name, asking_price, seller_address):
        print(f"\n[ {self.name} ] - Monitoring Moltbook for opportunities...")
        
        # 1. Check financial status
        current_balance = wallet.get_usdc_balance()
        print(f"Status: My balance is {current_balance} USDC")

        if current_balance < asking_price:
            print("Action: Opportunity skipped - Insufficient funds.")
            return

        # 2. Strategic Negotiation Logic
        # The agent tries to negotiate a 15% discount
        target_price = asking_price * 0.85
        print(f"Negotiation: Seller asks {asking_price} USDC. I'm offering {target_price:.2f} USDC.")

        # Simulate negotiation delay
        time.sleep(2)
        print("Update: Offer accepted by the seller agent!")

        # 3. Execution (Payment)
        # Note: Uncomment the line below when you are ready for a real transaction test
        # tx_id = wallet.pay_usdc(seller_address, target_price)
        # print(f"Execution: Payment successful! Transaction ID: {tx_id}")
        print("Execution: Transaction ready (Simulated for safety).")

if __name__ == "__main__":
    # Initialize the agent
    my_bot = NegotiationAgent("Agent-Alpha-Commerce")
    
    # Run a test scenario
    my_bot.run_trading_logic(
        service_name="Web3 Data Analysis", 
        asking_price=1.2, 
        seller_address="0x0000000000000000000000000000000000000000" # Replace with real address for testing
    )
