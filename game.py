import random

def get_difficulty():
    print("\n🎮 Choose your difficulty:")
    print("  1. Easy   (1–50,  10 tries)")
    print("  2. Medium (1–100,  7 tries)")
    print("  3. Hard   (1–200,  5 tries)")

    while True:
        choice = input("\nEnter 1, 2, or 3: ").strip()
        if choice == "1":
            return 50, 10, "Easy"
        elif choice == "2":
            return 100, 7, "Medium"
        elif choice == "3":
            return 200, 5, "Hard"
        else:
            print("❌ Please enter 1, 2, or 3.")


def play_round(max_number, max_tries, difficulty):
    secret = random.randint(1, max_number)
    print(f"\n🔢 I'm thinking of a number between 1 and {max_number}.")
    print(f"   You have {max_tries} tries. Good luck!\n")

    for attempt in range(1, max_tries + 1):
        tries_left = max_tries - attempt + 1

        while True:
            try:
                guess = int(input(f"  Attempt {attempt}/{max_tries} → Your guess: "))
                if 1 <= guess <= max_number:
                    break
                else:
                    print(f"  ⚠️  Please enter a number between 1 and {max_number}.")
            except ValueError:
                print("  ⚠️  That doesn't look like a number. Try again!")

        if guess == secret:
            score = calculate_score(attempt, max_tries, difficulty)
            print(f"\n  🎉 YES! The number was {secret}!")
            print(f"  ✅ You got it in {attempt} attempt(s)!")
            print(f"  ⭐ Score this round: {score} points")
            return score

        elif guess < secret:
            gap = secret - guess
            hint = get_hint(gap, max_number)
            print(f"  📈 Too low! {hint}")
        else:
            gap = guess - secret
            hint = get_hint(gap, max_number)
            print(f"  📉 Too high! {hint}")

        if tries_left > 1:
            print(f"     ({tries_left - 1} tries remaining)\n")

    print(f"\n  💀 Out of tries! The number was {secret}.")
    print("  Better luck next round!")
    return 0


def get_hint(gap, max_number):
    percent = (gap / max_number) * 100
    if percent <= 5:
        return "🔥 Super close!"
    elif percent <= 15:
        return "♨️  Getting warm..."
    elif percent <= 30:
        return "🌤️  Somewhat close."
    else:
        return "🧊 Way off!"


def calculate_score(attempts, max_tries, difficulty):
    multiplier = {"Easy": 1, "Medium": 2, "Hard": 3}[difficulty]
    base = max(10, (max_tries - attempts + 1) * 10)
    return base * multiplier


def show_banner():
    print("=" * 40)
    print("   🎯  NUMBER GUESSING GAME  🎯")
    print("=" * 40)


def main():
    show_banner()
    print("Welcome! Try to guess the secret number.")

    total_score = 0
    round_num = 0

    while True:
        round_num += 1
        print(f"\n{'─' * 40}")
        print(f"  📌 ROUND {round_num}  |  Total Score: {total_score}")
        print(f"{'─' * 40}")

        max_number, max_tries, difficulty = get_difficulty()
        round_score = play_round(max_number, max_tries, difficulty)
        total_score += round_score

        print(f"\n  🏆 Total Score: {total_score} points")
        again = input("\n  Play another round? (y/n): ").strip().lower()
        if again != "y":
            break

    print("\n" + "=" * 40)
    print(f"  Thanks for playing!")
    print(f"  🏅 Final Score: {total_score} points")
    if total_score >= 100:
        print("  🌟 Amazing job!")
    elif total_score >= 50:
        print("  👍 Nice work!")
    else:
        print("  💪 Keep practicing!")
    print("=" * 40)


if __name__ == "__main__":
    main()
