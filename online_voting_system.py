import time
import random

voters_db = {}  
has_voted = []  
candidates = {
    "1": {"name": "Candidate A", "votes": 0},
    "2": {"name": "Candidate B", "votes": 0},
    "3": {"name": "Candidate C", "votes": 0}
}

def register_voter():
    print("\n--- Voter Registration ---")
    v_id = input("Create a Voter ID: ")
    if v_id in voters_db:
        print("❌ Error: ID already exists!")
    else:
        pwd = input("Create a Password: ")
        voters_db[v_id] = pwd
        print(f"✅ Registration Successful for {v_id}!")

def cast_vote():
    print("\n--- Secure Voting ---")
    v_id = input("Enter your Voter ID: ")
    pwd = input("Enter your Password: ")

  
    if v_id in voters_db and voters_db[v_id] == pwd:
        if v_id in has_voted:
            print("❌ Security Alert: You have already voted!")
        else:
            print("\nCandidates List:")
            for key, val in candidates.items():
                print(f"{key}. {val['name']}")
            
            choice = input("Enter Candidate Number: ")
            if choice in candidates:
                candidates[choice]["votes"] += 1
                has_voted.append(v_id)
                print("✅ Vote cast successfully!")
            else:
                print("❌ Invalid Candidate.")
    else:
        print("❌ Login Failed. Check ID or Password.")


def ai_prediction_engine():
    """
    This simulates a basic ML concept: Trend Prediction.
    It analyzes current vote distribution to predict the winner.
    """
    print("\n--- AI Result Prediction Engine ---")
    total_votes = len(has_voted)
    
    if total_votes < 3:
        print("⚠️ Not enough data for AI to predict. Need at least 3 votes.")
        return

    print("Analyzing patterns...")
    time.sleep(1) 
    
    prediction = None
    max_prob = -1
    
    for key, data in candidates.items():
     
        probability = (data["votes"] / total_votes) * 100
        
       
        if probability > max_prob:
            max_prob = probability
            prediction = data["name"]
            
    print(f"🤖 AI Prediction: Based on current trends, {prediction} is likely to win.")
    print(f"📈 Confidence Level: {round(max_prob, 2)}%")



def main():
    while True:
        print("\n==============================")
        print("   DIGITAL VOTING SYSTEM V1   ")
        print("==============================")
        print("1. Register New Voter")
        print("2. Cast a Vote")
        print("3. View AI Predictions")
        print("4. Final Results & Exit")
        
        choice = input("\nSelect an option (1-4): ")
        
        if choice == "1":
            register_voter()
        elif choice == "2":
            cast_vote()
        elif choice == "3":
            ai_prediction_engine()
        elif choice == "4":
            print("\n--- FINAL RESULTS ---")
            for key, data in candidates.items():
                print(f"{data['name']}: {data['votes']} votes")
            print("\nShutting down system. Goodbye!")
            break
        else:
            print("❌ Invalid selection. Try again.")

if __name__ == "__main__":
    main()
