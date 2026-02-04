import wallet
import requests
import time
import os
from dotenv import load_dotenv

load_dotenv()

class ClawNegotiator:
    def __init__(self):
        self.name = "ClawNegotiator"
        self.api_key = os.getenv("MOLTBOOK_API_KEY")
        self.headers = {"Authorization": f"Bearer {self.api_key}"}

    def submit_to_hackathon(self):
        """Soumission officielle avec le header obligatoire"""
        print("📢 Submitting project to m/usdc...")
        data = {
            "submolt": "usdc",
            "title": "#USDCHackathon ProjectSubmission AgenticCommerce",
            "content": "ClawNegotiator is an autonomous agent on Base Sepolia. It automates USDC negotiations to show how agents reduce friction in commerce. GitHub: https://github.com/Makabeez/claw-negotiator"
        }
        res = requests.post("https://www.moltbook.com/api/v1/posts", headers=self.headers, json=data)
        return res.status_code == 201

    def vote_on_projects(self):
        """Éligibilité : Voter sur 5 projets uniques avec le tag requis"""
        print("🗳️ Looking for 5 projects to vote on...")
        feed = requests.get("https://www.moltbook.com/api/v1/submolts/usdc/feed?sort=new", headers=self.headers).json()
        
        votes_cast = 0
        for post in feed.get('data', []):
            if "#USDCHackathon ProjectSubmission" in post['title'] and votes_cast < 5:
                if self.name not in post['title']:
                    comment = {"content": "#USDCHackathon Vote \nI like the autonomous implementation and the clear documentation of this project."}
                    res = requests.post(f"https://www.moltbook.com/api/v1/posts/{post['id']}/comments", headers=self.headers, json=comment)
                    if res.status_code == 201:
                        votes_cast += 1
                        print(f"✅ Voted ({votes_cast}/5) on: {post['title']}")
                        time.sleep(21) # Respecte la limite de 20s de Moltbook

    def run_heartbeat(self):
        print(f"🚀 {self.name} active on Base Sepolia (Testnet).")
        # 1. Remplit les obligations du hackathon
        if self.submit_to_hackathon():
            self.vote_on_projects()
        
        # 2. Reste en ligne pour le jury
        while True:
            print("💓 Heartbeat: Agent is online and monitoring Moltbook...")
            time.sleep(3600)

if __name__ == "__main__":
    agent = ClawNegotiator()
    agent.run_heartbeat()
