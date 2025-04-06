from agents.agent_manager import orchestrate_agents
from tools.api_tool import fetch_mock_data

def main():
    customer_data = fetch_mock_data(customer_id="123")
    results = orchestrate_agents(customer_data)
    
    print("\n=== Customer Profile ===")
    print(results["profile"])
    
    print("\n=== Recommendations ===")
    print(results["recommendations"])

if __name__ == "__main__":
    main()
