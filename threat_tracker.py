from threat import Threat
import calendar
import datetime
import time


def main():
    print(f"🔐 Running Threat Tracker!")
    threat_file_path = "threats.csv"
    attack = 2000

    # Get user input for threat.
    threat = get_user_threat()

    # Write their threat to a file.
    save_threat_to_file(threat, threat_file_path)

    # Read file and summarize threats.
    summarize_threats(threat_file_path, attack)


def get_user_threat():
    print(f"❗️ Getting User threat tracker")
    print("Loading...")
    time.sleep(3)
    threat_name = input("Enter threat name: ")
    threat_amount = float(input("Enter the amount of threats!: "))
    threat_categories = [
        "🕵️ Spy",
        "💻💻💻 DDOS",
        "👺 Malware",
        "🦠 Hacker",
        "🚫 Misc",
    ]

    while True:
        print("Select a category: ")
        for i, category_name in enumerate(threat_categories):
            print(f"  {i + 1}. {category_name}")

        value_range = f"[1 - {len(threat_categories)}]"
        selected_index = int(input(f"Enter a category number {value_range}: ")) - 1

        if selected_index in range(len(threat_categories)):
            selected_category = threat_categories[selected_index]
            new_threat = Threat(
                name=threat_name, category=selected_category, amount=threat_amount
            )
            return new_threat
        else:
            print("Invalid category. Please try again!")


def save_threat_to_file(threat: Threat, threat_file_path):
    print(f"🔐 Saving User threat: {threat} to {threat_file_path}")
    with open(threat_file_path, "a") as f:
        f.write(f"{threat.name},{threat.amount},{threat.category}\n")


def summarize_threats(threat_file_path, attack):
    print(f"🔐 Summarizing User threat")
    threats:list[Threat] = []
    with open(threat_file_path, "r") as f:
        lines = f.readlines()
        for line in lines:
            threat_name, threat_amount, threat_category = line.strip().split(",")
            line_threat = Threat(
                name=threat_name,
                amount=float(threat_amount),
                category=threat_category,
            )
            threats.append(line_threat)

    amount_by_category = {}
    for threat in threats:
        key = threat.category
        if key in amount_by_category:
            amount_by_category[key] += threat.amount
        else:
            amount_by_category[key] = threat.amount

    print("Threats By Category 📈:")
    for key, amount in amount_by_category.items():
        print(f"  {key}: {amount:.2f}")

    total_attacks = sum([x.amount for x in threats])
    print(f"Total attacks: {total_attacks:.2f}")

    remaining_attacks = attack - total_attacks
    print(f" attacks Remaining: {remaining_attacks:.2f}")

    now = datetime.datetime.now()
    days_in_month = calendar.monthrange(now.year, now.month)[1]
    remaining_days = days_in_month - now.day

    daily_attack = remaining_attacks / remaining_days
    print(red(f"👉 attacks in the Day: {daily_attack:.2f}"))


def red(text):
    return f"\033[92m{text}\033[0m"


if __name__ == "__main__":
    main()